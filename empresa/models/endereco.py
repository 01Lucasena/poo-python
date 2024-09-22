from empresa.models.enum.unidade_federativa import Unidade_federativa

class Endereco:
    def __init__(self, logradouro:str, numero: str, cep: str, cidade: str, unidade_federativa: Unidade_federativa) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.cep = cep
        self.cidade = cidade
        self.unidade_federativa = unidade_federativa

    def __str__(self) -> str:
        return (
                f"\nLogradouro: {self.logradouro}"
                f"\nNúmero: {self.numero}"
                f"\nLogradouro: {self.cep}"
                f"\nLogradouro: {self.cidade}"
                f"\nLogradouro: {self.unidade_federativa}"
            )