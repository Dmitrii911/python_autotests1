import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '2dd1b3171c1a0042d93d483652e3a711'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN} 
trainer_id = 4410

def test_status_code():
    response = requests.get(url=f'{URL}/trainers', params = {'trainer_id' : trainer_id})
    assert response.status_code == 200


def test_part():
    response_get = requests.get(url=f'{URL}/trainers', params = {'trainer_id' : trainer_id})
    assert response_get.json()["data"],["id"] == 4410



