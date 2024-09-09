import os
from Class_endereco import Endereco
from Class_motoboy import Motoboy
from Class_gerente import Gerente

os.system("cls||clear")

motoboy_1 = Motoboy("Lucas","lucasena020@gmail.com","123456", 2000, endereco=Endereco("Rua A","01","Salvador"))
print(motoboy_1)

gerente_1 = Gerente("Lucas","lucasena020@gmail.com","123456", 2000, endereco=Endereco("Rua A","01","Salvador"))
print(gerente_1)