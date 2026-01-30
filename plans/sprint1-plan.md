# Plan du Premier Sprint - Application de Détection d'Espèces

## Vue d'Ensemble
Le premier sprint se concentre sur l'implémentation des fonctionnalités de base : authentification/autorisation, upload/gestion d'images, et détection d'espèces de base. Ces épics forment la fondation de l'application.

**Objectifs du Sprint :**
- Implémenter un système d'authentification fonctionnel
- Permettre l'upload et la gestion d'images
- Intégrer la détection d'espèces basique
- Total estimé : 32 points de story

## Épic 1 : Authentification et Autorisation
**Description** : Implémenter un système de base pour la connexion des utilisateurs et la gestion des rôles.

### User Stories
- En tant qu'utilisateur, je veux pouvoir m'inscrire avec un email et un mot de passe pour accéder à l'application.
- En tant qu'utilisateur, je veux pouvoir me connecter avec mes identifiants pour accéder à mes données.
- En tant qu'administrateur, je veux pouvoir gérer les rôles des utilisateurs (viewer, editor, admin).

### Tâches Techniques
1. Créer le modèle User avec champs email, password_hash, role (enum: viewer, editor, admin)
   - **Estimation** : 2 points
2. Implémenter le router auth avec endpoints /register, /login, /logout
   - **Estimation** : 5 points
3. Ajouter middleware d'authentification avec JWT pour protéger les routes
   - **Estimation** : 3 points
4. Implémenter vérification des rôles pour les endpoints sensibles
   - **Estimation** : 2 points

**Sous-total** : 12 points

## Épic 2 : Upload et Gestion d'Images
**Description** : Permettre aux utilisateurs d'uploader des images et de les gérer dans l'application.

### User Stories
- En tant qu'utilisateur, je veux pouvoir uploader une ou plusieurs images depuis l'interface web.
- En tant qu'utilisateur, je veux voir une liste de mes images uploadées avec leurs métadonnées.
- En tant qu'utilisateur, je veux pouvoir supprimer une image si elle n'est plus nécessaire.

### Tâches Techniques
1. Créer le modèle Image avec champs filename, filepath, user_id, upload_date, metadata
   - **Estimation** : 2 points
2. Compléter l'endpoint POST /images/upload avec validation et stockage (utiliser stockage local temporaire)
   - **Estimation** : 3 points
3. Implémenter GET /images/ pour lister les images de l'utilisateur avec pagination
   - **Estimation** : 2 points
4. Implémenter DELETE /images/{id} pour supprimer une image
   - **Estimation** : 2 points
5. Ajouter validation des images (taille, format, dimensions)
   - **Estimation** : 1 point

**Sous-total** : 10 points

## Épic 3 : Détection d'Espèces de Base
**Description** : Intégrer le modèle SpeciesNet pour détecter les espèces dans les images uploadées.

### User Stories
- En tant qu'utilisateur, je veux pouvoir lancer la détection d'espèces sur une image uploadée.
- En tant qu'utilisateur, je veux voir les résultats de détection avec les boîtes de délimitation et les labels d'espèces.
- En tant qu'utilisateur, je veux voir le score de confiance pour chaque détection.

### Tâches Techniques
1. Créer le modèle DetectionResult avec champs image_id, species, confidence, bbox (x,y,w,h)
   - **Estimation** : 2 points
2. Implémenter SpeciesNetService pour l'inférence avec le modèle pré-entraîné
   - **Estimation** : 5 points
3. Créer endpoint POST /images/{id}/detect pour lancer la détection
   - **Estimation** : 3 points
4. Implémenter GET /images/{id}/results pour récupérer les résultats de détection
   - **Estimation** : 2 points

**Sous-total** : 12 points

## Critères d'Acceptation du Sprint
- Authentification fonctionnelle avec inscription/connexion
- Upload d'images avec validation basique
- Détection d'espèces sur images uploadées avec résultats visibles
- Tests unitaires pour les endpoints principaux
- Documentation API mise à jour

## Risques et Dépendances
- Disponibilité du modèle SpeciesNet (pré-entraîné)
- Configuration de la base de données PostgreSQL
- Intégration du stockage MinIO (pour le sprint suivant)

## Métriques de Succès
- Toutes les user stories implémentées et testées
- Code review passé
- Déploiement en environnement de développement réussi