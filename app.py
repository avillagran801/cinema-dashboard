from flask import Flask, render_template, request
import plotly.express as px
from charts.choropleth_chart import create_choropleth
from charts.releases_chart import create_releases_chart

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def dashboard():
  #chart = request.form.get("which_chart")

  choropleth_chart = create_choropleth()
  releases_chart = create_releases_chart()

  return render_template(
    "dashboard.html",
    choropleth_chart=choropleth_chart,
    releases_chart=releases_chart
  )

if __name__ == "__main__":
  app.run(debug=True)