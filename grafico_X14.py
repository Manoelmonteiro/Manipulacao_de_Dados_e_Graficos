import matplotlib.pyplot as plt
import csv
import menu


# IMC = peso/altura**2

# função para apresentar os esportes para escolha do usuario
def selecionar_esporte(temporada):
    TodosEsportes = []

    with open('athlete_events.csv') as arq:
        tabela = csv.reader(arq, delimiter=',')
        for linha in tabela:
            if linha[10].upper() == temporada:
                TodosEsportes.append(linha[12])

    esportes = []
    for i in TodosEsportes:
        if i not in esportes:
            esportes.append(i)
    print(esportes)


def filtrarEntrada(esporte: str, temporada: str, quantidadeAnos: int):
    TodosOsAnos = []  # usado
    atletas_celulas = []  # usado

    #
    with open('athlete_events.csv') as arq:
        tabela = csv.reader(arq, delimiter=',')
        for linha in tabela:
            TodosOsAnos.append(linha[9])
            if linha[12].upper() == esporte:
                if linha[4] != 'NA' and linha[5] != 'NA':
                    atletas_celulas.append((linha[9], linha[5], linha[4]))
                    # atletas_celulas.append(ano, peso, altura)

    # Reponder a caso o esporte não corresponde a essa temporada
    if atletas_celulas == []:
        print('Esse esporte não possuí dados avaliavéis, tente outro.\n')
        menu.mostrarquestaoX14()
    else:
        pass

        # print(f'{atletas_celulas=}')
    # print(f'{inverno=}')

    # Separação de anos escolhidos
    possiveis_anos = []
    for i in TodosOsAnos:
        if i not in possiveis_anos:
            possiveis_anos.append(i)
    anos_final = possiveis_anos[1:]
    anos_final.sort()
    anos = anos_final[-quantidadeAnos:]

    # dic_IMC[ano] = imc, onde imc = [()]
    #
    dados_IMC = []
    for atleta in atletas_celulas:
        IMC = float(atleta[1]) / ((float(atleta[2]) / 100) ** 2)
        dados_IMC.append((atleta[0], IMC))
    # print(dados_IMC)

    colecao_anos = sorted(anos)
    dados_IMC_ano = {}
    for atleta in dados_IMC:
        if atleta[0] in colecao_anos:
            dados_IMC_ano[atleta[0]] = [*dados_IMC_ano.get(atleta[0], []), atleta[1]]

    # xlabel = anos, ylabel = imcs correspondente ao ano do xlabel
    row_xlabel = []
    row_ylabel = []
    imcs = sorted(dados_IMC_ano.items())
    for ano in imcs:
        row_xlabel.append(ano[0])
        row_ylabel.append(ano[1])

    return row_xlabel, row_ylabel, esporte, temporada


def montarGrafico(labels, data, nome_esporte, temporada):
    #
    if temporada == 'SUMMER':
        a = 'Verão'
    if temporada == 'WINTER':
        a = 'Inverno'
    #
    plt.figure(figsize=(13, 9))
    flierprops = dict(marker='D', markerfacecolor='#FFDAB9', markersize=5, linestyle='none')
    plt.style.use('fivethirtyeight')
    plt.xticks(rotation=35, fontsize=10)
    plt.yticks(fontsize=10)
    #
    plt.boxplot(data, labels=labels, flierprops=flierprops)
    plt.title("IMC por ano do " f'{nome_esporte}\n' "na temporada de "  f'{a}', fontsize=15)

    #
    plt.xlabel('Anos', fontsize=15)
    plt.ylabel('IMC (kg/m²)', fontsize=15)
    plt.savefig('./Imagens_graficos/boxplot.png')


def mostrarGraficoBP(a: str, b: str, c: int):
    tuplaDados = filtrarEntrada(a, b, c)
    montarGrafico(tuplaDados[0], tuplaDados[1], tuplaDados[2], tuplaDados[3])