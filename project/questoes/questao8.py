import hashlib
import json
import questao7

def calcular_user_id(login, senha):
    hashed_senha = hashlib.sha256(senha.encode()).hexdigest()
    user_id = hashlib.sha256((login + hashed_senha).encode()).hexdigest()
    return user_id

def cadastrar_usuario():
    print("\nCadastro de Usuário")

    login = input("Digite o seu login: ")
    senha = input("Digite a sua senha: ")

    if not questao1.validar_login_e_senha(login, senha):
        print("Erro: Login ou senha inválidos.")
        return

    novo_login = input("Digite o novo login: ")
    nova_senha = input("Digite a nova senha: ")
    nova_role = input("Digite a nova role (admin ou user): ")

    if nova_role not in ["admin", "user"]:
        print("Role inválida. Será definida como 'user'.")
        nova_role = "user"

    user_id = calcular_user_id(novo_login, nova_senha)

    questao7.salvar_usuario({"login": novo_login, "senha": nova_senha, "role": nova_role, "user_id": user_id})

    print("Usuário cadastrado com sucesso!")

def buscar_usuario_por_id(user_id):
    usuarios = questao7.carregar_usuarios()
    for usuario in usuarios:
        if usuario["user_id"] == user_id:
            return usuario
    return None

def menu():
    while True:
        print("\nMenu")
        print("1. Cadastrar Usuário")
        print("2. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
