# Parcours Utilisateurs - Application de Détection d'Espèces

## Vue d'Ensemble
Basé sur les personas et scénarios du PRD, voici les parcours utilisateurs principaux pour l'application.

## Parcours 1: Upload et Détection Automatique (Agent de Conservation)
```mermaid
journey
    title Parcours Upload et Détection
    section Connexion
        Se connecter à l'application: 5: Agent de Conservation
    section Upload
        Naviguer vers page Upload: 5: Agent de Conservation
        Sélectionner images depuis piège: 4: Agent de Conservation
        Uploader les images: 4: Agent de Conservation
    section Traitement
        Attendre traitement automatique: 3: Agent de Conservation
        Recevoir notification de complétion: 5: Agent de Conservation
    section Vérification
        Examiner résultats dans Gallery: 4: Agent de Conservation
        Corriger si nécessaire: 3: Agent de Conservation
```

## Parcours 2: Analyse et Révision (Chercheur en Biodiversité)
```mermaid
journey
    title Parcours Analyse et Révision
    section Accès
        Se connecter et accéder au Dashboard: 5: Chercheur
    section Exploration
        Parcourir Gallery des images traitées: 4: Chercheur
        Ouvrir Image Viewer pour détails: 5: Chercheur
    section Révision
        Vérifier détections automatiques: 4: Chercheur
        Annoter et corriger erreurs: 4: Chercheur
        Sauvegarder modifications: 5: Chercheur
    section Export
        Générer rapports depuis Reports: 4: Chercheur
        Exporter données pour analyse: 5: Chercheur
```

## Parcours 3: Gestion de Projet (Administrateur)
```mermaid
journey
    title Parcours Gestion de Projet
    section Administration
        Se connecter avec rôle Admin: 5: Administrateur
        Accéder au Dashboard de gestion: 5: Administrateur
    section Supervision
        Vérifier statut des uploads: 4: Administrateur
        Gérer utilisateurs et permissions: 4: Administrateur
    section Rapports
        Consulter métriques dans Reports: 5: Administrateur
        Générer rapports d'audit: 4: Administrateur
```

## Parcours 4: Apprentissage (Étudiant)
```mermaid
journey
    title Parcours Apprentissage
    section Découverte
        Se connecter et explorer Dashboard: 5: Étudiant
        Suivre tutoriels intégrés: 4: Étudiant
    section Interaction
        Tester upload d'images simples: 4: Étudiant
        Observer détections dans Gallery: 5: Étudiant
        Utiliser Image Viewer pour comprendre: 4: Étudiant
    section Apprentissage
        Lire explications sur les espèces: 5: Étudiant
        Accéder à visualisations simples: 4: Étudiant