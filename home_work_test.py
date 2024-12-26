import pytest
from home_work_main import get_api


def test_get_api_success(mocker):
    mock_get = mocker.patch('home_work_main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'id': '5ev',
        'url': 'https://cdn2.thecatapi.com/images/5ev.jpg',
        'width': 500,
    }
    user_date = get_api()
    assert user_date == {
        'id': '5ev',
        'url': 'https://cdn2.thecatapi.com/images/5ev.jpg',
        'width': 500,
    }

def test_get_api_error(mocker):
    mock_get = mocker.patch('home_work_main.requests.get')
    mock_get.return_value.status_code = 404
    user_date = get_api()
    assert user_date == None



