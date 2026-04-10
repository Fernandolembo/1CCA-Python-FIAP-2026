# OPERADORES DE ARIBUIÇÃO
num = 15
print(num)

num = num + 2
print(num)

num += 2
print(num)

# OPERADORES RELACIONAIS
print()
print(6==2)
print(6!=2)

idade = 20
print(idade==20)

maior_idade = idade >= 18
print(maior_idade)

# OPERADOR LÓGICO
# LOGICA E (and)

verifica_email = True
verifica_senha = False

login = verifica_email and verifica_senha
print(login)

if login:
    print("Entrar no programa")

print()

# NOTAS....
nota_final = 5

if nota_final < 4:
    print("Reprovado")
elif nota_final < 6:
    print("Recuperação")
else:
    print("Aprovado")

print("FIM")