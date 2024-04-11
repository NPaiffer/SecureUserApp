def encontrar_primo(N):
    if N < 2:
        raise ValueError("N deve ser maior ou igual a 2.")

    for num in range(N, 1, -1):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            return num

    raise ValueError("Não foi possível encontrar um número primo.")

def menu():
    while True:
        print("\nMenu")
        print("1. Cadastrar Usuário")
        print("2. Atualizar Login e Senha")
        print("3. Encontrar o Maior Número Primo até N")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            atualizar_login_e_senha()
        elif opcao == "3":
            try:
                N = int(input("Digite o valor de N: "))
                primo = encontrar_primo(N)
                print(f"O maior número primo até {N} é: {primo}")
            except ValueError as e:
                print(f"Erro: {e}")
        elif opcao == "4":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
