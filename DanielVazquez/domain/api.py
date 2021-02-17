import requests
import os
from config.logging import config_logger


def get_pokemon_info(pokemon: str):
    url = f"{os.getenv('API_URL')}/pokemon/{pokemon}"
    return _get_(url)


def get_species(pokemon_id: str):
    url = f"{os.getenv('API_URL')}/pokemon-species/{pokemon_id}"
    return _get_(url)


def get_evolution_trigger(pokemon_id: str):
    url = f"{os.getenv('API_URL')}/pokemon-species/{pokemon_id}"
    return _get_(url)


def get_pokemon_img_data(img_url: str):
    response = requests.get(img_url)
    return response.content


def _get_(url):
    log = config_logger()
    log.debug(f"GET:\t{url}")
    response = requests.request("GET", url)
    log.debug(f"Status: {response.status_code}")
    if not response.status_code == 200:
        return None
    return response.json()


