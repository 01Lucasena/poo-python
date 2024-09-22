from empresa.models.endereco import Endereco
from empresa.models.enum.bonificacao import Bonificacao
from empresa.models.enum.setor import Setor
from empresa.models.enum.sexo import Sexo
from empresa.models.funcionario import Funcionario
from abc import ABC

class Cargo_de_confianca(Funcionario,ABC):
        def __init__(self,bonificacao: Bonificacao, nome: str, cpf: str, rg: str, endereco: Endereco, setor: Setor, sexo: Sexo, salario: float, data_de_nascimento: str) -> None:
                super().__init__(nome, cpf, rg, endereco, setor, sexo, salario, data_de_nascimento)

                self.bonificacao = bonificacao

        