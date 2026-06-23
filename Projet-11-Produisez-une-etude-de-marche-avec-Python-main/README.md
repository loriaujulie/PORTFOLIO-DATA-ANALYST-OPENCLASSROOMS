# 🐔 **Projet 11 – Analyse de Marché & Recommandations d’Expansion Internationale**  
### *La Poule Qui Chante – Étude stratégique Data Analyst*

## 🎯 **Objectif du projet**
Identifier les pays les plus pertinents pour exporter du poulet biologique français, en s’appuyant sur une analyse statistique robuste et un cadrage business clair.  
L’étude vise à fournir au COMEX une **recommandation argumentée**, basée sur des données économiques, démographiques, politiques et sectorielles.

<img width="1119" height="628" alt="p11 Capture d’écran 2026-06-22 121642" src="https://github.com/user-attachments/assets/8f0e9273-c00f-4c33-8c21-a8e3936e0084" />
<img width="1119" height="582" alt="p11 Capture d’écran 2026-06-22 121720" src="https://github.com/user-attachments/assets/3b2fb648-1c95-4544-b2a2-065332121186" />
<img width="1119" height="628" alt="p11 Capture d’écran 2026-06-22 121751" src="https://github.com/user-attachments/assets/6ab62a28-d71e-4092-a299-2da77927f10e" />
<img width="1120" height="628" alt="p11 Capture d’écran 2026-06-22 121816" src="https://github.com/user-attachments/assets/a6cd5704-d1e4-451d-a6d9-a963d453ca1a" />

## 📂 Données utilisées
- **FAO** : disponibilité alimentaire, production, importations de volaille  
- **Banque Mondiale** : PIB/habitant, stabilité politique, facilité de faire des affaires  
- **CEPII** : distances géographiques  
- **Population mondiale** (2000–2018)

### 🧹 Préparation et Nettoyage des données
- Harmonisation des noms de pays (mapping multi-sources)  
- Nettoyage complet : valeurs manquantes, doublons, types, unités  
- Sélection de l’année **2017** pour garantir la cohérence inter-sources  
- Feature engineering :  
  - Production/habitant  
  - Importations/habitant  
  - TDI (taux de dépendance aux importations)  
- Constitution d’une table unique pour l’analyse multivariée  

## 🔍 **Méthodologie analytique**
### **1. Analyse exploratoire**
- Vérification des distributions  
- Détection et interprétation des outliers  
- Corrélations entre variables économiques, politiques et alimentaires  

### **2. ACP (Analyse en Composantes Principales)**
- 4 composantes expliquant **75 %** de la variance  
- Visualisation des axes pour comprendre les dynamiques pays  
- Identification des variables structurantes : PIB, stabilité politique, dépendance aux importations…

### **3. Clustering**
- CAH + K-means  
- Tests d’inertie et silhouette  
- Choix final : **4 clusters** cohérents économiquement et géographiquement  

---



