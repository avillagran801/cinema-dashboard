import pandas as pd
import numpy as np
import pycountry
import ast
import re
# from data.processor import movies_df
from data.processor import movies_df

def _get_top100_revenue_movies():

    df_revenue = movies_df.sort_values(by='revenue', ascending=False)
    df_revenue = df_revenue.drop(columns=['original_language',
                                            'overview',
                                            'production_companies',
                                            'production_countries',
                                            'spoken_languages',
                                            'cast',
                                            'director'
                                            ])
    
    df_revenue = df_revenue.drop(df_revenue[(df_revenue.vote_average < 1) | (df_revenue.vote_count < 2) | (df_revenue.popularity < 2)].index)
    
    def clean_and_parse_genres(genres_str):
        if pd.isna(genres_str) or not isinstance(genres_str, str):
            return []
        try:
            # Primero, intenta una evaluación directa (si ya tiene comillas)
            return ast.literal_eval(genres_str)
        except (ValueError, SyntaxError):
            # Si falla, intenta corregir el formato (ej. "[Action, Adventure]" -> "['Action', 'Adventure']")
            # Elimina los corchetes y divide por comas
            cleaned_str = genres_str.strip('[] ')
            if cleaned_str: # Si no está vacío
                # Añade comillas a cada elemento y reconstruye la lista
                formatted_genre_elements = []
                for g in cleaned_str.split(','):
                    # Aseguramos que cada género esté entre comillas dobles, por ejemplo: "Action"
                    formatted_genre_elements.append(f'"{g.strip()}"') 
                
                # Unimos los elementos con comas y los encerramos en corchetes para formar el string final
                genres_list_str = f"[{', '.join(formatted_genre_elements)}]"

                try:
                    return ast.literal_eval(genres_list_str)
                except (ValueError, SyntaxError):
                    return []
            return

    # Aplica la función para asegurar que 'genres' es una lista real
    df_revenue['genres_parsed'] = df_revenue['genres'].apply(clean_and_parse_genres)

    # Ahora, crea la columna 'genre' tomando el primer elemento de la lista parseada.
    df_revenue['genre'] = df_revenue['genres_parsed'].apply(lambda x: x[0] if x else 'Unknown')
    
    # Elimina la columna temporal 'genres_parsed'
    df_revenue = df_revenue.drop(columns=['genres_parsed'])

    top100_revenue_movies = df_revenue.iloc[:100]

    return top100_revenue_movies

top100_revenue_movies = _get_top100_revenue_movies()