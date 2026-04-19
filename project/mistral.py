import os
from dotenv import load_dotenv

from mistralai.client import Mistral
from pprint import pprint
from main import get_username
from github import get_info
username = get_username()
info = get_info(username)


load_dotenv()


mistral_api_key = os.getenv('MISTRAL_API_KEY')
model = 'mistral-small-latest'
role = 'user'
promt = f"""
Ты — технический рекрутер. Проанализируй профиль GitHub пользователя {username}.

Статистика:
- Дата регистрации: {info.get('created_at')}
- Подписчиков: {info.get('followers')}
- Публичных репозиториев: {info.get('all_repos')}
- Языки: {info.get('languages')}
- Всего звёзд: {info.get('total_stars')}
- Среднее колличество звёзд на аккаунт: {info.get('mean_count_stars')}
- Всего форков: {info.get('total_forks')}
- Всего readmes: {info.get('total_readmes')}
- Примерная активность: ~{info.get('activ')} коммитов за последний год


Напиши краткое резюме в 3-4 предложения: кто этот разработчик (стек, специализация), насколько активен, есть ли популярные проекты, что можно сказать о его опыте.
"""

with Mistral(api_key=mistral_api_key) as mistral:
    res = mistral.chat.complete(model=model, messages=[
        {
            'content': promt,
            'role': role
        }
    ], stream=False)

    print(res)
