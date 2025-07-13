import pandas as pd
import os

parts = [pd.read_csv(os.path.join('data', f"TMDB_all_movies_{i+1}.zip")) for i in range(5)]
movies_df = pd.concat(parts, ignore_index=True)


movies_df = movies_df[movies_df['status'] == 'Released']


columns_to_keep = ['id', 'title', 'director', 'cast', 'writers']
movies_df = movies_df[columns_to_keep]


movies_df = movies_df.fillna('')
movies_df = movies_df[movies_df['cast'].str.strip() != '']
movies_df = movies_df[movies_df['director'].str.strip() != '']
movies_df = movies_df[movies_df['writers'].str.strip() != '']

# Evita ciertas situaciones en las que el Jr de un nombre estaba separado por ","
movies_df['cast'] = movies_df['cast'].str.replace(', Jr.', ' Jr.', regex=False)
movies_df['writers'] = movies_df['writers'].str.replace(', Jr.', ' Jr.', regex=False)
movies_df['director'] = movies_df['director'].str.replace(', Jr.', ' Jr.', regex=False)

movies_df = movies_df.set_index('id')
people_in_movies = movies_df
