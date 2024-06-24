import requests
import json

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to fetch data for {pokemon_name}. Status code: {response.status_code}")
        return None

def main():
    pokemon_name = "pikachu"
    pokemon_data = fetch_pokemon_data(pokemon_name)

    if pokemon_data:
        print(f"Pokemon Name: {pokemon_data['name']}")
        print(f"Pokemon ID: {pokemon_data['id']}")
        print(f"Abilities:")
        for ability in pokemon_data['abilities']:
            print(f"- {ability['ability']['name']}")
    else:
        print("Failed to fetch Pokemon data.")

if __name__ == "__main__":
    main()
