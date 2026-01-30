# Wireframe - Image Viewer

## Description
Visualiseur détaillé d'une image avec annotations, boîtes de délimitation et outils d'édition.

## Layout Général
```
+-----------------------------+
| Header: Logo | Navigation  |
+-----------------------------+
| Sidebar: Menu               |
+-----------------------------+
| Main Content                |
| +-------------------------+ |
| | [Image avec Annotations]| |
| |                         | |
| | [Boîtes de délimitation] | |
| | [Labels d'espèces]      | |
| +-------------------------+ |
|                             |
| [Outils d'Édition]          |
| +-------------------------+ |
| | [Ajouter Annotation]    | |
| | [Corriger Détection]    | |
| | [Supprimer] [Sauvegarder]| |
| +-------------------------+ |
|                             |
| [Détails]                   |
| +-------------------------+ |
| | Espèce: Lion            | |
| | Taxonomie: Mammalia;     | |
| | Carnivora; Felidae;      | |
| | Panthera; leo; Lion     | |
| | Confiance: 95%          | |
| | Date: 2023-10-15        | |
| | Localisation: GPS coords| |
| +-------------------------+ |
|                             |
| [Navigation]                |
| +-------------------------+ |
| | < Précédent | Suivant > | |
| +-------------------------+ |
+-----------------------------+
```

## Éléments Clés
- **Image avec Annotations** : Affichage principal avec overlays.
- **Outils d'Édition** : Boutons pour modifier détections.
- **Détails** : Métadonnées et informations de détection.
- **Navigation** : Passer à l'image précédente/suivante.

## Responsive
- Mobile : Image zoomable, outils en bas, détails en modal.