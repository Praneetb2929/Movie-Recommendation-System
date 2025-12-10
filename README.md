# 🎬 Movie Recommendation System (Content-Based)

A machine learning project that recommends similar movies using content-based filtering based on genres, actors, keywords, and overview. It uses NLP based feature extraction along with cosine similarity to compute movie similarity scores.

---

## 📌 Objective
Build a movie recommendation system using:
- Content based filtering
- Bag of Words
- Cosine similarity

The final model enables a user to select a movie and receive 5 similar recommendations.

---

## 🧠 Technologies Used

| Component | Technology |
|----------|------------|
| Language | Python |
| Framework | Streamlit |
| Feature Extraction | CountVectorizer |
| Similarity | Cosine Similarity |
| Data | TMDB Movies & Credits dataset |
| Deployment | Local Streamlit Web App |

---

## 🪄 How it Works

1. Load movie metadata
2. Merge credits + movies using movie ID
3. Extract features:
   - genres
   - keywords
   - top 3 actors
   - director
4. Build a combined “tags” column
5. Vectorize using CountVectorizer
6. Compute cosine similarity matrix
7. Recommend top 5 similar movies

---

## 🔥 Example Recommendation

Input:
<img width="1919" height="1079" alt="Image" src="https://github.com/user-attachments/assets/6fce8cc2-18da-4dd4-a87e-e98a797b7243" />

Output:
<img width="1919" height="1079" alt="Image" src="https://github.com/user-attachments/assets/d884b99a-7467-4828-bf9f-8747b9da7055" />

