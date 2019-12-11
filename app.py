from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from Quote import return_quote
import advice
from Crypto import return_cryptoPrices
from Weather import return_weather
app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'quote' in incoming_msg:
        msg.body(return_quote())
        responded = True
    if 'cat' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True
    if 'advice' in incoming_msg:
        msg.body(advice.return_advice())
        responded = True
    if 'crypto' in incoming_msg:
        prices = return_cryptoPrices()
        msg.body(prices[0] + '\n' + prices[1] + '\n' + prices[2])
        responded = True
    if 'weather' in incoming_msg:
        data = return_weather(incoming_msg)
        msg.body(data)
        responded = True
    if 'hello' or 'good morning' or 'good night' in incoming_msg:
        # return a cat pic
        msg.media('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRoSM9gE3sFoLpEPU8OC4E7IwDyXnZT0vGR6h1Q9WEtchEpOKQT&s')
        responded = True
    if not responded:
        msg.body('Im sorry you asked something I do not know')
    return str(resp)


if __name__ == '__main__':
    app.run()
# https://whatsabb-bot-vanguard.herokuapp.com/bot
