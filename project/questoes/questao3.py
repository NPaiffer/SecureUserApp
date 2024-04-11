import questao1

usuarios = []

def validar_login_e_senha(login, senha):
    return len(login) >= 3 and len(senha) >= 6

def usuario_eh_admin():
    return any(usuario["role"] == "admin" for usuario in usuarios)

def cadastrar_usuario():
    print("\nCadastro de Usuário")

    login = input("Digite o seu login: ")
    senha = input("Digite a sua senha: ")

    if not validar_login_e_senha(login, senha):
        raise ValueError("Login ou senha inválidos.")

    if not any(usuario["role"] == "admin" for usuario in usuarios):
        raise PermissionError("Somente usuários do tipo 'admin' podem cadastrar novos usuários.")

    novo_login = input("Digite o novo login: ")
    nova_senha = input("Digite a nova senha: ")
    nova_role = input("Digite a nova role (admin ou user): ")

    if nova_role not in ["admin", "user"]:
        print("Role inválida. Será definida como 'user'.")
        nova_role = "user"

    usuarios.append({"login": novo_login, "senha": nova_senha, "role": nova_role})

    print("Usuário cadastrado com sucesso!")

def atualizar_login_e_senha():
    print("\nAtualização de Login e Senha")

    login = input("Digite o seu login: ")
    senha = input("Digite a sua senha: ")

    usuario_atual = None
    for usuario in usuarios:
        if usuario["login"] == login and usuario["senha"] == senha:
            usuario_atual = usuario
            break

    if usuario_atual is None:
        print("Usuário não encontrado ou senha incorreta.")
        return

    usuario_admin = usuario_eh_admin()
    if not usuario_admin and usuario_atual["role"] == "admin":
        print("Erro: Você não tem permissão para alterar as credenciais de um usuário admin.")
        return

    if not usuario_admin and usuario_atual["role"] == "user":
        novo_login = input("Digite o novo login: ")
        nova_senha = input("Digite a nova senha: ")

        if not validar_login_e_senha(novo_login, nova_senha):
            print("Erro: Login ou senha inválidos.")
            return

        usuario_atual["login"] = novo_login
        usuario_atual["senha"] = nova_senha

        print("Login e senha atualizados com sucesso!")
    elif usuario_admin:
        novo_login = input("Digite o novo login: ")
        nova_senha = input("Digite a nova senha: ")

        if not validar_login_e_senha(novo_login, nova_senha):
            print("Erro: Login ou senha inválidos.")
            return

        usuario_atual["login"] = novo_login
        usuario_atual["senha"] = nova_senha

        print("Login e senha atualizados com sucesso!")
    else:
        print("Erro: Você não tem permissão para alterar as credenciais de outro usuário.")

def menu():
    while True:
        print("\nMenu")
        print("1. Cadastrar Usuário")
        print("2. Atualizar Login e Senha")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            atualizar_login_e_senha()
        elif opcao == "3":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
