from controller.controller import create, listarContas
from model.conta import Conta
from model.pessoafisica import PessoaFisica
from model.pessoajuridica import PessoaJuridica

def menu():
    while True:
        aux = input("Cadastrar: C\n Listar: L\n Sair: X\n:> ")
        
        if aux.upper() == "C":
            camada2 = input("Qual seria o tipo de cadastro: \nPJ ou PF\n:> ").upper()

            if camada2 == "PJ":
                pj = PessoaJuridica("Empresa", 111, 1000, 222222)
                create(pj)

            elif camada2 == "PF":
                pf = PessoaFisica("Jean", 111, 1000, 2000)
                create(pf)

            else:
                print("Opção inválida")
            
        elif aux.upper() == "L":
            camada2 = input("Qual seria o tipo de conta: \nPJ ou PF\n:> ").upper()
            if camada2 == "PJ":
                listarContas("PJ")

            elif camada2 == "PF":
                listarContas("PF")
        else:
            break
        