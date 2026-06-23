# 📘 Projet 10 — Analyse mondiale de l’accès à l’eau potable  
### *Tableau de bord Power BI – Vue mondiale, continentale et nationale*

## 🎯 Objectif du projet  
Concevoir un tableau de bord Power BI permettant d’identifier les pays prioritaires selon trois axes d’intervention :  
1. **Création de services** (déploiement d’infrastructures d’accès à l’eau)  
2. **Modernisation des services existants**  
3. **Consulting & accompagnement politique**

L’enjeu principal : fournir une **vision claire, fiable et actionnable** de la situation mondiale de l’accès à l’eau, en croisant plusieurs sources internationales.

<img width="1413" height="794" alt="p10 Capture d’écran 2026-06-22 121500" src="https://github.com/user-attachments/assets/a2ac047d-00f0-493f-990b-324f167bb483" />
<img width="1415" height="796" alt="p10 Capture d’écran 2026-06-22 121528" src="https://github.com/user-attachments/assets/21087724-8501-410c-b786-76eeda0f2015" />
<img width="1411" height="793" alt="p10 Capture d’écran 2026-06-22 121549" src="https://github.com/user-attachments/assets/655607df-12a3-498c-8e86-03af9832709a" />

## 📂 Données utilisées
Données issues de plusieurs organismes internationaux :

- **OMS** : mortalité liée à l’eau insalubre, accès à l’eau potable (urbain/rural), installations basiques  
- **FAO** : population mondiale  
- **World Bank** : accès à l’électricité, indicateurs socio-économiques  
- **DataGouv** : infrastructures aéroportuaires  
- **Indices de stabilité politique**

Un travail important d’harmonisation a été nécessaire pour **aligner les noms de pays**, les années et les unités.

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
