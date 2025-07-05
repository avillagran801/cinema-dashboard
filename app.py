from flask import Flask, render_template, request
import plotly.express as px
from charts.test_chart import create_test_chart

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def dashboard():
  #chart = request.form.get("which_chart")

  chart_test = create_test_chart()

  return render_template("dashboard.html",
                         chart_test=chart_test
                         )

if __name__ == "__main__":
  app.run(debug=True)