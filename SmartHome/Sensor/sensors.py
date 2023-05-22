import sqlite3
import time 

class SensorDatabase:

    def __init__(self, database_name, scroll, light, display):
        self.database_name = database_name
        self.scroll = scroll
        self.light = light
        self.display = display

        self.connection = sqlite3.connect(self.database_name)

    def close(self):
        self.connection.close()

    def _select(self,table_name,col_name):
        cursor = self.connection.cursor()
        query=f'SELECT {col_name} FROM {table_name};' #SELECT col1, col2, col3 FROM table_name WHERE...
        cursor.execute(query)
        record=cursor.fetchone()
        cursor.close()
        return record[0]
        
    
    def _update(self,table_name,column,value): #ovaj _ prije update, ta metoda postaje privatna metoda. Ta metoda nitko iz vana ne moze zvati, ona je samo pomocna metoda. 
        cursor = self.connection.cursor()
        query=f'UPDATE {table_name} SET {column}="{value}";' #umjesto "{value}" moze biti ?
        cursor.execute(query) # ako stavimo ? moramo dodati (query,(value,))
        self.connection.commit()
        cursor.close()

    def get_temperature(self):
        return self._select(self.scroll,'temp')
        

    def get_humidity(self):
        return self._select(self.scroll,'hum')
    
    def get_pressure(self):
       return  self._select(self.scroll,'press')
    
    def get_light(self,number):
        return self._select(self.light,f'light_{number}')

    def set_display(self,text):
        self._update(self.display,'text', text)
        


    

def test(): 
    path='C:\\Algebra\\Vjezba1\\Na predavanju (10. tj.)\\Simulator_senzora\\Sensors.db'
    database = SensorDatabase(path, 'Scorll', 'Light', 'Display')
    iteration=0
    while True:
        temperature=database.get_temperature()
        light=database.get_light(1)
        print(temperature,light)
        database.set_display(f'{iteration}')
        iteration +=1
        time.sleep(2)
    

if __name__ == '__main__':
    test()

