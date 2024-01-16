import os
from pyunsplash import PyUnsplash
import requests

UNSPLASH_ACCESS_KEY = os.environ.get("UNSPLASH_ACCESS_KEY")

def unsplash_api_search(query=None, num=1):
    if query is None:
        return None
    api_url = 'https://api.unsplash.com/search/photos'
    params = {'query': query, 'client_id': UNSPLASH_ACCESS_KEY, 'orientation': 'landscape'}

    try:
        res = requests.get(api_url, params=params, allow_redirects=True)
        data = res.json()
        if not data.get('total'):
            return None
        return data['results'][num]['urls']['raw']

    except requests.exceptions.RequestException:
        return None

def download_image(image_url, file_path):
    """Downloads an image from the given URL and saves it to the specified file path.

    Args:
        image_url (str): The URL of the image to download.
        file_path (str): The full path where the image should be saved.
    """

    response = requests.get(image_url, stream=True)

    # Raise an exception if the download fails
    response.raise_for_status()

    # Create the directory structure if it doesn't exist
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, 'wb') as out_file:
        for chunk in response.iter_content(1024):
            out_file.write(chunk)


for i, num in enumerate(range(6, 7)):
    file_path = f"images/banners/banner{num}.JPG"
    img_url = unsplash_api_search('japanese garden', i)
    download_image(img_url, file_path)