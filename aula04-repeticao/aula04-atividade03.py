qyd_music = int(input("Digie a quantidade de musicas que você tem na playlist (DB): "))

for i in range(qyd_music):
    print(f"Musica {i}")

# For aninhado

for i in range(0,4):
    for j in range(0,3,2):
        print(f"i:{i}, j:{j}")