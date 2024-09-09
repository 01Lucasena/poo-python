from Abstract_funcionario import Funcionario

class Gerente(Funcionario):
    def salario_final(self) -> float:
        salarioFinal = self.verificar_salario(self.salario)
        return salarioFinal