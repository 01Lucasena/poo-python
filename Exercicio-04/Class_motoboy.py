from Class_endereco import Endereco
from Abstract_funcionario import Funcionario

class Motoboy(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, cnh: str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, endereco)

        self.cnh = cnh

    def calcular_salario(self) -> float:
        return 2000

    def __str__ (self) -> str:
        return f"\nCNH: {self.cnh} \nSalário: {calcular_salario()}"