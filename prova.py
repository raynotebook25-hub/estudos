# pedir informaçoes de um contatto e armazenar num dicionario 

# menu 

contatos = []

while True:
    print("=== MENU ===")
    print("[1] Adicionar contato")
    print("[2] Ver contatos")
    print("[3] Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = input("Digite o nome: ")
        telefone = int(input("Digite o telefone: "))
        email = input("Digite o email: ")

        contato = {
            'nome' : nome,
            'telefone' : telefone,
            'email' : email
        }

        contatos.append(contato) 
        
        print("Contato adicionado com sucesso!")

    elif opcao == 2:
        print("Lista de contatos:")
        for contato in contatos:
            print("=====================")
            print("Nome:", contato['nome'])
            print("Telefone:", contato['telefone'])
            print("Email:", contato['email'])
            print("=====================")

    elif opcao == 3:
        print("Tem certeza que deseja sair? (s/n)")            
        confirmar = input().lower()
        if confirmar ==  's':
            print("Saindo do programa....")
            break
        else:
            continue

    else:
        print("Opção inválida, tente novamente.")
        
            

