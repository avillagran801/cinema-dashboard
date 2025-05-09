import pandas as pd
import numpy as np

def preprocess_movies_data(df: pd.DataFrame):
  if df.empty:
    return df

  # Set index as the one used on the csv
  preprocessed_df = df.copy()
  preprocessed_df = preprocessed_df .set_index("id")

  # Drop columns that won't be used
  preprocessed_df  = preprocessed_df .drop(columns=['imdb_id', 'tagline','director_of_photography', 'writers', 'producers', 'music_composer', 'poster_path'])

  # Keep released movies only and drop column
  preprocessed_df  = preprocessed_df [preprocessed_df ['status'] == 'Released']
  preprocessed_df  = preprocessed_df .drop(columns=['status'])

  # Fill missing values based on datatype
  def custom_fillna(value):
    if pd.isna(value):
        if isinstance(value, (str, object)):
            return ''
        elif isinstance(value, (int, float)):
            return 0
        elif isinstance(value, (pd.Timestamp, np.datetime64)):
            return 'null'
    return value
  
  preprocessed_df = preprocessed_df.map(custom_fillna)

  return preprocessed_df