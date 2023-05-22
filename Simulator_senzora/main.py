from GUI.gui import GUI 
   #GUI folder, pa gui je modul, pa GUI je klasa
from Database.sensor_database import SensorDatabase


class State:  #sacuvamo neko stanje koje je nama bitno, pocetno stanje kad kreiramo taj objekt
   
    def __init__(self,database):
        self.database=database
        self.temperature=22
        self.humidity=40
        self.pressure=1013

        self.switches=[False]*4
        self.display=''

    def set_temperature(self,value): #kad pozovem ovu funciju,zelim da s enesto spremi u bazu pod.
        self.temperature=value 
        self.database.update_temperature(value) #ako zelimo upisati u bazu, samo vidimo kako pozivamo (update_temperature)

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
    database = SensorDatabase('Sensors.db', 'Scorll', 'Light', 'Display') #kreiraj objekt sensordatabase
    database.create_tables() # pa probamo napraviti tablicu
    database.reset_to_defaults() #da aplikacija krene ispocetka kad je pokrenemo
    state=State(database) #ovaj objekt nam cuva stanje, za tvoje stanje bitna je baza podataka
    #objekt je state, on moze napraviti neku akciju, a to je set temperature jer je to definirano u klasi State
    #state zna da postoji database i moze update temperaturu 

    gui=GUI(state) #stvaramo objekt gui, dodajemo callback tako sto dodajemo klasu State, jer je to komunikacija izmedju GUI i main. py, oni komunicijrau pomocu poziva metoda
    #main stvara gui koji zna da postoji state, ali ne moze direktno komunicirti s bazom, moze samo raditi akcije koje definiramo u stateu

    gui.mainloop()

if __name__ == '__main__':
    main()