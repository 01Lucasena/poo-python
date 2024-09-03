class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str)  -> None:
        
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

        def __str__(self) -> str:
            return f"Logradouro: {self.logradouro} \nNúmero: {self.numero} \nComplemento: {self.complemento} 
            \nCEP: {self.cep} \n Cidade: {self.cidade}"