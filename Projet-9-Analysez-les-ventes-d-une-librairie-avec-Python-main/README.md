# 📘 Projet 9 — Analyse des données de la Librairie Lapage  
*Parcours Data Analyst — Julie Loriau Sensenbrenner*

## 🎯 Objectif du projet  
Ce projet vise à analyser l’activité commerciale de la librairie Lapage, à la fois sur le plan **business (CA, ventes, produits)** et sur le plan **comportemental (profils clients, corrélations statistiques)**.  
L’objectif final : fournir une vision exploitable pour le pilotage stratégique et l’optimisation marketing.

---

## 🗂️ Données utilisées  
- **Transactions** (ventes, prix, dates)  
- **Produits** (catégories, références)  
- **Clients** (âge, genre, type B2B/B2C)  
- **Sessions d’achat**  

Nettoyage réalisé :  
- Suppression doublons  
- Correction valeurs aberrantes (prix, âges)  
- Normalisation des catégories  
- Construction d’indicateurs (panier moyen, fréquence d’achat, CA client)

---

## 🧰 Stack technique  
- **Python** : pandas, numpy, seaborn, matplotlib  
- **Statistiques** : Chi², Spearman, Kruskal‑Wallis  
- **Visualisation** : Plotly / Matplotlib  
- **Jupyter Notebook**

---

## 🔍 Principaux résultats  

### 📈 Pilotage commercial  
- **CA total : 12 M€** (2021–2023)  
- **687 534 ventes** et **8 600 clients distincts**  
- Pas de saisonnalité forte : variations liées aux sorties littéraires et événements.  
- **Catégorie 1** = meilleure performance globale (volume + CA).  

### 🛒 Produits  
- **Top ventes** : majoritairement catégorie 0 et 1.  
- **Top CA** : dominé par la catégorie 2 (produits premium).  
- **Flops** : essentiellement catégorie 0 (entrée de gamme).  

### 👥 Clients B2B  
- 4 clients majeurs → **84 297 € de CA**  
- Achats concentrés sur la catégorie 0 (60 %).  
- Forte récurrence d’achat → segment stratégique à suivre.

### 👤 Clients B2C  
- **Indice de Gini : 0,40** → inégalité modérée du CA.  
- Âge médian : **55 ans**.  
- Panier moyen : **13,99 €**.  
- Répartition produits :  
  - Catégorie 0 : 60 %  
  - Catégorie 1 : 34 %  
  - Catégorie 2 : 5 %  

### 🔗 Corrélations  
- **Genre ↔ Catégorie** : p-value significative mais association très faible.  
- **Âge ↔ Montant total** : corrélation négative faible (Spearman = -0,185).  
- **Âge ↔ Fréquence d’achat** : corrélation positive modérée (0,212).  
- **Âge ↔ Catégorie** : différences significatives (Kruskal‑Wallis).  

---

## 🧭 Recommandations  
- **Segmentation marketing par âge** :  
  - Catégorie 0 → 35–50 ans  
  - Catégorie 1 → 35–60 ans  
  - Catégorie 2 → 18–30 ans  
- **Renforcer la fidélisation B2C** (programmes, offres ciblées).  
- **Suivi dédié B2B** pour sécuriser les gros comptes.  
- **Optimisation catalogue** : maintenir la catégorie 1, dynamiser la catégorie 2.

---

## 📌 Livrables  
- Notebook d’analyse complet  
- Visualisations (CA, ventes, profils clients, corrélations)  
- Rapport synthétique & recommandations  
