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

def adicionar_produto():
    return