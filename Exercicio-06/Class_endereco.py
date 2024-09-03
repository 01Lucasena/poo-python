class Endereco:
    
    def __init__(self, logradouro: str, numero: str, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.cidade = cidade

        def __str__(self) -> str:
            return f"Logradouro: {self.logradouro} \nNúmero: {self.numero} \nCidade: {self.cidade}"