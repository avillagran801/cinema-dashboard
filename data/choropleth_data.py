import pandas as pd
import numpy as np
import pycountry
from data.processor import movies_df

def _movies_by_country_counter():
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
  countries_df = countries_df.drop(columns=[
    'original_language',
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

movies_by_country_count = _movies_by_country_counter()