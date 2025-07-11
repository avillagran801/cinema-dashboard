import plotly.express as px
from data.releases_data import released_movies_by_year

def create_releases_chart():
  fig = px.line(
    released_movies_by_year,
    x="Year",
    y="Number of movies",
    # title="Number of Movies Released by Year"
  )

  fig.update_layout(
    height=400,
  )

  return fig.to_html(full_html=False)