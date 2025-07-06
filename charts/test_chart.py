import plotly.express as px
from data.processor import get_movies_by_country

def create_test_chart():
  df = get_movies_by_country()

  fig = px.choropleth(df,
                       locations="ISO_Alpha3",
                       hover_name="Country",
                       color="Number of movies",
                       color_continuous_scale=px.colors.sequential.Plasma,
                       title="Number of movies released by country"
                       )
  
  fig.update_layout(
    xaxis_title="Country",
    yaxis_title="Number of movies",
    height=400
  )

  return fig.to_html(full_html=False)
