from Class_endereco import Endereco
from Class_engenheiro import Engenheiro
from Class_medico import Medico
from Class_motoboy import Motoboy

engenheiro1 = Engenheiro("Fulano", "(xx) x xxxx xxxx", "email@email.com", "37845325425", Endereco("Rua A", "2","Casa do aralho","00000","Bruxelas"))


print(f"=== DADOS DO ENGENHEIRO ===")
print(engenheiro1.nome)
print(engenheiro1.telefone)
print(engenheiro1.email)
print(engenheiro1.crea)
print(engenheiro1.endereco)
