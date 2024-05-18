import requests
import time


'''
    Author: David Galstyan

    Date: 28.04.2024

    Description: This code returns the costs of cryptocurrencies and updates costs every 5s
'''


URL = 'https://api.coincap.io/v2/assets'


def get_data_from_url(URL):
    '''
        Description: get information of API converted into json

        Parameters: URL of API

        Returns: information of API converted into json
    '''

    response = requests.get(URL)

    data = response.json()

    return data


def get_crypto_list(data):
    '''
        Description: get list of dictionaries of each crypto

        Parameters: data of API

        Returns: list of each crypto 
    '''

    ml = []
    for i in range(len(data['data'][0])):
        md = {}
        md['name'] = data['data'][i]['name']
        md['symbol'] = data['data'][i]['symbol']
        md['current_price'] = str(round(float(data['data'][i]['priceUsd']),3))  + '$'
        md['market_cap'] = str(round(float(data['data'][i]['marketCapUsd'])))  + '$'
        md['total_volume'] = str(round(float(data['data'][i]['volumeUsd24Hr'])))  + '$'
        md['price_24h'] = str(round(float(data['data'][i]['vwap24Hr'])))  + '$'
        ml.append(md)
    return ml


def get_each_crypto():
    '''    
        Description: prints the information of cryptocurrencies every 5s
    '''

    while True:
        data = get_data_from_url(URL)
        cryptos = get_crypto_list(data)
        for crypto in cryptos:
            print('Name:', crypto['name'])
            print('Symbol:', crypto['symbol'])
            print('Current Price:', crypto['current_price'])
            print('Market Cap:', crypto['market_cap'])
            print('Total_Volume:', crypto['total_volume'])
            print('Price 24h:', crypto['price_24h'])
            print()
        time.sleep(5)


def main():
    '''
        The main function
    '''

    # get_each_crypto()

data = get_data_from_url(URL)
print(data['data'][:10])
if __name__ == '__main__':
    main()
