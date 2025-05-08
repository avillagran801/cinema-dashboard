from flask import Flask
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('revenues_per_day.zip')

@app.route("/")
def alo():
    return f"<p>{df.head()}<p>"