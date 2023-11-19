import requests

def get_fact():
    return requests.get('https://dog-api.kinduff.com/api/facts').json()['facts'][0]