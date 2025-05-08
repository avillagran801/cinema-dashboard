from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# Allow frontend on localhost:3000 to access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/data")
def get_data():
    # Replace with your own CSV/ZIP file
    df = pd.read_csv("revenues_per_day.zip")

    # Clean NaN and infinite values in the DataFrame
    df = df.replace([float("inf"), float("-inf")], None)  # Replace infinities with None
    df = df.dropna()  # Drop rows with NaN values (optional)
    
    # Return as JSON
    return df.to_dict(orient="records")