import sqlite3

class SensorDatabase:

    def __init__(self, database_name, scroll, light, display):
        self.database_name = database_name
        self.scroll = scroll
        self.light = light
        self.display = display

        self.connection = sqlite3.connect(self.database_name)

    def close(self):
        self.connection.close()

    def create_tables(self):

        scroll_table = f"""CREATE TABLE IF NOT EXISTS {self.scroll} (
                            id INTEGER PRIMARY KEY,
                            temp REAL NOT NULL,
                            hum REAL NOT NULL,
                            press REAL NOT NULL
                       );"""
        
        light_table = f"""CREATE TABLE IF NOT EXISTS {self.light} (
                            id INTEGER PRIMARY KEY,
                            light_1 BOOLEAN NOT NULL,
                            light_2 BOOLEAN NOT NULL,
                            light_3 BOOLEAN NOT NULL,
                            light_4 BOOLEAN NOT NULL
                       );"""
        
        display_table = f"""CREATE TABLE IF NOT EXISTS {self.display} (
                            id INTEGER PRIMARY KEY,
                            text TEXT NOT NULL
                       );"""
             
        cursor = self.connection.cursor()
        for query in [scroll_table, light_table, display_table]:
            cursor.execute(query)
        self.connection.commit()
        cursor.close()

    def reset_to_defaults(self):

        cursor = self.connection.cursor()
        for table_name in [self.scroll, self.light, self.display]:
            delete_query = f'DELETE FROM {table_name};'
            cursor.execute(delete_query)

        insert_scroll = f'INSERT INTO {self.scroll} (temp, hum, press) VALUES (22, 40, 1013);'
        insert_light = f'INSERT INTO {self.light} (light_1, light_2, light_3, light_4) VALUES (FALSE, FALSE, FALSE, FALSE);'
        insert_text = f'INSERT INTO {self.display} (text) VALUES ("");'

        for query in [insert_scroll, insert_light, insert_text]:
            cursor.execute(query)

        self.connection.commit()
        cursor.close()


    def _update(self,table_name,column,value): #ovaj _ prije update, ta metoda postaje privatna metoda. Ta metoda nitko iz vana ne moze zvati, ona je samo pomocna metoda. 
        cursor = self.connection.cursor()
        query=f'UPDATE {table_name} SET {column}={value};' 
        cursor.execute(query)
        self.connection.commit()
        cursor.close()

    def update_temperature(self,value):
        self._update(self.scroll,'temp',value)

    def update_humidity(self,value):
        self._update(self.scroll,'hum',value)
    
    def update_pressure(self,value):
        self._update(self.scroll,'press',value)
    
    def update_light(self,number,value):
        self._update(self.light,f'light_{number}',value)

    def read_display(self):
        cursor = self.connection.cursor()
        query=f'SELECT * FROM {self.display};' #SELECT col1, col2, col3 FROM table_name WHERE...
        cursor.execute(query)
        record=cursor.fetchone()
        cursor.close()
        return record[1]


    

def test():
    database = SensorDatabase('Sensors.db', 'Scorll', 'Light', 'Display')
    database.create_tables()
    database.reset_to_defaults()
    database.update_humidity(58)
    database.update_temperature(32)
    database.update_pressure(1016)
    database.update_light(1,True)
    database.update_light(2,False)
    database.update_light(3,True)
    database.update_light(4,False)
    

if __name__ == '__main__':
    test()

