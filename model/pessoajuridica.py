from model.conta import Conta

class PessoaJuridica(Conta):
    def __init__(self,titular, numero, saldo, cnpj):
        super().__init__(titular, numero, saldo)
        self.__cnpj = cnpj
    
    @property
    def cnpj(self):
        return self.__cnpj
    
    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj
        
    def __str__(self):
        return (super().__str__() + " CNPJ: " + str(self.__cnpj))