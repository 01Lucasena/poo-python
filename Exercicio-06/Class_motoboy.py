from .Class_endereco import Endereco
from Abstract_funcionario import Funcionario

class Motoboy(Funcionario):

    def __init__(self, nome: str, email: str, salario: float, cnh: str, endereco: Endereco) -> None:
        super().__init__(nome, email, salario, endereco)

        self.cnh = cnh

        