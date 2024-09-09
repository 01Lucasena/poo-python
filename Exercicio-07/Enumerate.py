import os
from enum import Enum

os.system("cls||clear")

class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"
    NAO_BINARIO = "Não Binário"

class Pessoa:
    def __init__(self, nome: str, idade: int, sexo: Sexo) -> None:
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def __str__(self) -> str:
        return (f"\nNome: {self.nome}"
                f"\nIdade: {self.idade}"
                f"\nSexo: {self.sexo.value}")

#Instanciando classe pessoa
pessoa_1 = Pessoa("Luscas", 25, Sexo.MASCULINO)

print(pessoa_1)