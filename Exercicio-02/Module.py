import os


os.system("cls||clear") #Limpar terminal

class Livro:

    #construtor
    def __init__(self, titulo: str, autor: str, numeroDePaginas: int, preco: float) -> None:
        
        #atributos
        self.titulo = titulo
        self.autor = autor
        self.numeroDePaginas = numeroDePaginas
        self.preco = preco
    
    def __str__(self) -> str:
        return f"Titulo: {self.titulo} \nAutor: {self.autor} \nNúmero de páginas: {self.numeroDePaginas} \nPreço: {self.preco}"
    

