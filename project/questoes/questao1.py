import string

def criar_login_e_senha():
    while True:
        try:
            tipo_login = input("Escolha o tipo de login (email, user-name, CPF ou RG): ").lower()
            if tipo_login == "email":
                login = input("Digite o seu email: ")
                if "@" not in login or "." not in login:
                    raise ValueError("Email inválido. Deve estar no formato xxxxx@yyy.zzz")
            elif tipo_login == "user-name":
                login = input("Digite o seu user-name: ")
                if not all(char.isalnum() or char == "_" for char in login):
                    raise ValueError("User-name inválido. Deve conter apenas caracteres alfanuméricos e '_'")
            elif tipo_login == "cpf":
                login = input("Digite o seu CPF (no formato XXX.XXX.XXX-XX ou XXXXXXXXXXX): ")
                if not (login.isdigit() and len(login) in [11, 14] and (len(login) == 11 or login[3] == "." and login[7] == "." and login[11] == "-")):
                    raise ValueError("CPF inválido. Deve estar no formato XXX.XXX.XXX-XX ou XXXXXXXXXXX")
            elif tipo_login == "rg":
                login = input("Digite o seu RG (no formato XX.XXX.XXX-X ou XXXXXXXXX): ")
                if not (login.isdigit() and len(login) in [9, 12] and (len(login) == 9 or login[2] == "." and login[6] == "." and login[10] == "-")):
                    raise ValueError("RG inválido. Deve estar no formato XX.XXX.XXX-X ou XXXXXXXXX")
            else:
                raise ValueError("Tipo de login inválido.")
            break

        except Exception as e:
            print(f"Erro: {e}")

    senha = input("Digite a sua senha: ")

    tipos_caracteres = {
        "numérico": False,
        "maiúsculo": False,
        "minúsculo": False,
        "especial": False
    }
    for char in senha:
        if char.isdigit():
            tipos_caracteres["numérico"] = True
        elif char.isupper():
            tipos_caracteres["maiúsculo"] = True
        elif char.islower():
            tipos_caracteres["minúsculo"] = True
        elif char in "!@#$%&*()[]{};,.:/\\":
            tipos_caracteres["especial"] = True
        
    if len(senha) < 12 or not all(tipos_caracteres.values()):
        print("Senha inválida. Deve conter ao menos 12 caracteres e pelo menos 2 caracteres de cada tipo: numérico, maiúsculo, minúsculo e especial.")
        return

    print("Login e senha criados com sucesso!")
criar_login_e_senha()
