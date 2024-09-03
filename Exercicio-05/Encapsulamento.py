import os
os.system ("cls||clear")

class SaldoInsuficienteError(Exception):
    pass

class ValorNegativoError(Exception):
    pass

class Conta:
    
    def __init__(self, numero_conta: int, agencia: int ) -> None:
        self.numero_conta = numero_conta
        self.agencia = agencia
        self._saldo = 0 #atributo protegido

    @property
    def saldo(self):
        return self._saldo
    
    def sacar(self, valor):
        try:
            self._verificar_sacar(valor)
        except SaldoInsuficienteError as error:
            return f"Erro: (error)"

        self._saldo -= valor
        return self._saldo
    
    def _verificar_sacar(self,valor): #metodo privado
        if valor > self._saldo:
            raise SaldoInsuficienteError("Saldo Insuficiente.") #lançando um erro
        
    def _verificar_depositar(self,valor): #metodo privado
        if valor < 0:
            raise ValorNegativoError ("Não é possível depositar um valor negativo .") #lançando um erro
   
    def depositar(self, valor):
        try:
            self._verificar_depositar(valor)
        except ValorNegativoError as error:
            return f"Erro: (error)"
        
        self._saldo += valor
        return self._saldo

class ContaCorrente(Conta):
    pass

class ContaPoupanca(Conta):
    pass

conta_corrente = ContaCorrente(200,2)
conta_poupanca = ContaPoupanca(111,4)

print(conta_corrente.saldo)
print(conta_corrente.depositar(200))
print(conta_corrente.sacar(20))
print(conta_corrente.saldo)