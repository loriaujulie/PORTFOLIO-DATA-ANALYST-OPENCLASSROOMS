import joblib
import pandas as pd

# Liste exacte des variables géométriques requises par le modèle
colonnes_entrainement = [
    "diagonal",
    "height_left",
    "height_right",
    "margin_low",
    "margin_up",
    "length",
]

# Choix du mode d'input 
print("CHOIX DU MODE D'INPUT")
while True:
    mode = (
        input("Entrez 'csv' pour charger un fichier ou 'manuel' pour une saisie manuelle des données: ")
        .strip()
        .lower()
    )
    if mode in ["csv", "manuel"]:
        MODE_INPUT = mode
        break
    print("Choix invalide. Veuillez taper exactement 'csv' ou 'manuel' (sans les guillemets).\n")


# Chargement des données selon le mode choisi 
nouvelles_donnees = None
X_evaluation = None

if MODE_INPUT == "csv":
    # chemin par défaut
    chemin_csv = "..\\Data\\billets_production.csv"
    print(f"\n Chargement du fichier depuis : {chemin_csv}")
    try:
        nouvelles_donnees = pd.read_csv(chemin_csv)
        X_evaluation = nouvelles_donnees[colonnes_entrainement]
    except FileNotFoundError:
        print(f"Erreur : Le fichier à l'emplacement est introuvable.")
        exit()
    except KeyError:
        print(
            f"Erreur : Le CSV ne contient pas toutes les colonnes requises : {colonnes_entrainement}"
        )
        exit()

elif MODE_INPUT == "manuel":
    print("\n Saisie manuelle des mesures (Utilisez le point '.' pour les décimales)")
    valeurs_saisies = {}

    # Boucle sur chaque caractéristique géométrique requise
    for col in colonnes_entrainement:
        while True:
            saisie = input(f"Entrez la valeur pour '{col}' : ").strip()
            try:
                # conversion des données en décimal
                valeur_float = float(saisie)

                # On vérifie que la mesure est positive
                if valeur_float <= 0:
                    print("Erreur de format : La mesure doit être supérieure à 0.")
                    continue

                # Si la conversion réussit, on stocke la valeur dans une liste (requis pour Pandas)
                valeurs_saisies[col] = [valeur_float]
                break  

            except ValueError:
                # Si la conversion en float échoue
                print(
                    "Erreur de format : Vous devez entrer un nombre valide (ex: 171.5)."
                )

    # Transformation des données saisies manuellement en DataFrame d'une seule ligne
    nouvelles_donnees = pd.DataFrame(valeurs_saisies)
    nouvelles_donnees["id"] = "Billet_Manuel"
    X_evaluation = nouvelles_donnees[colonnes_entrainement]


# Chargement du modèle et prédiction 
try:
    pipeline_final = joblib.load("modele_prediction_billets.joblib")
except FileNotFoundError:
    print("Erreur : Le fichier 'modele_prediction_billets.joblib' est introuvable.")
    exit()

# Définition des prédictions et probabilités
predictions = pipeline_final.predict(X_evaluation)
probas = pipeline_final.predict_proba(X_evaluation)

# Enregistrement des résultats
nouvelles_donnees["is_fake_pred"] = predictions
nouvelles_donnees["proba_faux"] = probas[:, 1].round(4)
nouvelles_donnees["proba_vrai"] = probas[:, 0].round(4)

# Interprétation des résultats
nouvelles_donnees["Resultat"] = nouvelles_donnees["is_fake_pred"].map(
    {True: "Faux billet", False: "Vrai billet"}
)

# Affichage des résultats
print(f"\n RÉSULTATS DES PRÉDICTIONS (Mode : {MODE_INPUT.upper()})")
if "id" in nouvelles_donnees.columns:
    print(nouvelles_donnees[["id", "proba_faux", "proba_vrai", "Resultat"]])
else:
    print(nouvelles_donnees[["proba_faux", "proba_vrai", "Resultat"]])