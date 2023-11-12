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
    titulo("Dados Gerais sobre Acidentes")
    
    total = len(colisoes)
    print(f"O número total de acidentes é: {total}")

    mortes = sum(int(linha['NUMBER OF PERSONS KILLED']) if linha['NUMBER OF PERSONS KILLED'] else 0 for linha in colisoes)
    print(f"Número de acidentes com mortes: {mortes}")

    sem_mortes = total - mortes
    print(f"Número de acidentes sem mortes: {sem_mortes}")

    return total, mortes, sem_mortes


def acidentes_bairros():
    titulo("Número de Acidentes por Bairro")

    bairros = {}
    for linha in colisoes:
        bairro = linha['BOROUGH']
        if bairro in bairros:
            bairros[bairro] += 1
        else:
            bairros[bairro] = 1

    for bairro, num_acidentes in bairros.items():
        if bairro:
            print(f"{bairro}: {num_acidentes} acidentes")


def grafico_acidentes_ano():
    titulo("Gráfico de Acidentes por Bairro e Ano")

    dados_grafico = {}              #cria dicio
    for linha in colisoes:
        bairro = linha['BOROUGH']
        ano = linha['CRASH DATE'][-4:]

        if bairro not in dados_grafico:
            dados_grafico[bairro] = {}

        if ano in dados_grafico[bairro]:
            dados_grafico[bairro][ano] += 1
        else:
            dados_grafico[bairro][ano] = 1

    for bairro, dados_ano in dados_grafico.items():
        anos, num_acidentes = zip(*dados_ano.items())
        plt.pie(num_acidentes, labels=[f'{ano} - {bairro}' for ano in anos], autopct='%1.1f%%', startangle=140)
        plt.title(f'Acidentes por Bairro em {bairro}')
        plt.show()

def grafico_acidentes_c_mortes():
    titulo("Gráfico de Acidentes com Mortes por Bairro")

    dados_grafico = {}          #cria dicio
    for linha in colisoes:
        bairro = linha['BOROUGH']
        mortes = int(linha['NUMBER OF PERSONS KILLED'])

        if mortes > 0:
            if bairro in dados_grafico:
                dados_grafico[bairro] += 1
            else:
                dados_grafico[bairro] = 1

    bairros, num_mortes = zip(*dados_grafico.items())
    plt.pie(num_mortes, labels=bairros, autopct='%1.1f%%', startangle=140)
    plt.title('Acidentes com Mortes por Bairro')
    plt.show()

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
