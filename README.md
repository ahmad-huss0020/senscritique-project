# 🎬 Projet Test – Recommandation de Critiques  

Ce projet a été réalisé dans le cadre d’un **test technique**.  
Il s’agit d’une application **Streamlit** permettant de recommander des critiques similaires à partir d’un dataset de SensCritique.  

---

## 🚀 Lancer l’application  

👉 Vous pouvez tester directement l’application en ligne :  
🔗 [Accéder à l’app](https://senscritique-project.streamlit.app)  

---

## ✅ Fonctionnalités  

- Choisir un **film** (`Fight Club` ou `Interstellar`)  
- Sélectionner une **critique** et afficher son texte complet  
- Lancer une **recommandation** de 5 ou 10 critiques similaires  
- Les résultats sont calculés avec :  
  - **Embeddings sémantiques (Sentence-BERT)**  
  - Une légère pondération selon la **note (rating)**  
- Visualisation : Score de similarité + expander pour lire la critique entière

---

## 🛠️ Stack utilisée  

- **Python 3.10+**  
- **Streamlit** (interface web)  
- **Sentence-Transformers** (modèle `paraphrase-multilingual-MiniLM-L12-v2`)  
- **scikit-learn** (similarité cosinus)  
- **pandas / numpy** (traitement des données)  

---

## 🤖 Note sur l’utilisation de l’IA  

Ce projet a été développé en partie avec l’aide de ChatGPT afin d’accélérer le développement et d’améliorer certains aspects du code.
Mon rôle a consisté à :  
- Définir l’architecture du projet et les choix techniques (embeddings sémantiques vs TF-IDF, mise en cache, interface Streamlit).  
- Guider l’IA avec des instructions précises pour obtenir un code adapté aux données fournies.  
- Écrire et adapter certaines parties de code moi-même.  
- Tester, ajuster et corriger jusqu’à obtenir une solution fonctionnelle et conforme au sujet.  

👉 Je suis capable d’écrire l’ensemble du code sans IA, mais j’ai choisi de l’utiliser comme **outil de productivité** : cela permet d’aller plus vite si l’on comprend l’algorithme et la logique sous-jacente.    

---

## 🔹 Choix techniques et justification  

- **Données (CSV)** : critiques de films fournies dans des fichiers CSV (*Fight Club*, *Interstellar*).  
  - Format léger, facile à manipuler avec **pandas**.  

- **Nettoyage du texte (NLTK + pandas)** : suppression des valeurs manquantes, conversion en chaînes, retrait des stopwords.  
  - Améliore la **qualité des représentations textuelles**.  

- **Vectorisation sémantique (Sentence-BERT)** : modèle `paraphrase-multilingual-MiniLM-L12-v2`.  
  - Multilingue (français + anglais), léger et rapide pour un test technique.  
  - Chaque critique est transformée en vecteur de **384 dimensions**.  

- **Cache embeddings (.npy)** : calcul sauvegardé après la première exécution.  
  - Permet une **réutilisation immédiate** sans recalcul à chaque lancement.  

- **Calcul de similarité (cosine similarity)** : comparaison des critiques avec une légère pondération selon la différence de **rating**.  
  - Combine **ressemblance de contenu** et **proximité d’opinion**.  

- **Interface (Streamlit)** : application web interactive permettant de :  
  - Choisir un **film**  
  - Sélectionner une **critique**  
  - Lancer la **recommandation** (5 ou 10 résultats)  
  - Interface simple et intuitive.  

- **Déploiement (Streamlit Cloud)** : accessible via un **lien public**, sans installation locale.  

---

👨‍💻 Auteur : Ahmad Hussein  
📅 Projet réalisé dans le cadre d’un **test technique**
