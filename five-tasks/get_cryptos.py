# import requests
# import time


# url = 'https://api.coincap.io/v2/assets'


# def get_data(url):

#     response = requests.get(url)

#     data = response.json()

#     return data


# def get_crypto_list(data):
#     ml = []
#     for i in range(len(data['data'][0])):
#         md = {}
#         md['name'] = data['data'][i]['name']
#         md['symbol'] = data['data'][i]['symbol']
#         md['current_price'] = str(round(float(data['data'][i]['priceUsd']),3))  + '$'
#         md['market_cap'] = str(round(float(data['data'][i]['marketCapUsd'])))  + '$'
#         md['total_volume'] = str(round(float(data['data'][i]['volumeUsd24Hr'])))  + '$'
#         md['price_24h'] = str(round(float(data['data'][i]['vwap24Hr'])))  + '$'
#         ml.append(md)
#     return ml


# def get_each_crypto():
#     while True:
#         data = get_data(url)
#         cryptos = get_crypto_list(data)
#         for crypto in cryptos:
#             print('Name:', crypto['name'])
#             print('Symbol:', crypto['symbol'])
#             print('Current Price:', crypto['current_price'])
#             print('Market Cap:', crypto['market_cap'])
#             print('Total_Volume:', crypto['total_volume'])
#             print('Price 24h:', crypto['price_24h'])
#             print()
#         time.sleep(5)


# def main():
#     get_each_crypto()


# if __name__ == '__main__':
#     main()