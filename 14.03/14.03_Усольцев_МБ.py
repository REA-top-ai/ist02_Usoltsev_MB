from modules.api_methods import get_everything
import requests as r
import pprint
import json


apiKey = 'c63bf198cdcf4034806c57f1f18ce0df'
url = 'https://newsapi.org/v2/everything'

data = get_everything(apiKey, q='news', sortBy='publishedAt', language='ru')

filtered_data = []

for article in data['articles']:
    artdict = {}
    title = article['title']
    artdict['title'] = title
    urllink = article['url']
    artdict['url'] = urllink
    description = article['description']
    artdict['description']= description
    artdict['date'] = article['publishedAt']
    
    if (title != '[removed]') and (urllink is not None) and (len(description) >= 50):
        filtered_data.append(artdict)
    if len(filtered_data) == 50:
        break

print(filtered_data)
