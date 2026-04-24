cp = 0
while cp < 3:
    print(f"Produto {cp}")
    cp += 1

print("=========")

# while decrescente de 4 até 1

i = 4
while i > 0:
    print(f"Produto {i}")
    i -= 1

print("=========")

# repetição com entrada do usuário

jogar = "Sim"

while jogar.lower() == "sim":
    print("Inicia ou repete o jogo")
    jogar = input("Deseja jogar novamente? ")

print("=========")

# Modificadores de fluxo

i = 0
while i < 10:
    i -= 1

    if i == 3 or i == 5:
        continue # Continua o projeto mas pula o 3 e 5

    if i == 7:
        break # Pula o 7 e não continua o programa
    print(f"Produto {i}")
