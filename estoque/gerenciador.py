import os

arquivo_do_estoque = 'estoque.txt'

def carregar_estoque():
    estoque={}
    if not os.path.exists(arquivo_do_estoque):
        return estoque 
    with open (arquivo_do_estoque,'r') as f:
        for linha in f:
            partes = linha.strip().split(',')
            if len(partes)==5:
                id_produto = int(partes[0])
                nome_do_produto = partes[1]
                quantidades = int(partes[2])
                valor_compra = float(partes[3])
                preco_venda = float(partes[4])
                estoque[id_produto]={
                    "nome do produto":nome_do_produto,
                    "quantidade":quantidades,
                    "valor da compra":valor_compra,
                    "preço da venda":preco_venda
                }
    return estoque
                
def salvar_estoque(estoque):
    with open(arquivo_do_estoque,'w') as f:
        for id_produto, dados in estoque.items():
            f.write(f"{id_produto},{dados['nome']},{dados['quantidade']},{dados['valor_compra']:.2f},{dados['preco_venda']:.2f}\n")

def gerar_id(estoque):
    return max(estoque.keys(), default=0)+1

def adicionar_produto(estoque,nome,quantidade,valor):
    novo_id = gerar_id(estoque)
    preco_venda = round(valor*1.10, 2)
    estoque[novo_id]={
        "nome do produto":nome,
        "quantidade":quantidade,
        "valor da compra":valor,
        "preço da venda":preco_venda
    }
    salvar_estoque(estoque)
    print(f"Produto '{nome}' cadastrado com ID {novo_id} e preço de venda R$ {preco_venda:.2f}.")
    
def listar(estoque):
    if not estoque:
        print("estoque vazio")
        return
    print("/n--- Produtos no Estoque ---")
    for id_prod, p in estoque.items():
        print(f"ID: {id_prod} | Nome: {p['nome']} | Qtde: {p['quantidade']} | Compra: R$ {p['valor_compra']:.2f} | Venda: R$ {p['preco_venda']:.2f}")
    print("----------------------------")