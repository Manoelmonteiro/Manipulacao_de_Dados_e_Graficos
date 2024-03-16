import matplotlib.pyplot as plt
import csv
import menu


def filtrarEntrada(a: str):
    womans = []  # usado
    mens = []  # usado

    with open('athlete_events.csv') as arq:
        tabela = csv.reader(arq, delimiter=',')
        for linha in tabela:
            # Encontrar aqueles que ganharam pelo menos uma medalha
            if linha[14] != 'NA' and linha[4] != 'NA':
                # Encontrar aqueles que tem a altura registrada
                if linha[2] == 'F':
                    womans.append((linha[9], linha[4]))
                if linha[2] == 'M':
                    mens.append((linha[9], linha[4]))

    # funcao para tratagem de dados
    def tratagem_dados(lista: list, a: str):
        anos = {}
        colecao_anos = {}
        # Separar as alturas e fazer a media dos numeros
        for pessoa in lista:
            if pessoa[0] in anos:
                anos[int(pessoa[0])] += float(pessoa[1])
                anos[pessoa[0] + 'quantidade'] += 1
            else:
                anos[int(pessoa[0])] = float(pessoa[1])
                anos[pessoa[0] + 'quantidade'] = 1
        for pessoa in lista:
            media = anos[int(pessoa[0])] / anos[pessoa[0] + 'quantidade']
            colecao_anos[pessoa[0]] = media
        # Ajustar o eixo x e o eixo y
        sortedanos = sorted(colecao_anos.items(), key=lambda x: x[0])
        x, y = [], []
        for item in sortedanos:
            x.append(item[0])
            y.append(item[1])
        return x, y, a

    # especificcar quais dados queremos
    if a == 'F':
        print("Seu grafico foi gerado com sucesso.")
        return tratagem_dados(womans, 'Mulheres')

    if a == 'M':
        print("Seu grafico foi gerado com sucesso.")
        return tratagem_dados(mens, 'Homens')


def montarGrafico(x, y, a: str):
    plt.figure(figsize=(9, 6))
    plt.title('Evolução da altura de ' f'{a}', fontsize=10)
    plt.xlabel('Anos', fontsize=10)
    plt.ylabel('Altura', fontsize=10)
    plt.plot(x, y, marker='.', linewidth=5, color='#ff6600')
    plt.grid(True)
    plt.xticks(rotation=30, fontsize=8)
    plt.yticks(fontsize=8)
    plt.autoscale(axis='x', tight=True)
    plt.savefig('./Imagens_graficos/linha.png')
    plt.close()
    menu.mostrarquestaoL10()


def mostrarGraficoLinha(a: str):
    tuplaDados = filtrarEntrada(a)
    montarGrafico(tuplaDados[0], tuplaDados[1], tuplaDados[2])
