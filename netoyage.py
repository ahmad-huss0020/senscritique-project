import pandas as pd
import re

def clean_reviews(input_file, output_file):
    # Charger le fichier Excel
    df = pd.read_excel(input_file)

    # Vérifier les colonnes
    print("Colonnes disponibles :", df.columns.tolist())

    # Nettoyer la colonne Critique (supprimer HTML si présent)
    df["Critique"] = df["Critique"].astype(str).apply(lambda x: re.sub("<.*?>", "", x))

    # Créer un extrait de 100 caractères
    df["Extrait"] = df["Critique"].str[:100] + "..."

    # Garder les colonnes utiles
    df_clean = df[["ID", "User", "Rating", "Titre", "Critique", "Extrait"]]

    # Sauvegarder en CSV
    df_clean.to_csv(output_file, index=False, encoding="utf-8")
    print(f"✅ Fichier nettoyé sauvegardé : {output_file}")


# Nettoyer Fight Club
clean_reviews("fight_club_critiques.xlsx", "fight_club_clean.csv")

# Nettoyer Interstellar
clean_reviews("interstellar_critique.xlsx", "interstellar_clean.csv")
