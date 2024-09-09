from abc import ABC, abstractmethod
from Class_endereco import Endereco

class Funcionario(ABC):

    #construtor
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco) -> None:

        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    @abstractmethod
    def calcular_salario(self) -> float:
        pass

        