# 📘 Projet 10 — Analyse mondiale de l’accès à l’eau potable  
### *Tableau de bord Power BI – Vue mondiale, continentale et nationale*

## 🎯 Objectif du projet  
Concevoir un tableau de bord Power BI permettant d’identifier les pays prioritaires selon trois axes d’intervention :  
1. **Création de services** (déploiement d’infrastructures d’accès à l’eau)  
2. **Modernisation des services existants**  
3. **Consulting & accompagnement politique**

L’enjeu principal : fournir une **vision claire, fiable et actionnable** de la situation mondiale de l’accès à l’eau, en croisant plusieurs sources internationales.

---

## 🌍 Sources de données  
Données issues de plusieurs organismes internationaux :

- **OMS** : mortalité liée à l’eau insalubre, accès à l’eau potable (urbain/rural), installations basiques  
- **FAO** : population mondiale  
- **World Bank** : accès à l’électricité, indicateurs socio-économiques  
- **DataGouv** : infrastructures aéroportuaires  
- **Indices de stabilité politique**

Un travail important d’harmonisation a été nécessaire pour **aligner les noms de pays**, les années et les unités.

---

## 🛠️ Préparation & Modélisation  
### Étapes clés du traitement :
- Normalisation des noms de pays (création d’une table de mapping)  
- Gestion des valeurs manquantes et des doublons  
- Conversion des types (dates, numériques)  
- Création de champs calculés (DAX)  
- Vérification de la cohérence temporelle entre les tables  
- Construction d’un **modèle en étoile** optimisé pour Power BI

### Optimisation du dashboard :
- Palette bleue cohérente avec l’identité DWFA  
- Filtres croisés, navigation fluide, bouton de réinitialisation  
- Info-bulles enrichies, titres explicites, contrastes accessibles  
- Limitation du nombre de visuels pour améliorer la vitesse d’affichage

---

## 📊 Contenu du Dashboard  
Le tableau de bord est structuré en **3 vues complémentaires** :

### 1. **Vue mondiale**
- Carte choroplèthe : stabilité politique  
- Taux d’accès à l’eau potable  
- Indicateur Domaine 3 : efficacité politique (accès + mortalité)  
- Cartes de synthèse : mortalité WASH, accès à l’eau

### 2. **Vue continentale**
- Scatter plots par domaine d’expertise  
- Comparaison des taux d’accès, infrastructures basiques, population  
- Indicateurs de priorisation par continent

### 3. **Vue nationale**
- Évolution de la stabilité politique  
- Accès à l’eau en zone urbaine / rurale  
- Évolution de la population  
- Analyse détaillée par pays sélectionné

---

## 🧭 Résultats & Apports  
- Identification des zones prioritaires selon les 3 domaines  
- Mise en évidence des pays cumulant **faible accès à l’eau + forte mortalité + instabilité politique**  
- Vision claire des écarts entre zones urbaines et rurales  
- Outil interactif permettant une **prise de décision rapide et argumentée**

---

## 📌 Conclusion  
Ce projet fournit un tableau de bord complet, accessible et robuste, permettant d’appuyer les décisions stratégiques liées à l’accès à l’eau potable.  
La modélisation, la qualité des données et l’optimisation du modèle Power BI garantissent un outil fiable, évolutif et adapté aux besoins opérationnels.
