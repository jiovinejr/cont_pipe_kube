import requests


API_KEY = 'SpqnGUJ7hFDSDtZD2TpiLYxxWR3QSMDbwJ7hFsYu88dqyimyjOp9yzxERVrT'
BASE_URL = 'https://api.sportmonks.com/v3/football/leagues'


url = f'{BASE_URL}?api_token={API_KEY}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Convert response to JSON
    print(data)
else:
    print("Error:", response.status_code)