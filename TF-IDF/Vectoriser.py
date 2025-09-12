import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import nltk

# Télécharger stopwords une seule fois
#nltk.download("stopwords")

# Charger le CSV
df = pd.read_csv("fight_club_clean.csv")

# Supprimer critiques vides
df = df.dropna(subset=["Critique"])
df["Critique"] = df["Critique"].astype(str)

# Stopwords français
stopwords_fr = stopwords.words("french")

# TF-IDF
vectorizer = TfidfVectorizer(stop_words=stopwords_fr)
tfidf_matrix = vectorizer.fit_transform(df["Critique"])

print("Shape TF-IDF matrix:", tfidf_matrix.shape)
