import os
import json
import questao9

def atualizar_banco_de_dados():
    if not os.path.exists("usuarios.json"):
        with open("usuarios.json", "w") as arquivo:
            json.dump({}, arquivo)

    with open("usuarios.json", "r") as arquivo:
        banco_de_dados = json.load(arquivo)

    print("Dados antes da atualização:", banco_de_dados)

    for usuario_id, usuario_info in banco_de_dados.items():
        if "poke_human" not in usuario_info:
            usuario_info = questao9.encontrar_pokemon(usuario_id)
            if usuario_info:
                banco_de_dados[usuario_id] = usuario_info

    with open("usuarios.json", "w") as arquivo:
        json.dump(banco_de_dados, arquivo, indent=4)

    print("Dados após a atualização:", banco_de_dados)

    print("Banco de dados atualizado com as informações dos Pokémon.")

if __name__ == "__main__":
    atualizar_banco_de_dados()
