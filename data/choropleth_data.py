import pandas as pd
import numpy as np
import country_converter as coco
import io
from data.processor import movies_df

def _movies_by_country_counter():
  countries = movies_df['production_countries']
  countries = countries.apply(lambda x: x.strip())

  # Separate countries and keep the first three
  countries = countries.str.split(',', expand=True).iloc[:, :3]
  countries.columns = ['country_1', 'country_2', 'country_3']
  countries = countries.fillna('')

  # Merge with original DataFrame
  countries_df = movies_df.reset_index()

  countries_df = pd.concat([countries_df[['id']], countries], axis=1)

  melted = countries_df.melt(
      id_vars=['id'],
      value_vars=['country_1', 'country_2', 'country_3'],
      value_name='Country'
  )

  # Clean and drop empty values
  melted['Country'] = melted['Country'].str.strip()
  melted = melted[melted['Country'] != '']

  # Drop duplicate (movie_id, country) pairs to avoid inflated counts
  melted = melted.drop_duplicates(subset=['id', 'Country'])

  # Count unique movies per country
  country_count = melted['Country'].value_counts().reset_index()
  country_count.columns = ['Country', 'Number of movies']

  manual_map = {
      "Soviet Union": "Russia",
      "Yugoslavia": "Serbia",
      "East Germany": "Germany",
      "Serbia and Montenegro": "Serbia",
      "Northern Ireland": "United Kingdom",
      "Congo": "Republic of the Congo",  # or "Democratic Republic of the Congo"
      "Guadaloupe": "Guadeloupe",
      "Netherlands Antilles": "Curaçao",  # or another successor
      "Samoa": "Samoa"
  }

  # Replace historical names in Country column
  country_count['Country'] = country_count['Country'].replace(manual_map)

  # Function to get ISO Alpha-3 code
  def get_iso_alpha3(country_name):
      # Try using country_converter
      code = coco.convert(names=country_name, to='ISO3')
      return None if code == 'not found' else code

  # Add ISO codes to the DataFrame
  country_count['ISO_Alpha3'] = country_count['Country'].apply(get_iso_alpha3)

  return country_count

movies_by_country_count = _movies_by_country_counter()