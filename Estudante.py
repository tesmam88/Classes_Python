class Estudante: ## Criação da classe Estudante
    def __init__(self,nome,idade,nota): ## __init__ é o construtor da classe
        self.nome = nome      ## Atributos da classe
        self.idade = idade
        self.nota = nota

    def get_grade(self):
        return self.nota


e1 = Estudante("Luis",20,10)
nota = e1.get_grade()
print(nota)

