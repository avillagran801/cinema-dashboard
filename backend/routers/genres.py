from fastapi import APIRouter, HTTPException
from data_manipulation import genres_df

router = APIRouter()



@router.get("/genres")
def get_genres_data():
  if genres_df.empty:
      raise HTTPException(status_code=500, detail="Data not loaded")
  return genres_df.head(200).to_dict(orient="records")
