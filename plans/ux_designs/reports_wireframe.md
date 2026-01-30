# Wireframe - Reports

## Description
Page de génération et visualisation de rapports sur les données de détection d'espèces.

## Layout Général
```
+-----------------------------+
| Header: Logo | Navigation  |
+-----------------------------+
| Sidebar: Menu               |
+-----------------------------+
| Main Content                |
|                             |
| [Sélection de Rapport]      |
| +-------------------------+ |
| | Type: [Dropdown]        | |
| | Période: [Calendrier]   | |
| | Projet: [Dropdown]      | |
| | [Générer Rapport]       | |
| +-------------------------+ |
|                             |
| [Visualisations]            |
| +-------------------------+ |
| | [Graphique Espèces]     | |
| | [Carte Distribution]    | |
| | [Tendances Temporelles] | |
| +-------------------------+ |
|                             |
| [Tableau de Données]        |
| +-------------------------+ |
| | Espèce | Taxonomie | Comptage | %  | |
| |--------|-----------|----------|-----| |
| | Lion   | Mammalia;Carnivora;Felidae;Panthera;leo | 45 | 30% | |
| | Éléphant| Mammalia;Proboscidea;Elephantidae;Loxodonta;africana | 32 | 21% | |
| +-------------------------+ |
|                             |
| [Actions]                   |
| +-------------------------+ |
| | [Exporter PDF]          | |
| | [Exporter CSV]          | |
| | [Partager]              | |
| +-------------------------+ |
+-----------------------------+
```

## Éléments Clés
- **Sélection de Rapport** : Paramètres pour personnaliser le rapport.
- **Visualisations** : Graphiques et cartes interactives.
- **Tableau de Données** : Données brutes exportables.
- **Actions** : Options d'export et partage.

## Responsive
- Mobile : Visualisations empilées, tableau scrollable horizontalement.