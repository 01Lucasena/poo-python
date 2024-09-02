from abc import ABC, abstractmethod

class Funcionario(ABC):

    #construtor
    def __init__(self, nome: str, telefone: str, email: str, endereco: str) -> None:

        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

        @abstractmethod
        def calcular_salario(self) -> float:
            pass

        