from api_methods import (
    get_top_headlines,
    get_everything,
    get_sources
)
from pprint import pprint

if __name__ == '__main__':
    API_KEY = 'c63bf198cdcf4034806c57f1f18ce0df'

    print("Top headlines 'apple':")
    headlines = get_top_headlines(api_key=API_KEY, q='apple')
    pprint(headlines)

    print("\narticles 'bitcoin':")
    everything = get_everything(api_key=API_KEY, q='bitcoin', page_size=3)
    pprint(everything)

    print("\nNews sources:")
    sources = get_sources(api_key=API_KEY, category='business', language='en')
    pprint(sources)
