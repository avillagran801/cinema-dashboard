from .movies import router as movies_router
from .genres import router as genres_router

__all__ = ["movies_router", "genres_router"]  # Explicitly expose the router