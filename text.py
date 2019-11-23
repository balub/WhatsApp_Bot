import requests

url = 'https://rest.coinapi.io/v1/exchangerate/ETH/USD'
headers = {'X-CoinAPI-Key': 'DB69F134-B4F1-4FFF-8BED-B6D217B9FB1C'}
response = requests.get(url, headers=headers)
print(response.json()["rate"])
