class DictDatabase:
    def __init__(self):
        self.baza= dict() #svaki put kad korisnik pozove DictDatabase uvijek se stvori dictionary

    def create(self, key, value): #zelimo implementirati CRUD
        if key in self.baza:   #da ne moze korisnik ubaciti isti key, da se ne prebrise
            return False
        if type(key)!=str:
            return False
        
        self.baza[key]= value #u nas dictionary dodali jedan par kljuca i valua 
        return True
    
    def read(self,key):
        if key not in self.baza:
            return None
        return self.baza[key]
    
    def update(self,key,value):
        if key in self.baza: #provjerimo je li key vec unutra
            exists=True
        else:
            exists=False

        self.baza[key]=value #dodamo ako nije, a update-amo ako je bio unutra

        return exists # javimo true ili false, ovisno je li prije updatea postojao vec ili ne
    
    def delete(self,key):
        if key not in self.baza:
            return False
        
        self.baza.pop(key)
        return True

    
def main():
    database=DictDatabase() #kreirali smo objekt koji nam glumi bazu podataka. Init pridruzi 

    check=database.create('test', 10)
    print(check)
    print(database.read('test'))
    print(database.update('test','nemamo predavanja'))
    print(database.read('test'))
    print(database.delete('test'))
    print(database.read('test'))


if __name__=='__main__':
    main()

