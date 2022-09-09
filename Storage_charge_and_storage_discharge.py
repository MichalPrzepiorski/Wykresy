import csv
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

filename = 'Results_MPC_DSR5.csv'
with open(filename) as f:
    reader = csv.reader(f, delimiter=';')
    header_row = next(reader)

    xlista = []
    StoragechargedLISTA = []
    StorageDischargedLISTA = []

    for row in reader:
        x = row[0]
        Storagecharged = row[8].replace(',','.')
        StorageDischarged = row[9].replace(',','.')
        if Storagecharged and StorageDischarged and x:
            xlista.append(x)
            StoragechargedLISTA.append(float(Storagecharged))
            StorageDischargedLISTA.append(float(StorageDischarged))




legend_elements = [Patch(facecolor='#2e75b6', label='Storagecharged'),
Patch(facecolor='#c00000', label='StorageDischarged')]
plt.plot(xlista, StoragechargedLISTA, '#2e75b6', alpha=0)
plt.plot(xlista, StorageDischargedLISTA, '#c00000', alpha=0)
plt.ylabel('kW')
plt.title('Storage charge and discharge cycles')
plt.xticks(xlista[0::3])
plt.xticks(rotation=90)
plt.ylim([-300,300])
plt.legend(handles=legend_elements,loc='upper center', ncol=6, prop={'size': 8})
plt.fill_between(xlista, StoragechargedLISTA, color='#2e75b6')
plt.fill_between(xlista, StorageDischargedLISTA, color='#c00000')
plt.grid(axis='y')
plt.show()