import requests
BASE_URL = 'https://newsapi.org/v2'


def _make_request(endpoint: str, api_key: str, params: dict[str,str] = None) -> dict:
    url = f"{BASE_URL}/{endpoint}"
    default_params = {'apiKey': api_key}

    if params:
        default_params.update(params)

    try:
        response = requests.get(url, params=default_params, timeout=10)
        return response.json()
    
    except requests.exceptions.RequestException as e:
        raise Exception(f"Ошибка при запросе к NewsAPI {endpoint}: {e}")
    
    except ValueError as e:
        raise Exception(f"Ошибка при парсинге json {endpoint}: {e}")
    
def get_top_headlines(api_key: str, q: str, country: str=None,
                      category: str=None, sources: str=None,
                        page_size: int=None, page: int=None ) -> dict:
    params = {'q':q,'country': country, 'category':category,
              'pagesize':page_size, 'page':page,}
    final_params = {key: value for key, value in params.items() if value is not None}
    return _make_request('top-headlines',api_key,final_params)
def get_everything(api_key:str, q: str, searchIn: str = None, domains: str = None, excludeDomains: str = None,
                   from_date: str = None, to_date: str = None, language: str = None, sortBy: str = None,
                      sources: str = None, page_size: int = None, page: int = None) -> dict:


    params = {'q': q, 'searchIn': searchIn, 'domains': domains, 'sources': sources, 'excludeDomains': excludeDomains,
              'from': from_date, 'to': to_date, 'language': language, 'sortBy': sortBy,
              'pageSize': page_size, 'page': page}

    final_params = {key:value for key, value in params.items() if value is not None}

    return _make_request('everything', api_key, final_params)
