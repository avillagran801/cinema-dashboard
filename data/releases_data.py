import pandas as pd
import numpy as np
from data.processor import movies_df

def _movies_by_year_counter():
  movies_by_year = movies_df.copy()
  movies_by_year["Year"] = movies_by_year["release_date"].dt.year
  movies_by_year = movies_by_year.groupby("Year").size().reset_index(name="Number of movies")
  movies_by_year = movies_by_year[movies_by_year["Year"] <= 2024] 

  return movies_by_year

released_movies_by_year = _movies_by_year_counter()