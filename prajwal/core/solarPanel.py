from prajwal.core.pvCell import PVCell

class SolarPanel:
    """Solar Panel Class"""
    def __init__(self,ratedPower,ratedEfficiency,area,nominalCellTemp,cellCount,tempCofficient = -0.005):
        """ratedPower - watts
            ratedEfficiency - %
            area - m^2
            cellCount - costant
            nominalCellTemp - *C """
        self.cellCount = cellCount
        self.area = area
        self.cell = PVCell(ratedPower/cellCount,ratedEfficiency/100,nominalCellTemp,tempCofficient)

    def getElectricPower(self,ambidentTemp,radiation):
        return self.cell.getElectricPower(ambidentTemp,radiation,self.area/self.cellCount)*self.cellCount

    def getEfficiency(self,ambidentTemp,radiation):
        return self.cell.getEfficiency(ambidentTemp,radiation)