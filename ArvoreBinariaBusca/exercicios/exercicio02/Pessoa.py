#  1 . Em Python, crie uma classe Pessoa, com os atributos id, sobrenome, nome e idade.

# 2.  Em um outro arquivo, crie uma lista de contatos com N objetos Pessoa.

# 3. Utilize o algoritmo Insertion Sort (estudado na aula anterior) para ordenar 
# a lista de contatos por id, idade, nome e sobrenome

class Pessoa:
    def __init__(self, id, sobrenome, nome, idade):
        self.id = id
        self.sobrenome = sobrenome
        self.nome = nome
        self.idade = idade
    
    def getId(self):
        return self.id
    
    def getNome(self):
        return self.nome
    

    def getSobrenome(self):
        return self.sobrenome
    
    def getIdade(self):
        return self.idade

    def setId(self, id):
        self.id = id

    def setNome(self, nome):
        self.nome = nome

    def setSobrenome(self, sobrenome):
        self.sobrenome = sobrenome

    def setIdade(self, idade):
        self.idade = idade
    def getRegistro(self):
        '''
        :return: (str) Registro completo, com id, nome, sobrenome e idade
        '''
        return str(self.id) + " - " + self.nome + " " + self.sobrenome + " - " + str(self.idade)