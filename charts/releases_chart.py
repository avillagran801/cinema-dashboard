import plotly.express as px
from data.releases_data import released_movies_by_year, movies_by_year_filter

def create_releases_chart(filter_type=None, filter_value=None):
  if(not filter_type or not filter_value):
    fig = px.line(
      released_movies_by_year,
      x="Year",
      y="Number of movies",
    )

    fig.update_layout(
      height=400,
    )

    return fig.to_html(full_html=False)
  
  fig = px.line(
    movies_by_year_filter(filter_type, filter_value),
      x="Year",
      y="Number of movies",
    )

  fig.update_layout(
    height=400,
  )

  return fig.to_html(full_html=False)