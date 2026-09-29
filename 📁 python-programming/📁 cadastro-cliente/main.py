usuarios = []

def adicionar_usuario(nome, idade, email):
    usuario = {
        "nome": nome,
        "idade": idade,
        "email": email
    }
    usuarios.append(usuario)
    print(f"Usuário {nome} adicionado com sucesso!")

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    print("\nLista de Usuários:")
    for usuario in usuarios:
        print(f"Nome: {usuario['nome']}, Idade: {usuario['idade']}, E-mail: {usuario['email']}")

def remover_usuario(nome):
    for usuario in usuarios:
        if usuario["nome"] == nome:
            usuarios.remove(usuario)
            print(f"Usuário {nome} removido com sucesso!")
            return

    print(f"Usuário {nome} não encontrado.")

# 🔥 MENU
while True:
    print("\n1 - Adicionar usuário")
    print("2 - Listar usuários")
    print("3 - Remover usuário")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        email = input("Email: ")
        adicionar_usuario(nome, idade, email)

    elif opcao == "2":
        listar_usuarios()

    elif opcao == "3":
        nome = input("Digite o nome para remover: ")
        remover_usuario(nome)

    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")