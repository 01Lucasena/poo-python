from empresa.models.endereco import Endereco
from empresa.models.enum.setor import Setor
from empresa.models.enum.sexo import Sexo
from empresa.models.funcionario import Funcionario


class Advogado (Funcionario):
    def __init__(self,oab: str, nome: str, cpf: str, rg: str, endereco: Endereco, setor: Setor, sexo: Sexo, salario: float, data_de_nascimento: str) -> None:
        super().__init__(nome, cpf, rg, endereco, setor, sexo, salario, data_de_nascimento)
        self.oab = oab

    def salario_final(self)-> float:
        return self.salario
    
    def __str__(self) -> str:
        return (
                f"{super().__str__()}"
                f"CNH: {self.cnh}"
        )