#  Para cada jogador serão mantidos os seguintes dados:
#         a. Código
#         b. Nome
#         c. Sobrenome
#         d. Idade
#         e. Quantidade de Partidas
#         f. Quantidade de Gols


class Jogador:
    def __init__(self, codigo, nome, sobrenome, idade, quantidadePartidas, quantidadeGols):
        self.codigo = codigo
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.quantidadePartidas = quantidadePartidas
        self.quantidadeGols = quantidadeGols

    def getCodigo(self):
        return self.codigo
    
    def getNome(self):
        return self.nome
    
    def getSobrenome(self):
        return self.sobrenome

    def getIdade(self):
        return self.idade
    
    def getQuantidadePartidas(self):
        return self.quantidadePartidas
    
    def getQuantidadeGols(self):
        return self.quantidadeGols
    
    def getRegistro(self):
        return str(self.codigo) + " - " + self.nome + " " + self.sobrenome + " - " + str(self.idade) + " - " + str(self.quantidadePartidas) + " - " + str(self.quantidadeGols) + " "

if __name__ == '__main__':
    '''
    Exemplo de como criar um objeto pessoa: 
    '''
    p = Jogador(1,'Silva','Maria',34, 12, 7)
    print(p.getRegistro())