import csv
import menu


def executarT1():
    EquipesCidades = []  # usado

    with open('athlete_events.csv') as arq:
        tabela = csv.reader(arq, delimiter=',')
        next(tabela)
        for linha in tabela:
            # Encontrar aqueles que ganharam pelo menos uma medalha
            if linha[6] != 'NA':
                if linha[11] != 'NA':
                    EquipesCidades.append((linha[6], linha[11].upper()))

    def tratagem_dados(lista: list):
        cidades = {}
        # Separar as alturas e fazer a media dos numeros
        for pessoa in lista:
            if pessoa[1] in cidades:
                cidades[(pessoa[1])] += (pessoa[0])
            else:
                cidades[(pessoa[1])] = (pessoa[0])
        return cidades

    def ListaCidades(x: dict):  # imprime lista das cidades que sediaram as olimpiadas
        chaves = []
        for k in x.keys():
            chaves.append(k)
        print(chaves)

        def controlarentrada():  # controla a entrada do usuario
            escolha_cidade = input('De qual cidade da lista acima você deseja saber? \n').upper()
            menu.FecharPrograma(escolha_cidade)
            menu.RetornaAoMenu(escolha_cidade)
            if escolha_cidade not in chaves:
                print('Digite um país da lista:')
                ListaCidades(x)
            if escolha_cidade in chaves:
                limpaChave(x, escolha_cidade)

        controlarentrada()

    def limpaChave(x, escolha_cidade):  # elimina as equipes duplicadas da cidade
        limpa = list(set(x[escolha_cidade]))
        print('A quantidade de países que participaram das olímpiadas na cidade de', escolha_cidade, 'é de', len(limpa),
              'equipes.')

    ListaCidades(tratagem_dados(EquipesCidades))
