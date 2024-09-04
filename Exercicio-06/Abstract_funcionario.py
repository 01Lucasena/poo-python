from abc import ABC, abstractmethod
from Class_endereco import Endereco

class Funcionario(ABC):

    def __init__(self, nome: str, email: str, salario: float, endereco: Endereco ) -> None:
        super().__init__()

        self.nome = nome
        self.email = email
        self.salario = salario
        self.endereco = endereco

        @abstractmethod
        def calcular_salario(self) -> float:
            pass