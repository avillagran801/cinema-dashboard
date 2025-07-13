import pandas as pd
import numpy as np
from data.processor import movies_df

def _get_categories():
  return ['---', 'Country of production', 'Genres', 'Language']

def _get_genres():
  genres = movies_df['genres']
  genres = genres.str.split(',', expand=True).iloc[:, :3]
  genres = genres.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
  genres = genres.replace('', pd.NA).dropna(how="all")
  genres = genres[[0, 1, 2]].stack().dropna().unique()
  genres = ['---'] + sorted(genres.tolist())
  
  return genres

def _get_countries():
  countries = movies_df['production_countries']
  countries = countries.str.split(',', expand=True).iloc[:, :3]
  countries = countries.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
  countries = countries.replace('', pd.NA).dropna(how="all")
  countries = countries[[0, 1, 2]].stack().dropna().unique()
  countries = ['---'] + sorted(countries.tolist())

  return countries

categories_list = _get_categories()
genres_list = _get_genres()
countries_list = _get_countries()