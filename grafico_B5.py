import matplotlib.pyplot as plt
import csv

#Olímpiadas anos em sequência, para fazer a inversão
#Idade média
#Separar as de verão, inverno
#Separar por sexo

def filtrarEntrada(a: str, b: int):
  possiveis_anos = [] #usado
  verao, inverno = [], []#usado
  anos_colecao = {} #usado

  #Ler o arquivo e separar entre a verao x inverno, além de separar a lista para ter a ordem de anos
  with open('athlete_events.csv') as arq:
    tabela = csv.reader(arq, delimiter=',')
    for linha in tabela:
      possiveis_anos.append(linha[9])
      if linha[3] != 'NA':
        if linha[10] == 'Summer':
          verao.append((linha[9], linha[3], linha[2]))
        else:
          inverno.append((linha[9], linha[3], linha[2]))
  #print(verao)
  #print(row_anos)

  #Tratar os anos para separar os anos existentes
  anos = []
  for i in possiveis_anos:
    if i not in anos:
      anos.append(i)
  anos_final = anos[1:]
  anos_final.sort()
  utilizaveis = anos_final[-b:]

  quantidade = {}
  for ano in utilizaveis:
    anos_colecao[ano] = 0 #row_anos
    quantidade[ano] = 0 #vezes_somadas de numeros somados
  #print(anos_colecao)

  def tratagem_dados(temporada, row_anos, row_quantidade, a):
    media_anos = {}
    womans, mens = [], [] #usado

    for pessoas in temporada:
      if pessoas[2] == 'F':
          womans.append((pessoas[0], float(pessoas[1])))
      else:
          mens.append((pessoas[0], float(pessoas[1])))
    #print(womans)
    #print(f"{sorted(mens)=}")

    def separar_dadosPor(genero, anos_usados, numeros_somados):
      sexo = genero.copy()
      anos = anos_usados.copy()
      total_idade = numeros_somados.copy()
      for atleta in sexo:
        if atleta[0] in anos:
          anos[atleta[0]] += float(atleta[1])
          total_idade[atleta[0]] += 1
        else:
          pass
      #print(row_anos)
      #print(quantidade)
      media_anos = anos.copy()
      for chave in sexo:
        if chave[0] in anos:
          media = anos[chave[0]] / total_idade[chave[0]]
          media_anos[chave[0]] = media
      return media_anos

    homens = separar_dadosPor(mens, row_anos, row_quantidade).items()
    mulheres = separar_dadosPor(womans, row_anos, row_quantidade).items()
    #print(homens)
    #print(mulheres)

    for olimp_m in homens:
      for olimp_w in mulheres:
        if olimp_m[0] == olimp_w[0]:
          if olimp_m[1] == 0 and olimp_w[1] == 0:
            continue
          media_anos[olimp_w[0]] = (olimp_m[1], olimp_w[1])
    #print(media_anos)
    anos, homens_mulheres, homem, mulher = [], [], [], []
    for elemente in media_anos.items():
      anos.append(int(elemente[0]))
      homens_mulheres.append(elemente[1])
    for intem in homens_mulheres:
      homem.append(intem[0])
      mulher.append(intem[1])
    return (anos, homem, mulher, a)


  #Para fazer o processo de acordo com o parâmetro recebido
  if a == 'SUMMER':
    return tratagem_dados(verao[1:], anos_colecao, quantidade, a)
  if a == 'WINTER':
    return tratagem_dados(inverno[1:], anos_colecao, quantidade, a)

def montarGrafico(x, y, w, temporada):
#
  if temporada == 'SUMMER':
    a = 'Verão'
  if temporada == 'WINTER':
    a = 'Inverno'

#
  barwidth = 0.30
  plt.figure(figsize=(18, 11))
#
  r1 = range(len(y))
  r2 = [i + barwidth for i in r1]
#
  barra1 =plt.bar(r1, y, color='#008B8B', width=barwidth, label='Homens', align='edge')
  barra2 =plt.bar(r2, w, color='#B22222', width=barwidth, label='Mulheres', align='edge')
  plt.legend(fontsize=20, loc='lower center', markerscale=3, shadow=True, facecolor='#F0F8FF')
  plt.grid(True)

  plt.xlabel('Anos por olímpiada', fontsize =20)
  plt.xticks([r + barwidth for r in range(len(y))], x, rotation=35, fontsize=15)
  plt.yticks(fontsize=15)
  plt.tick_params(axis='x', pad=5)
  plt.autoscale(axis = 'x', tight=True)
  plt.ylabel('Idades médias', fontsize=20)
  plt.title('Idades médias de homens e mulheres por olímpiada \n' 'Temporada de ' f'{a}', fontsize=20)

  plt.bar_label(barra1, fmt= '%.1f', fontsize=13)
  plt.bar_label(barra2, fmt= '%.1f', fontsize=13)
#
  plt.savefig('./Imagens_graficos/barras.png')
  plt.close

def mostrarGraficoBarra(a: str, b: int):
  tuplaDados = filtrarEntrada(a, int(b))
  montarGrafico(tuplaDados[0], tuplaDados[1], tuplaDados[2], tuplaDados[3])

