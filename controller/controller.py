def create(conta):

    if type(conta).__name__ == "PessoaFisica":
        contaDB = open("contasPF.txt","a")
        aux = f"{conta.titular};{conta.numero};{conta.saldo};{conta.cpf}\n"
        contaDB.write(aux)
        contaDB.close()

    elif type(conta).__name__ == "PessoaJuridica":
        contaDB = open("contasPJ.txt","a")
        aux = f"{conta.titular};{conta.numero};{conta.saldo};{conta.cnpj}\n"
        contaDB.write(aux)
        contaDB.close()

    else:
        print("Erro! Tipo de conta incorreta!")

def listarContas(tipoConta):
    if tipoConta == "PF":
        contaDB = open("contasPF.txt","r")
    elif tipoConta == "PJ":
        contaDB = open("contasPJ.txt","r")
    else:
        print("Opcao inválida")
    for conta in contaDB:
        print(conta)