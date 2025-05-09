import pandas as pd

def process_genres(movies_df: pd.DataFrame):
  # Delete extra white space
  genres = movies_df['genres']
  genres = genres.apply(lambda x: x.strip())

  # Separate genres and keep the first three
  genres = genres.str.split(',', expand=True).iloc[:, :3]
  genres.columns = ['genre_1', 'genre_2', 'genre_3']

  # Fill new missing values with an empty string
  genres = genres.fillna('')

  # Concat to new copy of movies_df
  genres_df = movies_df.copy()
  genres_df = pd.concat([genres_df, genres], axis=1)

  # Drop columns that won't be used to analyze genres
  genres_df = genres_df.drop(columns=['title', 'original_language', 'original_title', 'overview', 'production_companies', 'production_countries', 'spoken_languages', 'genres', 'cast', 'director'])

  return genres_df