from Abstract_funcionario import Funcionario

class Gerente(Funcionario):
    def calcular_salario(self) -> float:
        #Acréscimo de 20%
        BONIFICACAO = 1.2
        salario_final = self.salario * BONIFICACAO
        return salario_final


