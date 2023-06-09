import sqlite3

class FloraDatabase:
    def __init__(self, databse_name, biljka, posuda):
        self.database_name=databse_name
        self.biljka=biljka
        self.posuda=posuda

        self.connection = sqlite3.connect(self.database_name)
        # omoguciti da return bude kao dictionary
        self.connection.row_factory = sqlite3.Row

    def close(self):
        self.connection.close()

    def create_tables(self):
        biljke_table= f"""CREATE TABLE IF NOT EXISTS {self.biljka} (
                            id INTEGER PRIMARY KEY,
                            ime_biljke REAL NOT NULL UNIQUE,
                            slika REAL NOT NULL,
                            vlaznost INTEGER NOT NULL,
                            svjetlo INTEGER NOT NULL,
                            supstrat BOOLEAN NOT NULL
                        );"""
        posude_table= f"""CREATE TABLE IF NOT EXISTS {self.posuda} (
                            id INTEGER PRIMARY KEY,
                            naziv REAL NOT NULL,
                            biljka TEXT,
                            UNIQUE (biljka, naziv)
                            FOREIGN KEY (biljka) REFERENCES biljke_table(naziv)
                        );"""
        
        cursor = self.connection.cursor()
        for query in [biljke_table, posude_table]:
            cursor.execute(query)
        self.connection.commit()
        cursor.close()

    #punim bazu pocetnim postavkama
    def base_fillup(self):
        self.insert_biljka('Bosiljak', 'bosiljak.jpg', 30, 100, True)
        self.insert_biljka('Ruzmarin', 'ruzmarin.jpg', 20, 30, True)
        self.insert_biljka('Kaktus', 'kaktus.jpg', 10, 80, False)
        self.insert_biljka('Ruza', 'ruza.jpg', 80, 10, True)
        self.insert_biljka('Orhideja', 'orhideja.jpg', 60, 50, False)
        self.insert_biljka('Narcis', 'narcis.jpg', 75, 20, True)
        self.insert_biljka('Suncokret', 'suncokret.jpg', 30, 60, True)
        self.insert_biljka('Paprika', 'paprika.jpg', 90, 10, True)
        self.insert_biljka('Hortenzija', 'hortenzija.jpg', 10, 80, False)
        self.insert_biljka('Dalija', 'dalija.jpg', 60, 80, True)

        self.insert_posuda('Balkon', 'Ruzmarin')
    
    #dodajem biljku
    def insert_biljka(self,naziv, slika, vlaznost, svjetlo, supstrat, provjeri_constraint=True):
        if provjeri_constraint:
            sub_query = 'OR IGNORE'
        else:
            sub_query=''
        query= f'INSERT {sub_query} INTO {self.biljka} (ime_biljke, slika, vlaznost, svjetlo, supstrat) VALUES (?, ?, ?, ?, ?);'
        cursor = self.connection.cursor()
        cursor.execute(query,(naziv, slika, vlaznost, svjetlo, supstrat))
        self.connection.commit()
        cursor.close()

    def insert_posuda(self, naziv, biljka, provjeri_constraint=True): 
        if provjeri_constraint:
            sub_query = 'OR IGNORE'
        else:
            sub_query=''
        query= f'INSERT {sub_query} INTO {self.posuda} (naziv, biljka) VALUES (?, ?);'
        cursor = self.connection.cursor()
        cursor.execute(query,(naziv, biljka))
        self.connection.commit()
        cursor.close()

    def dohvati_posudu_po_imenu(self, naziv):
        query= f'SELECT * FROM {self.posuda} WHERE naziv={naziv};'
        cursor = self.connection.cursor()
        resp = cursor.execute(query).fetchall()
        self.connection.commit()
        cursor.close()
        return resp

    def dohvati_biljku_po_imenu(self, naziv):
        query= f'SELECT * FROM {self.biljka} WHERE naziv={naziv};'
        cursor = self.connection.cursor()
        resp = cursor.execute(query).fetchall()
        self.connection.commit()
        cursor.close()
        return resp

    #joinala sam biljke u posdude, to mi treba u GUI-ju skupa
    def dohvati_sve_posude(self, join_biljke=True):
        if join_biljke:
            sub_query = f"JOIN {self.biljka} ON {self.biljka}.ime_biljke = {self.posuda}.biljka"
        else:
            sub_query = ''
        query = f'SELECT * from {self.posuda} {sub_query};'
        cursor = self.connection.cursor()
        resp = cursor.execute(query).fetchall()
        self.connection.commit()
        cursor.close()
        return resp


    def dohvati_sve_biljke(self):
        query = f'SELECT * from {self.biljka};'
        cursor = self.connection.cursor()
        resp = cursor.execute(query).fetchall()
        self.connection.commit()
        cursor.close()
        return resp

    def update_ime_posude(self, record_id, novo_ime):
        cursor=self.connection.cursor()
        query=f'UPDATE {self.posuda} SET naziv="{novo_ime}" WHERE id={record_id};'
        cursor.execute(query)
        self.connection.commit()
        cursor.close()

    def update_ime_biljke(self, record_id, novo_ime):
        cursor=self.connection.cursor()
        query=f'UPDATE {self.biljka} SET ime_biljke="{novo_ime}" WHERE id={record_id};'
        cursor.execute(query)
        self.connection.commit()
        cursor.close()

    def izbrisi_posudu(self):
        pass

    def izbrisi_biljku(self):
        pass



    # def _update(self, table_name, column, row, value): #dodam row, pa da
    #     cursor=self.connection.cursor()
    #     query=f'UPDATE {table_name} SET {column,row}={value};' 
    #     cursor.execute(query)
    #     self.connection.commit()
    #     cursor.close()

    

    
def test():
    database = FloraDatabase('PyFlora.db', 'Biljke', 'Posude')
    database.create_tables()





if __name__ == '__main__':
    test()