import pytest
from main import get_weather, get_github_user
# pip install pytest-mock


def test_get_weather_success(mocker):
    mock_get = mocker.patch('main.requests.get')
    # Создаем мок-ответ для успешного запроса
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'weather': [{'description': 'clear sky'}],
        'main': {'temp': 273.15}
    }

    api_key = 'test_api_key'
    city = 'London'

    weather_data = get_weather(api_key, city)

    assert weather_data == {
        'weather': [{'description': 'clear sky'}],
        'main': {'temp': 273.15}
    }


# функция с ошибкой 404

def test_get_github_user_with_error(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 404

    api_key = 'test_api_key'
    city = 'London'

    weather_data = get_weather(api_key, city)
    assert weather_data == None


# для функции get_github_user

def test_get_github_user_success(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'login': 'test_user',
        'id': 12345,
        'name': 'Sasha'
    }
    user_data = get_github_user('luboy_text_nevagno')
    assert user_data == {
        'login': 'test_user',
        'id': 12345,
        'name': 'Sasha'
    }

def test_get_github_user_error(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 404
    mock_get.return_value.json.return_value = {
        'login': 'test_user',
        'id': 12345,
        'name': 'Sasha'
    }
    user_data = get_github_user('luboy_text_nevagno')
    assert user_data == None




