import streamlit as st
import pickle
import pandas as pd
import requests
from pathlib import Path


def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    try:
        response = requests.get(
            url,
            params={
                "api_key": "2072b3e155032d185ac40791c3bf7afa",
                "language": "en-US",
            },
            timeout=10,
        )
        response.raise_for_status()
        poster_path = response.json().get("poster_path")
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path.lstrip('/')}"
    except (requests.RequestException, ValueError) as error:
        print(f"Unable to fetch poster for movie {movie_id}: {error}")
    return None


def recommend(movie):
    movie = movie.strip()
    if movie not in movies["title"].values:
        print(f"'{movie}' not found in the dataset.")
        return []

    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    similar_movies = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    recommended = [movies.iloc[idx]["title"] for idx, _ in similar_movies]
    recommended_poster = [fetch_poster(movies.iloc[idx]["movie_id"]) for idx, _ in similar_movies]
    
    print(recommended)
    return recommended , recommended_poster





def load_recommender_data():
    data_dir = Path(__file__).resolve().parent
    with (data_dir / "movies.pkl").open("rb") as movies_file:
        movies_dict = pickle.load(movies_file)
    with (data_dir / "similarity.pkl").open("rb") as similarity_file:
        similarity = pickle.load(similarity_file)
    return pd.DataFrame(movies_dict), similarity


movies, similarity = load_recommender_data()

st.title("Movies Recomender System")

selected_movie_name = st.selectbox(
    "which types of movies you want to see",
    movies["title"].values,
)


if st.button("recommended"):
    recommended_movies, recommended_posters = recommend(selected_movie_name)
    if recommended_movies:
        columns = st.columns(len(recommended_movies))
        for column, title, poster in zip(columns, recommended_movies, recommended_posters):
            with column:
                st.write(title)
                if poster:
                    st.image(poster)
                else:
                    st.write("Poster unavailable")
    else:
        st.write("No recommendations found.")
