import csv
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

filename = 'Results_MPC_DSR5.csv'
with open(filename) as f:
    reader = csv.reader(f, delimiter=';')
    header_row = next(reader)

    xlista = []
    PVWINDLISTA = []
    ST_SOCLISTA = []

    for row in reader:
        x = row[0]
        PVWIND = row[23].replace(',','.')
        ST_SOC = row[24].replace(',','.')
        if PVWIND and ST_SOC and x:
            xlista.append(x)
            PVWINDLISTA.append(float(PVWIND))
            ST_SOCLISTA.append(float(ST_SOC))

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.plot(xlista, PVWINDLISTA, color='#d6e9ca')
ax2.plot(xlista, ST_SOCLISTA, color='#c41212')

ax1.set_ylabel('RES generation, kW')
ax2.set_ylabel('Energy stored, kWh')
legend_elements = [Patch(facecolor='#d6e9ca', label='PV+WIND'),
Patch(facecolor='#c41212', label='ST_SOC')]
plt.title('Storage charge in relation to renewable production')
plt.xticks(xlista[0::3])
ax1.tick_params(axis='x', rotation=90)
plt.legend(handles=legend_elements,loc='upper center', ncol=2, prop={'size': 8})
ax1.fill_between(xlista, PVWINDLISTA, color='#d6e9ca')
plt.grid(axis='y')
plt.show()