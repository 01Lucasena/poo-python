import os
from enum import Enum

os.system("cls||clear")

class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"
    NAO_BINARO = "Não binário"
    NAO_ESPECIFICADO = "Não especificado"

class Setor(Enum):
    FINANCEIRO = "Financeiro"
    RECURSOS_HUMANOS = "Recursos Humanos"
    VENDAS = "Vendas"
    MARKETING = "Marketing"

class Funcionario:

    def __init__(self,id: int,nome: str,idade: int,salario: float,setor: Setor,sexo: Sexo) -> None:
        self.id = id
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.setor = setor
        self.sexo = sexo

        def __str__(self) -> str:
            return (f"\nID: {self.id}"
                    f"\nNome: {self.nome}"
                    f"\nIdade: {self.idade}"
                    f"\nSalário: {self.salario}"
                    f"\nSexo: {self.sexo.value}"
                    f"\nSetor: {self.setor.value}")

funcionario_1 = Funcionario(123,"Luscas",24,7000.00,Setor.FINANCEIRO,Sexo.MASCULINO)

print(funcionario_1)