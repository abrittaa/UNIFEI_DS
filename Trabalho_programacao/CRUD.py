
from inventario import criar_produto, dictionary
 
 
def adicionar_produto():
    """Solicita dados ao usuário e adiciona um novo produto ao inventário."""
    print("\n── Adicionar Produto ──")
    nome = input("Nome do produto: ").strip().upper()
    if not nome:
        print("O nome não pode ser vazio.")
        return
 
    for p in dictionary["inventario"]:
        if p["nome"] == nome:
            print(f"Já existe um produto com o nome '{nome}'. Use 'Atualizar' para editá-lo.")
            return
 
    try:
        preco = float(input("Preço do produto: R$ "))
        quantidade = int(input("Quantidade em estoque: "))
    except ValueError:
        print("Valor inválido. Preço e quantidade devem ser numéricos.")
        return
 
    if preco < 0 or quantidade < 0:
        print("Preço e quantidade não podem ser negativos.")
        return
 
    dictionary["inventario"].append(criar_produto(nome, quantidade, preco))
    print(f"Produto '{nome}' adicionado com sucesso!")
 
 
def buscar_produto():
    """Busca um produto pelo nome (parcial) ou ID exato."""
    print("\n── Buscar Produto ──")
    termo = input("Digite o nome ou ID do produto: ").strip()
    encontrados = []
 
    for produto in dictionary["inventario"]:
        if termo.isdigit() and produto["id"] == int(termo):
            encontrados.append(produto)
            break
        elif not termo.isdigit() and termo.lower() in produto["nome"].lower():
            encontrados.append(produto)
 
    if not encontrados:
        print("Nenhum produto encontrado.")
        return
 
    print(f"\n{'ID':<5} | {'Nome':<20} | {'Qtd':<8} | {'Preço':<10}")
    print("-" * 52)
    for p in encontrados:
        print(f"{p['id']:<5} | {p['nome']:<20} | {p['quantidade']:<8} | R$ {p['preco']:>8.2f}")
 
 
def atualizar_produto():
    """Atualiza o preço e/ou quantidade de um produto existente."""
    print("\n── Atualizar Produto ──")
    termo = input("Digite o nome ou ID do produto a ser atualizado: ").strip()
 
    for produto in dictionary["inventario"]:
        match_id = termo.isdigit() and produto["id"] == int(termo)
        match_nome = not termo.isdigit() and produto["nome"].lower() == termo.lower()
 
        if match_id or match_nome:
            print(f"\nProduto encontrado: [{produto['id']}] {produto['nome']} "
                  f"- R${produto['preco']:.2f} | Qtd: {produto['quantidade']}")
            try:
                novo_preco = input("Novo preço (Enter para manter): R$ ").strip()
                nova_qtd   = input("Nova quantidade (Enter para manter): ").strip()
 
                if novo_preco:
                    produto["preco"] = float(novo_preco)
                if nova_qtd:
                    produto["quantidade"] = int(nova_qtd)
            except ValueError:
                print("Valor inválido. Nenhuma alteração foi salva.")
                return
 
            print(f"Produto '{produto['nome']}' atualizado com sucesso!")
            return
 
    print("Produto não encontrado.")
 
 
def remover_produto():
    """Remove um produto do inventário pelo nome exato ou ID."""
    print("\n── Remover Produto ──")
    termo = input("Digite o nome ou ID do produto a ser removido: ").strip()
    inventario = dictionary["inventario"]
    original   = len(inventario)
 
    inventario[:] = [
        p for p in inventario
        if not (
            (termo.isdigit() and p["id"] == int(termo)) or
            (not termo.isdigit() and p["nome"].lower() == termo.lower())
        )
    ]
 
    if len(inventario) < original:
        print("Produto removido com sucesso!")
    else:
        print("Produto não encontrado.")
