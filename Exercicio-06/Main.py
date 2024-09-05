import os
from Class_endereco import Endereco
from Class_motoboy import Motoboy

os.system("cls||clear")

motoboy = Motoboy("Lucas","lucasena020@gmail.com","123456", 2000, endereco=Endereco("Rua A","01","Salvador"))

print(motoboy.nome)