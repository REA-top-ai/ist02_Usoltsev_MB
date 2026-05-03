from google_auth_oauthlib.flow import InstalledAppFlow
from dotenv import load_dotenv
import os

load_dotenv()

CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID_FOR_AUTH_APP")
CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET_FOR_AUTH_APP")

flow = InstalledAppFlow.from_client_config({
    "installed": {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "redirect_uris": ["http://localhost:8080/"]
    }
}, scopes=["openid", "email", "profile"])

if __name__ == '__main__':
    creds = flow.run_local_server(port=8080)
    print("Token:", creds.token)