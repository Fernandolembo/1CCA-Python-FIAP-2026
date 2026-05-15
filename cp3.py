temperaturas = [[28, 31, 34, 33],
                [25, 27, 29, 28],
                [32, 35, 36, 34],
                [24, 26, 25, 27]]

maior_criticos = -1
sala_maior_risco = 0
n_sala = 1

for sala in temperaturas:
    soma_temperaturas = 0
    qtd_leituras = 0
    registros_criticos = 0

    for temp in sala:
        soma_temperaturas = soma_temperaturas + temp
        qtd_leituras = qtd_leituras + 1

        if temp >=33:
            registros_criticos = registros_criticos +1

    media = soma_temperaturas / qtd_leituras

    print(f"Sala {n_sala}")
    print(f"Média : {media}")
    print(f"Registros críticos: {registros_criticos}")
    print()

    if registros_criticos > maior_criticos:
        maior_criticos = registros_criticos
        sala_maior_risco = n_sala

    n_sala = n_sala + 1

print(f"Sala com maior risco: Sala {sala_maior_risco}")



