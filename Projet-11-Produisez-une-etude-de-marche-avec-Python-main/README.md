# 🐔 **Projet 11 – Analyse de Marché & Recommandations d’Expansion Internationale**  
### *La Poule Qui Chante – Étude stratégique Data Analyst*

## 🎯 **Objectif du projet**
Identifier les pays les plus pertinents pour exporter du poulet biologique français, en s’appuyant sur une analyse statistique robuste et un cadrage business clair.  
L’étude vise à fournir au COMEX une **recommandation argumentée**, basée sur des données économiques, démographiques, politiques et sectorielles.

---

## 📊 **Sources & Préparation des Données**
### **Sources mobilisées**
- **FAO** : disponibilité alimentaire, production, importations de volaille  
- **Banque Mondiale** : PIB/habitant, stabilité politique, facilité de faire des affaires  
- **CEPII** : distances géographiques  
- **Population mondiale** (2000–2018)

### **Étapes de préparation**
- Harmonisation des noms de pays (mapping multi-sources)  
- Nettoyage complet : valeurs manquantes, doublons, types, unités  
- Sélection de l’année **2017** pour garantir la cohérence inter-sources  
- Feature engineering :  
  - Production/habitant  
  - Importations/habitant  
  - TDI (taux de dépendance aux importations)  
- Constitution d’une table unique pour l’analyse multivariée  

---

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

## 🌍 **Résultats – Segmentation des pays**
### **Cluster cible retenu : Cluster 1**
Caractéristiques :
- Pouvoir d’achat élevé  
- Stabilité politique forte  
- Forte dépendance aux importations de volaille  
- Proximité géographique favorable (faible empreinte carbone)

### **Top 10 des pays cibles**
1. **Allemagne**  
2. **Émirats Arabes Unis**  
3. **Danemark**  
4. **Autriche**  
5. Suède  
6. Suisse  
7. Irlande  
8. Luxembourg  
9. Norvège  
10. Islande  

---

## 🥇 **Recommandation finale**
Les pays les plus pertinents pour une première phase d’expansion sont :

### 🇩🇪 **Allemagne**  
- Marché très proche  
- Importations massives  
- Stabilité politique élevée  
- Population importante  
- Normes européennes harmonisées

### 🇩🇰 **Danemark**  
- Très forte stabilité  
- Pouvoir d’achat élevé  
- Forte dépendance aux importations

### 🇦🇹 **Autriche**  
- Marché premium  
- Très bonne stabilité  
- Forte capacité d’achat

---

## 📌 **Pourquoi ces pays ?**
- **Logistique optimisée** (proximité, transport terrestre)  
- **Réglementation commune** (UE)  
- **Marchés solvables et demande forte**  
- **Empreinte carbone réduite**  
- **Concurrence maîtrisable**  

---

## 🧭 **Conclusion**
L’analyse statistique et économique converge vers une stratégie d’expansion européenne ciblée, priorisant des marchés **riches, stables, proches et fortement importateurs**.  
L’Allemagne, le Danemark et l’Autriche constituent un **socle optimal** pour une première phase d’exportation.
