from Abstract_funcionario import Funcionario
from Class_endereco import Endereco

class Motoboy(Funcionario):

    def __init__(self, nome: str, email: str, cnh: str, endereco : Endereco) -> None:
        super().__init__(nome, email, endereco)

        self.cnh = cnh

        def __str__ (self) -> str:
            return f"CNH: {self.cnh} \nSalário: {self.salario}"
        