lista_nomes = []
lista_medidas = []
lista_quantidade = []
lista_descricao = []

ID = {lista_nomes[]: lista_medidas[]: lista_quantidade[]: lista_descricao[] for i in range(len(lista_nomes))}W


def adicionar_produto():
     nome_produto = input("Nome do produto: ")
     unidade_medida = input("Unidade de medida: ")
     quantidade = input("Quantidade: ")
     descricao_produto = input("Descricao: ")

     lista_nomes.append(nome_produto)
     lista_medidas.append(unidade_medida)
     lista_quantidade.append(quantidade)
     lista_descricao.append(descricao_produto)

def remover_produto():
    nome_produto = input("Nome do produto: ")
    unidade_medida = input("Unidade de medida: ")
    quantidade = input("Quantidade: ")
    descricao_produto = input("Descricao: ")

    lista_nomes.remove(nome_produto)
    lista_medidas.remove(unidade_medida)
    lista_quantidade.remove(quantidade)
    lista_descricao.remove(descricao_produto)

def pesquisar_produto():
     produto = input("Nome do produto: ")
     print(ID[produto])



print("Bem vindo à sua lista de compras\n")

while True:
    opcao = input("""Menu
A. Adicionar Produto
B. Remover Produto
C. Pesquisar Produtos
D. Sair do programa\n""")

    if opcao == "A":
        adicionar_produto()
    elif opcao == "B":
        remover_produto()
    elif opcao == "C":
        pesquisar_produto()
    elif opcao == "D":
        print("Saindo do programa...")
        break
    else:
        print("Não é uma opção valida.")

