import json
import urllib.request
from prajwal.core.solarPanel import SolarPanel

class Handler:
    def __init__(self):
        self.panel = 'panel'
        self.radiation = 1000
        self.panelCount = 1
        self.temp = 25
        self.lat = 20.8
        self.lon = 80.9

    def setLocation(self,lat,lon):
        self.lat = float(lat)
        self.lon = float(lon)

    def setRadiation(self,radiation):
        self.radiation = float(radiation)

    def setPanel(self,ratedPower,ratedEfficiency,nominalCellTemp,panelArea,cellCount,panelCount):
        self.panelCount = int(panelCount)
        self.panel = SolarPanel(float(ratedPower),float(ratedEfficiency),float(nominalCellTemp),float(panelArea),int(cellCount))

    def loadApiKey(self):
        try:
            with open('apiKey.txt','r') as f:
                key = f.readline()
        except:
            key = '746f6fd0c9a7640e6f07eca2eff86c71'
        return key

    def fetchTemp(self):
        url = 'https://api.openweathermap.org/data/2.5/onecall?lat='+str(self.lat)+'&lon='+str(self.lon)+'&exclude={part}&appid='+self.loadApiKey()
        try:
            with urllib.request.urlopen(url) as f:
                data = json.load(f)
                temp = float(data['current']['temp'])
        except:
            temp = 298
        self.temp = float(temp-273)

    def getElectricPower(self):
        return self.panel.getElectricPower(self.temp,self.radiation)*self.panelCount

    def getEfficiency(self):
        return self.panel.getEfficiency(self.temp,self.radiation)