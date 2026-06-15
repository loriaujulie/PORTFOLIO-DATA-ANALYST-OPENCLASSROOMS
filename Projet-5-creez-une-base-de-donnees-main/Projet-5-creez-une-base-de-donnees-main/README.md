# 🏡 Projet 5 — Créer et exploiter une base de données immobilière  
*Parcours Data Analyst – OpenClassrooms*

## 🎯 Objectif du projet  
L’objectif de ce projet était de construire une base de données relationnelle complète à partir de données immobilières publiques (DVF, INSEE, référentiel géographique), puis d’exécuter des requêtes SQL permettant d’analyser le marché immobilier français.

Ce travail s’inscrit dans le cadre du projet **DATAImmo**, mené pour l’entreprise fictive **Laplace Immo**, un réseau national d’agences immobilières souhaitant améliorer la prédiction des prix de vente et accompagner ses clients grâce à une base de données fiable et normalisée.

---

## 📂 Données utilisées  
Les données initiales proviennent de plusieurs sources :

- **DVF (Demandes de Valeurs Foncières)** — transactions immobilières en France  
- **INSEE** — recensement des populations  
- **Référentiel géographique** (régions, départements, communes)  
- Fichiers Excel fournis par la CTO de Laplace Immo  

Un important travail de tri, de compréhension et de sélection des colonnes a été réalisé afin de ne conserver que les données pertinentes pour le besoin métier.

---

## 🔐 Stratégie RGPD et conformité  
La construction de la base a été menée dans le respect des principes du RGPD :

### **1. Cartographie et registre**
- Création d’un dictionnaire des données complet  
- Mise en place d’un schéma relationnel clair et documenté  

### **2. Minimisation**
- Suppression des colonnes inutiles, redondantes ou non pertinentes  
- Exclusion des données sensibles (ex. : nom de l’acquéreur)

### **3. Information et consentement**
- Utilisation de données publiques et ouvertes  
- Données DVF collectées légalement lors des actes notariés  

### **4. Sécurité**
- Accès restreint à la base au sein de l’entreprise  
- Modèle final mis à disposition uniquement pour les besoins métier  

### **5. DPO**
- Le métier d’agent immobilier impliquant des données personnelles, la présence d’un DPO est indispensable  

---

## 🧱 Construction de la base de données  

### **1. Dictionnaire des données**
Un dictionnaire structuré a été élaboré pour chaque table :  
- Region  
- Departement  
- Commune  
- Local  
- Bien  
- Vente  

Chaque colonne y est décrite : type, nature, règles de gestion, règles de calcul.

### **2. Schéma relationnel normalisé**
Le modèle respecte les **formes normales 1NF, 2NF et 3NF** :  
- colonnes atomiques  
- clés primaires uniques  
- absence de dépendances transitives  

Les tables sont liées par des clés étrangères cohérentes (ex. : `dep_code`, `com_code`, `loc_code`, `id_bien`).

### **3. Création et import des tables**
Les tables ont été créées en SQL puis alimentées à partir des fichiers bruts.  
Les contrôles suivants ont été effectués :  
- cohérence des clés primaires  
- absence de doublons  
- correspondance entre les volumes attendus et les volumes importés  

Exemples de résultats :  
- 34 991 communes  
- 34 169 biens  
- 34 169 ventes  
- 19 régions  
- 109 départements  

---

## 🔍 Requêtes SQL réalisées  
Une **vue “jointure”** a été créée pour simplifier les requêtes et améliorer la maintenabilité.

Les analyses suivantes ont été menées :

### **1. Nombre total d’appartements vendus au 1er semestre 2020**  
→ **31 378 ventes**

### **2. Nombre de ventes d’appartements par région**  
→ L’Île‑de‑France arrive largement en tête (**13 995 ventes**)

### **3. Répartition des ventes d’appartements par nombre de pièces**  
→ Les T2 et T3 représentent la majorité des transactions

### **4. Top 10 des départements les plus chers au m²**  
→ Paris en tête (**12 083 €/m²**)

### **5. Prix moyen du m² d’une maison en Île‑de‑France**  
→ **3 764 €/m²**

### **6. Top 10 des appartements les plus chers**  
→ Tous situés en Île‑de‑France

### **7. Taux d’évolution des ventes entre T1 et T2 2020**  
→ **+3,68 %**

### **8. Classement des régions selon le prix au m² des appartements > 4 pièces**  
→ L’Île‑de‑France reste la région la plus chère

### **9. Communes ayant eu au moins 50 ventes au T1 2020**  
→ Paris, Nice, Bordeaux, Marseille, etc.

### **10. Différence de prix au m² entre T2 et T3**  
→ **–12,67 %** (les T3 sont moins chers au m²)

### **11. Top 3 des communes les plus chères dans les départements 6, 13, 33, 59 et 69**  
→ Exemples : Saint‑Jean‑Cap‑Ferrat, Lège‑Cap‑Ferret, Ville‑sur‑Jarnioux…

---

## 🗂 Structure du dépôt  
```
📁 Projet_05_Creation_BDD_Immobiliere
│── README.md
│── LORIAU_Julie_2_support_presentation_122025.pdf
└── LORIAU_Julie_1_dictionnaire_des_donnees_122025.xlsx
```

---

## 🚀 Ce que ce projet démontre  
Ce projet met en avant ma capacité à :

- analyser et structurer des données brutes  
- concevoir une base de données relationnelle normalisée  
- rédiger un dictionnaire des données complet  
- implémenter une base SQL cohérente et fiable  
- exécuter des requêtes avancées pour analyser le marché immobilier  
- présenter des résultats clairs et exploitables pour un besoin métier  

Il constitue une étape essentielle dans la maîtrise de SQL et de la modélisation de données.
