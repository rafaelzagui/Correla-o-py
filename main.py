import matplotlib.pyplot as plt  # biblioteca para visualização de dados
import numpy as np  # biblioteca com funces matematicas
import pandas as pd  # biblioteca para manipulação de dados
from pandas import read_csv
from pandas import set_option
import csv  # classe para manipulação de dados em arquivos.csv ou .txt

padrao = []
dados4 = []


def dadosUm():
    print("***********************************************")
    print("EFETUANDO A LEITURA DOS DADOS DO ARQUIVO PADRAO")

    path = "arquivoPadrao.txt"
    with open(path, 'r', newline='') as archive:
        dados = csv.reader(archive)
        dadosLista = list(dados)
        for i in range(0, len(dadosLista)):
            dadosFloat = float(dadosLista[i][0])
            padrao.append(dadosFloat)

    # PLOTAR DADOS
    plt.plot(padrao, 'b')
    plt.title("SINAL DO ARQUIVO PADRÃO")
    plt.xlabel("AMOSTRA [s]")
    plt.ylabel("AMPLITUDE")
    plt.show()


def dadosQuatro():
    print("***********************************************")
    print("EFETUANDO A LEITURA DOS DADOS DO ARQUIVO PADRAO")
    path = 'VIBRACAOMOTORSTREAM002CC.txt'
    with open(path, 'r', newline='') as archive:
        dados = csv.reader(archive)
        dadosLista = list(dados)
        for i in range(0, len(dadosLista)):
            x = float(dadosLista[i][0])
            dados4.append(x)

    plt.plot(dados4, 'b')
    plt.title("SINAL DO ARQUIVO 4")
    plt.xlabel("AMOSTRAS [S]")
    plt.ylabel("AMPLITUDE")
    plt.show()


dadosQuatro()
dadosUm()

# DEFINIR DataFrame COM OS VALORES LIDOS PARA APLICAR CORRELACAO
auxDF = []
dataFrame = []
# z VARIAVEL AUXILIAR PARA MONTAGEM DO DATAFRAME
auxDF += [(float(float(padrao[i])), float(dados4[i])) for i in range(0, len(padrao))]
# MONTAGEM
DataFrame = pd.DataFrame(auxDF, columns=['PADRAO', 'DADOS4'])
# CALCULAR A CORRELAÇÃO
correlacao = DataFrame.corr(method='pearson')
print("\nCORRELAÇÃO TEMPORAL: ")
print(correlacao)
print("\nDADOS ESTATISTICOS BÁSICOS - TEMPORAL: ")
print("NUMERO DE AMOSTRAS/CAMPOS: ", DataFrame.shape)
print(DataFrame.describe())
