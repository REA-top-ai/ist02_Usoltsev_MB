import requests as r
from requests.auth import HTTPDigestAuth

BASE_URL = "https://httpbin.org"
TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.KMUFsIDTnFmyG3nMiGM6H9FNFUROf3wh7SmqJp-QV30'


def main():
    ba = r.get(f'{BASE_URL}/basic-auth/user/passwd', auth=('user', 'pass'))
    br = r.get(f'{BASE_URL}/bearer', headers={'Authorization': f'Bearer {TOKEN}'})
    da = r.get(f'{BASE_URL}/digest-auth/auth/user/passwd',auth=HTTPDigestAuth('user', 'pass'))

if __name__ == "__main__":
    main()