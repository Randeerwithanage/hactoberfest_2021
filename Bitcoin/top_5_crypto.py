'''
Problem Statement : Get the price in Dollar and Rupee of top 5 crypto currency
'''

import requests


import json


key = '1f9711731ed59151e9d85ebb045744c6c18c48b30f676e32eb42b2e6e803fccd'

# send the request to api and store the result in url object
url = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,XRP,LTC,USDT&tsyms=USD,INR'
response = requests.get(url)
print(response)
rate = response.text
print(rate)