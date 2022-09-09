import csv
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

filename = 'Results_MPC_DSR5.csv'
with open(filename) as f:
    reader = csv.reader(f, delimiter=';')
    header_row = next(reader)

    xlista = []
    y1lista = []
    y2lista = []
    
    for row in reader:
        x = row[0]
        y1 = row[21].replace(',','.')
        y2 = row[7].replace(',','.')
        if y1 and x and y2:
            xlista.append(x)
            y1lista.append(float(y1))
            y2lista.append(float(y2))


legend_elements = [Line2D([0], [0], color='black', lw=2, label='Load'),
Patch(facecolor='#8497b0', label='Total Production')]

plt.plot(xlista, y1lista, 'black')
plt.plot(xlista, y2lista, '#8497b0', alpha=0.2)
plt.ylabel('kW')
plt.title('Aggregated demand coverage')
plt.xticks(xlista[0::3])
plt.xticks(rotation=90)
plt.ylim([0,600])
plt.legend(handles=legend_elements, loc='upper center', prop={'size': 8})
plt.fill_between(xlista, y2lista, color='#8497b0')
plt.grid(axis='y')
plt.show()
