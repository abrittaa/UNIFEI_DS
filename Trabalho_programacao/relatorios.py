def valor_total(inventario):
    """
    Calcula o valor total do estoque multiplicando a quantidade de 
    cada produto pelo seu preço e somando tudo.
    """
    total = 0.0
    for produto in inventario:
        total += produto['quantidade'] * produto['preco']
    return total


def estoque_baixo(inventario, limite_minimo=10):
    """
    Filtra e retorna uma lista de produtos que estão com a quantidade 
    abaixo do limite mínimo estipulado (o padrão é 10).
    """
    produtos_em_alerta = []
    for produto in inventario:
        if produto['quantidade'] < limite_minimo:
            produtos_em_alerta.append(produto)
    return produtos_em_alerta


def exibir_relatorio(inventario, limite_minimo=10):
    """
    Gera uma exibição formatada das estatísticas do estoque, incluindo
    o valor total e os alertas de estoque baixo.
    """
    print("\n" + "="*50)
    print(" "*14 + "RELATÓRIO DE ESTOQUE")
    print("="*50)

    if not inventario:
        print("O inventário está vazio no momento.")
        print("="*50)
        return

    # 1. Exibir a lista de produtos formatada em tabela
    print(f"{'ID':<4} | {'Nome do Produto':<20} | {'Qtd':<5} | {'Preço (R$)':<10}")
    print("-" * 50)
    for prod in inventario:
        print(f"{prod['id']:<4} | {prod['nome']:<20} | {prod['quantidade']:<5} | R$ {prod['preco']:<8.2f}")
    
    # 2. Calcular e exibir o valor total (usando sua função)
    total_financeiro = valor_total(inventario)
    print("-" * 50)
    print(f"VALOR TOTAL DO ESTOQUE: R$ {total_financeiro:.2f}")

    # 3. Calcular e exibir produtos com estoque baixo (usando sua função)
    print("\n--- ALERTA DE ESTOQUE BAIXO (Abaixo de {limite_minimo} un.) ---")
    produtos_baixos = estoque_baixo(inventario, limite_minimo)
    
    if produtos_baixos:
        for prod in produtos_baixos:
            print(f" ⚠️ ATENÇÃO: '{prod['nome']}' tem apenas {prod['quantidade']} unidade(s)!")
    else:
        print(" ✅ Tudo certo! Nenhum produto com estoque baixo.")
    
    print("="*50 + "\n")