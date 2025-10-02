class Pessoa:
    def __init__(self,nome,cpf,email,cidade,estado):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.cidade = cidade
        self.estado = estado

        

    def imprimir_tudo(self):
        print(f'Nome:{self.nome} , CPF:{self.cpf}, Email: {self.email}, Cidade: {self.cidade}, Estado: {self.estado}')

pessoa = Pessoa("Aureo",2345354,"aureo@gmail.com","campo grande","MS")

print(pessoa.nome,pessoa.cpf,pessoa.email,pessoa.cidade,pessoa.estado)          
        