from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia                                    
        self.conta = conta
        self.saldo = saldo 
                                    
       
    
    def detalhes(self):
       print(f'Agencia: {self.agencia}', end='')
       print(f'Conta: {self.conta}', end='')
       print(f'Saldo: {self.saldo}')
           
    def depositar(self, valor):
      if not isinstance(valor,(int, float)):
            raise ValueError('Valor do deposito precia ser numerico')
      self.saldo += valor
      self.detalhes()
    
    @abstractmethod
    def sacar(self, valor):
        pass    

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
           print('Saldo Insuficiente') 
           return
        self.saldo -= valor
        self.detalhes() 
class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self.limite = limite
    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
           print('Saldo Insuficiente') 
           return
        self.saldo -= valor
        self.detalhes() 