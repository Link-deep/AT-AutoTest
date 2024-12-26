# ✅ Mock-объект — объект, имитирующий поведение реального объекта или сервиса.
# ✅ Patch — изменение поведения функции или объекта во время выполнения теста.
# ✅ Spy — объект, записывающий информацию о вызовах, методах и параметрах.
# ✅Stub — реализация интерфейса, возвращающая предопределенные данные.


import requests

def get_weather(api_key, city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None



def get_github_user(username):
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
