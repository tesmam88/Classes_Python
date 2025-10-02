## HERANÇA E POLIMORFISMO
class Funcionario:
    def __init__(self,nome,login,senha):
        self.nome = nome
        self.login = login   
        self.senha = senha

    def logar(self):
        print(f"{self.nome} logado com sucesso")

    def set_senha(self,nova_senha):
        self.senha = nova_senha 
        return True

class Gerente(Funcionario):
    def __init__(self,nome,login,senha,setor):
        super().__init__(nome,login,senha)
        self.setor = setor

    def logar(self):  ### POLIMORFISMO
        confirm = input("Digite o tolken: ")
        if confirm:
            print(f"Gerente {self.nome} logado com sucesso no Setor: {self.setor}")


luan = Gerente("Luan Victor","lulu@yahoo.com","222555","vendas")
luan.logar()
luan.set_senha("55555")
print(luan.senha)



f1 = Funcionario("Eliandro","eli@ali.com","1234")
f2 = Funcionario("Felix","felix@gamil.com","4321")

f1.logar()

