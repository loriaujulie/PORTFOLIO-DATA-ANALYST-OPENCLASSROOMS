# 🌍 Projet 4 — Réaliser une étude de santé publique  
*Parcours Data Analyst – OpenClassrooms*

## 🎯 Objectif du projet  
L’objectif de ce projet était d’analyser plusieurs jeux de données issus de la FAO (Food and Agriculture Organization of the United Nations) afin d’étudier la situation alimentaire mondiale entre 2013 et 2017.  
L’analyse porte sur la sous‑nutrition, la disponibilité alimentaire, l’aide alimentaire et la production végétale/animale.

Ce projet m’a permis de manipuler plusieurs sources de données, de les nettoyer, de les harmoniser, puis de produire des indicateurs clés et des visualisations pertinentes.


<img width="1118" height="655" alt="P3 Capture d’écran 2026-06-22 115628" src="https://github.com/user-attachments/assets/6091c29d-3c7b-47a6-886e-56f432a9c620" />
<img width="918" height="562" alt="P3 Capture d’écran 2026-06-22 115606" src="https://github.com/user-attachments/assets/a1c2fcbe-edb1-4b2e-a9e4-ab8ec9b03fee" />
<img width="1116" height="646" alt="P3 Capture d’écran 2026-06-22 115701" src="https://github.com/user-attachments/assets/60d80222-c6b4-4a47-981b-065ba41376e2" />


## 📂 Données utilisées  
Les datasets fournis par la FAO couvrent les thématiques suivantes :
- **Population mondiale**  
- **Sous‑nutrition**  
- **Disponibilité alimentaire** 
- **Aide alimentaire**

Période étudiée : **2013 à 2017**

## 🧹 Préparation et nettoyage des données  
Plusieurs étapes ont été nécessaires avant l’analyse :

- harmonisation des unités (conversion en kg, kcal, millions d’individus…)  
- suppression ou remplacement des valeurs manquantes  
- conversion des colonnes textuelles en valeurs numériques  
- création de tables intermédiaires  
- jointures entre les datasets (notamment population × sous‑nutrition pour l’année 2017)

Ces étapes ont été réalisées en Python avec **pandas**, **numpy**, **matplotlib** et **seaborn**.

## 📊 Visualisations  
Les graphiques produits incluent :

- camemberts  
- bar charts  
- courbes d’évolution  
- comparaisons par pays  
- analyses par produit (manioc, riz, seigle…)
