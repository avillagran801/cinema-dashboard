import pandas as pd
import numpy as np
import os

parts = [pd.read_csv(os.path.join('data', f"TMDB_all_movies_{i+1}.zip")) for i in range(5)]
# For testing -------------
# parts = [pd.read_csv(os.path.join(f"TMDB_all_movies_{i+1}.zip")) for i in range(5)]
# -------------------------
movies_df = pd.concat(parts, ignore_index=True)

# Set index as the one used on the csv
movies_df = movies_df.set_index("id")

# Drop columns that won't be used
movies_df = movies_df.drop(columns=['imdb_id', 'tagline','director_of_photography', 'writers', 'producers', 'music_composer', 'poster_path'])

# Keep released movies only
movies_df = movies_df[movies_df['status'] == 'Released']
movies_df = movies_df.drop(columns=['status'])

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

movies_df = movies_df.applymap(custom_fillna)

# Convert release_date column from string to datetime
movies_df['release_date'] = pd.to_datetime(movies_df['release_date'])

# Generate decade column
movies_df['decade'] = (movies_df['release_date'].dt.year // 10)*10

