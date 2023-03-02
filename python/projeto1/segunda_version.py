import yaml

produtos = []

with open('banco_dados.yaml','r') as file:
    produtos = yaml.safe_load(file)
if produtos == None:
    	produtos = []

def upd_bd():
    with open('banco_dados.yaml','w') as file:
    	yaml.dump(produtos,file)

def cadastrar_produtos():
    global produtos
    nome = str(input("Informe o nome do produto: "))
    quantidade = int(input("Informe a quantidade de itens: "))
    valor = float(input("Informe o valor do item: "))
    produto = [nome,quantidade,valor]
    produtos.append(produto)
    upd_bd()
    print("Produto cadastrado com Sucesso!\n")

def consultar_produtos():
    if len(produtos) > 0:
        for produto in produtos:
            ident = produtos.index(produto)
            nome,quantidade,valor = produto
            print("id: " + str(ident) + "\nnome: " + nome + "\nestoque: " + str(quantidade) + "\nvalor: " + str(valor) +  "\n***********************************")

def atualizar_produto():
    opcao = int(input("Digite o id do produto a ser atualizado"))
    nome,quantidade,valor = produtos[opcao]
    upd_bd()
    produto_velho = "Produto: " + nome + " Quantidade: " + str(quantidade) + " Valor: " + str(valor)

    n = str(input("Digite um novo nome para atualizar ou deixe em branco para manter o nome atual"))
    if  not n == "":
        nome = n

    q = str(input("Digite uma nova quantidade ou deixe em branco para manter a quantidade atual"))
    if not q == "": 
        quantidade = int(q) 

    v = str(input("Digite um novo valor ou deixe em branco para manter o valor atual"))
    if not v == "":
        valor = float(v)

    produto_novo = "Produto: " + nome + " Quantidade: " + str(quantidade) + " Valor: " + str(valor)

    if produto_velho == produto_novo:
        print("O produto manteve os mesmo valores")
    else:
        Print("Antes: " + produto_velho)
        Print("Depois: " + produto_novo)
        produtos[opcao] = [nome,quantidade,valor]


def menu():
    rodando = True
    while rodando:
        opcao = int(input("\nDigite \n1 para cadastrar\n2 para consultar\n3 para atualizar um produto\n0 para sair\n"))
        if opcao == 1:
            cadastrar_produtos()
        elif opcao == 2:
            consultar_produtos()
        elif opcao == 3:
            atualizar_produto()
        elif opcao == 0:
            rodando = False
        else:
            Print("\nEste não é um código valido")

menu()
