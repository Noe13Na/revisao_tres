def imprimir_nomes():
    nomes = ["João", "Maria", "Fulano", "Ciclano"]
    for i, nome in enumerate(nomes, start=1):
        print(f"{i}-{nome}")

# Chamando a função para imprimir os nomes
imprimir_nomes()