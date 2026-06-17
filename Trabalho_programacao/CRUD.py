#importar a função criar_produto e o dicionário dictionary do módulo inventario
from inventario import criar_produto, dictionary 
 
#função para adicionar um produto ao inventário
def adicionar_produto():
    print("\n── Adicionar Produto ──")
    nome = input("Nome do produto: ").strip().upper()
    if not nome:
        print("O nome não pode ser vazio.")
        return
#checar a lista para ver o se o produto já consta no inventário 
    for p in dictionary["inventario"]:
        if p["nome"] == nome:
            print(f"Já existe um produto com o nome '{nome}'. Use 'Atualizar' para editá-lo.")
            return
#checar se o preço e a quantidade são válidos (não negativos e numéricos) 
    try:
        preco = float(input("Preço do produto: R$ "))
        quantidade = int(input("Quantidade em estoque: "))
    except ValueError:
        print("Valor inválido. Preço e quantidade devem ser numéricos.")
        return 
    if preco < 0 or quantidade < 0:
        print("Preço e quantidade não podem ser negativos.")
        return

#finalmente, adiiconar o produto ao inventário e informar o usuário
    dictionary["inventario"].append(criar_produto(nome, quantidade, preco))
    print(f"Produto '{nome}' adicionado com sucesso!")
 
#função para buscar os produtos no inventário
def buscar_produto():
    print("\n── Buscar Produto ──")
    termo = input("Digite o nome ou ID do produto: ").strip()
    encontrados = []

#percorrer o inventário e verificar se o termo digitado corresponde ao nome ou ID do produto 
    for produto in dictionary["inventario"]:
        if termo.isdigit() and produto["id"] == int(termo):
            encontrados.append(produto)
            break
        elif not termo.isdigit() and termo.lower() in produto["nome"].lower():
            encontrados.append(produto)

#se não houver produtos encontrados, retorna que não foi encontrado
    if not encontrados:
        print("Nenhum produto encontrado.")
        return

#printa uma tabela com os produtos encontrados, formatando as colunas para melhor visualização
    print(f"\n{'ID':<5} | {'Nome':<20} | {'Qtd':<8} | {'Preço':<10}")
    print("-" * 52)
    for p in encontrados:
        print(f"{p['id']:<5} | {p['nome']:<20} | {p['quantidade']:<8} | R$ {p['preco']:>8.2f}")
 

#função para atualizar a situação de um produto ja listado no inventário
def atualizar_produto():
    print("\n── Atualizar Produto ──")
    termo = input("Digite o nome ou ID do produto a ser atualizado: ").strip()

#percorre o inventário e ve se o item está no inventário
    for produto in dictionary["inventario"]:
        match_id = termo.isdigit() and produto["id"] == int(termo)
        match_nome = not termo.isdigit() and produto["nome"].lower() == termo.lower()

#se o produto for encontrado, abre um input para atualizar os valores
        if match_id or match_nome:
            print(f"\nProduto encontrado: [{produto['id']}] {produto['nome']} "
                  f"- R${produto['preco']:.2f} | Qtd: {produto['quantidade']}")
            try:
                novo_preco = input("Novo preço (Enter para manter): R$ ").strip()
                nova_qtd   = input("Nova quantidade (Enter para manter): ").strip()

#muda os valores para o que o usuario digitou, caso ele tenha digitado algo. Se não, mantém o valor antigo 
                if novo_preco:
                    produto["preco"] = float(novo_preco)
                if nova_qtd:
                    produto["quantidade"] = int(nova_qtd)
#se der erro de valor, ele nao altera nada e retorna uma mensagem de erro
            except ValueError:
                print("Valor inválido. Nenhuma alteração foi salva.")
                return
#informa o usuario que o valor foi alterado 
            print(f"Produto '{produto['nome']}' atualizado com sucesso!")
            return
 
    print("Produto não encontrado.")

#função para remover um produto do inventário
def remover_produto():
    print("\n── Remover Produto ──")
    termo = input("Digite o nome ou ID do produto a ser removido: ").strip()
    inventario = dictionary["inventario"]
    original   = len(inventario)

#percorre o inventário e remove o produto que corresponde ao termo digitado, seja pelo ID ou pelo nome. 
    inventario[:] = [
        p for p in inventario
        if not (
            (termo.isdigit() and p["id"] == int(termo)) or
            (not termo.isdigit() and p["nome"].lower() == termo.lower())
        )
    ]

#informa o usuario se o produto foi removido ou se não foi encontrado 
    if len(inventario) < original:
        print("Produto removido com sucesso!")
    else:
        print("Produto não encontrado.")
