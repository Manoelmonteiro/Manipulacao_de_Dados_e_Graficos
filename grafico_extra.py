import csv
import matplotlib.pyplot as plt
import menu


def selecionar_ano():
    TodosOsAnos = []

    with open('athlete_events.csv') as arq:
        tabela = csv.reader(arq, delimiter=',')
        for linha in tabela:
            if linha[9] not in TodosOsAnos:
                TodosOsAnos.append(linha[9])
    anos = sorted(TodosOsAnos[1:])
    return anos


# ...L15. Evolução da média do IMC dos atletas no período que vai desde o <ano 1> até o
# <ano 2> em olimpíadas de <Tipo de Olimpíada>, separados por sexo (duas linhas
# no mesmo gráfico).

def filtrarEntrada(ano1: int, ano2: int, tipoOlimpiada: str):
    homens = []  # usado
    mulheres = []
    with open('athlete_events.csv') as arq:
        tabela = csv.reader(arq, delimiter=',')
        next(tabela)
        for linha in tabela:
            # Filrando os dados e adicionando nas respectivas listas
            if (linha[10]).upper() == tipoOlimpiada:
                if linha[4] != 'NA' and linha[5] != 'NA':
                    if linha[2] == 'M':
                        homens.append((linha[9], float(linha[5]), float(linha[4])))
                    if linha[2] == 'F':
                        mulheres.append((linha[9], float(linha[5]), float(linha[4])))
                    # lista.append(ano, peso, altura)
        # save(f'{homens=}', 'homens')
        # save(f'{mulheres=}', 'mulheres')

    # Resposta a listas vazias
    if homens == [] and mulheres:
        print('Esses anos não possuem dados avaliavéis, tente outros')
        menu.mostrarquestaoExtra()
    else:
        pass

    # Seleção de anos
    dict_anos = {}
    dict_quantidade = {}
    lista_intermedio = selecionar_ano()
    primeiro_numero, segundo_numero = lista_intermedio.index(str(ano1)), lista_intermedio.index(str(ano2))
    anos = lista_intermedio[primeiro_numero: segundo_numero + 1]
    # print(f'{lista_intermedio=}')
    # print(anos)
    for ano in anos:
        dict_anos[ano] = 0
        dict_quantidade[ano] = 0
        # print(f'{dict_anos=}')

    # print(f'{dict_quantidade=}')

    #
    def apresentarIMC(lista: list):
        dados_IMC = []
        for atleta in lista:
            IMC = float(atleta[1]) / ((float(atleta[2]) / 100) ** 2)
            dados_IMC.append((atleta[0], IMC))
        return dados_IMC

    Imc_homens = apresentarIMC(homens)
    Imc_mulheres = apresentarIMC(mulheres)

    # save(f'{Imc_homens=}', 'homens')
    # save(f'{Imc_mulheres=}', 'mulheres')

    def tratagemDADOS(lista_genero: list, anos: dict, contagem: dict):
        anos_dicionario = anos.copy()
        genero = lista_genero.copy()
        soma_individuos = contagem.copy()
        for individuo in genero:
            if individuo[0] in anos_dicionario:
                anos_dicionario[individuo[0]] += float(individuo[1])
                soma_individuos[individuo[0]] += 1
            else:
                pass

        media_anos = anos_dicionario.copy()
        for dados in genero:
            if dados[0] in anos:
                media = anos_dicionario[dados[0]] / soma_individuos[dados[0]]
                media_anos[dados[0]] = media
        return media_anos.items()

    mens = tratagemDADOS(Imc_homens, dict_anos, dict_quantidade)
    womans = tratagemDADOS(Imc_mulheres, dict_anos, dict_quantidade)
    # save(f'{mens=}', 'mens')
    # save(f'{womans=}', 'womans')

    media_anos = {}  # para juntar homens e mulheres no mesmo ano
    for olimp_m in mens:
        for olimp_w in womans:
            if olimp_m[0] == olimp_w[0]:
                if olimp_m[1] == 0 and olimp_w[1] == 0:
                    continue
                media_anos[olimp_w[0]] = (olimp_m[1], olimp_w[1])

    # Retornar um xlabel = anos e um ylabel = (Imc médio de homens, Imc médio de mulheres).
    anos, homens_mulheres, homem, mulher = [], [], [], []
    for elemente in media_anos.items():
        anos.append(int(elemente[0]))
        homens_mulheres.append(elemente[1])
    for intem in homens_mulheres:
        homem.append(intem[0])
        mulher.append(intem[1])
    # save(f'{anos=}')
    # save(f'{homem=}', 'homem_final')
    # save(f'{mulher=}', 'mulher_final')
    # print(anos, homem, mulher, tipoOlimpiada)
    return anos, homem, mulher, tipoOlimpiada


def montarGrafico(xlabel, ylabel1, ylabel2, a: str):
    # xlabel=anos, ylabel1=dados de Imc dos homens, ylabel2=dados de Imc das mulheres
    #
    if a == 'SUMMER':
        temporada = 'Verão'
    if a == 'WINTER':
        temporada = 'Inverno'
    #
    plt.figure(figsize=(10, 7))
    plt.title('Evolução da media de IMC dos atletas \n' 'na temporada de %s' % (temporada), fontsize=15)
    plt.xlabel('Anos', fontsize=15)
    plt.ylabel('Médias de IMC (kg/m²)', fontsize=15)
    plt.plot(xlabel, ylabel1, marker='D', linewidth=3, color='#3CB371', label='Homens')
    plt.plot(xlabel, ylabel2, marker='D', linewidth=3, color='#BA55D3', label='Mulheres')
    plt.grid(True)
    plt.legend()
    plt.xticks(rotation=30, fontsize=10)
    plt.yticks(fontsize=10)
    plt.savefig('./Imagens_graficos/linhaDupla.png')
    plt.close()


def mostrarGraficoLinhaDupla(ano1: int, ano2: int, TipoOlimpiada: str):
    tuplaDados = filtrarEntrada(ano1, ano2, TipoOlimpiada)
    montarGrafico(tuplaDados[0], tuplaDados[1], tuplaDados[2], tuplaDados[3])