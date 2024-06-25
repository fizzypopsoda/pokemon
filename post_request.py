import requests
import pandas as pd
import sqlalchemy as db

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for {pokemon_name}. Status code: {response.status_code}")
        return None

def pokemon_data_to_dataframe(pokemon_data):
    abilities = ', '.join([ability['ability']['name'] for ability in pokemon_data['abilities']])
    data = {
        'id': [pokemon_data['id']],
        'name': [pokemon_data['name']],
        'base_experience': [pokemon_data['base_experience']],
        'height': [pokemon_data['height']],
        'weight': [pokemon_data['weight']],
        'abilities': [abilities]
    }
    return pd.DataFrame.from_dict(data)

def save_to_database(df, table_name='pokemon', db_name='pokemon.db'):
    engine = db.create_engine(f'sqlite:///{db_name}')
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    print(f"Data saved to {table_name} table in {db_name} database.")
    return engine

def query_database(engine, table_name='pokemon'):
    with engine.connect() as connection:
        query_result = connection.execute(db.text(f"SELECT * FROM {table_name};")).fetchall()
        df_result = pd.DataFrame(query_result, columns=['id', 'name', 'base_experience', 'height', 'weight', 'abilities'])
        print(df_result)

def main():
    pokemon_name = "pikachu"
    pokemon_data = fetch_pokemon_data(pokemon_name)
    if pokemon_data:
        df = pokemon_data_to_dataframe(pokemon_data)
        engine = save_to_database(df)
        query_database(engine)
    else:
        print("Failed to fetch Pokémon data.")

if __name__ == "__main__":
    main()

