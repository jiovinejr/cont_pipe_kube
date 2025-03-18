from src.api import fetch_pokemon

def main():
    data = fetch_pokemon()
    if data:
        print("First Pokémon:", data["results"][0]["name"])
    else:
        print("Failed to fetch Pokémon data.")

if __name__ == "__main__":
    main()
