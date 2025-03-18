import requests

def fetch_pokemon():
    url = 'https://pokeapi.co/api/v2/pokemon'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None
