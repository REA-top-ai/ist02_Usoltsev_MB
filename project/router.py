from fastapi import APIRouter
from repository import Repository

router = APIRouter()

@router.post("/user")
async def post_info(username: str) -> dict:
    full_info = await  Repository.get_full_info(username)
    return full_info
