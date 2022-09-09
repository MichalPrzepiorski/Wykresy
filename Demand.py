import csv
import matplotlib.pyplot as plt

filename = 'Results_MPC_DSR5.csv'
with open(filename) as f:
    reader = csv.reader(f, delimiter=';')
    header_row = next(reader)

    xlista = []
    ylista = []
    
    for row in reader:
        y = row[20].replace(',','.')
        x = row[0]
        if y and x:
            ylista.append(float(y))
            xlista.append(x)




plt.plot(xlista, ylista, 'grey')
plt.ylabel('kW')
plt.title('Demand')
plt.xticks(xlista[0::3])
plt.xticks(rotation=90)
plt.ylim([0,600])
plt.legend(["Load"], loc='upper center', prop={'size': 8})
plt.grid(axis='y')
plt.ylim(ymin=0)
plt.show()
