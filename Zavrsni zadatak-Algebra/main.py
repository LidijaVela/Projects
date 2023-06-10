
from GUI.gui import GlavnaAplikacija
from Database.database import FloraDatabase


if __name__ == '__main__':
    database= FloraDatabase('PyFlora.db', 'Biljke', 'Posude')
    database.create_tables()
    database.base_fillup()
    app= GlavnaAplikacija(database=database, name="PyFlora Lidija")
    app.run()
