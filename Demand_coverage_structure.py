import csv
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

filename = 'Results_MPC_DSR5.csv'
with open(filename) as f:
    reader = csv.reader(f, delimiter=';')
    header_row = next(reader)

    xlista = []
    DIESEL1LISTA = []
    DIESEL2LISTA = []
    WINDLISTA = []
    PVLISTA = []
    GRIDPURCHASELISTA = []
    LOADLISTA = []

    for row in reader:
        x = row[0]
        DIESEL1 = row[5].replace(',','.')
        DIESEL2 = row[6].replace(',','.')
        WIND = row[3].replace(',','.')
        PV = row[1].replace(',','.')
        GRIDPURCHASE = row[9].replace(',','.')
        LOAD = row[20].replace(',','.')
        if DIESEL1 and DIESEL2 and WIND and PV and GRIDPURCHASE and LOAD and x:
            xlista.append(x)
            DIESEL1LISTA.append(float(DIESEL1))
            DIESEL2LISTA.append(float(DIESEL2))
            WINDLISTA.append(float(WIND))
            PVLISTA.append(float(PV))
            GRIDPURCHASELISTA.append(float(GRIDPURCHASE))
            LOADLISTA.append(float(LOAD))


DIESEL2LISTA2=[]
WINDLISTA2 = []
PVLISTA2 = []
GRIDPURCHASELISTA2 = []

for i in range(len(DIESEL1LISTA)):
    DIESEL2ZMIENNA=DIESEL1LISTA[i]+DIESEL2LISTA[i]
    DIESEL2LISTA2.append(DIESEL2ZMIENNA)
    WINDLISTAZMIENNA=DIESEL2LISTA2[i]+WINDLISTA[i]
    WINDLISTA2.append(WINDLISTAZMIENNA)
    PVLISTA2ZMIENNA=WINDLISTA2[i]+PVLISTA[i]
    PVLISTA2.append(PVLISTA2ZMIENNA)
    GRIDPURCHASEZMIENNA=PVLISTA2[i]+GRIDPURCHASELISTA[i]
    GRIDPURCHASELISTA2.append(GRIDPURCHASEZMIENNA)





legend_elements = [Patch(facecolor='#c7c4c4', label='DIESEL1'),
Patch(facecolor='#a58f4c', label='DIESEL2'),
Patch(facecolor='#8cb9e2', label='WIND'),
Patch(facecolor='#ffd659', label='PV'),
Patch(facecolor='#9ac57e', label='GRIDPURCHASE'),
Line2D([0], [0], color='black', lw=2, label='Load')]




plt.plot(xlista, DIESEL1LISTA, '#c7c4c4', alpha=0)
plt.plot(xlista, DIESEL2LISTA2, '#a58f4c', alpha=0)
plt.plot(xlista, WINDLISTA2, '#8cb9e2', alpha=0)
plt.plot(xlista, PVLISTA2, '#ffd659', alpha=0)
plt.plot(xlista, GRIDPURCHASELISTA2, '#9ac57e', alpha=0)
plt.plot(xlista, LOADLISTA, 'black')
plt.ylabel('kW')
plt.title('Demand coverage structure')
plt.xticks(xlista[0::3])
plt.xticks(rotation=90)
plt.ylim([0,600])
plt.legend(handles=legend_elements, loc='upper center', ncol=6, prop={'size': 8})
plt.fill_between(xlista, GRIDPURCHASELISTA2, color='#9ac57e')
plt.fill_between(xlista, PVLISTA2, color='#ffd659')
plt.fill_between(xlista, WINDLISTA2, color='#8cb9e2')
plt.fill_between(xlista, DIESEL2LISTA2, color='#a58f4c')
plt.fill_between(xlista, DIESEL1LISTA, color='#c7c4c4')
plt.grid(axis='y')
plt.ylim(ymin=0)
plt.show()