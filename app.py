from flask import Flask, render_template
from charts.choropleth_chart import create_choropleth
from charts.releases_chart import create_releases_chart
from charts.bar_chart import (
    create_top10_actors_bar,
    create_top10_directors_bar,
    create_top10_writers_bar
)
from charts.waffle_chart import create_waffle
from charts.budget_chart import create_line_budget_revenue
from charts.word_chart import generate_wordclouds_by_genre
from data.selector_options import categories_list, genres_list, countries_list

app = Flask(__name__)

@app.route("/", methods=["GET"])
def dashboard():
    choropleth_chart = create_choropleth()
    waffle_chart = create_waffle()
    revenue_budget_line_chart = create_line_budget_revenue()
    releases_chart = create_releases_chart()

    actors_bar_chart = create_top10_actors_bar()
    writers_bar_chart = create_top10_writers_bar()
    directors_bar_chart = create_top10_directors_bar()
    wordclouds = generate_wordclouds_by_genre()
    initial_genre = next(iter(wordclouds.keys()))

    return render_template(
        "dashboard.html",
        category_options=categories_list,
        genre_options=genres_list,
        country_options=countries_list,
        choropleth_chart=choropleth_chart,
        waffle_chart=waffle_chart,
        revenue_budget_line_chart=revenue_budget_line_chart,
        releases_chart=releases_chart,
        actors_bar_chart=actors_bar_chart,
        writers_bar_chart=writers_bar_chart,
        directors_bar_chart=directors_bar_chart,
        wordclouds=wordclouds,
        initial_genre=initial_genre
    )

if __name__ == "__main__":
    app.run(debug=True)
