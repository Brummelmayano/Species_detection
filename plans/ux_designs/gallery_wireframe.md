# Wireframe - Gallery

## Description
Galerie d'images traitées avec filtres et recherche pour naviguer dans les collections.

## Layout Général
```
+-----------------------------+
| Header: Logo | Navigation  |
+-----------------------------+
| Sidebar: Menu               |
+-----------------------------+
| Main Content                |
|                             |
| [Filtres et Recherche]      |
| +-------------------------+ |
| | Projet: [Dropdown]      | |
| | Espèce: [Champ]         | |
| | Date: [Calendrier]      | |
| | [Rechercher]           | |
| +-------------------------+ |
|                             |
| [Vue Grille]                |
| +---+ +---+ +---+ +---+     |
| |Img| |Img| |Img| |Img|     |
| |   | |   | |   | |   |     |
| |Esp| |Esp| |Esp| |Esp|     |
| +---+ +---+ +---+ +---+     |
|                             |
| [Pagination]                |
| +-------------------------+ |
| | < 1 2 3 ... 10 >       | |
| +-------------------------+ |
|                             |
| [Actions Groupées]          |
| +-------------------------+ |
| | [Sélectionner Tout]     | |
| | [Télécharger] [Supprimer]| |
| +-------------------------+ |
+-----------------------------+
```

## Éléments Clés
- **Filtres et Recherche** : Options pour affiner la vue (projet, espèce, date).
- **Vue Grille** : Miniatures avec overlay d'espèces détectées.
- **Pagination** : Navigation pour gros volumes.
- **Actions Groupées** : Opérations sur plusieurs images sélectionnées.

## Responsive
- Mobile : Grille 2 colonnes, filtres en modal.