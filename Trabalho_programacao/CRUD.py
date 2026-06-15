def adicionar_produto(produtos):
    nome = input("Digite o nome do produto: ").upper()
    preco = float(input("Digite o preço do produto: R$ "))
    quantidade = int(input("Digite a quantidade em estoque: "))
    produtos.append({"nome": nome, "preco": preco, "quantidade": quantidade})
    print("Produto adicionado com sucesso!")

def remover_produto(produtos):
    nome = input("Digite o nome do produto a ser removido: ")
    original = len(produtos)
    produtos[:] = [p for p in produtos if p["nome"].lower() != nome.lower()]
    if len(produtos) < original:
        print("Produto removido com sucesso!")
    else:
        print("Produto não encontrado.")

def atualizar_produto(produtos):
    nome = input("Digite o nome do produto a ser atualizado: ")
    for produto in produtos:
        if produto["nome"].lower() == nome.lower(): 
            produto["preco"] = float(input("Digite o novo preço: R$ "))
            produto["quantidade"] = int(input("Digite a nova quantidade: "))
            print("Produto atualizado com sucesso!")
            return
    print("Produto não encontrado.")

def buscar_produto(produtos):
    nome = input("Digite o nome do produto a ser buscado: ")
    for produto in produtos:
        if nome.lower() in produto["nome"].lower(): 
            print(f"Encontrado: {produto['nome']} - R${produto['preco']:.2f} | Qtd: {produto['quantidade']}")
            return
    print("Produto não encontrado.")

def listar_produtos(produtos):
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    print("\n--- Lista de Produtos ---")
    for i, produto in enumerate(produtos, start=1):
        print(f"{i}. {produto['nome']} - R${produto['preco']:.2f} | Qtd: {produto['quantidade']}")
    print("-------------------------\n")