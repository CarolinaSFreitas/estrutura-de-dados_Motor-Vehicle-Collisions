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
    print("1. Dados Gerais sobre as Colisões")
    print("2. Acidentes Agrupados por Bairro")
    print("3. Gráfico de Acidentes por Bairro e Ano")
    print("4. Gráfico de Acidentes com Mortes por Bairro")
    print("5. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
       total_acidentes()
    elif opcao == 2:
        acidentes_bairros() 
    elif opcao == 3:
        grafico_acidentes_ano()
    elif opcao == 4:
        grafico_acidentes_c_mortes()
    else:
        break