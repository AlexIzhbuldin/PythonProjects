import requests
import json

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '{token}'
HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN
}

body_create = {
    "name": "a1exvip",
    "photo_id": -1  
}
body_name = {
    "pokemon_id": "353378",
    "name": "Саня из Уфы",
    "photo_id": 2
}
body_add_pokeball = {
    "pokemon_id": "353378",
}

'''response_create = requests.post(f'{URL}/pokemons', headers=HEADER, json=body_create)
print(response_create.text)'''

'''response_name = requests.put(f'{URL}/pokemons', headers=HEADER, json=body_name)
print(response_name.text)'''

response_add_pokeball= requests.post(f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_add_pokeball)
print(response_add_pokeball.text)