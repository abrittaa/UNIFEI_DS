import csv
import os

# ==========================================
# MÓDULO 3: RELATÓRIOS
# ==========================================

def valor_total(inventario):
    "Calcula o valor total de todos os produtos no estoque."
    total = 0.0
    for produto in inventario:

# Multiplica a quantidade pelo preço de cada item

        qtd = float(produto['quantidade'])
        preco = float(produto['preco'])
        total += (qtd * preco)
    return total

def estoque_baixo(inventario, limite=5):
    "lista de produtos que estão com a quantidade abaixo do limite."
    produtos_baixos = []
    for produto in inventario:
        if int(produto['quantidade']) < limite:
            produtos_baixos.append(produto)
    return produtos_baixos

def exibir_relatorio(inventario):
    "Gera um texto formatado com o resumo do estoque ."
    if not inventario:
        return "O inventário está vazio no momento."

    linhas = ["--- RELATÓRIO DE ESTOQUE ---"]

    for p in inventario:
        linha = f"ID: {p['id']} | Nome: {p['nome']} | Qtd: {p['quantidade']} | Preço: R$ {float(p['preco']):.2f}"
        linhas.append(linha)

    linhas.append(f"\nValor Total em Estoque: R$ {valor_total(inventario):.2f}")

    baixos = estoque_baixo(inventario)
    if baixos:
        linhas.append("\nATENÇÃO! Produtos com estoque baixo:")
        for b in baixos:
            linhas.append(f"- {b['nome']} (Apenas {b['quantidade']} em estoque)")

# Junta todas as linhas em um texto só
    return "\n".join(linhas)


# ==========================================
# MÓDULO 4: PERSISTÊNCIA DE DADOS (ARQUIVO)
# ==========================================

def salvar_inventario(inventario, nome_arquivo="inventario.csv"):
    """Salva a lista de dicionários em um arquivo CSV."""
    if not inventario:

# Se estiver vazio, cria um arquivo em branco só com o cabeçalho

        colunas = ['id', 'nome', 'quantidade', 'preco']
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=colunas)
            escritor.writeheader()
        return "Inventário vazio salvo com sucesso."

# AJUSTE DE INTEGRAÇÃO: Evita erro de IndexError caso a lista seja enviada de forma inesperada
    if isinstance(inventario, list) and len(inventario) > 0:
        colunas = inventario[0].keys()
    else:
        colunas = ['id', 'nome', 'quantidade', 'preco']

    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=colunas)
        escritor.writeheader()
        for produto in inventario:
            escritor.writerow(produto)

    return f"Dados salvos com sucesso em {nome_arquivo}!"

def carregar_inventario(nome_arquivo="inventario.csv"):
    """Lê o arquivo CSV e devolve a lista de dicionários."""
    inventario_carregado = []

# Se o arquivo ainda não existir, retorna a lista vazia pra não dar erro na primeira vez que rodar

    if not os.path.exists(nome_arquivo):
        return inventario_carregado

    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            # Valida se todas as chaves necessárias estão presentes
            if not all(key in linha for key in ['id', 'nome', 'quantidade', 'preco']):
                print(f"⚠️ Aviso: Linha incompleta ignorada: {linha}")
                continue

# Como o CSV salva tudo como texto, precisamos converter os números de volta

            try:
                produto = {
                    'id': int(linha['id']),
                    'nome': linha['nome'],
                    'quantidade': int(linha['quantidade']),
                    'preco': float(linha['preco'])
                }
                inventario_carregado.append(produto)
            except (ValueError, KeyError) as e:
                print(f"⚠️ Aviso: Erro ao processar linha {linha}: {e}")
                continue

    return inventario_carregado