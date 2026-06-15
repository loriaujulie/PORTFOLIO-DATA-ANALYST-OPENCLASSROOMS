# 📊 **README — Projet 7 : SANITORAL Dashboard**  
*Pilotage global des projets IT & Marketing*

## 🎯 **Objectif du projet**
Ce projet consiste à construire un **dashboard Power BI complet** permettant au client *SANITORAL* de **piloter l’ensemble de ses projets IT et Marketing** à l’échelle mondiale.

L’objectif est de fournir une vision claire et actionnable sur :  
- les **retards**,  
- les **surcoûts**,  
- les **écarts de livrables**,  
- l’**avancement global**,  
- la **performance par région, pays et projet**.

Le tableau de bord doit permettre aux différents niveaux de direction (DG, Directeurs Régionaux, Directeurs de Pays) de **prendre des décisions rapides et éclairées**.

---

# 🧩 **1. Données utilisées**
Les données proviennent de plusieurs fichiers Excel fournis par SANITORAL :

- **Projects_Locations**  
- **Projects_Plans**  
- **Actual_Costs**  
- **Actual_Duration**  
- **Actual_Delivrables**  
- **Country_Profiles**

Chaque fichier contient une partie du modèle : localisation, planning, coûts, livrables, etc.

---

# 🛠️ **2. Préparation & Transformation des données**

### ✔️ **Étape 1 — Importation dans Power Query**
- Import des fichiers Excel dans Power BI  
- Nettoyage initial :  
  - suppression des lignes vides  
  - suppression des colonnes inutiles  
  - promotion des en‑têtes  
  - uniformisation des noms de colonnes (ex : `Project_ID`)  
- Vérification du typage (dates, entiers, texte…)

### ✔️ **Étape 2 — Construction du modèle**
- Mise en place d’un **modèle en étoile** :  
  - **Tables de faits** : coûts, durées, livrables  
  - **Tables de dimensions** : pays, régions, projets  
- Vérification des cardinalités et des relations  
- Correction du typage du `Project_ID` dans *Actual_Delivrables* (passage en texte pour permettre le filtrage)

### ✔️ **Étape 3 — Mesures DAX**
Création des mesures nécessaires au pilotage :
- % de projets en retard  
- % de projets en surcoût  
- % de livrables en alerte  
- Cumul jours de retard  
- Cumul surcoût  
- Écarts prévisionnel / réel  
- Indicateurs d’alerte (> 15 %)

---

# 🧭 **3. Product Strategy Canvas**

### 👤 **Utilisateurs cibles**
- Directeur Général  
- Directeurs Régionaux  
- Directeurs de Pays  

### 📌 **Principales User Stories**
- Être alerté des projets en écart significatif (> 15 %)  
- Suivre la performance globale  
- Comparer les régions et les pays  
- Accéder au détail des projets et comprendre les causes des retards  
- Visualiser les phases critiques (retard, surcoût, livrables)

---

# 📈 **4. Contenu du Dashboard**

## 🟦 **Vue Globale**
- Synthèse mondiale  
- Nombre total de projets  
- Projets en alerte / à surveiller  
- Indicateurs clés :  
  - Avancement  
  - Coût  
  - Livraison  
- Carte interactive par région et pays  
- Recommandation stratégique automatique

---

## 🟥 **Vue Retard**
- Nombre de projets en retard  
- Cumul jours de retard  
- Histogramme des retards par phase  
- Évolution du retard par année  
- Carte des projets en retard

---

## 🟧 **Vue Coût**
- Projets en surcoût  
- Surcoût cumulé  
- Surcoût par phase  
- % de surcoût par année  
- Carte des projets en surcoût

---

## 🟩 **Vue Livrables**
- Nombre total de livrables  
- Livrables en retard  
- Retard par phase  
- % de retard par année  
- Phases en alerte / à surveiller

---

## 🟪 **Vue Gantt**
- Diagramme de Gantt interactif  
- Visualisation des phases par projet  
- Navigation par année, mois, semaine, jour  
- Accès rapide aux projets via le filtre `Project_ID`

---

# 🧠 **5. Points clés du projet**

### ✔️ Modèle de données robuste  
### ✔️ Dashboard interactif et ergonomique  
### ✔️ Indicateurs d’alerte automatisés  
### ✔️ Navigation multi‑niveaux (Monde → Région → Pays → Projet)  
### ✔️ Visualisation claire des phases critiques  
### ✔️ Recommandations stratégiques intégrées  

---

# 🚀 **6. Compétences mobilisées**
- Power BI Desktop  
- Power Query  
- Modélisation en étoile  
- DAX (mesures, KPI, indicateurs d’alerte)  
- Data cleaning  
- UX appliquée à la dataviz  
- Gestion de projet & compréhension métier  

---

# 📦 **7. Livrables**
- Dashboard Power BI complet  
- Modèle de données nettoyé et structuré  
- Product Strategy Canvas  
- Documentation du modèle  
- README (ce document)

---

# 📝 **8. Conclusion**
Ce projet m’a permis de construire un **outil de pilotage complet**, capable d’accompagner SANITORAL dans la gestion de ses projets à l’échelle mondiale.  
Le dashboard offre une vision claire, hiérarchisée et actionnable, tout en restant simple d’utilisation pour les différents niveaux de direction.
