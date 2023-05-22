from GUI.gui import GUI 
   #GUI folder, pa gui je modul, pa GUI je klasa
from Database.sensor_database import SensorDatabase


class State: 
   
    def __init__(self,database):
        self.database=database
        self.temperature=22
        self.humidity=40
        self.pressure=1013

        self.switches=[False]*4
        self.display=''

    def set_temperature(self,value): 
        self.temperature=value 
        self.database.update_temperature(value) 

    def set_pressure(self,value):
        self.pressure=value
        self.database.update_pressure(value)
    
    def set_humidity(self,value):
        self.humidity=value
        self.database.update_humidity(value)

    def set_light(self,number):
        self.switches[number]= not self.switches[number]
        self.database.update_light(number + 1,self.switches[number])
   
    def read_display(self):
        return self.database.read_display()
       


def main():
    database = SensorDatabase('Sensors.db', 'Scorll', 'Light', 'Display') 
    database.create_tables() 
    database.reset_to_defaults() 
    state=State(database) 

    gui=GUI(state)
    gui.mainloop()

if __name__ == '__main__':
    main()
