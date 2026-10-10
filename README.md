# Movie Recommendation System

A content-based movie recommendation web app built with Python and Streamlit. Select a movie from the dropdown to receive five similar movie recommendations, with posters fetched from The Movie Database (TMDB) API.

## Features

- Select a movie from the available movie list.
- Recommend five similar movies using cosine similarity.
- Use movie metadata such as overview, genres, keywords, cast, and crew.
- Display movie posters using the TMDB API.
- Provide a simple interactive interface with Streamlit.

## Tech Stack

- Python
- Pandas and NumPy
- Scikit-learn (`CountVectorizer` and `cosine_similarity`)
- Streamlit
- Requests
- TMDB API

## How It Works

1. Load and merge the TMDB movie and credits datasets.
2. Select relevant movie metadata and preprocess the text features.
3. Combine the selected features into a text representation for each movie.
4. Convert the text into vectors with `CountVectorizer` (up to 5,000 features, excluding English stop words).
5. Calculate cosine similarity between movie vectors.
6. When a user selects a movie, return the five most similar movies and fetch their posters from TMDB.

## Project Files

```text
movie-recommendation-system/
├── app.py
├── movie_recomender.ipynb
├── movies.pkl
├── similarity.pkl
├── requirements.txt
├── .gitignore
└── README.md
```

The pickle files are generated data artifacts required by `app.py`. Keep the filenames consistent: `app.py` expects `movies.pkl` and `similarity.pkl`. If your notebook currently saves the movie dictionary as `movies_dict.pkl`, either save/copy it as `movies.pkl` in the expected format or update `app.py` to use the actual filename.

The original TMDB CSV files (`tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`) are needed to rerun the notebook from the beginning. Add them to the repository only if their size and applicable dataset terms allow it.

## Setup and Run Locally

1. Clone your repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
   cd YOUR-REPOSITORY
   ```

2. Create and activate a virtual environment (optional but recommended):

   **Windows**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

   **macOS/Linux**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure your TMDB API key as an environment variable (see Security below), then run:

   ```bash
   streamlit run app.py
   ```

## TMDB API Configuration and Security

Do not commit API keys or other secrets to GitHub. The version of `app.py` you shared contains a hard-coded TMDB API key. Remove it from the source code and read it from an environment variable instead, for example:

```python
import os

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
```

Then use `TMDB_API_KEY` in the request parameters. Set the environment variable before launching the app. If the key has already been pushed to a public repository, revoke or regenerate it in your TMDB account; deleting it from the latest code does not remove it from Git history.

For Streamlit Community Cloud, you can store the key in the app's **Secrets** settings and read it with `st.secrets` (with an appropriate local fallback if desired).

## Notes

- Recommendations are based on similarity between movie metadata; they are not personalized using individual users' ratings or watch history.
- Poster images depend on TMDB API access and poster availability.
- Pickle files should only be loaded from trusted sources.

## Acknowledgements

- Movie metadata: TMDB 5000 Movies and Credits datasets.
- Movie poster metadata and images: [The Movie Database (TMDB)](https://www.themoviedb.org/).

---

Created as a learning project to practise Python, data preprocessing, text vectorization, similarity metrics, and building a small interactive ML application.
