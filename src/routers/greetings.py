"""
File contains endpoint routerController for /hello/
"""
from fastapi import APIRouter, Response

router = APIRouter(tags=["Greetings"])


@router.get("/greet/{name}")
async def greet(name: str) -> Response:
    """Greets the provided name"""
    return {"message": f"Hello {name}!"}
