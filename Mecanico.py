class Mecanico:
    def __init__(self,name,matricula,nivel):
        self.name = name
        self.matricula = matricula
        self.nivel = nivel
        self.salario = 0

    def passar_orcamento(self):     
        print("Seu carro ficou tanto...")

    def realizar_diagnostico(self):
        print(f"{self.name} diagnosticando o veiculo...")

    def get_salario(self):
        return self.salario

    def set_salario(self,valor):
        self.salario = valor     

    def calcular_comissao(self,servicos):
        comissao = servicos* 0.15
        self.salario += comissao
        return True

m1 = Mecanico("GARRIDO","123465","n2")
m1.passar_orcamento()
m1.realizar_diagnostico()

sal = m1.get_salario()  ## acessa o get_salario
print(sal)
m1.set_salario(5000)    ## altera o salario com o set_salario
m1.calcular_comissao(9000)   ## fez o calculo da comissão  
if m1.calcular_comissao(9000):  ## outra forma de calcular a comissão
    print("Salario Atualizado com sucesso")
    print(f"Salario Atual do {m1.name} é {m1.get_salario()}")

sal2 = m1.get_salario()
print(sal2)

m2 = Mecanico("JOAO","56789","n2")
m2.set_salario(9000)
x = m2.get_salario()
print(f"Salario do {m2.name} é {m2.salario}")