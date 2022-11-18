from model.conta import Conta

class PessoaFisica(Conta):
    def __init__(self,titular, numero, saldo, cpf):
        super().__init__(titular, numero, saldo)
        self.__cpf = cpf
    
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
        
    def __str__(self):
        return (super().__str__() + " CPF: " + str(self.__cpf))