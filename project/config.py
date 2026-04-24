import os
from dotenv import load_dotenv


load_dotenv()

MISTRAL_API_KEY = os.getenv('MISTRAL_API_KEY')
GITHUB_API_KEY = os.getenv('GITHUB_API_KEY')

HOST = os.getenv('POSTGRES_HOST')
PORT = os.getenv('POSTGRES_PORT')
USERNAME = os.getenv('POSTGRES_USER')
PASSWORD = os.getenv('POSTGRES_PASSWORD')

DB_NAME = 'API_PROJECT'

DB_URL = f'postgresql+asyncpg://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'
SERVER_URL = f'postgresql+asyncpg://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/postgres'