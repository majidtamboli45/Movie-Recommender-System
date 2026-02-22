import streamlit as st
import pickle
import pandas as pd
import os
import requests

# ==============================
# CONFIG
# ==============================
SIMILARITY_URL = "https://huggingface.co/datasets/Majid4377/movie-recommender-files/resolve/main/similarity.pkl"
SIMILARITY_FILE = "similarity.pkl"

# ==============================
# DOWNLOAD FUNCTION
# ==============================
def download_similarity():
    if not os.path.exists(SIMILARITY_FILE):
        with st.spinner("Downloading similarity matrix... (First run only)"):
            response = requests.get(SIMILARITY_URL)
            with open(SIMILARITY_FILE, "wb") as f:
                f.write(response.content)

# ==============================
# LOAD DATA (Cached)
# ==============================
@st.cache_resource
def load_data():
    download_similarity()
    movies = pickle.load(open("movies.pkl", "rb"))
    similarity = pickle.load(open("similarity.pkl", "rb"))
    return movies, similarity

movies, similarity = load_data()

# ==============================
# RECOMMEND FUNCTION
# ==============================
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# ==============================
# UI
# ==============================
st.set_page_config(page_title="Movie Recommender", page_icon="🎬")

st.title("🎬 Movie Recommender System")
st.write("Select a movie and get similar recommendations.")

selected_movie = st.selectbox(
    "Choose a movie:",
    movies['title'].values
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    st.subheader("Recommended Movies:")
    for movie in recommendations:
        st.write("👉", movie)