# Construa uma aplicação em Python que disponibilize uma estrutura interna, para armazenagem e manipulação dos dados e a 
# interação com o usuário a partir de um menu com as seguintes opções:

# 1 - Cadastrar 
# 2 - Pesquisar
# 3 - Excluir
# 4 - Listar
# 5 - Ordenar Por Nome
# 6 - Ordenar Por Código
# 7 - Ordenar Por Gols
# 8 - Salvar
# 0 - Sair
# Especificações: 
# 1 - Para a opção cadastrar, solicitar ao usuário qual a quantidade de jogadores a serem inseridos. Utilizar o gerador de 
# nomes e o gerador de número randômicos no cadastramento.
# 2 - Para a Pesquisa, possibilitar ao usuário a consulta pelo código do jogador.; 
# 3 - A opção excluir deverá solicitar ao usuário o código do jogador a ser excluído e em seguida removê-lo da estrutura;
# 4 - A opção listar deverá listar todos os dados de todos os jogadores;
# 5 - Ordenar por nome deverá utilizar o algoritmos de ordenação BubbleSort (Modificado no exercício anterior);
# 6 - Ordenar por Código deverá utilizar o algoritmo de Ordenação InsertionSort;
# 7 - Ordenar por Quantidade de gols deverá utilizar o algoritmo de Ordenação SelectionSort;
# 8 - A Opção Salvar deverá salvar a relação de jogadores em um arquivo texto.

from Gerador import Gerador
from Jogador import Jogador

jogadores = []

def gerador_jogadores(tamanho):
    numero_jogadores = tamanho
    g = Gerador()
    for i in range(numero_jogadores):
        p = Jogador(g.geraCodigo(), g.geraNome(), g.geraSobrenome(), g.geraIdade(), g.geraPartidas(), g.geraGols())
        jogadores.append(p)
 

# 1 - Para a opção cadastrar, solicitar ao usuário qual a quantidade de jogadores a serem inseridos. Utilizar o gerador de 
# nomes e o gerador de número randômicos no cadastramento.
def cadastrar():
    quantidadeJogadores = int(input("Digite a quantidade de jogadores: "))
    gerador_jogadores(quantidadeJogadores) 
    menu()

# 2 - Para a Pesquisa, possibilitar ao usuário a consulta pelo código do jogador.; 
def consulta():
    codigoConsulta = int(input("Digite um código para consulta: "))

    while codigoConsulta < 1000 and codigoConsulta > 9999:
        codigoConsulta = input("Digite um código VALIDO para consulta: ")
    
    jogadoresConsulta = []
    for k in range(len(jogadores)):
        if str(codigoConsulta) in str(jogadores[k].getCodigo()):
            jogadoresConsulta.append(jogadores[k])

    print("JOGADORES COM O CODIGO:")
    for k in range(len(jogadoresConsulta)):
        print(jogadoresConsulta[k].getRegistro())
    menu()


# 3 - A opção excluir deverá solicitar ao usuário o código do jogador a ser excluído e em seguida removê-lo da estrutura;
def excluir():
    codigoJogador = int(input("Inisra o codigo do jogador: "))
    for k in range(len(jogadores)):
        if jogadores[k].getCodigo() == codigoJogador:
            jogadorExcluir = jogadores[k]

    jogadores.remove(jogadorExcluir)
    print("Jogador excluido foi: \n " + jogadorExcluir.getRegistro())
    menu()

# 4 - A opção listar deverá listar todos os dados de todos os jogadores;
def listar():
    print("===============JOGAODRES CADASTRADOS================")
    for k in range(len(jogadores)):
        print(jogadores[k].getRegistro())
    if len(jogadores) <= 0: print("SEM JOGADORES CADASTRADOS")
    menu()

# 5 - Ordenar por nome deverá utilizar o algoritmos de ordenação BubbleSort (Modificado no exercício anterior);
def ordenarNome():
    for i in range(len(jogadores)-1,0,-1):
        for j in range(i): 
            if jogadores[j].getNome() > jogadores[j+1].getNome(): 
                temp = jogadores[j]
                jogadores[j] = jogadores[j+1]
                jogadores[j+1] = temp
           
    print("LISTA ORDENADO POR NOME: ")
    listar()
    menu()

# 6 - Ordenar por Código deverá utilizar o algoritmo de Ordenação InsertionSort;
def ordenarCodigo():
    # percorre o vetor a partir da segunda posição
    for i in range(1, len(jogadores)):
        key = jogadores[i]
        j = i - 1
        while j >= 0 and jogadores[j].getCodigo() > key.getCodigo():
            jogadores[j + 1] = jogadores[j] 
            j -= 1
        jogadores[j + 1] = key
    print("LISTA ORDENADO POR CODIGO: ")
    listar()
    menu()

# 7 - Ordenar por Quantidade de gols deverá utilizar o algoritmo de Ordenação SelectionSort;
def ordenarGols():
    for i in range(len(jogadores) - 1, 0, -1):
        maior_idx = 0
        for j in range(1, i + 1):
            if jogadores[j].getQuantidadeGols() > jogadores[maior_idx].getQuantidadeGols(): 
                maior_idx = j 
        temp = jogadores[i]
        jogadores[i] = jogadores[maior_idx]
        jogadores[maior_idx] = temp
    print("LISTA ORDENADO POR GOLS: ")
    listar()
    menu()

# 8 - A Opção Salvar deverá salvar a relação de jogadores em um arquivo texto.
def salvar():
    print("CRIANDO ARQUIVO....")
    arquivoListaJogadores = open('arquivoListaJogadores.txt','w')
    print("Salvando arquivos...")
    for i in range(len(jogadores)):
        arquivoListaJogadores.write(jogadores[i].getRegistro() + " \n")
        print(".")
    arquivoListaJogadores.close()
    print("ARQUIVOS SALVOS")
    menu()


def menu():
    
    print("1 - Cadastrar")
    print("2 - Pesquisar")
    print("3 - Excluir")
    print("4 - Listar")
    print("5 - Ordenar Por Nome")
    print("6 - Ordenar Por Código")
    print("7 - Ordenar Por Gols")
    print("8 - Salvar")
    print("0 - Sair")

    opcao = int(input("INSIRA UMA DAS OPÇÕES ACIMA: "))

    if opcao == 1 : cadastrar()
    if opcao == 2 : consulta()
    if opcao == 3 : excluir()
    if opcao == 4 : listar()
    if opcao == 5 : ordenarNome()
    if opcao == 6 : ordenarCodigo()
    if opcao == 7 : ordenarGols()
    if opcao == 8 : salvar()
    if opcao == 0 : print("================SAINDO DA APLICAÇÃO===========")
    


menu()
