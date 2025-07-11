from flask import Flask, render_template, request
import plotly.express as px
from charts.choropleth_chart import create_choropleth
from charts.waffle_chart import create_waffle

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def dashboard():
  #chart = request.form.get("which_chart")

  choropleth_chart = create_choropleth()
  waffle_chart = create_waffle()

  return render_template("dashboard.html",
                         choropleth_chart=choropleth_chart,
                         waffle_chart=waffle_chart
                         )

if __name__ == "__main__":
  app.run(debug=True)