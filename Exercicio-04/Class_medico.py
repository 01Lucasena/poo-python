from Class_endereco import Endereco
from Abstract_funcionario import Funcionario

class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, crm: str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, endereco)

        self.crm = crm

        def calcular_salario(self) -> float:
            return 7500

        def __str__ (self) -> str:
            return f"\nCRM: {self.crm} \nSalário: {calcular_salario()}"