def create(conta):
    contaDB = open("contas.txt","a")
    
    if type(conta).__name__ == "PessoaFisica":
        aux = f"{conta.titular};{conta.numero};{conta.saldo};{conta.cpf}\n"
    
    elif type(conta).__name__ == "PessoaJuridica":
        aux = f"{conta.titular};{conta.numero};{conta.saldo};{conta.cnpj}\n"
    else:
        print("Erro! Tipo de conta incorreta!")
    contaDB.write(aux)
    contaDB.close()

def listarContas():
    contaDB = open("contas.txt","r")
    for conta in contaDB:
        print(conta)