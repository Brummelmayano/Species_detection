# Wireframe - Page Upload

## Description
Page dédiée à l'upload d'images depuis les pièges photographiques, avec options pour métadonnées.

## Layout Général
```
+-----------------------------+
| Header: Logo | Navigation  |
+-----------------------------+
| Sidebar: Menu               |
+-----------------------------+
| Main Content                |
|                             |
| [Sélection de Projet]       |
| +-------------------------+ |
| | Projet: [Dropdown]      | |
| +-------------------------+ |
|                             |
| [Zone de Drop]              |
| +-------------------------+ |
| | Glisser-déposer vos     | |
| | images ici              | |
| | Ou [Parcourir]          | |
| +-------------------------+ |
|                             |
| [Métadonnées]               |
| +-------------------------+ |
| | Date: [Champ]           | |
| | Localisation GPS: [Champ]| |
| | Notes: [Textarea]       | |
| +-------------------------+ |
|                             |
| [Options Avancées]          |
| +-------------------------+ |
| | Traitement automatique: | |
| | [ ] Oui [ ] Non         | |
| +-------------------------+ |
|                             |
| [Bouton Upload]             |
| +-------------------------+ |
| | [Uploader 0 images]     | |
| +-------------------------+ |
|                             |
| [Progression]               |
| +-------------------------+ |
| | Upload en cours...      | |
| | [Barre de progression]  | |
| +-------------------------+ |
+-----------------------------+
```

## Éléments Clés
- **Sélection de Projet** : Associer les images à un projet existant.
- **Zone de Drop** : Interface drag-and-drop intuitive.
- **Métadonnées** : Champs pour date, GPS, notes.
- **Options Avancées** : Choix pour traitement automatique.
- **Bouton Upload** : Désactivé jusqu'à sélection d'images.
- **Progression** : Feedback en temps réel pendant l'upload.

## Responsive
- Mobile : Zone de drop plus grande, champs métadonnées en accordéon.