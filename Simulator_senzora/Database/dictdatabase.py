class DictDatabase:
    def __init__(self):
        self.baza= dict() 
    def create(self, key, value): 
        if key in self.baza:   
            return False
        if type(key)!=str:
            return False
        
        self.baza[key]= value 
        return True
    
    def read(self,key):
        if key not in self.baza:
            return None
        return self.baza[key]
    
    def update(self,key,value):
        if key in self.baza: 
            exists=True
        else:
            exists=False

        self.baza[key]=value 

        return exists
    
    def delete(self,key):
        if key not in self.baza:
            return False
        
        self.baza.pop(key)
        return True

    
def main():
    database=DictDatabase() 

    check=database.create('test', 10)
    print(check)
    print(database.read('test'))
    print(database.update('test','nnnn'))
    print(database.read('test'))
    print(database.delete('test'))
    print(database.read('test'))


if __name__=='__main__':
    main()

