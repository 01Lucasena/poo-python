from Class_endereco import Endereco
from Abstract_funcionario import Funcionario

class Engenheiro(Funcionario):
    
    def __init__(self, nome: str, telefone: str, email: str, crea: str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, endereco)
        
        self.crea = crea

    def calcular_salario(salario) -> float:
        salario = 5000
        return salario

    def __str__ (self) -> str:
        return f"\nCREA: {self.crea} \nSalário: {calcular_salario}"