from empresa.models.endereco import Endereco
from empresa.models.enum.sexo import Sexo
from empresa.models.enum.setor import Setor
from abc import ABC, abstractmethod

class Salario_negativo_error(Exception):
    pass

class Funcionario(ABC):
    def __init__(self, nome: str,cpf: str,rg: str,endereco: Endereco,setor: Setor,sexo: Sexo, salario: float,data_de_nascimento: str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.endereco = endereco
        self.setor = setor
        self.sexo = sexo
        self.verificar_salario(salario)
        self.data_de_nascimento = data_de_nascimento

    #metódos para cálculo e verificação de salário
    @abstractmethod
    def calcular_salario(self) -> float:
        pass

    def verificar_salario(self,valor):
        try:
            self.mensagem(valor)
        except Salario_negativo_error as error:
            return f"\nErro: {error}"

    def mensagem(self,valor):
        if valor < 0:
            raise Salario_negativo_error("Não é possivel adicionar um valor negativo")


    def __str__(self) -> str:
        return (
            f"\nNome: {self.nome}"
            f"\nCPF: {self.cpf}"
            f"\nRG: {self.rg}"
            f"\nEndereço: {self.endereco}"
            f"\nSetor: {self.setor.value}"
            f"\nSexo: {self.sexo.value}"
            f"\nSalário: {self.verificar_salario(self)}"
            f"\nData de Nascimento: {self.data_de_nascimento}"
        )