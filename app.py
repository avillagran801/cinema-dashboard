from flask import Flask, render_template, request
import plotly.express as px
from charts.choropleth_chart import create_choropleth
from charts.releases_chart import create_releases_chart
from data.selector_options import categories_list, genres_list, countries_list

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def dashboard():
  #chart = request.form.get("which_chart")

  choropleth_chart = create_choropleth()
  releases_chart = create_releases_chart()

  return render_template(
    "dashboard.html",
    category_options=categories_list,
    genre_options=genres_list,
    country_options=countries_list,
    choropleth_chart=choropleth_chart,
    releases_chart=releases_chart
  )

if __name__ == "__main__":
  app.run()