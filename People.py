class People:
    nome = None
    idade = None

    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def getAnoNascimento(self,AnoAtual):
        return AnoAtual - self.idade


pessoa = People("Pedro",21)
print(pessoa.getAnoNascimento(2013))      