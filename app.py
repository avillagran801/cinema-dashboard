from flask import Flask, render_template
from charts.choropleth_chart import create_choropleth
from charts.bar_chart import create_top10_actors_bar
from charts.waffle_chart import create_waffle

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def dashboard():
    choropleth_chart = create_choropleth()
    waffle_chart = create_waffle()
    actors_bar_chart = create_top10_actors_bar()
    return render_template(
        "dashboard.html",
        choropleth_chart=choropleth_chart,
        actors_bar_chart=actors_bar_chart,
        waffle_chart=waffle_chart
    )

if __name__ == "__main__":
    app.run(debug=True)
