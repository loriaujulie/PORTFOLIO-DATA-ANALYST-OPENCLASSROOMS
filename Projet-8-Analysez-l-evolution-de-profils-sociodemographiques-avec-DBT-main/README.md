# 📘 README — Analyse du Profil Sociodémographique des Étudiants (2022‑2025)

## 🎯 Objectif du projet  
Ce projet vise à analyser l’évolution du profil sociodémographique des étudiants inscrits au parcours **Data Analyst** entre **2022 et 2025**, en croisant les données internes OpenClassrooms avec les données publiques de l’INSEE.  
L’objectif est double :  
- **Mieux comprendre les dynamiques d’âge, de genre et de répartition territoriale**.  
- **Industrialiser la transformation des données** via un pipeline **DBT** fiable, documenté et reproductible.

---

## 🗂️ Sources de données  
### Données internes OpenClassrooms  
- Inscriptions aux parcours Data Analyst  
- Variables : `USER_ID`, `YEAR_PATH_STARTED`, `REGION`, `GENDER`, `AGE_GROUP`, `NB_ETUDIANTS`  

### Données INSEE  
- Référentiel démographique régional (2022–2025)  
- Variables : `POPULATION`, `REGION`, `GENRE`, `TRANCHE_AGE`  

Un travail d’harmonisation a été nécessaire (régions, tranches d’âge, genre).

---

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

---

## 🔐 Conformité RGPD  
- Données strictement **agrégées** (aucune donnée personnelle conservée)  
- Hébergement Snowflake **EU‑Paris**  
- Accès restreint (RBAC)  
- Risque de ré‑identification **très faible**  

---

## 📊 Principaux résultats  
- **3 401 étudiants analysés**  
- Sur‑représentation marquée des **30‑34 ans**  
- Ratio **H/F très déséquilibré**, avec une sous‑représentation persistante des femmes  
- **Île‑de‑France** largement sur‑représentée (+25 pts vs population nationale)  
- Cohortes stables sur la période 2022‑2025  

---

## 💡 Recommandations  
- **Renforcer la féminisation** (partenariats, communication ciblée)  
- **Développer les 20‑24 ans** via des formats adaptés  
- **Rééquilibrer territorialement** (DROM, régions sous‑représentées)  
- **Industrialiser le pilotage** via dashboards automatisés  

---

## 🔭 Limites & pistes d’amélioration  
- Données OC **agrégées**, limitant les analyses fines  
- Données 2025 **partielles**  
- Comparaison avec la population totale et non la population active  
- Pistes : intégrer **niveau d’études**, **statut professionnel**, **population active INSEE**
