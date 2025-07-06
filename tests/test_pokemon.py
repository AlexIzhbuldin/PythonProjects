import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'fa68583f17ca714ef6c7214934efc466'
HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN
}
ID = '33035'

def test_status_code():
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url=f'{URL}/trainers', params={'trainer_id' : ID})
    assert response_get.json()['data'][0]['id'] == "33035"
