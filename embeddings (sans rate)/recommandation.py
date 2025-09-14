import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def recommend_semantic_reviews(review_id, df, embeddings, top_n=10):
    # Vérifier si l'ID existe
    if review_id not in df["ID"].values:
        print("❌ ID introuvable")
        return pd.DataFrame()

    # Trouver l'index correspondant à l'ID
    idx = df.index[df["ID"] == review_id].tolist()[0]

    # Calculer similarité cosinus avec toutes les autres critiques
    cosine_sim = cosine_similarity(
        embeddings[idx].reshape(1, -1),
        embeddings
    ).flatten()

    # Trier par similarité décroissante (ignorer la critique elle-même)
    similar_idx = np.argsort(cosine_sim)[::-1][1:top_n+1]

    # Retourner un DataFrame avec les critiques similaires et leur score
    result = df.iloc[similar_idx][["ID", "User", "Rating", "Titre", "Critique"]].copy()
    result["Score"] = cosine_sim[similar_idx]
    return result

# Exemple d’utilisation
if __name__ == "__main__":
    from vectoriser_embeddings import df, embeddings  # ton fichier qui charge embeddings
    review_id = 308975541  # critique de départ
    resultats = recommend_semantic_reviews(review_id, df, embeddings, top_n=10)
    print(resultats[["ID", "User", "Rating", "Titre", "Score"]])
