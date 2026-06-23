# 🏡 Projet 5 — Créer et exploiter une base de données immobilière  
*Parcours Data Analyst – OpenClassrooms*

## 🎯 Objectif du projet  
L’objectif de ce projet était de construire une base de données relationnelle complète à partir de données immobilières publiques (DVF, INSEE, référentiel géographique), puis d’exécuter des requêtes SQL permettant d’analyser le marché immobilier français.

Ce travail s’inscrit dans le cadre du projet **DATAImmo**, mené pour l’entreprise fictive **Laplace Immo**, un réseau national d’agences immobilières souhaitant améliorer la prédiction des prix de vente et accompagner ses clients grâce à une base de données fiable et normalisée.

<img width="955" height="535" alt="p5 Capture d’écran 2026-06-22 120136" src="https://github.com/user-attachments/assets/40f141a9-2caf-445c-8005-10fe0916eec1" />
<img width="951" height="529" alt="p5 Capture d’écran 2026-06-22 120328" src="https://github.com/user-attachments/assets/f425c9fb-51b4-4d3e-9676-e1e1fe537d34" />
<img width="948" height="530" alt="p5 Capture d’écran 2026-06-22 120417" src="https://github.com/user-attachments/assets/6959cbad-03b8-4489-a5d9-eae854404f0c" />

## 📂 Données utilisées  
Les données initiales proviennent de plusieurs sources :

- **DVF (Demandes de Valeurs Foncières)** — transactions immobilières en France  
- **INSEE** — recensement des populations  
- **Référentiel géographique** (régions, départements, communes)  
- Fichiers Excel fournis par la CTO de Laplace Immo  

Un important travail de tri, de compréhension et de sélection des colonnes a été réalisé afin de ne conserver que les données pertinentes pour le besoin métier.

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

Les tables sont liées par des clés étrangères cohérentes (ex. : `dep_code`, `com_code`, `loc_code`, `id_bien`)
