# 📘 Projet 12 — Détection de faux billets

*Parcours Data Analyst — Julie Loriau Sensenbrenner*

## 🎯 Objectif du projet

Ce projet a été réalisé pour le compte de l'**Organisation nationale de lutte contre le faux-monnayage (ONCFM)**. L'objectif est de concevoir un modèle de classification automatique capable de différencier les vrais des faux billets en euros à partir de leurs caractéristiques géométriques, puis d'industrialiser ce processus à l'aide d'un script fonctionnel et d'un modèle de prédiction packagé.

---

## 🗂️ Ressources & Données

L'étude s'appuie sur une base de données historique comprenant **1 500 billets scannés** :
* **1 000** vrais billets (`is_genuine = True`)
* **500** faux billets (`is_genuine = False`)

Chaque billet est caractérisé par **6 mesures géométriques** (en mm) :
* `length` : La longueur du billet.
* `height_left` : La hauteur du côté gauche.
* `height_right` : La hauteur du côté droit.
* `margin_up` : La marge supérieure.
* `margin_low` : La marge inférieure *(comporte 37 valeurs manquantes à traiter)*.
* `diagonal` : La diagonale du billet.

---

## 🏗️ Architecture du Pipeline & Modélisation

Pour éviter tout risque de *Data Leakage* (fuite de données) et garantir une industrialisation robuste, un pipeline d'apprentissage rigoureux a été mis en place via **Scikit-Learn** :

1. **Imputation** : Utilisation d'un `SimpleImputer(strategy='median')` pour combler automatiquement les 37 valeurs manquantes de la variable `margin_low` sur la base de la médiane du jeu d'entraînement.
2. **Standardisation** : Application d'un `StandardScaler` pour centrer et réduire les variables géométriques, étape indispensable pour assurer la stabilité de l'algorithme.
3. **Classification** : Entraînement d'un modèle de régression logistique (`LogisticRegression`) léger, rapide et performant, offrant une excellente séparabilité des classes.

Le pipeline complet intégrant le traitement et le modèle est sauvegardé sous la forme d'un fichier sérialisé : `modele_prediction_billets.joblib`.

---

## ⚙️ Application Fonctionnelle & Script d'Évaluation

Le dépôt intègre un script Python opérationnel (`Loriau_Julie_2_script_062026.py`) qui permet d'exécuter des prédictions sur de nouveaux billets en production selon deux modes d'entrée :

* **Mode CSV** : Lecture automatique d'un fichier de données de masse (ex: `billets_production.csv`).
* **Mode Manuel** : Saisie interactive dans le terminal des 6 dimensions géométriques d’un billet unique à tester.

### Sorties générées
* `is_fake_pred` : Prédiction finale (True si le billet est détecté comme faux).
* `proba_faux` / `proba_vrai` : Probabilités associées à la prédiction permettant de mesurer l'indice de confiance du modèle.

---

## 🔐 Conformité & Robustesse

* **Traitement automatisé** : Le pipeline intègre nativement l'imputation et la mise à l'échelle. Aucune manipulation manuelle préalable des données brutes n'est requise en production.
* **Reproductibilité** : L'utilisation d'états aléatoires fixes (`random_state=42`) assure des résultats constants lors de chaque réentraînement du modèle.
