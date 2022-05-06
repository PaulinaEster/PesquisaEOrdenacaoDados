
# Altere o programa anterior, transferindo os métodos 
#  que representam as operações (adição, subtração, multiplicação
#   e divisão) para uma Classe chamada Calculadora.Java. Crie
#    uma outra classe chamada Principal.Java que inicialize o
#     programa
#  e utilize a classe Calculadora.Java para 
# realizar as operações.


class Calculadora:
    def __init__(self, a, b):
        self.a = a;
        self.b = b
    
    def soma(self):
        return self.a + self.b

    def subtracao(self):
        return self.a - self.b
    
    def multiplicacao(self):
        return self.a * self.b

    def divisao(self):
        return self.a/self.b