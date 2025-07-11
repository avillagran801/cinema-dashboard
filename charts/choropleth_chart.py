import plotly.express as px
from data.choropleth_data import movies_by_country_count

def create_choropleth():
  fig = px.choropleth(
    movies_by_country_count,
    locations="ISO_Alpha3",
    locationmode="ISO-3",
    hover_name="Country",
    hover_data={"ISO_Alpha3": False},
    color="Number of movies",
    color_continuous_scale="Viridis",
    title="Number of Movies Released by Country",
    projection="natural earth",
    labels={"Number of movies": "Movies Released"},
  )

  fig.update_geos(
    resolution=50,  # Lower resolution (50 or 110 for crude maps)
    scope="world",  # Avoid loading unused regions
    showsubunits=False  # Hide states/provinces
  )

  fig.update_traces(
    marker_line_color="white",  # Force white country borders
    marker_line_width=0.5 
  )
  
  fig.update_layout(
      height=500,
      margin={"r": 0, "t": 40, "l": 0, "b": 0},
      geo=dict(
        showframe=True,          
        showcountries=True,       
        countrycolor="white",    
        countrywidth=1,         
        showcoastlines=False,     
        bgcolor="rgba(0,0,0,0)",
        landcolor="lightgray",    # Fill color for non-data countries
      ),
      coloraxis_colorbar=dict(
        title="Movies Released",
        thickness=15,           
        len=0.6,                
      ),
      font=dict(
        family="Arial",
        color="black"
      ),
      hoverlabel=dict(
        bgcolor="white",
        font_size=12,
        font_family="Arial",
      ),
  )

  return fig.to_html(full_html=False)