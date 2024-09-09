from abc import ABC, abstractmethod
from Class_endereco import Endereco

class SalarioNegativoError(Exception):
    pass

class Funcionario(ABC):

    def __init__(self, nome: str, email: str, salario: float, endereco: Endereco ) -> None:
        self.nome = nome
        self.email = email
        self.salario = salario
        self.endereco = endereco
        self.verificar_salario(salario)

    @abstractmethod
    def salario_final(self) -> float:
        pass

    def verificar_salario(self,valor):
        try:
            self.mensagem(valor)
        except SalarioNegativoError as error:
            return f"Erro: {error}"

    def mensagem(self, valor):
        if valor > 0:
            raise SalarioNegativoError("Não é possível adicionar um valor negativo")
    
    def __str__(self) -> str:
        return (f"\nNome: {self.nome}" 
        f"\nE-mail: {self.email}" 
        f"\nSalário: {self.verificar_salario(salario)}" 
        f"\nEndereço: {self.endereco}")