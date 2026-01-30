# Wireframe - Dashboard

## Description
Le dashboard est la page d'accueil de l'application, offrant un aperçu rapide des projets, statistiques et actions récentes.

## Layout Général
```
+-----------------------------+
| Header: Logo | Navigation  |
+-----------------------------+
| Sidebar: Menu (Dashboard,   |
| Upload, Gallery, Reports)   |
+-----------------------------+
| Main Content                |
|                             |
| [Statistiques Clés]         |
| +-------------------------+ |
| | Images traitées: 1,234  | |
| | Espèces détectées: 56   | |
| | Projets actifs: 3       | |
| +-------------------------+ |
|                             |
| [Actions Rapides]           |
| +-------------------------+ |
| | [Upload Images]         | |
| | [Voir Gallery]          | |
| | [Générer Rapport]       | |
| +-------------------------+ |
|                             |
| [Projets Récents]           |
| +-------------------------+ |
| | Projet A - 50 images    | |
| | Projet B - 120 images   | |
| | Projet C - 75 images    | |
| +-------------------------+ |
|                             |
| [Notifications]             |
| +-------------------------+ |
| | Traitement terminé pour  | |
| | batch XYZ               | |
| +-------------------------+ |
+-----------------------------+
```

## Éléments Clés
- **Header** : Logo à gauche, navigation utilisateur (profil, déconnexion) à droite.
- **Sidebar** : Navigation principale avec icônes.
- **Statistiques Clés** : Cartes avec métriques importantes.
- **Actions Rapides** : Boutons pour les tâches communes.
- **Projets Récents** : Liste des projets avec statut.
- **Notifications** : Alertes récentes (traitements terminés, erreurs).

## Responsive
- Mobile : Sidebar devient menu hamburger, statistiques en grille verticale.