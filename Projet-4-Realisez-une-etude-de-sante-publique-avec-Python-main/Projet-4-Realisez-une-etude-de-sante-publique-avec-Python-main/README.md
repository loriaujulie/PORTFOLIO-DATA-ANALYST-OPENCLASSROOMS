# 🌍 Projet 4 — Réaliser une étude de santé publique  
*Parcours Data Analyst – OpenClassrooms*

## 🎯 Objectif du projet  
L’objectif de ce projet était d’analyser plusieurs jeux de données issus de la FAO (Food and Agriculture Organization of the United Nations) afin d’étudier la situation alimentaire mondiale entre 2013 et 2017.  
L’analyse porte sur la sous‑nutrition, la disponibilité alimentaire, l’aide alimentaire et la production végétale/animale.

Ce projet m’a permis de manipuler plusieurs sources de données, de les nettoyer, de les harmoniser, puis de produire des indicateurs clés et des visualisations pertinentes.

---

## 📂 Données utilisées  
Les datasets fournis par la FAO couvrent les thématiques suivantes :

- **Population mondiale**  
- **Sous‑nutrition**  
- **Disponibilité alimentaire** (kcal, protéines, matières grasses, production, pertes…)  
- **Aide alimentaire** (quantités reçues par pays)  

Période étudiée : **2013 à 2017**

---

## 🧹 Préparation et nettoyage des données  
Plusieurs étapes ont été nécessaires avant l’analyse :

- harmonisation des unités (conversion en kg, kcal, millions d’individus…)  
- suppression ou remplacement des valeurs manquantes  
- conversion des colonnes textuelles en valeurs numériques  
- création de tables intermédiaires  
- jointures entre les datasets (notamment population × sous‑nutrition pour l’année 2017)

Ces étapes ont été réalisées en Python avec **pandas**, **numpy**, **matplotlib** et **seaborn**.

---

## 🔍 Analyses réalisées  

### **1. Proportion de personnes en état de sous‑nutrition en 2017**  
- Population mondiale : **7,55 milliards**  
- Personnes sous‑alimentées : **535,7 millions**  
- Proportion mondiale : **7,10 %**

Une visualisation en camembert met en évidence l’ampleur du phénomène.

---

### **2. Nombre théorique de personnes pouvant être nourries en 2017**  
En comparant la disponibilité alimentaire mondiale au besoin nutritionnel moyen (2 200 kcal/jour), la capacité théorique dépasse la population réelle.

➡️ **+26 % de capacité supplémentaire**  
Ce résultat souligne un paradoxe : la production mondiale est suffisante, mais la répartition reste inégale.

---

### **3. Capacité alimentaire issue uniquement des végétaux**  
L’analyse montre que la disponibilité végétale seule permettrait déjà de nourrir l’ensemble de la population mondiale.

➡️ **104 % de la population mondiale pourrait être nourrie uniquement avec les végétaux**  
Ce résultat doit toutefois être nuancé : les humains ne sont pas les seuls consommateurs de végétaux (alimentation animale, pertes, usages industriels…).

---

### **4. Répartition de la disponibilité intérieure**  
La disponibilité intérieure se répartit entre :

- **Nourriture : 49,46 %**  
- **Alimentation animale : 13,23 %**  
- **Pertes : 4,6 %**  
- **Semences, traitement, autres utilisations : 32,7 %**

Cette répartition met en lumière l’importance des pertes et des usages non alimentaires.

---

### **5. Utilisation des principales céréales**  
Analyse détaillée des céréales majeures (blé, riz, maïs, orge, sorgho, millet, avoine, seigle…) :

- forte part dédiée à l’alimentation animale  
- pertes importantes selon les produits  
- disparités entre usages humains et non humains

---

### **6. Top 10 des pays les plus touchés par la sous‑nutrition (2017)**  
Exemples :  
- Haïti : **48,26 %**  
- Corée du Nord : **47,19 %**  
- Madagascar : **41,06 %**

La majorité des pays les plus touchés se situent en Afrique et en Asie.

---

### **7. Top 10 des pays ayant reçu le plus d’aide alimentaire (2013–2016)**  
Les trois pays principaux absorbent près des deux tiers de l’aide totale :

- Syrie  
- Éthiopie  
- Yémen  

Une visualisation montre l’évolution de l’aide pour les cinq pays les plus concernés.

---

### **8. Disponibilité alimentaire par habitant**  
Deux classements ont été réalisés :

- **Top 10 des pays avec la plus faible disponibilité alimentaire**  
  (ex. : République centrafricaine, Zambie, Madagascar…)

- **Top 10 des pays avec la plus forte disponibilité alimentaire**  
  (ex. : Autriche, Belgique, États‑Unis, Israël…)

---

### **9. Étude détaillée : le manioc en Thaïlande**  
- 63 millions d’habitants  
- 9 % en sous‑nutrition  
- Capacité alimentaire : **+27 %**  
- **83 % de la production de manioc est exportée**  
- La Thaïlande est le **1er exportateur mondial**  
- La Chine est le **1er importateur mondial**

---

## 📊 Visualisations  
Les graphiques produits incluent :

- camemberts  
- bar charts  
- courbes d’évolution  
- comparaisons par pays  
- analyses par produit (manioc, riz, seigle…)

Ils ont été intégrés dans la présentation finale.

---

## 🗂 Structure du dépôt  
```
📁 Projet_04_Etude_sante_publique
│── README.md
│── Loriau_Julie_2_presentation_012026.pdf
└── Loriau_Julie_3_notebook_pdf_012026.pdf
```

---

## 🚀 Ce que ce projet démontre  
Ce projet met en avant ma capacité à :

- manipuler plusieurs sources de données complexes  
- nettoyer, harmoniser et structurer des datasets volumineux  
- produire des indicateurs pertinents  
- réaliser des visualisations claires et adaptées  
- synthétiser des résultats pour une présentation professionnelle  

Il constitue une étude complète mêlant analyse statistique, enjeux de santé publique et compréhension des mécanismes alimentaires mondiaux.

