import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def recommend_similar_reviews(review_id, df, tfidf_matrix, top_n=5):
    # Vérifier si l'ID existe
    if review_id not in df["ID"].values:
        print("❌ ID introuvable")
        return pd.DataFrame()

    # Trouver l'index correspondant à l'ID
    idx = df.index[df["ID"] == review_id].tolist()[0]

    # Calculer similarité cosinus avec toutes les autres critiques
    cosine_sim = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()

    # Trier par similarité décroissante (en ignorant la critique elle-même)
    similar_idx = cosine_sim.argsort()[::-1][1:top_n+1]

    # Retourner un DataFrame avec les critiques similaires
    result = df.iloc[similar_idx][["ID", "User", "Rating", "Titre", "Critique"]].copy()
    return result

# Exemple d’utilisation (à exécuter seulement si tu lances ce fichier directement)
if __name__ == "__main__":
    from Vectoriser import df, tfidf_matrix  # importe df et tfidf_matrix depuis ton fichier vectorisation
    resultats = recommend_similar_reviews(review_id=14018277, df=df, tfidf_matrix=tfidf_matrix, top_n=5)
    print(resultats[["ID", "User", "Rating", "Titre"]])  # affiche les infos principales
