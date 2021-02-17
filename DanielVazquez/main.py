from dotenv import load_dotenv
from config import logging
from config import args
from domain import api
from gui import image_window as image
from datetime import datetime as dt


def main():
    load_dotenv()
    log = logging.config_logger()
    arguments = args.get_args()

    log.info(f"Session start at: {dt.now()}")

    print_header()

    pokemon = arguments.pokemon
    another = True

    while another:
        if pokemon is None:
            pokemon = input("Enter pokemon name or number: ")

        log.info(f"Searching for pokemon: {pokemon}...")
        pokemon_info = api.get_pokemon_info(pokemon.lower())

        if pokemon_info is None:
            print(f"The requested pokemon [{pokemon}] doesn't exists!")
        else:
            log.info(f"Pokemon found! Searching for pokemon species for id: {pokemon_info['id']}...")
            species = api.get_species(pokemon_info['id'])
            print_pokemon_name(pokemon_info['name'])
            print_pokemon_info(pokemon_info)
            print_pokemon_species(species)
            print("*" * 64)
            print("Please close the window before continue...")
            image.show_window(pokemon_info)

        search_again = input("Search another pokemon? (y/n)")

        if search_again == "y" or search_again == "Y":
            another = True
            pokemon = None
        else:
            another = False

    log.info(f"Session end at: {dt.now()}")


def print_header():
    print(" _____      _                              ")
    print("|  __ \\    | |     _                       ")
    print("| |__) |__ | | ___/ /_ __ ___   ___  _ __  ")
    print("|  ___/ _ \\| |/ / _ \\ '_ ` _ \\ / _ \\| '_ \\ ")
    print("| |  | (_) |   <  __/ | | | | | (_) | | | |")
    print("|_|   \\___/|_|\\_\\___|_| |_| |_|\\___/|_| |_|")

def print_pokemon_name(name: str):
    spaces = " " * round((64 - len(name)) / 2)
    print("*" * 64)
    print(f"{spaces}{name.upper()}")
    print("*" * 64)


def print_pokemon_info(pi: dict):
    print(f"ID: {pi['id']}")
    types = pi['types']
    s_types = s_types = f"{types[0]['type']['name']}"
    if len(types) == 2:
        s_types = f"{s_types} and {types[1]['type']['name']}"

    print(f"Type(s): {s_types}")
    print(f"Height: {pi['height']/10} m")
    print(f"Weight: {pi['weight']/10} Kg")
    print("Base Stats:")
    print_base_stats(pi['stats'])


def print_base_stats(stats: list):
    for stat in stats:
        print(f"\t{stat['stat']['name']}: {stat['base_stat']}")


def print_pokemon_species(species: dict):
    print(f"Color: {species['color']['name']}")
    if species['evolves_from_species'] is not None:
        print(f"Evolves from: {species['evolves_from_species']['name']}")
    desc = None
    for flavor_text in species['flavor_text_entries']:
        if flavor_text['language']['name'] == "en":
            desc = flavor_text['flavor_text']
            break
    if desc is not None:
        print(f"Description: {desc}")


if __name__ == "__main__":
    main()
