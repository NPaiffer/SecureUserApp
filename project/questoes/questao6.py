import questao2
import questao5

def realizar_login():
    print("\nLogin")

    login = input("Digite o seu login: ")
    senha = input("Digite a sua senha: ")

    usuario = buscar_usuario(login)
    if usuario is None:
        print("Usuário não encontrado.")
        return

    senha_hash_digitada = questao5.hash_senha(senha)

    if senha_hash_digitada == usuario["senha"]:
        print("Login realizado com sucesso!")
    else:
        print("Senha incorreta.")

def buscar_usuario(login):
    for usuario in questao2.usuarios:
        if usuario["login"] == login:
            return usuario
    return None

if __name__ == "__main__":
    realizar_login()
