class Persona: ## superclass herança
    def __init__(self,nome,email,senha):
        self.name = nome 
        self.mail = email
        self.password = senha

    def hello(self):
        print(f"Hellooooooooo{self.name} ")

class Student(Persona): ##Classe herdeira 
    def __init__(self,nome,email,senha,ra):
        super().__init__(nome,email,senha)
        self.ra = ra

p1 = Persona("JAVANCHO","javancho@java.com.br","1233245")
p1.hello()

s1 = Student("TESMAM","tespereyra@yahoo.com","6969966","55")
s1.hello()