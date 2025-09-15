import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def recommend_semantic_reviews(review_id, df, embeddings, top_n=20, alpha=0.1):
    if review_id not in df["ID"].values:
        print("❌ ID introuvable")
        return pd.DataFrame()

    # Index de la critique de référence
    idx = df.index[df["ID"] == review_id].tolist()[0]

    # Similarité cosinus brute (texte)
    cosine_sim = cosine_similarity(
        embeddings[idx].reshape(1, -1),
        embeddings
    ).flatten()

    # Note de la critique choisie
    rating_ref = df.loc[idx, "Rating"]

    # Pénalisation par différence de notes
    rating_diff = abs(df["Rating"] - rating_ref) / 10
    score_final = cosine_sim - alpha * rating_diff

    # Trier les critiques par score final décroissant (sauf elle-même)
    similar_idx = np.argsort(score_final)[::-1][1:top_n+1]

    # Construire le résultat
    result = df.iloc[similar_idx][["ID", "User", "Rating", "Titre", "Critique"]].copy()
    result["ScoreTexte"] = cosine_sim[similar_idx]
    result["ScoreFinal"] = score_final.to_numpy()[similar_idx]  # <-- fix ici
    return result



if __name__ == "__main__":
    from vectoriser_embeddings import df, embeddings  # charge dataset + embeddings

    # Exemple : choisir une critique de départ
    review_id = 127689867  # critique de départ

    resultats = recommend_semantic_reviews(
        review_id=review_id,
        df=df,
        embeddings=embeddings,
        top_n=20,
        alpha=0.1
    )

    print(resultats[["ID", "User", "Rating", "Titre", "ScoreTexte", "ScoreFinal"]])
