# 🌍 Projet 4 — Réaliser une étude de santé publique  
*Parcours Data Analyst – OpenClassrooms*

## 🎯 Objectif du projet  
L’objectif de ce projet était d’analyser plusieurs jeux de données issus de la FAO (Food and Agriculture Organization of the United Nations) afin d’étudier la situation alimentaire mondiale entre 2013 et 2017.  
L’analyse porte sur la sous‑nutrition, la disponibilité alimentaire, l’aide alimentaire et la production végétale/animale.

Ce projet m’a permis de manipuler plusieurs sources de données, de les nettoyer, de les harmoniser, puis de produire des indicateurs clés et des visualisations pertinentes.

<img width="1276" height="715" alt="p4 Capture d’écran 2026-06-22 115829" src="https://github.com/user-attachments/assets/bd204658-4d5d-407b-8060-8832940ded99" />
<img width="811" height="853" alt="p4 Capture d’écran 2026-06-22 120037" src="https://github.com/user-attachments/assets/09709eba-7fc5-4deb-a7c1-2d065a476282" />
<img width="1277" height="718" alt="P4 Capture d’écran 2026-06-22 115951" src="https://github.com/user-attachments/assets/e1d1d8c7-b06e-4859-b1d2-9156f494a7d6" />

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
