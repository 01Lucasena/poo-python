class Endereco:
    def __init__(self, logradouro: str, numero: str, cidade: str) -> str:
        self.logradouro = logradouro
        self.numero = numero
        self.cidade = cidade

    def __str__(self) -> str:
        return (f"\nLogradouro: {self.logradouro}" 
        f"\nNúmero: {self.numero}" 
        f"\nCidade: {self.cidade}")
    