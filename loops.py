questão 2
def imprimir_contagem():
    for i in range(21):
        print(i)

# Chamando a função para imprimir a contagem
imprimir_contagem()

questão 3
def substituir_alimentos(array_inicial):
    # Pede ao usuário para digitar 3 nomes de alimentos
    alimentos_digitados = []
    for i in range(3):
        alimento = input(f"Digite o {i+1}º alimento: ")
        alimentos_digitados.append(alimento)

    # Substitui os alimentos no array inicial
    for i in range(3):
        array_inicial[i] = alimentos_digitados[i]

    # Imprime os alimentos um abaixo do outro
    for i, alimento in enumerate(array_inicial, start=1):
        print(f"{i} - {alimento}")

# Array inicial
array_inicial = ["Macarrão", "Pepino", "Batata"]

# Chama a função com os alimentos digitados pelo usuário
substituir_alimentos(array_inicial)
