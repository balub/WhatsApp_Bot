from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'quote' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True
    if 'cat' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True
    if 'advice' in incoming_msg:
        # return advice
        r = requests.get('https://api.adviceslip.com/advice')
        if r.status_code == 200:
            data = r.json();
            advice = f'{data["slip"]["advice"]}'
            msg.body(advice)
        responded = True
    if 'crypto' in incoming_msg:
        url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
        headers = {'X-CoinAPI-Key': 'DB69F134-B4F1-4FFF-8BED-B6D217B9FB1C'}
        response = requests.get(url, headers=headers)
        prices = ["The Price of Bitcoin is " + str(response.json()["rate"]) + "$"]
        url = 'https://rest.coinapi.io/v1/exchangerate/ETH/USD'
        headers = {'X-CoinAPI-Key': 'DB69F134-B4F1-4FFF-8BED-B6D217B9FB1C'}
        response = requests.get(url, headers=headers)
        prices.append("The Price of Etherium is " + str(response.json()["rate"]) + "$")
        url = 'https://rest.coinapi.io/v1/exchangerate/LTC/USD'
        headers = {'X-CoinAPI-Key': 'DB69F134-B4F1-4FFF-8BED-B6D217B9FB1C'}
        response = requests.get(url, headers=headers)
        prices.append("The Price of Litecoin  is " + str(response.json()["rate"]) + "$")
        msg.body(prices[0] + '\n' + prices[1] + '\n' + prices[2])
        responded = True
    if 'weather' in incoming_msg:
        words = incoming_msg.split(" ")
        print(words)
        r = data = requests.get(
            'http://api.openweathermap.org/data/2.5/weather?q=' + words[1] + '&APPID=5305e66d631b9da248c2112c5f48c600')
        if data.json()['cod'] == 200:
            weather = data.json()['weather'][0]['description']
            loc = data.json()['name']
            msg.body("The weather forecast for " + loc + " is: " + weather)
        else:
            msg.body("The Location provided is incorrect")
        responded = True
    if not responded:
        msg.body('Im sorry you asked something I do not know')
    return str(resp)


if __name__ == '__main__':
    app.run()
# https://whatsabb-bot-vanguard.herokuapp.com/bot
