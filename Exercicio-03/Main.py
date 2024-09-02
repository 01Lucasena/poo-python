from Class_gerente import Gerente
from Class_motoboy import Motoboy

gerente1 = Gerente("Fulano D. Tal", 20, 5000)
print(f"=== DADOS DO GERENTE ===")
print(f"\nNome: {gerente1.nome}")
print(f"Idade: {gerente1.idade}")
print(f"Salário: {gerente1.calcular_salario()}")

motoboy1 = Motoboy("Ciclano D. Tal", 21, 2000, "11111-000")
print(f"\n=== DADOS DO MOTOBOY ===")
print(f"\nNome: {motoboy1.nome}")
print(f"Idade: {motoboy1.idade}")
print(f"CNH: {motoboy1.cnh}")
print(f"Salário: {motoboy1.calcular_salario()}")