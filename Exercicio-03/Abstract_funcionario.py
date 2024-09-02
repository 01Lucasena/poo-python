from abc import ABC, abstractmethod

class Funcionario(ABC):

    #construtor
    def __init__(self, nome: str, idade: int, salario:float ) -> None:

        self.nome = nome
        self.idade = idade
        self.salario = salario

        @abstractmethod
        def calcular_salario(self) -> float:
            pass
 

    

