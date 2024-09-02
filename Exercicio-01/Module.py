import os

os.system("cls||clear") #Limpar terminal

class Endereco:

    #construtor
    def __init__(self, logradouro: str, numero: str) -> None:

        #atributos
        self.logradouro = logradouro
        self.numero = numero

    #(toString())
    def __str__(self) -> str:
        return f"Logradouro: {self.logradouro} \nNúmero: {self.numero}"

class Aluno:


    #construtor
    def __init__(self, nome: str, idade: int, endereco: Endereco) -> None:    
        
        #atributos
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    #(toString())
    def __str__(self) -> str:
        return f"Nome: {self.nome} \nIdade: {self.idade} \nEndereço: {self.endereco}"
    
