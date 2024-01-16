import os
from pyunsplash import PyUnsplash
import requests

UNSPLASH_ACCESS_KEY = os.environ.get("UNSPLASH_ACCESS_KEY")

def unsplash_api_search(query=None):
    if query is None:
        return None
    api_url = 'https://api.unsplash.com/search/photos'
    params = {'query': query, 'client_id': UNSPLASH_ACCESS_KEY, 'orientation': 'landscape'}

    try:
        res = requests.get(api_url, params=params, allow_redirects=True)
        data = res.json()
        if not data.get('total'):
            return None
        return data['results'][1]['urls']['raw']

    except requests.exceptions.RequestException:
        return None

print(unsplash_api_search('travel'))