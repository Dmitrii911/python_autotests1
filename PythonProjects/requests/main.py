import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '2dd1b3171c1a0042d93d483652e3a711'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
body_create = {
    "name": "generate",
    "photo_id": -1
}

body_newname = {
    "pokemon_id": "42085",
    "name": "биба",
    "photo_id": -1
}

body_add_pokeball = {
    "pokemon_id": "42085"
}


response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)

print(response_create.text)


response_newname = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_newname)

print(response_newname.text)

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)

print(response_add_pokeball.text)