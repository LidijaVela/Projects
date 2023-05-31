import sqlite3

class FloraDatabase:
    def __init__(self, databse_name, biljka, posuda):
        self.database_name=databse_name
        self.biljka=biljka
        self.posuda=posuda

        self.connection=sqlite3.connect(self.database_name)

    def close(self):
        self.connection.close()

    def create_tables(self):
        biljke_table= f"""CREATE TABLE IF NOT EXISTS {self.biljka} (
                            id INTEGER PRIMARY KEY,
                            naziv REAL NOT NULL,
                            slika REAL NOT NULL,
                            vlaznost INTEGER NOT NULL,
                            svjetlo INTEGER NOT NULL,
                            supstrat BOOLEAN NOT NULL
                        );"""
        posude_table= f"""CREATE TABLE IF NOT EXISTS {self.posuda} (
                            id INTEGER PRIMARY KEY,
                            naziv REAL NOT NULL,
                            biljka TEXT,
                            FOREIGN KEY (biljka) REFERENCES biljke_table(naziv)
                        );"""
        
        cursor = self.connection.cursor()
        for query in [biljke_table, posude_table]:
            cursor.execute(query)
        self.connection.commit()
        cursor.close()

    def insert_biljka(self,naziv, slika, vlaznost, svjetlo, supstrat):
        query= f'INSERT INTO {self.biljka} (naziv, slika, vlaznost, svjetlo, supstrat) VALUES (?, ?, ?, ?, ?);'
        cursor = self.connection.cursor()
        cursor.execute(query,(naziv, slika, vlaznost, svjetlo, supstrat))
        self.connection.commit()
        cursor.close()


    def insert_posuda(self, naziv, biljka): #mozda maknuti vrijednosti ili ostaviti? execute kako?
        query= f'INSERT INTO {self.posuda} (naziv, biljka) VALUES (?, ?);'
        cursor = self.connection.cursor()
        cursor.execute(query,(naziv, biljka))
        self.connection.commit()
        cursor.close()


    # def reset_to_defaults(self):

    #     cursor = self.connection.cursor()
    #     for table_name in [self.biljka, self.posuda]:
    #         delete_query = f'DELETE FROM {table_name};'
    #         cursor.execute(delete_query)

    #     insert_biljka = f'INSERT INTO {self.biljka} (naziv, slika, vlaznost, svjetlo, supstrat) VALUES (Orhideja, orhideja.jpg, 40, 70, TRUE);'
    #     insert_biljka = f'INSERT INTO {self.biljka} (naziv, slika, vlaznost, svjetlo, supstrat) VALUES (Ruza, ruza.jpg, 60, 80, TRUE);'
    #     insert_biljka = f'INSERT INTO {self.biljka} (naziv, slika, vlaznost, svjetlo, supstrat) VALUES (Tulipan, tulipan.jpg, 30, 90, FALSE);'
    #     insert_biljka = f'INSERT INTO {self.biljka} (naziv, slika, vlaznost, svjetlo, supstrat) VALUES (Ljubicica, ljubicica.jpg, 20, 75, FALSE);'
    #     insert_biljka = f'INSERT INTO {self.biljka} (naziv, slika, vlaznost, svjetlo, supstrat) VALUES (Kaktus, kaktus.jpg, 10, 20, FALSE);'
    #     insert_biljka = f'INSERT INTO {self.biljka} (naziv, slika, vlaznost, svjetlo, supstrat) VALUES (Ljiljan, ljiljan.jpg, 50, 50, FALSE);'
    #     insert_biljka = f'INSERT INTO {self.biljka} (naziv, slika, vlaznost, svjetlo, supstrat) VALUES (Dalija, dalija.jpg, 40, 90, FALSE);'
    #     insert_biljka = f'INSERT INTO {self.biljka} (naziv, slika, vlaznost, svjetlo, supstrat) VALUES (Bozur, bozur.jpg, 60, 80, TRUE);'
    #     insert_biljka = f'INSERT INTO {self.biljka} (naziv, slika, vlaznost, svjetlo, supstrat) VALUES (Tratincica, tratincica.jpg, 30, 60, FALSE);'
    #     insert_biljka = f'INSERT INTO {self.biljka} (naziv, slika, vlaznost, svjetlo, supstrat) VALUES (Mimoza, mimoza.jpg, 30, 20, FALSE);'

    #     insert_posuda= f'INSERT INTO {self.posuda} (naziv, biljka) VALUES (Balkon);'
        

    #     for query in [insert_biljka, insert_posuda]:
    #         cursor.execute(query)

    #     self.connection.commit()
    #     cursor.close()


    def _update(self, table_name,column,value):
        cursor=self.connection.cursor()
        query=f'UPDATE {table_name} SET {column}={value};' 
        cursor.execute(query)
        self.connection.commit()
        cursor.close()

    def update_name_b(self, value): # kako znam koji update radim?? moram znati koji red 
        self._update(self.biljka,'naziv',value)

    def update_picture(self,value):
        self._update(self.biljka,'slika',value)
    
    def update_humidity(self,value):
        self._update(self.biljka,'vlaznost',value)
    
    def update_light(self,value):
        self._update(self.biljka,'svjetlo',value)

    def update_add(self,value):
        self._update(self.biljka,'supstrat',value)
    
    def update_name_p(self,value):
        self._update(self.posuda,'naziv',value)
    

def test():
    database = FloraDatabase('PyFlora.db', 'Biljke', 'Posude')
    database.create_tables()
    #database.insert_biljka('Orhideja', 'orhideja.jpg', 40, 70, True)
    # database.insert_biljka('Ruza', 'ruza.jpg', 60, 80, True)
    # database.insert_biljka('Tulipan', 'tulipan.jpg', 30, 90, False)
    # database.insert_biljka('Ljubicica', 'ljubicica.jpg', 20, 75, False)
    # database.insert_biljka('Kaktus', 'kaktus.jpg', 10, 20, False)
    # database.insert_biljka('Ljiljan', 'ljiljan.jpg', 50, 50, False)
    # database.insert_biljka('Dalija', 'dalija.jpg', 40, 90, False)
    # database.insert_biljka('Bozur', 'bozur.jpg', 60, 80, True)
    # database.insert_biljka('Tratincica', 'tratincica.jpg', 30, 60, False)
    # database.insert_biljka('Mimoza', 'mimoza.jpg', 30, 20, False)
    
    database.insert_posuda ('Balkon',)
    database.
 




if __name__ == '__main__':
    test()