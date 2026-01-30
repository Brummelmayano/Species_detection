import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import Login from '../pages/Login';
import { AuthProvider } from '../contexts/AuthContext';
import axios from 'axios';

// Mock axios
jest.mock('axios');
const mockedAxios = axios;

// Mock useNavigate
const mockNavigate = jest.fn();
jest.mock('react-router-dom', () => ({
  ...jest.requireActual('react-router-dom'),
  useNavigate: () => mockNavigate,
}));

const renderLogin = () => {
  return render(
    <BrowserRouter>
      <AuthProvider>
        <Login />
      </AuthProvider>
    </BrowserRouter>
  );
};

describe('Login Component', () => {
  beforeEach(() => {
    mockedAxios.post.mockClear();
    mockNavigate.mockClear();
  });

  it('should render login form', () => {
    renderLogin();

    expect(screen.getByLabelText(/nom d'utilisateur/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/mot de passe/i)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /connexion/i })).toBeInTheDocument();
    expect(screen.getByText(/s'inscrire/i)).toBeInTheDocument();
  });

  it('should handle successful login', async () => {
    const mockLoginResponse = { data: { access_token: 'token123' } };
    const mockUserResponse = { data: { id: 1, username: 'testuser' } };

    mockedAxios.post.mockResolvedValueOnce(mockLoginResponse);
    mockedAxios.get.mockResolvedValueOnce(mockUserResponse);

    renderLogin();

    const usernameInput = screen.getByLabelText(/nom d'utilisateur/i);
    const passwordInput = screen.getByLabelText(/mot de passe/i);
    const submitButton = screen.getByRole('button', { name: /connexion/i });

    fireEvent.change(usernameInput, { target: { value: 'testuser' } });
    fireEvent.change(passwordInput, { target: { value: 'password123' } });
    fireEvent.click(submitButton);

    await waitFor(() => {
      expect(mockedAxios.post).toHaveBeenCalledWith('http://localhost:8000/auth/login', {
        username: 'testuser',
        password: 'password123',
      });
      expect(mockNavigate).toHaveBeenCalledWith('/');
    });
  });

  it('should handle login error', async () => {
    mockedAxios.post.mockRejectedValueOnce(new Error('Login failed'));

    renderLogin();

    const usernameInput = screen.getByLabelText(/nom d'utilisateur/i);
    const passwordInput = screen.getByLabelText(/mot de passe/i);
    const submitButton = screen.getByRole('button', { name: /connexion/i });

    fireEvent.change(usernameInput, { target: { value: 'wronguser' } });
    fireEvent.change(passwordInput, { target: { value: 'wrongpass' } });
    fireEvent.click(submitButton);

    await waitFor(() => {
      expect(screen.getByText(/erreur de connexion/i)).toBeInTheDocument();
    });
  });

  it('should validate required fields', async () => {
    renderLogin();

    const submitButton = screen.getByRole('button', { name: /connexion/i });
    fireEvent.click(submitButton);

    // HTML5 validation should prevent submission with empty fields
    expect(mockedAxios.post).not.toHaveBeenCalled();
  });

  it('should have link to register page', () => {
    renderLogin();

    const registerLink = screen.getByText(/s'inscrire/i);
    expect(registerLink).toBeInTheDocument();
    expect(registerLink.closest('a')).toHaveAttribute('href', '/register');
  });
});