# 📘 README — Analyse du Profil Sociodémographique des Étudiants (2022‑2025)

## 🎯 Objectif du projet  
Ce projet vise à analyser l’évolution du profil sociodémographique des étudiants inscrits au parcours **Data Analyst** entre **2022 et 2025**, en croisant les données internes OpenClassrooms avec les données publiques de l’INSEE.  
L’objectif est double :  
- **Mieux comprendre les dynamiques d’âge, de genre et de répartition territoriale**.  
- **Industrialiser la transformation des données** via un pipeline **DBT** fiable, documenté et reproductible.

<img width="1274" height="715" alt="p8 Capture d’écran 2026-06-22 121100" src="https://github.com/user-attachments/assets/027f2ed4-edd9-41c9-8891-d2e6d2322613" />
<img width="1276" height="719" alt="p8 Capture d’écran 2026-06-22 121133" src="https://github.com/user-attachments/assets/8708ae75-e06f-4fcf-a31c-622099f1eeee" />
<img width="1274" height="714" alt="p8 Capture d’écran 2026-06-22 121213" src="https://github.com/user-attachments/assets/c04deace-1b83-4e12-9972-e93cb735bb91" />

## 🗂️ Sources de données  
### Données internes OpenClassrooms  
- Inscriptions aux parcours Data Analyst  
- Variables : `USER_ID`, `YEAR_PATH_STARTED`, `REGION`, `GENDER`, `AGE_GROUP`, `NB_ETUDIANTS`  

### Données INSEE  
- Référentiel démographique régional (2022–2025)  
- Variables : `POPULATION`, `REGION`, `GENRE`, `TRANCHE_AGE`  

Un travail d’harmonisation a été nécessaire (régions, tranches d’âge, genre).

## 🏗️ Pipeline DBT  
Le pipeline repose sur une architecture classique :  
```
RAW → STAGING → INTERMEDIATE → MART
```

### Étapes clés  
- **Nettoyage & normalisation** (régions, âges, genre)  
- **Tests DBT** : `unique`, `not_null`, `accepted_values`  
- **Documentation YAML** + génération automatique du lineage  
- **Table finale MART** dédiée à l’analyse croisée OC × INSEE  

## 🔐 Conformité RGPD  
- Données strictement **agrégées** (aucune donnée personnelle conservée)  
- Hébergement Snowflake **EU‑Paris**  
- Accès restreint (RBAC)  
- Risque de ré‑identification **très faible**  
