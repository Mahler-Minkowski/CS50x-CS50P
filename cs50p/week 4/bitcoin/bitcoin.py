import sys
import requests
import json

try:
    convert=requests.get(
        "https://rest.coincap.io/v3/assets/bitcoin?apiKey=bb4de73ce4a04dc71711ea7c24246b4f68dffd75c8c4754246ee10604695a625")
    convert=convert.json()
    data=convert['data']
    num=round(float(data['priceUsd']), 6)
    cost=float(sys.argv[1])*num
    if cost>0:
        print(f'${cost:,.4f}',end='')
    else:
        raise ValueError
except (requests.RequestException,ValueError,IndexError):
    sys.exit('Command-line argument is not a number ')
