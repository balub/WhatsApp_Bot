import requests


def return_quote():
    r = requests.get('https://api.quotable.io/random')
    if r.status_code == 200:
        data = r.json()['content']
    else:
        data = "Error Unable to fetch a quote for you"

    return data


