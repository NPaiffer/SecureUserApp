import requests
import questao8

def encontrar_pokemon(user_id):
    base_url = "https://pokeapi.co/api/v2/pokemon/"
    usuario = questao8.buscar_usuario_por_id(user_id)

    if not usuario:
        print("Usuário não encontrado.")
        return

    nome_pokemon = usuario.get("login")
    url = base_url + nome_pokemon.lower()
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        abilities = []
        for ability in data["abilities"]:
            ability_info = {
                "name": ability["ability"]["name"],
                "nomes": [(name["name"], name["language"]["name"]) for name in ability["ability"]["names"]],
                "efeitos": [effect["effect"] for effect in ability["ability"]["effect_entries"]],
                "flavors": [flavor["flavor_text"] for flavor in ability["ability"]["flavor_text_entries"]],
                "pokemon_com_mesma_habilidade": [pokemon["pokemon"]["name"] for pokemon in ability["ability"]["pokemon"]]
            }
            abilities.append(ability_info)

        usuario["poke_human"] = {
            "name": nome_pokemon,
            "abilities": abilities
        }

        print("Informações do Pokémon atualizadas com sucesso.")
    else:
        print("Erro ao buscar dados do Pokémon. Status code:", response.status_code)

    return usuario

if __name__ == "__main__":
    user_id = input("Digite o ID do usuário: ")
    encontrar_pokemon(user_id)
