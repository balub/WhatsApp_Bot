import requests

urls = ['https://rest.coinapi.io/v1/exchangerate/BTC/USD', 'https://rest.coinapi.io/v1/exchangerate/ETH/USD',
        'https://rest.coinapi.io/v1/exchangerate/LTC/USD']
headers = {'X-CoinAPI-Key': 'DB69F134-B4F1-4FFF-8BED-B6D217B9FB1C'}
data = []


def return_cryptoPrices():
    for url in urls:
        r = requests.get(url, headers=headers).json()
        data.append(f'The Price of {r["asset_id_base"]} is {str(r["rate"])} $')
    return  data




#
# url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
# headers = {'X-CoinAPI-Key': 'DB69F134-B4F1-4FFF-8BED-B6D217B9FB1C'}
# response = requests.get(url, headers=headers)
# prices = ["The Price of Bitcoin is " + str(response.json()["rate"]) + "$"]
# url = 'https://rest.coinapi.io/v1/exchangerate/ETH/USD'
# headers = {'X-CoinAPI-Key': 'DB69F134-B4F1-4FFF-8BED-B6D217B9FB1C'}
# response = requests.get(url, headers=headers)
# prices.append("The Price of Etherium is " + str(response.json()["rate"]) + "$")
# url = 'https://rest.coinapi.io/v1/exchangerate/LTC/USD'
# headers = {'X-CoinAPI-Key': 'DB69F134-B4F1-4FFF-8BED-B6D217B9FB1C'}
# response = requests.get(url, headers=headers)
# prices.append("The Price of Litecoin  is " + str(response.json()["rate"]) + "$")
# msg.body(prices[0] + '\n' + prices[1] + '\n' + prices[2])
