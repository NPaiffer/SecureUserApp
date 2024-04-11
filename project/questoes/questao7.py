import questao2
import json

def salvar_usuarios(usuarios):
    with open("usuarios.json", "w") as arquivo_json:
        json.dump(usuarios, arquivo_json)

def carregar_usuarios():
    try:
        with open("usuarios.json", "r") as arquivo_json:
            return json.load(arquivo_json)
    except FileNotFoundError:
        return []

usuarios = carregar_usuarios()

def validar_login_e_senha(login, senha):
    return len(login) >= 3 and len(senha) >= 6

def cadastrar_usuario():
    print("\nCadastro de Usuário")

    if not usuario_eh_admin():
        print("Erro: Somente usuários do tipo 'admin' podem cadastrar novos usuários.")
        return

    login = input("Digite o seu login: ")
    senha = input("Digite a sua senha: ")

    if not validar_login_e_senha(login, senha):
        print("Erro: Login ou senha inválidos.")
        return

    novo_login = input("Digite o novo login: ")
    nova_senha = input("Digite a nova senha: ")
    nova_role = input("Digite a nova role (admin ou user): ")

    if nova_role not in ["admin", "user"]:
        print("Role inválida. Será definida como 'user'.")
        nova_role = "user"

    usuarios.append({"login": novo_login, "senha": nova_senha, "role": nova_role})

    salvar_usuarios(usuarios)

    print("Usuário cadastrado com sucesso!")

def usuario_eh_admin():
    return any(usuario["role"] == "admin" for usuario in usuarios)

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
