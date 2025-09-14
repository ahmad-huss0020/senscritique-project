import streamlit as st
import pandas as pd
from vectoriser_embeddings import load_embeddings
from recommandation_rate import recommend_semantic_reviews

# -----------------------------
# Config générale
# -----------------------------
st.set_page_config(page_title="SensCritique Recommandation", layout="centered")

# -----------------------------
# Titre centré
# -----------------------------
st.markdown("<h1 style='text-align: center;'>🎬 Recommandation de critiques similaires</h1>", unsafe_allow_html=True)

# -----------------------------
# Étape 1 : choix du film
# -----------------------------
film_choice = st.selectbox(
    "👉 Choisissez un film :",
    ["fight_club_clean.csv", "interstellar_clean.csv"],
    format_func=lambda x: "Fight Club" if "fight_club" in x else "Interstellar"
)

# -----------------------------
# Étape 2 : charger dataset + embeddings (avec cache)
# -----------------------------
df, embeddings = load_embeddings(film_choice)

# Préparer résumé des critiques
df["Résumé"] = df["Critique"].str[:120].str.replace("\n", " ") + "..."
review_display = df.apply(
    lambda x: f"[{x['ID']}] {x['User']} ({x['Rating']}/10) – {x['Résumé']}",
    axis=1
)
review_map = dict(zip(review_display, df["ID"]))

# -----------------------------
# Étape 3 : choix d'une critique
# -----------------------------
selected_review = st.selectbox("📖 Sélectionnez une critique :", ["-- Choisissez une critique --"] + list(review_display))

if selected_review != "-- Choisissez une critique --":
    review_id = review_map[selected_review]

    # Critique choisie → affichage automatique
    review_ref = df[df["ID"] == review_id].iloc[0]
    st.markdown("### 📌 Critique sélectionnée")
    st.markdown(f"**{review_ref['User']}** ({review_ref['Rating']}/10) — *{review_ref['Titre']}*")
    st.write(review_ref["Critique"])

    # -----------------------------
    # Étape 4 : choix du nombre de recommandations
    # -----------------------------
    top_n = st.radio("👉 Nombre de recommandations :", [5, 10], horizontal=True)

    # -----------------------------
    # Étape 5 : bouton de lancement
    # -----------------------------
    if st.button("🚀 Lancer la recommandation"):
        with st.spinner("🔎 Recherche de critiques similaires..."):
            results = recommend_semantic_reviews(review_id, df, embeddings, top_n=top_n)

        if results.empty:
            st.warning("Aucune critique similaire trouvée.")
        else:
            st.markdown("<h3 style='text-align: center;'>✨ Critiques similaires</h3>", unsafe_allow_html=True)
            for _, row in results.iterrows():
                st.markdown(
                    f"**{row['User']}** ({row['Rating']}/10) — *{row['Titre']}*  — ID: `{row['ID']}`",
                    unsafe_allow_html=True
                )
                st.write(row['Critique'][:300] + "...")
                with st.expander("Voir la critique complète"):
                    st.write(row['Critique'])
                st.caption(f"Score: {row['ScoreFinal']:.3f}")
                st.divider()

else:
    st.info("👉 Veuillez sélectionner une critique pour voir son texte et lancer la recommandation.")
