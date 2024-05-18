import requests


'''

Author: David Galstyan
Date: 28.04.2024
Description: This code returns forecast of the given city

'''


api_key = '4ce14ec96659e7a0d805d06e96444648'


def get_city_name():
    '''

        Description: user should input the name of a city
        Parameters: None
        Returns: The name of a city
    
    '''

    name = input('Enter a city name: ')

    return name


def get_data(key, city_name):
    '''
    
        Description: get information of API changed into json
        Parameters: key of API; The name of a city
        Returns: information of forecast of the city
    
    '''

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}'

    response = requests.get(url)

    data = response.json()

    return data


def main():
    '''
    
        Description: The main function
        Parameters: None
        Returns: prints forecast of the city
    
    '''

    city_name = get_city_name()
    answer = get_data(api_key, city_name)
    print(answer)


if __name__ == '__main__':
    main()
