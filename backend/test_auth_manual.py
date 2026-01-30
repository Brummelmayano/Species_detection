#!/usr/bin/env python3
"""
Script de test manuel pour l'authentification FastAPI
Utilise requests pour simuler les interactions utilisateur
"""

import requests
import json
import sys

# Configuration du serveur
BASE_URL = "http://localhost:8000"
AUTH_URL = f"{BASE_URL}/auth"

def print_separator(title):
    print(f"\n{'='*50}")
    print(f" {title}")
    print(f"{'='*50}")

def test_register():
    """Test de l'inscription d'un nouvel utilisateur"""
    print_separator("TEST: Inscription d'utilisateur")

    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpass123",
        "full_name": "Test User",
        "role": "USER"
    }

    try:
        response = requests.post(f"{AUTH_URL}/register", json=user_data)
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            token_data = response.json()
            print("✅ Inscription réussie!")
            print(f"Token reçu: {token_data.get('access_token', 'N/A')[:50]}...")
            return token_data.get('access_token')
        else:
            print("❌ Échec de l'inscription:")
            print(f"Response: {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur de connexion: {e}")
        return None

def test_login():
    """Test de connexion"""
    print_separator("TEST: Connexion")

    login_data = {
        "username": "testuser",
        "password": "testpass123"
    }

    try:
        response = requests.post(f"{AUTH_URL}/login", data=login_data)
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            token_data = response.json()
            print("✅ Connexion réussie!")
            print(f"Token reçu: {token_data.get('access_token', 'N/A')[:50]}...")
            return token_data.get('access_token')
        else:
            print("❌ Échec de connexion:")
            print(f"Response: {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur de connexion: {e}")
        return None

def test_get_me(token):
    """Test d'accès aux informations utilisateur"""
    print_separator("TEST: Accès aux informations utilisateur (/me)")

    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = requests.get(f"{AUTH_URL}/me", headers=headers)
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            user_data = response.json()
            print("✅ Accès réussi aux informations utilisateur!")
            print(f"Utilisateur: {user_data.get('username', 'N/A')}")
            print(f"Email: {user_data.get('email', 'N/A')}")
            print(f"Rôle: {user_data.get('role', 'N/A')}")
        else:
            print("❌ Échec d'accès aux informations utilisateur:")
            print(f"Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur de connexion: {e}")

def test_unauthorized_access():
    """Test d'accès sans token (devrait échouer)"""
    print_separator("TEST: Accès non autorisé (sans token)")

    try:
        response = requests.get(f"{AUTH_URL}/me")
        print(f"Status Code: {response.status_code}")

        if response.status_code == 401:
            print("✅ Accès correctement refusé (401 Unauthorized)")
        else:
            print("⚠️ Réponse inattendue:")
            print(f"Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur de connexion: {e}")

def test_invalid_token():
    """Test avec un token invalide"""
    print_separator("TEST: Token invalide")

    headers = {"Authorization": "Bearer invalid_token_123"}

    try:
        response = requests.get(f"{AUTH_URL}/me", headers=headers)
        print(f"Status Code: {response.status_code}")

        if response.status_code == 401:
            print("✅ Token invalide correctement rejeté (401 Unauthorized)")
        else:
            print("⚠️ Réponse inattendue:")
            print(f"Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur de connexion: {e}")

def main():
    """Fonction principale pour exécuter tous les tests"""
    print("🚀 Démarrage des tests d'authentification manuels")
    print(f"Serveur cible: {BASE_URL}")
    print("\nAssurez-vous que le serveur FastAPI est en cours d'exécution!")

    # Test 1: Inscription
    token = test_register()

    if not token:
        # Si l'inscription échoue (utilisateur existe déjà), essayer la connexion
        print("\nℹ️ Tentative de connexion avec un utilisateur existant...")
        token = test_login()

    if not token:
        print("\n❌ Impossible d'obtenir un token. Arrêt des tests.")
        sys.exit(1)

    # Test 2: Accès autorisé
    test_get_me(token)

    # Test 3: Accès non autorisé
    test_unauthorized_access()

    # Test 4: Token invalide
    test_invalid_token()

    print_separator("FIN DES TESTS")
    print("🎉 Tests terminés!")

if __name__ == "__main__":
    main()