from empresa.models.endereco import Endereco
from empresa.models.enum.setor import Setor
from empresa.models.enum.sexo import Sexo
from empresa.models.funcionario import Funcionario

class motorista(Funcionario):
    def __init__(self,cnh: str, nome: str, cpf: str, rg: str, endereco: Endereco, setor: Setor, sexo: Sexo, salario: float, data_de_nascimento: str) -> None:
        super().__init__(nome, cpf, rg, endereco, setor, sexo, salario, data_de_nascimento)

        self.cnh = cnh
    
    def __str__(self) -> str:
        return (
                f"\nCNH: {self.cnh}"
                )
