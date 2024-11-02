# Programa com um menu de gerenciamento de usuários
while True:
    print("\nMENU")
    print("1 = Incluir usuário")
    print("2 = Excluir usuário")
    print("3 = Consultar usuário")
    print("4 = Alterar usuário")
    print("5 = Listar todos os usuários cadastrados")
    print("9 = Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Opção 1: Incluir usuário")
    elif opcao == "2":
        print("Opção 2: Excluir usuário")
    elif opcao == "3":
        print("Opção 3: Consultar usuário")
    elif opcao == "4":
        print("Opção 4: Alterar usuário")
    elif opcao == "5":
        print("Opção 5: Listar todos os usuários cadastrados")
    elif opcao == "9":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")
