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

👨‍💻 Auteur : Ahmad Hussein  
📅 Projet réalisé dans le cadre d’un **test technique**
