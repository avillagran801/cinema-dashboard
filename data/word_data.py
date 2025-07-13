import pandas as pd
import os

parts = [pd.read_csv(os.path.join('data', f"TMDB_all_movies_{i+1}.zip")) for i in range(5)]
movies_df = pd.concat(parts, ignore_index=True)

movies_df = movies_df[movies_df['status'] == 'Released']
movies_df = movies_df[['overview', 'genres']].fillna('')

movies_df['genres'] = movies_df['genres'].apply(lambda x: x.split(',')[0].strip() if ',' in x else x.strip())
movies_df = movies_df[(movies_df['overview'] != '') & (movies_df['genres'] != '')]

word_data = movies_df
