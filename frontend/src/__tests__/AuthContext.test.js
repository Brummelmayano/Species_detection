import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import { AuthProvider, useAuth } from '../contexts/AuthContext';
import axios from 'axios';

// Mock axios
jest.mock('axios');
const mockedAxios = axios;

// Test component to access context
const TestComponent = () => {
  const { user, loading, login, register, logout } = useAuth();
  return (
    <div>
      <div data-testid="user">{user ? user.username : 'no-user'}</div>
      <div data-testid="loading">{loading ? 'loading' : 'not-loading'}</div>
      <button onClick={() => login('testuser', 'password')}>Login</button>
      <button onClick={() => register('testuser', 'test@example.com', 'password')}>Register</button>
      <button onClick={logout}>Logout</button>
    </div>
  );
};

describe('AuthContext', () => {
  beforeEach(() => {
    localStorage.clear();
    mockedAxios.defaults.headers.common = {};
  });

  it('should initialize with no user and not loading', async () => {
    mockedAxios.get.mockResolvedValueOnce({ data: null });

    render(
      <AuthProvider>
        <TestComponent />
      </AuthProvider>
    );

    await waitFor(() => {
      expect(screen.getByTestId('loading')).toHaveTextContent('not-loading');
      expect(screen.getByTestId('user')).toHaveTextContent('no-user');
    });
  });

  it('should load user from token on mount', async () => {
    const mockUser = { id: 1, username: 'testuser', email: 'test@example.com' };
    localStorage.setItem('token', 'valid-token');
    mockedAxios.get.mockResolvedValueOnce({ data: mockUser });

    render(
      <AuthProvider>
        <TestComponent />
      </AuthProvider>
    );

    await waitFor(() => {
      expect(screen.getByTestId('user')).toHaveTextContent('testuser');
      expect(mockedAxios.defaults.headers.common['Authorization']).toBe('Bearer valid-token');
    });
  });

  it('should handle login successfully', async () => {
    const mockLoginResponse = { data: { access_token: 'new-token' } };
    const mockUserResponse = { data: { id: 1, username: 'testuser', email: 'test@example.com' } };

    mockedAxios.post.mockResolvedValueOnce(mockLoginResponse);
    mockedAxios.get.mockResolvedValueOnce(mockUserResponse);

    render(
      <AuthProvider>
        <TestComponent />
      </AuthProvider>
    );

    const loginButton = screen.getByText('Login');
    loginButton.click();

    await waitFor(() => {
      expect(localStorage.getItem('token')).toBe('new-token');
      expect(mockedAxios.defaults.headers.common['Authorization']).toBe('Bearer new-token');
      expect(screen.getByTestId('user')).toHaveTextContent('testuser');
    });
  });

  it('should handle register successfully', async () => {
    const mockRegisterResponse = { data: { access_token: 'new-token' } };
    const mockUserResponse = { data: { id: 1, username: 'testuser', email: 'test@example.com' } };

    mockedAxios.post.mockResolvedValueOnce(mockRegisterResponse);
    mockedAxios.get.mockResolvedValueOnce(mockUserResponse);

    render(
      <AuthProvider>
        <TestComponent />
      </AuthProvider>
    );

    const registerButton = screen.getByText('Register');
    registerButton.click();

    await waitFor(() => {
      expect(localStorage.getItem('token')).toBe('new-token');
      expect(screen.getByTestId('user')).toHaveTextContent('testuser');
    });
  });

  it('should handle logout', async () => {
    const mockUser = { id: 1, username: 'testuser', email: 'test@example.com' };
    localStorage.setItem('token', 'valid-token');
    mockedAxios.get.mockResolvedValueOnce({ data: mockUser });

    render(
      <AuthProvider>
        <TestComponent />
      </AuthProvider>
    );

    await waitFor(() => {
      expect(screen.getByTestId('user')).toHaveTextContent('testuser');
    });

    const logoutButton = screen.getByText('Logout');
    logoutButton.click();

    await waitFor(() => {
      expect(localStorage.getItem('token')).toBeNull();
      expect(screen.getByTestId('user')).toHaveTextContent('no-user');
    });
  });
});