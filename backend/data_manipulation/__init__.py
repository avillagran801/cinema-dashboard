
from .loader import load_movies_data
from .preprocessor import preprocess_movies_data
from .process_genres import process_genres
from pathlib import Path

_raw_data = load_movies_data()

# Make available at package level
movies_df = preprocess_movies_data(_raw_data)

genres_df = process_genres(movies_df)