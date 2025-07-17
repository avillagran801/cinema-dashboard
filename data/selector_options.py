import pandas as pd
from langcodes import Language
from data.processor import movies_df

def _get_genres():
  genres = movies_df['genres']
  genres = genres.str.split(',', expand=True).iloc[:, :3]
  genres = genres.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
  genres = genres.replace('', pd.NA).dropna(how="all")
  genres = genres[[0, 1, 2]].stack().dropna().unique()
  genres = sorted(genres.tolist())
  
  return genres

def _get_countries():
  countries = movies_df['production_countries']
  countries = countries.str.split(',', expand=True).iloc[:, :3]
  countries = countries.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
  countries = countries.replace('', pd.NA).dropna(how="all")
  countries = countries[[0, 1, 2]].stack().dropna().unique()
  countries = sorted(countries.tolist())

  return countries

def _get_languages():
  languages = movies_df['original_language']
  languages = languages.unique().tolist()
  languages = [ {'iso': x, 'name': Language.get(x).display_name() if x != 'cn' else 'Chinese'} for x in languages if x != 'xx']
  languages = sorted(languages, key=lambda x: x['name'])

  return languages

genres_list = _get_genres()
countries_list = _get_countries()
languages_list = _get_languages()