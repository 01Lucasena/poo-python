from Abstract_funcionario import Funcionario

class Motoboy(Funcionario):
    def __init__(self, nome: str, idade: int, salario: float, cnh: str) -> None:
        super().__init__(nome, idade, salario)
        self.cnh = cnh
    
    def calcular_salario(self) -> float:
        #Acréscimo de 20%
        BONIFICACAO = 1.1
        salario_final = self.salario * BONIFICACAO
        return salario_final