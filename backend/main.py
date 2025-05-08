from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse
import pandas as pd

app = FastAPI()

# Allow frontend on localhost:3000 to access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

try:
  movies_df = pd.read_csv("TMDB_all_movies.zip")
  movies_df = movies_df.replace([float("inf"), float("-inf")], None)  # Replace infinities with None
  print("CSV loaded:", movies_df.shape)

except Exception as e:
  print("Failed to load CSV:", str(e))
  movies_dataframe = pd.DataFrame()


@app.get("/data", response_class=ORJSONResponse)
def get_data():
    if movies_df.empty:
        raise HTTPException(status_code=500, detail="Data not loaded.")
    return movies_df.head(200).to_dict(orient="records")