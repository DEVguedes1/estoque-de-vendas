from .gerenciador import salvar_estoque

def registro_de_vendas(estoque,id_prod,qntd):
    if id_prod not in estoque:
        print(f"Erro: Produto com ID {id_prod} não encontrado.")
        return
    
    produto = estoque[id_prod]
    nome = produto['nome']
    
    if qntd > produto['quantidade']:
        print(f"Erro: Estoque insuficiente para '{nome}'. Disponível: {produto['quantidade']}, Requisitado: {qntd}")
        return
    
    produto['quantidade']-= qntd
    salvar_estoque(estoque)
    total = produto['preço do produto']*qntd
    print(f"Venda registrada: {qntd}x '{nome}' por R$ {produto['preco_venda']:.2f} cada. Total: R$ {total:.2f}")