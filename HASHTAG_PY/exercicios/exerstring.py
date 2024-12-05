#Inserir o CPF apenas números e, caso tenha algo diferente de números ou for menor de 11 números, avisa um erro

cpf = input("Digite seu CPF (Apenas números): ")
if (not cpf.isnumeric() or len(cpf) != 11):
    print("Digite seu CPF corretamente e apenas números.")
else:
    print("Tudo certo com seu CPF.")

print(cpf.isnumeric()) #Retorna um boolean se é numérico ou não

