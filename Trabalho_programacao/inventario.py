dictionary = {
    "inventario": [],
    "id_serial": 1
}

def criar_produto(nome, quantidade, preco):
    
    produto = {
        "id": dictionary["id_serial"],
        "nome": nome,
        "quantidade": quantidade,
        "preco": float(preco)
    }
    
    #Para não ter que inserir um serial number manualmente, o sistema mesmo cria, por meio desse contador simples.
    dictionary["id_serial"] += 1
    return produto

def listar_produtos():
    """
    Percorre a lista de inventário dentro do dicionário "dictionary" e puxa apenas a variável "inventario" para conseguir listar os produtos por meio de for. Caso não tenha nada, mostra que o inventário está vazio.
    """
    lista = dictionary["inventario"]
    
    if not lista:
        print("O inventário está vazio.")
        return

    #Organizei o cabeçalho da tabela. Deixei essas partes com :<5 e afins para a coluna ficar de tamanho fixo, saca? Ficou legal
    print(f"{'ID':<5} | {'Nome':<20} | {'Qtd':<8} | {'Preço':<10}")
    print("-" * 50)
    
    #Isso aqui serve para printar os dados no terminal (é isso que precisava, andré?)
    for prod in lista:
        print(f"{prod['id']:<5} | {prod['nome']:<20} | {prod['quantidade']:<8} | R$ {prod['preco']:>8.2f}")


# -------------------------------------------------------------
# FUNÇÃO ADICIONADA: Necessária para a integração dos módulos
# -------------------------------------------------------------
def sincronizar_contador():
    """Atualiza o id_serial baseado no maior ID do inventário atual para evitar duplicidade."""
    if dictionary["inventario"]:
        maior_id = max(prod["id"] for prod in dictionary["inventario"])
        dictionary["id_serial"] = maior_id + 1