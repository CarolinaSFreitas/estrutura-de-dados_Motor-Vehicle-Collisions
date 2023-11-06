import matplotlib.pyplot as plt
import csv

colisoes = []

def carrega_dados():
    with open('Motor_Vehicle_Collisions_-_Crashes.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for linha in csv_reader:
            colisoes.append(linha)    # lista de dicionários


def titulo(texto, traco="-"):
    print()
    print(texto)
    print(traco*40)


def total_acidentes():
    titulo("Número Total de Acidentes")

    total = len(colisoes)
    print(f"O número total de acidentes é: {total}")
    return total


def acidentes_c_mortes():
    titulo("Número de Acidentes com Mortes")

    acidentes_mortes = 0

    for acidente in colisoes:
        num_mortes = acidente.get('NUMBER OF PERSONS KILLED', '0')  # Obtém o número de mortes, se não existir, considera como '0'
        if int(num_mortes) > 0:
            acidentes_mortes += 1

    print(f"O número de acidentes com mortes é: {acidentes_mortes}")
    return acidentes_mortes

def acidentes_s_mortes():
    pass


def acidentes_bairros():
    pass


def grafico_acidentes_ano():
    pass


def grafico_acidentes_c_mortes():
    pass


# ---------------------------------------------------------------------  Programa Principal
carrega_dados()

while True:
    titulo("Colisões de Veículos em Nova Iorque", "=")
    print("1. Nº Total de Acidentes")
    print("2. Nº de Acidentes com Mortes")
    print("3. Nº de Acidentes sem Mortes")
    print("4. Acidentes por Bairro")
    print("5. Gráfico Acidentes por Ano")
    print("6. Gráfico de Acidentes com Mortes")
    print("7. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
       total_acidentes()
    elif opcao == 2:
        acidentes_c_mortes()
    elif opcao == 3:
        acidentes_s_mortes()
    elif opcao == 4:
        acidentes_bairros()
    elif opcao == 5:
        grafico_acidentes_ano()
    elif opcao == 6:
        grafico_acidentes_c_mortes()
    else:
        break
