# 📌 Projet 6 — Analyse du stock et des ventes du site Bottleneck  
*Réalisation d’une analyse exploratoire et d’un reporting métier*

## 🎯 Objectif du projet  
Dans ce projet, j’ai analysé les données issues du site e‑commerce **Bottleneck – Fine Wine & Spirit** afin d’identifier :  
- les produits les plus performants en termes de ventes et de chiffre d’affaires,  
- les produits problématiques (prix incohérents, stocks négatifs, ventes nulles),  
- les tendances générales du catalogue (prix, volumes, marges),  
- les corrélations entre prix, ventes et stock,  
- les axes d’amélioration pour optimiser la gestion commerciale.

L’analyse repose sur trois fichiers :  
- `erp.xlsx`  
- `web.xlsx`  
- `liaison.xlsx`  
Ces fichiers ont été fusionnés après nettoyage pour obtenir une base consolidée.

---

# 🧹 1. Nettoyage et préparation des données

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

---

# 📊 2. Analyses univariées

### 💶 Prix des produits  
- La majorité des prix se situe entre **0 et 50 €**.  
- Médiane : **23 €**.  
- Quelques produits premium (champagnes millésimés, cognacs) tirent la distribution vers le haut.  
- Aucun prix négatif après nettoyage.

### 🍾 Prix par type de produit  
- Les catégories présentent des niveaux de prix cohérents :  
  - Champagne : gamme premium  
  - Vin : large amplitude  
  - Gin / Huile d’olive : faible diversité → analyse limitée

---

# 📈 3. Analyses complémentaires

### 🛒 Répartition des ventes  
- Le volume de ventes par produit se concentre entre **5 et 11 unités**.  
- Le maximum observé atteint **36 ventes** pour un produit.  
- Aucun volume négatif après nettoyage.

### 🥇 Top 20 — Chiffre d’affaires  
- CA total du mois : **143 680 €**.  
- Le **Champagne** domine largement le classement.  
- Le Top 3 représente **plus de 3 % du CA global**.

### 🥇 Top 20 — Quantités vendues  
- Total des ventes : **5 751 bouteilles**.  
- Le vin occupe **100 % du podium** en volume.  
- Le Top 20 représente **382 unités vendues**.

### 🧊 Flop 20 — Stock  
- Valeur totale du stock : **277 300 €**.  
- Le Flop 20 représente **31 % du stock total**.  
- 95 % des produits du Flop sont… du **Champagne**.  
- Durée de stock : entre **14 et 31 mois**.

### 📉 Corrélations  
- Stock ↔ Ventes : **+0,45** (corrélation positive modérée)  
- Prix ↔ Stock : **–0,10** (faible corrélation négative)  
- Prix ↔ Ventes : **–0,52** (corrélation négative modérée)  
→ Plus le prix augmente, plus les ventes diminuent.

### 💰 Taux de marge  
- Marge moyenne autour de **60 %**.  
- Les alcools forts (whisky, cognac) sont les plus rentables.  
- Stratégie commerciale cohérente mais à confirmer sur d’autres périodes.

---

# 🚀 4. Recommandations

### 🔧 Nettoyage & cohérence  
- Revoir les produits présents dans le **TOP stock** mais dans le **FLOP ventes**.  
- Vérifier les SKU problématiques (doublons, incohérences).  
- Faire remonter les anomalies de prix et de stock aux équipes concernées.

### 📦 Gestion du stock  
- Identifier les produits à rotation lente (14–31 mois).  
- Ajuster les commandes futures pour éviter l’immobilisation financière.

### 📈 Suivi mensuel  
- Reproduire ce reporting sur plusieurs mois pour :  
  - détecter les tendances saisonnières,  
  - affiner les prévisions,  
  - ajuster les stratégies d’achat et de pricing.

---

# 🧠 5. Compétences mobilisées  
- Nettoyage avancé de données (Pandas)  
- Analyse exploratoire (EDA)  
- Visualisation (Plotly Express, Seaborn)  
- Fusion de datasets hétérogènes  
- Détection d’anomalies  
- Calculs métiers (CA, marges, corrélations)  
- Rédaction d’un rapport analytique structuré

---

# 📁 Contenu du dépôt GitHub  
- `notebook.ipynb` : Notebook complet du projet  
- `erp.xlsx`, `web.xlsx`, `liaison.xlsx` : données sources  
- `README.md` : documentation du projet (ce fichier)  
- `visualisations/` : graphiques exportés  
- `rapport_presentation.pdf` : support de présentation

---
