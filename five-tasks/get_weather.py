import requests

api_key = '4ce14ec96659e7a0d805d06e96444648'


def get_city_name():
    name = input('Enter a city name: ')

    return name


def get_data(key, city_name):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

    response = requests.get(url)

    data = response.json()

    return data


def check_city_name():
    while True:
        city_name = get_city_name()
        data = get_data(api_key, city_name)
        if data == {'cod': '404', 'message': 'city not found'}:
            print('There is no such city.Try again')
            continue

        return data


def main():
    answer = check_city_name()
    print(answer)


if __name__ == '__main__':
    main()
