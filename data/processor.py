import pandas as pd
import numpy as np
import pycountry
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

def get_movies_by_country():
  countries = movies_df['production_countries']
  countries = countries.apply(lambda x: x.strip())

  # Separate countries and keep the first three
  countries = countries.str.split(',', expand=True).iloc[:, :3]
  countries.columns = ['country_1', 'country_2', 'country_3']
  countries = countries.fillna('')

  # Concat the new columns
  countries_df = movies_df.copy()
  countries_df = pd.concat([countries_df, countries], axis=1)

  # Drop columns that won't be used
  countries_df = countries_df.drop(columns=['original_language',
                                            'original_title',
                                            'overview',
                                            'production_companies',
                                            'production_countries',
                                            'spoken_languages',
                                            'genres',
                                            'cast',
                                            'director'
                                            ])

  country_count = countries_df[['country_1', 'country_2', 'country_3']].stack().value_counts()
  country_count = country_count.reset_index()
  country_count.columns = ['Country', 'Number of movies']

  # Function to get ISO Alpha-3 code (handles edge cases like 'USA' vs 'United States')
  def get_iso_alpha3(country_name):
      try:
          return pycountry.countries.lookup(country_name).alpha_3
      except (AttributeError, LookupError):
          return None  # Handle missing/ambiguous countries
      
  # Add ISO codes to the DataFrame
  country_count['ISO_Alpha3'] = country_count['Country'].apply(get_iso_alpha3)

  # Drop rows with missing ISO codes
  country_count = country_count.dropna(subset=['ISO_Alpha3'])
  
  return country_count

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