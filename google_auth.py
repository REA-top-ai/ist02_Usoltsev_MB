from google_auth_oauthlib.flow import InstalledAppFlow

CLIENT_ID = '219775451235-31dbamg4vltmnujskqj1va7d2gqvdq2f.apps.googleusercontent.com'
CLIENT_SECRET = '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'

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