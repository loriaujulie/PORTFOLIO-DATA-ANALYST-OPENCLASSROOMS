# 📌 Projet 6 — Analyse du stock et des ventes du site Bottleneck  
*Réalisation d’une analyse exploratoire et d’un reporting métier*

## 🎯 Objectif du projet  
Dans ce projet, j’ai analysé les données issues du site e‑commerce **Bottleneck – Fine Wine & Spirit** afin d’identifier :  
- les produits les plus performants en termes de ventes et de chiffre d’affaires,  
- les produits problématiques (prix incohérents, stocks négatifs, ventes nulles),  
- les tendances générales du catalogue (prix, volumes, marges),  
- les corrélations entre prix, ventes et stock,  
- les axes d’amélioration pour optimiser la gestion commerciale.

<img width="957" height="537" alt="p6 Capture d’écran 2026-06-22 120554" src="https://github.com/user-attachments/assets/4ef59b4c-39fe-4afb-8acf-d52ad3f0fc17" />
<img width="958" height="536" alt="p6 Capture d’écran 2026-06-22 120617" src="https://github.com/user-attachments/assets/87149ce3-01d5-4e8a-b56d-537b5f835cc3" />
<img width="960" height="538" alt="p6 Capture d’écran 2026-06-22 120645" src="https://github.com/user-attachments/assets/b7853892-fdae-4c89-ae50-04cc957cab3d" />

## 📂 Données utilisées
L’analyse repose sur trois fichiers :  
- `erp.xlsx`  
- `web.xlsx`  
- `liaison.xlsx`  
Ces fichiers ont été fusionnés après nettoyage pour obtenir une base consolidée.

# 🧹 Nettoyage et préparation des données

### ✔️ Étapes réalisées  
- Analyse exploratoire des trois fichiers (dimensions, types, valeurs manquantes, incohérences).  
- Correction des anomalies :  
  - prix négatifs,  
  - stocks négatifs,  
  - incohérences entre `stock_status` et `stock_quantity`,  
  - valeurs manquantes dans les SKU.  
- Création d’une copie du fichier web pour éviter d’écraser les données initiales.  
- Sélection des colonnes pertinentes pour l’analyse métier.  
- Fusion des datasets via la table de liaison (`product_id` ↔ `sku`).  
- Vérification systématique des merges via `df.info()`.

### ✔️ Choix méthodologiques  
- Les produits avec prix négatif ont été conservés mais passés en *outofstock* en attendant un inventaire.  
- Les stocks négatifs ont été signalés et exclus des analyses de performance.  
- Les colonnes non pertinentes pour l’analyse métier (ex. `post_content`, `guid`, `rating_count`) ont été supprimées.
