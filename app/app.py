import streamlit as st
import joblib
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("🎬 Movie Recommendation System")

movies_dict = joblib.load("app/movies_dict.pkl")


movies = pd.DataFrame(movies_dict)

cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()

similarity = cosine_similarity(vectors)

movies = movies_dict['title'].values


def recommend(movie):
    movie = movie.lower()
    if movie not in movies_dict['title'].str.lower().values:
        return ["Movie not found"]
    index = movies_dict[movies_dict['title'].str.lower() == movie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [movies_dict.iloc[i[0]].title for i in movie_list]

selected_movie = st.selectbox("Select a Movie:", movies)

if st.button("Recommend"):
    results = recommend(selected_movie)
    for m in results:
        st.write(m)
