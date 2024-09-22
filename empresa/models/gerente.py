from empresa.models.cargo_de_confiaca import Cargo_de_confianca
from empresa.models.endereco import Endereco
from empresa.models.enum.bonificacao import Bonificacao
from empresa.models.enum.setor import Setor
from empresa.models.enum.sexo import Sexo

class Gerente(Cargo_de_confianca):
    def __init__(self, bonificacao: Bonificacao, nome: str, cpf: str, rg: str, endereco: Endereco, setor: Setor, sexo: Sexo, salario: float, data_de_nascimento: str) -> None:
        super().__init__(bonificacao, nome, cpf, rg, endereco, setor, sexo, salario, data_de_nascimento)

        def __str__ (self) -> str:
            return self.Funcionario
   