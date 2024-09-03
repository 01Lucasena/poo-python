
class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str)  -> None:
        
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

        def __str__(self) -> str:
            return f"\nEndereço do funcionário: \nLogradouro:{self.logradouro} \nNúmero: {self.numero} 
            \nComplemento: {self.complemento} \nCep: {self.cep} \nCidade: {self.cidade}"

