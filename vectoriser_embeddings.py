import os
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import streamlit as st

@st.cache_resource
def load_model():
    return SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

@st.cache_data
def load_embeddings(film_file: str):
    BASE_DIR = os.path.dirname(__file__)
    embeddings_file = os.path.join(BASE_DIR, film_file.replace(".csv", "_embeddings.npy"))

    # Charger dataset
    df = pd.read_csv(film_file)
    df = df.dropna(subset=["Critique"])
    df["Critique"] = df["Critique"].astype(str)

    # Charger modèle depuis cache_resource
    model = load_model()

    # Vérifier si embeddings sont déjà sauvegardés en .npy
    if os.path.exists(embeddings_file):
        embeddings = np.load(embeddings_file)
    else:
        embeddings = model.encode(df["Critique"].tolist(), convert_to_tensor=False)
        np.save(embeddings_file, embeddings)

    return df, embeddings

# Test rapide si on exécute directement ce fichier
if __name__ == "__main__":
    df, embeddings = load_embeddings("fight_club_clean.csv")
    print("Embeddings shape:", embeddings.shape)
    print(df.head())
