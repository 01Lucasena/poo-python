from abc import ABC, abstractmethod
from Class_endereco import Endereco

class Funcionario(ABC):

    def __init__(self, nome: str, ) -> None:
        super().__init__()