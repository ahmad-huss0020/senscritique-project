import os
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

# --- Choix du film ---
# Change "fight_club_clean.csv" en "interstellar_clean.csv" si besoin
FILM_FILE = "fight_club_clean.csv"

# Génération du nom du fichier cache embeddings
BASE_DIR = os.path.dirname(__file__)
EMBEDDINGS_FILE = os.path.join(BASE_DIR, FILM_FILE.replace(".csv", "_embeddings.npy"))

# Charger critiques
df = pd.read_csv(FILM_FILE)
df = df.dropna(subset=["Critique"])
df["Critique"] = df["Critique"].astype(str)

# Charger modèle multilingue rapide (français + anglais)
model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
# Alternative plus précise mais plus lente : LaBSE
# model = SentenceTransformer("sentence-transformers/LaBSE")

# Vérifier si embeddings existent déjà
if os.path.exists(EMBEDDINGS_FILE):
    print(f"✅ Chargement des embeddings depuis {EMBEDDINGS_FILE}...")
    embeddings = np.load(EMBEDDINGS_FILE)
else:
    print("⚡ Calcul des embeddings (première fois, peut prendre 30s)...")
    embeddings = model.encode(df["Critique"].tolist(), convert_to_tensor=False)
    np.save(EMBEDDINGS_FILE, embeddings)
    print(f"💾 Embeddings sauvegardés dans {EMBEDDINGS_FILE}")

print("Embeddings shape:", embeddings.shape)
print(f"➡️ Embeddings utilisés : {EMBEDDINGS_FILE}")
