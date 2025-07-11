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

movies_df = movies_df.map(custom_fillna)

# Convert release_date column from string to datetime
movies_df['release_date'] = pd.to_datetime(movies_df['release_date'])

# Generate decade column
movies_df['decade'] = (movies_df['release_date'].dt.year // 10)*10

def get_top100_revenue_movies():

    df_revenue = movies_df.sort_values(by='revenue', ascending=False)
    df_revenue = df_revenue.drop(columns=['original_language',
                                            'overview',
                                            'production_companies',
                                            'production_countries',
                                            'spoken_languages',
                                            'genres',
                                            'cast',
                                            'director'
                                            ])
    
    df_revenue = df_revenue.drop(df_revenue[(df_revenue.vote_average < 1) | (df_revenue.vote_count < 2) | (df_revenue.popularity < 2)].index)
    top100_revenue_movies = df_revenue.iloc[:100]

    return top100_revenue_movies