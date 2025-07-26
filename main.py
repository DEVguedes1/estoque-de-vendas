from estoque.gerenciador import *
from estoque.vendas import *

def menu():
    print("\n==== SISTEMA DE VENDAS ====")
    print("1. Incluir produto")
    print("2. Listar produtos no estoque")
    print("3. Buscar produto por nome")
    print("4. Registrar venda de produto")
    print("5. Sair")
    return int(input("escolha uma das opções:"))

def main():
    estoque = carregar_estoque()
    
    while True:
        opcao=menu()
        
        if opcao==1:
            try:
                nome_produto = input("Nome do produto: ")
                quantidade = int(input("Quantidade: "))
                valor_compra = float(input("Valor da compra: "))
                adicionar_produto(estoque,nome_produto,quantidade,valor_compra)
            except ValueError:
                print("Erro: entrada invalida")
        elif opcao==2:
            listar(estoque)
        elif opcao==3:
            termo = input("Digite o nome ou parte do nome do produto: ")    
            buscar(estoque,termo)
        elif opcao==4:
            try:
                id_prod = int(input("ID do produto: "))
                quantidade = int(input("Quantidade a vender: "))
                registro_de_vendas(estoque,id_prod,quantidade)
            except ValueError:
                print("Erro: entrada invalida")
        elif opcao==5:
            print("saindo do sistema...")
            break
        else:
            print("Erro: entrada invalida")
if __name__ == '__main__':
    main()
            