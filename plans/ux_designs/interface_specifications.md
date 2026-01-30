# Spécifications d'Interface Utilisateur

## Général
- **Thème** : Couleurs naturelles (verts, bruns) pour thème biodiversité.
- **Typographie** : Sans-serif moderne, hiérarchie claire.
- **Accessibilité** : Conformité WCAG 2.1 AA, support clavier, lecteurs d'écran.
- **Responsive** : Design mobile-first, breakpoints standard.

## Dashboard
- **Composants** : Cartes statistiques, boutons d'action, liste projets.
- **Interactions** : Clic sur cartes pour détails, boutons pour navigation rapide.
- **États** : Chargement pour métriques, notifications en temps réel.

## Upload
- **Composants** : Zone drag-and-drop, formulaires, barre progression.
- **Interactions** : Drag-and-drop, validation en temps réel, feedback upload.
- **États** : Désactivation bouton si pas d'images, progression avec pourcentage.

## Gallery
- **Composants** : Grille images, filtres, pagination, sélecteurs.
- **Interactions** : Filtrage dynamique, sélection multiple, navigation pagination.
- **États** : Survol miniatures, chargement lazy, états sélectionnés.

## Image Viewer
- **Composants** : Canvas image, outils annotation, panneau détails avec taxonomie complète.
- **Interactions** : Zoom/pan, édition boîtes, sauvegarde modifications.
- **États** : Mode édition activé, annotations temporaires.

## Reports
- **Composants** : Formulaires sélection, graphiques, tableaux avec taxonomie, boutons export.
- **Interactions** : Génération rapport, interactions graphiques, export.
- **États** : Chargement génération, aperçus interactifs.

## Navigation
- **Header** : Logo cliquable vers dashboard, menu utilisateur.
- **Sidebar** : Navigation principale, indicateurs actifs.
- **Breadcrumbs** : Pour pages profondes.

## Feedback Utilisateur
- **Messages** : Toasts pour succès/erreurs, modals pour confirmations.
- **Loading** : Skeletons, spinners appropriés.
- **Erreurs** : Messages clairs, suggestions de correction.