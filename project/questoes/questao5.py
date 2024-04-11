import questao2

def hash_senha(senha):
    num_primo = 17  # Número primo menor que N (pode substituir por outro)
    senha_ord = "".join(str(ord(c)) for c in senha)
    senha_hash = int(senha_ord) % num_primo
    return senha_hash

def proteger_senhas():
    num_primo = 17 # Se substituir em cima, faça o mesmo aqui!
    for usuario in questao2.usuarios:
        senha = usuario["senha"]
        senha_hash = hash_senha(senha)
        usuario["senha"] = senha_hash
        usuario["num_primo"] = num_primo

    print("Senhas protegidas com sucesso!")

if __name__ == "__main__":
    proteger_senhas()
