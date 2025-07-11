import pandas as pd
import numpy as np
import os

# Necesito tener unas columnas que están dropeadas en processor :( entonces hago aparte esto pa no tocar el processor. -Cano
parts = [
    pd.read_csv(os.path.join('data', f"TMDB_all_movies_{i+1}.zip"))
    for i in range(5)
]

movies_df = pd.concat(parts, ignore_index=True)
#movies_df = movies_df.set_index("id")
movies_df = movies_df[movies_df['status'] == 'Released']
movies_df = movies_df.drop(columns=['status'])
columns_to_keep = ['title', 'director', 'cast', 'writers']
movies_df = movies_df[columns_to_keep]
movies_df = movies_df.fillna('')

people_in_movies = movies_df
