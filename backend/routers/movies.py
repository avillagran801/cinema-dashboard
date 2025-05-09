from fastapi import APIRouter, HTTPException
from data_manipulation import movies_df

router = APIRouter()

@router.get("/movies")
def get_movies():
    if movies_df.empty:
        raise HTTPException(status_code=500, detail="Data not loaded")
    return movies_df.head(200).to_dict(orient="records")
