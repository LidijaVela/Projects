from Sensor.sensors import SensorDatabase
import time
from GUI.gui import GUI


class State:
    def __init__(self):
        self.temperature=22
        self.humidity=40
        self.pressure=1013


    def wanted_temperature(self,value): 
        self.temperature=value 
        
    
    def wanted_humidity(self,value):
        self.humidity=value
        


def main():
    path='C:\\Algebra\\Vjezba1\\Na predavanju (10. tj.)\\Simulator_senzora\\Sensors.db'
    sensors = SensorDatabase(path, 'Scorll', 'Light', 'Display')
    sensors_temp=SensorDatabase.get_temperature
    sensors_hum=SensorDatabase.get_humidity

    state=State()

    Gui=GUI(state)

    Gui.mainloop()

if __name__ == '__main__':
    main()
