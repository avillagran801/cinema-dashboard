import pandas as pd
from pathlib import Path

# LOAD DATA TO DATAFRAME
def load_movies_data():
  try:
    current_dir = Path(__file__).parent
    path = current_dir.parent / "TMDB_all_movies.zip"
    movies_df = pd.read_csv(path)
    print("CSV loaded:", movies_df.shape)
    return movies_df

  except Exception as e:
    print("Failed to load CSV:", str(e))
    return pd.DataFrame()