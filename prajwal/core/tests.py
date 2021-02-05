import matplotlib.pyplot as plt
from pvCell import PVCell


with open('pvCellTestData.txt','r') as f:
    f.readline()
    line = f.readline()
    data = list(map(float,line.split(' ')))
    cell = PVCell(data[1],data[2],data[3],data[4])

temp = []
cellTemp,efficiecy,output = [],[],[]
for i in range(20):
    temp.append(5*i)
    cellTemp.append(cell.getCellTemp(5*i,1000))
    efficiecy.append(cell.getEfficiency(5*i,1000))
    output.append(cell.getElectricPower(5*i,1000,.25))

plt.plot(temp,cellTemp)
plt.ylabel('cell temprature')
plt.axis([0,200,0,200])
plt.show()

plt.plot(temp,efficiecy)
plt.ylabel('electrical efficiency')
plt.axis([0,100,0,1])
plt.show()

plt.plot(temp,output)
plt.ylabel('electrical energy (watts/m^2)')
plt.show()