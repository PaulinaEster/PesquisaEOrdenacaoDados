# 2.  Em um outro arquivo, crie uma lista de contatos com N objetos Pessoa.
#  1 . Em Python, crie uma classe Pessoa, com os atributos id, sobrenome, nome e idade.

# 3. Utilize o algoritmo Insertion Sort (estudado na aula anterior) para ordenar 
# a lista de contatos por id, idade, nome e sobrenome

from Pessoa import Pessoa

p1 = Pessoa(54, "silva", "carla", 12)
p2 = Pessoa(2, "lucas", "marcela", 16)
p3 = Pessoa(34, "santos", "camila", 32)
p4 = Pessoa(90, "pereira", "luciana", 56)
p5 = Pessoa(5, "ferrari", "maria", 25)
p6 = Pessoa(7, "benta", "joana", 42)


def insertionSortId(v):
 # percorre o vetor a partir da segunda posição
 for i in range(1, len(v)):
    key = v[i].getId()
    #Move os elementos de v[0..i-1],
    # que são maiores que a chave (key),
    # para uma posição à frente da atual
    j = i - 1
    while j >= 0 and v[j].getId() > key:
        v[j + 1].setId(v[j].getId())
        j -= 1
    v[j + 1].setId(key) 

def insertionSortNome(v):
 # percorre o vetor a partir da segunda posição
 for i in range(1, len(v)):
    key = v[i].getNome()
    #Move os elementos de v[0..i-1],
    # que são maiores que a chave (key),
    # para uma posição à frente da atual
    j = i - 1
    while j >= 0 and v[j].getNome() > key:
        v[j + 1].setNome(v[j].getNome())
        j -= 1
    v[j + 1].setNome(key) 

def insertionSortSobrenome(v):
 # percorre o vetor a partir da segunda posição
 for i in range(1, len(v)):
    key = v[i].getSobrenome()
    #Move os elementos de v[0..i-1],
    # que são maiores que a chave (key),
    # para uma posição à frente da atual
    j = i - 1
    while j >= 0 and v[j].getSobrenome() > key:
        v[j + 1].setSobrenome(v[j].getSobrenome())
        j -= 1
    v[j + 1].setSobrenome(key) 


def insertionSortIdade(v):
 # percorre o vetor a partir da segunda posição
 for i in range(1, len(v)):
    key = v[i].getIdade()
    #Move os elementos de v[0..i-1],
    # que são maiores que a chave (key),
    # para uma posição à frente da atual
    j = i - 1
    while j >= 0 and v[j].getIdade() > key:
        v[j + 1].setIdade(v[j].getIdade())
        j -= 1
    v[j + 1].setIdade(key) 
print("================ ARRAY SEM ORDENAÇÃO==============")
pessoas = [ p1, p2, p3, p4, p5, p6]
for i in range(len(pessoas)):
    print("ID", pessoas[i].id, "Nome: ", pessoas[i].nome, " sobrenome: ",pessoas[i].sobrenome , " idade: ", pessoas[i].idade)

print("================ SORTEIO PELO ID ==============")
insertionSortId(pessoas)
for i in range(len(pessoas)):
    print("ID", pessoas[i].id)


insertionSortNome(pessoas)
print("================ SORTEIO PELO NOME ==============")
for i in range(len(pessoas)):
    print("Nome: ", pessoas[i].nome)


print("================ SORTEIO PELO SOBRENOME ==============")
insertionSortSobrenome(pessoas)
for i in range(len(pessoas)):
    print(" sobrenome: ",pessoas[i].sobrenome)


print("================ SORTEIO PELA IDADE ==============")
insertionSortIdade(pessoas)
for i in range(len(pessoas)):
    print( " idade: ", pessoas[i].idade)
