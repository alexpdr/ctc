"""Main file of the CTC App"""
from fastapi import FastAPI, Response

from routers import ROUTERS

# Initialize app
app = FastAPI()

# Add additional routers
[app.include_router(router) for router in ROUTERS]


# Default entry point
@app.get("/", tags=["Greetings"])
async def index() -> Response:
    """Says hello to visitors"""
    return {"message": "Hello!"}
