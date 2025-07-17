import pandas as pd
import numpy as np
from data.processor import movies_df

# standard data
def _movies_by_year_counter():
  movies_by_year = movies_df.copy()
  movies_by_year["Year"] = movies_by_year["release_date"].dt.year
  movies_by_year = movies_by_year[movies_by_year["Year"] <= 2024] 
  movies_by_year = movies_by_year.groupby("Year").size().reset_index(name="Number of movies")

  return movies_by_year

released_movies_by_year = _movies_by_year_counter()

def movies_by_year_filter(filter_type, filter_value):
  if filter_type == "genre":
    column = "genres"
  elif filter_type == "language":
    column = "original_language"
  elif filter_type == "country":
    column = "production_countries"
  else:
    return

  movies_filter = movies_df.copy()
  movies_filter["Year"] = movies_filter["release_date"].dt.year
  movies_filter = movies_filter[movies_filter["Year"] <= 2024]

  movies_filter = movies_filter[movies_filter[column].str.contains(filter_value, case=False)]

  movies_filter = movies_filter.groupby("Year").size().reset_index(name="Number of movies")

  return movies_filter

