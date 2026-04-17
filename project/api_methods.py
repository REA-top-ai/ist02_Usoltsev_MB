import requests as r

Base_URL = 'https://api.github.com/'

def _make_request(endpoint: str, api_key: str, params: dict = None) -> dict:
    url = f'{Base_URL}{endpoint}'
    default_params = {'apiKey': api_key}

    if params:
        default_params.update(params)

    try:
        response = r.get(url, params=default_params, timeout=10)
        response.raise_for_status()
        return response.json()
    except r.exceptions.RequestException as e:
        raise Exception(f'Ошибка при запросе к GitHub ({endpoint}): {e}')
    except ValueError as e:
        raise Exception(f'Ошибка при парсинге JSON ({endpoint}): {e}')
