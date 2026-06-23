🌍 Projet 3 — Requêtez une base de données avec SQL

Analyste de données de parcours – OpenClassrooms

🎯 Objectif du projet

L'objectif de ce projet était de concevoir, manipuler et interroger une base de données relationnelle à partir de fichiers de données brutes (.csv).
Il s'agissait de modéliser les données, de créer une base fonctionnelle sous SQLite et de réaliser une série de requêtes SQL pour répondre à des problématiques métier précises 
concernant des contrats d'assurance.

<img width="1118" height="655" alt="P3 Capture d’écran 2026-06-22 115628" src="https://github.com/user-attachments/assets/6dbccead-d96c-4f52-885e-2f4287efb4ab" />
<img width="918" height="562" alt="P3 Capture d’écran 2026-06-22 115606" src="https://github.com/user-attachments/assets/38df631f-9948-4d25-ab2c-471e95926b5d" />
<img width="920" height="517" alt="p3 Capture d’écran 2026-06-22 115528" src="https://github.com/user-attachments/assets/3370d61a-239a-4047-a582-af6bcc23abd5" />
<img width="1116" height="646" alt="P3 Capture d’écran 2026-06-22 115701" src="https://github.com/user-attachments/assets/62641d17-64d7-4c89-b273-004e6ffcb352" />

📂 Données utilisées

Les données sont structurées en deux tables principales: 

Contrat : Contient les informations sur les logements assurés (ID, surface, type, cotisation, etc.).
Région : Contient les données géographiques associées (département, région, académie, commune).

🧹 Préparation et Nettoyage des données

La mise en place de la base a nécessité :

La création d'un dictionnaire de données pour définir les types (VARCHAR, INT, CHAR) et les contraintes (NOT NULL, PK, FK).  
La conception du schéma relationnel (via Power Architect) pour structurer les relations entre les tables.  
L'importation, le nettoyage et le formatage des données brutes dans le SGBD DBeaver, incluant la résolution de problèmes de correspondance entre les clés étrangères.  


📊 Visualisations

Le projet s'est concentré sur l'extraction de données via le langage SQL. 

Les résultats incluent : 
Des listes filtrées de contrats selon des critères spécifiques (ex: code postal, type de local).
Des calculs d'agrégats (moyennes de cotisation, surfaces, comptages de contrats).  
Des regroupements de données (GROUP BY) pour des analyses multicritères par région ou valeur de bien.  
Des captures d'écran des jeux de résultats SQL validant chaque requête réalisée. 


