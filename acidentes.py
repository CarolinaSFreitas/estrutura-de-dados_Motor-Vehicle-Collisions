import matplotlib.pyplot as plt
import csv
acidentes = []


def carrega_dados():
    with open('Motor_Vehicle_Collisions_-_Crashes.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for linha in csv_reader:
            acidentes.append(linha)


def titulo(msg, traco="-"):
    print()
    print(msg)
    print(traco*40)


def acidentes_geral():
    titulo("Dados Gerais de Acidentes")

    num = len(acidentes)
    num_com_mortes = 0
    num_sem_mortes = 0

    for acidente in acidentes:
        if acidente["NUMBER OF PERSONS KILLED"]:
            mortos = int(acidente["NUMBER OF PERSONS KILLED"])
            if mortos > 0:
                num_com_mortes += 1
            else:
                num_sem_mortes += 1

    print(f"\nNº Total de Acidentes: {num}")
    print(f"\nNº Total de Acidentes: {num:_.0f}".replace("_", "."))
    print(
        f"- Nº de Acidentes com Mortes: {num_com_mortes:_.0f}".replace("_", "."))
    print(
        f"- Nº de Acidentes sem Mortes: {num_sem_mortes:_.0f}".replace("_", "."))


def acidentes_por_bairro():
    titulo("Acidentes Agrupados por Bairro")

    bairros = []
    numeros = []

    for acidente in acidentes:
        if acidente["BOROUGH"]:
            if acidente["BOROUGH"] in bairros:
                indice = bairros.index(acidente["BOROUGH"])
                numeros[indice] += 1
            else:
                bairros.append(acidente["BOROUGH"])
                numeros.append(1)

    print("\nBairro.........: Nº Acidentes")

    for bairro, num in zip(bairros, numeros):
        print(f"{bairro:20} {num:_.0f}".replace("_", "."))


def grafico_acidentes_por_bairro():
    titulo("Gráfico de Acidentes por Bairro")

    bairros_anos = []
    numeros = []

    for acidente in acidentes:
        bairro = acidente["BOROUGH"]
        ano = acidente["CRASH DATE"].split("/")[2]

        if not bairro or not ano:
            continue
        
        if ano < "2015":
            continue

        if bairro+"-"+ano in bairros_anos:
            indice = bairros_anos.index(bairro+"-"+ano)
            numeros[indice] += 1
        else:
            bairros_anos.append(bairro+"-"+ano)
            numeros.append(1)

    print("\nBairro.........: Nº Acidentes")

    # ordena por bairro (e ano) e numeros
    bairros_anos2, numeros2 = zip(*sorted(zip(bairros_anos, numeros)))

    bronx = []
    brooklyn = []
    manhattan = []
    queens = []

    for bairro, num in zip(bairros_anos2, numeros2):
        print(f"{bairro:20} {num:_.0f}".replace("_", "."))
        if bairro.split("-")[0] == "BRONX":
            bronx.append(num)
        elif bairro.split("-")[0] == "BROOKLYN":
            brooklyn.append(num)
        elif bairro.split("-")[0] == "MANHATTAN":
            manhattan.append(num)
        elif bairro.split("-")[0] == "QUEENS":
            queens.append(num)

    anos = list(range(2015, 2024))

    # Criar figura e eixos
    fig, ax = plt.subplots()

    # Plotar os dados
    ax.plot(anos, bronx, label='BRONX')
    ax.plot(anos, brooklyn, label='BROOKLYN')
    ax.plot(anos, manhattan, label='MANHATTAN')
    ax.plot(anos, queens, label='QUEENS')

    # Mostrar os rótulos dos eixos e a legenda do gráfico
    ax.set_xlabel('Ano')
    ax.set_ylabel('Nº de Acidentes')
    ax.legend()

    # Exibir o gráfico pronto
    plt.show()


def grafico_acidentes_por_bairro_mortes():
    pass


carrega_dados()

while True:
    titulo("Estatística de Acidentes em NYC", "=")
    print("1. Dados Gerais")
    print("2. Acidentes Agrupados por Bairro")
    print("3. Gráfico de Acidentes por Bairro e Ano")
    print("4. Gráfico de Acidentes com Mortes por Bairro")
    print("5. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        acidentes_geral()
    elif opcao == 2:
        acidentes_por_bairro()
    elif opcao == 3:
        grafico_acidentes_por_bairro()
    elif opcao == 4:
        grafico_acidentes_por_bairro_mortes()
    else:
        break
