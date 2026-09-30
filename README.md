# python-analyste

Scripts d'apprentissage Python pour l'analyse de données, avec pandas.

## m3.py — Pipeline de consolidation d'exports marketing

Ingère un dossier d'exports CSV hétérogènes, les nettoie, les consolide et produit un fichier unique exploitable, en une commande.

### Ce que fait le pipeline

- **Découverte automatique** : parcourt le dossier `donnees/` et traite tous les CSV présents, sans avoir à les lister dans le code
- **Chargement de formats hétérogènes** : gère les différences d'encodage (utf-8, cp1252), de séparateur (virgule, point-virgule, tabulation) et les lignes d'en-tête parasites
- **Nettoyage** : harmonisation des noms de colonnes, normalisation des libellés de canaux, conversion des montants au format français (espaces, virgules décimales, symbole €), typage des dates, suppression des doublons et des lignes de total
- **Tolérance aux erreurs** : un fichier non conforme est signalé et ignoré, sans interrompre le traitement des autres
- **Rapport qualité** : nombre de fichiers traités et en échec, comptage des valeurs manquantes par colonne, et liste des lignes concernées
- **Consolidation** : empilement des sources, calcul du coût par conversion, agrégation par canal, export d'un CSV trié par date

### Structure du dépôt

- `donnees/` — les exports bruts, non modifiés
- `sorties/` — le fichier consolidé produit par le script
- `m3.py` — le pipeline
- `m1.py`, `m2.py`, `m2-2.py` — exercices d'apprentissage

### Utilisation

py -V:3.12 m3.py


Pour ajouter une nouvelle source, déposer le fichier dans `donnees/` et ajouter sa fiche dans le dictionnaire `CONFIGS` : séparateur, encodage, lignes à ignorer, correspondance des colonnes et format de date. Le code de traitement n'a pas à être modifié.

### Choix de conception

- **Les valeurs manquantes ne sont ni comblées ni supprimées.** Remplacer un montant absent par 0 fausserait silencieusement les ratios : le coût par conversion apparaîtrait plus bas que la réalité. Les trous sont conservés et listés dans le rapport qualité, pour être remontés au producteur de la donnée plutôt que corrigés en aval.
- **Les valeurs non convertibles sont neutralisées, pas ignorées.** Une dépense saisie en texte libre devient une valeur manquante explicite, comptabilisée dans le rapport.
- **La configuration est séparée du traitement.** Les spécificités de chaque source vivent dans un dictionnaire, la logique de nettoyage est unique et partagée.

### Stack

Python 3.12, pandas, pathlib