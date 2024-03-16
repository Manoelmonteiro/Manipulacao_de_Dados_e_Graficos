import grafico_L10
import grafico_B5
import grafico_X14
import questao_T1
import grafico_extra
import os


# Menu de Opções para acesso do usuário
def inicializarmenu_Opcoes():
    # Opções de escolha com base nos gráficos e questões sorteadas para a dupla
    questoes = input('''
  > Qual resposta você gostaria de ver? \n
  O grafico L10: Evolução da altura média dos atletas que ganharam medalhas em alguma das Olimpíadas. Digite: A. \n
  O grafico B5: Idade média dos atletas em cada uma das últimas escolhidas, por tipo de olímpiada e separados por sexo. Digite: B. \n
  O grafico X14: IMC dos atletas do esporte escolhido nas últimas olímpiadas selecionadas e do tipo de olimpiada selecionado. Digite: C. \n
  A resposta textual T1: Quantos países participaram da Olimpíada da cidade escolhida. Digite: D. \n
  O gráfico L15(questão extra): Evolução da média do IMC dos atletas no período entre dois anos selecionados do tipo de olímpiada escolhido, separados por sexo (duas linhas
  no mesmo gráfico). Digite: E. \n
  O usuário poderá digitar 'menu' para retornar a seleção\n
  Ou 'sair' para fechar o programa\n
  ''').upper()
    while True:
        FecharPrograma(questoes)
        if questoes in 'ABCDE':
            if questoes == 'A':
                mostrarquestaoL10()
            if questoes == 'B':
                mostrarquestaoB5()
            if questoes == 'C':
                mostrarquestaoX14()
            if questoes == 'D':
                mostrarquestaoT1()
            if questoes == 'E':
                mostrarquestaoExtra()
        else:
            print('Digite apenas A, B, C, D ou E para escolher a questão')
            return inicializarmenu_Opcoes()

def mostrarquestaoL10():
    escolha_genero = input(
        "Escolha o gênero que deve ser apresentado no gráfico, M para masculino e F para feminino. \n").upper()
    RetornaAoMenu(escolha_genero)
    FecharPrograma(escolha_genero)
    if escolha_genero == 'MF':
        print('Erro! Digite apenas M ou F')
        mostrarquestaoL10()
    if escolha_genero in 'MF':
        grafico_L10.mostrarGraficoLinha(escolha_genero)
    else:
        print('Erro! Digite apenas M ou F')
        return mostrarquestaoL10()


def mostrarquestaoB5():
    escolha_quantidade = input("Quantas olímpiadas você quer analisar? Digite um número inteiro. \n").upper()
    RetornaAoMenu(escolha_quantidade)
    FecharPrograma(escolha_quantidade)

    escolha_Tipo = input(
        "Qual das temporadas você escolhe? Digite summer para verão, ou winter para inverno. \n").upper()
    while True:
        RetornaAoMenu(escolha_Tipo)
        FecharPrograma(escolha_Tipo)
        try:
            if escolha_Tipo in "SUMMERWINTER":
                if escolha_Tipo == 'SUMMER':
                    return grafico_B5.mostrarGraficoBarra('SUMMER', int(escolha_quantidade))
                    break
                if escolha_Tipo == "WINTER":
                    return grafico_B5.mostrarGraficoBarra('WINTER', int(escolha_quantidade))
                    break
            else:
                print('Erro! Digite apenas M ou F')
                return mostrarquestaoB5()
        except:
            print('Erro! Leia as questões com atenção.')
            mostrarquestaoB5()


def mostrarquestaoX14():
    escolha_Tipo = input(
        "Qual das temporadas você escolhe? Digite summer para verão, ou winter para inverno. \n").upper()
    RetornaAoMenu(escolha_Tipo)
    FecharPrograma(escolha_Tipo)
    grafico_X14.selecionar_esporte(escolha_Tipo)
    escolha_esporte = input("Qual esporte você deseja analisar das opções acima? \n").upper()
    RetornaAoMenu(escolha_esporte)
    FecharPrograma(escolha_esporte)
    escolha_quantidade = input("Quantas olímpiadas você quer analisar? Digite um número inteiro. \n").upper()
    RetornaAoMenu(escolha_quantidade)
    FecharPrograma(escolha_quantidade)

    try:
        grafico_X14.mostrarGraficoBP(escolha_esporte, escolha_Tipo, int(escolha_quantidade))
    except:
        print('\nOcorreu um erro com os valores digitados. Leia as questões com atenção e tente novamente.\n')
        mostrarquestaoX14()


def mostrarquestaoT1():
    '''
    escolha_cidade = input("De qual cidade você deseja saber? \n").upper()
    return grafico_T1.apresentarResultado(escolha_cidade)
    '''
    questao_T1.executarT1()


def mostrarquestaoExtra():
    print(grafico_extra.selecionar_ano())
    ano1 = input('Escolha o primeiro ano para ser o começo do intervalo. \n').upper()
    RetornaAoMenu(ano1)
    FecharPrograma(ano1)
    ano2 = input('Escolha o segundo ano para ser o final do intervalo. \n').upper()
    RetornaAoMenu(ano2)
    FecharPrograma(ano2)
    tipoOlimpiada = input(
        "Qual das temporadas você escolhe? Digite summer para verão, ou winter para inverno. \n").upper()
    RetornaAoMenu(tipoOlimpiada)
    FecharPrograma(tipoOlimpiada)

    try:
        grafico_extra.mostrarGraficoLinhaDupla(int(ano1), int(ano2), tipoOlimpiada)
    except:
        print(
            '--Houve um problema com os valores digitados. Por favor, leia as questões com atenção e tente novamente--')
        mostrarquestaoExtra()


def FecharPrograma(x):
    if x == 'SAIR':
        print('---Programa encerrado---')
        exit()


def RetornaAoMenu(x):
    if x == 'MENU':
        inicializarmenu_Opcoes()