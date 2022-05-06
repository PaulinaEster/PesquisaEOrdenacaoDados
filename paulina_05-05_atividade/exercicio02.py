# Utilizando a linguagem Java, crie um programa que implemente as 
# operações de uma calculadora simples (adição, subtração, multiplicação 
# e divisão). Para cada operação, crie um método, que receberá dois 
# valores como parâmetro e retornará o resultado do processamento. 
# Não é necessário ler os valores do teclado,
#  você pode deixar os valores dos parâmetros fixos no código.

def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if(num1 != 0 and num2 != 0):
        return num1/num2


print("soma: ", soma(1, 2))

print("divisao: ", divisao(1, 2))
print("subtracao: ", subtracao(1, 2))
print("multiplicacao: ", multiplicacao(1, 2))

