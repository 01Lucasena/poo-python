import os
from Class_endereco import Endereco
from Class_engenheiro import Engenheiro


os.system("cls||clear")

engenheiro1 = Engenheiro("Fulano", "(xx) x xxxx xxxx", "email@email.com", "37845325425", endereco=Endereco("Rua A", "2","Casa do aralho","00000","Bruxelas"))


print(f"=== DADOS DO ENGENHEIRO ===")
print(engenheiro1.nome)
print(engenheiro1.telefone)
print(engenheiro1.email)
print(engenheiro1.endereco)