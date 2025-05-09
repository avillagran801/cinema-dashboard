from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import *
app = FastAPI()

# Allow frontend on localhost:3000 to access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add routes
app.include_router(movies_router)
app.include_router(genres_router)