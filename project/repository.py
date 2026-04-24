from github import get_info
from mistral import get_resume
from schemas import UserCreate
from database import new_sessions
from models import GithubUser

from datetime import datetime

class Repository:
    @classmethod
    async def get_full_info(cls, username: str) -> dict:
        async with new_sessions() as session:
            cache = await session.get(GithubUser, username)
            if cache:
                return {
                    'data': cache.data,
                    'resume': cache.resume,
                }

            info = await get_info(username)
            resume = await get_resume(info)

            github_user = GithubUser(
                username=username,
                data=info,
                resume=resume,
            )
            session.add(github_user)

            #session.add(History(username=username, user=user))

            await session.commit()
            return {'info': info, 'resume': resume}



