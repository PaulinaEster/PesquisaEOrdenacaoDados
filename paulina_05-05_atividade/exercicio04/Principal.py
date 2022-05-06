# Altere o programa anterior para que o usuário possa escolher 
# uma das operações e em seguida forneça os valores dos 
# parâmetros para o processamento. Não é necessário utilizar 
# Interface Gráfica.

from Calculadora import Calculadora

operacao = int(input("Escolha Uma Operação \n"
                     "1 - Soma \n"
                     "2 - Subtração \n"
                     "3 - Multiplicação \n"
                     "4 - Divisão\n"))

x = int(input("Digite um valor inteiro para x\n"))
y = int(input("Digite um valor inteiro para y\n"))

c = Calculadora(x, y)

if(operacao == 1):
    print("Soma: ", c.soma())
if(operacao == 2 ):
    print("Subtracao: ", c.subtracao())
if(operacao == 3):
    print("Multiplicacao: ", c.multiplicacao())
if(operacao == 4):
    print("Divisao: ", c.divisao())

