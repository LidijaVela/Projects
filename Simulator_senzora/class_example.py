#1. pisemo stalno ime pa prezime, hocemo prointati inicijale

ime1='Dino'
prezime1='Rada'

ime2='Goran'
prezime2='Jaran'

print(ime1[0]+prezime1[0])
print(ime2[0]+prezime2[0])

#2. idemo napraviti funkciju za inicijale 

def inicijali(ime,prezime): #napravimo funkciju inicijali
    return ime[0]+prezime[0]


print(inicijali(ime1,prezime1))
 
#mozemo pozvati i ime1 i prezime2. Ta osoba ne postoji, pogreska. Funckija je pregeneralna
#3.mozemo napraviti da ime i prezime vezemo. Tuple

osoba1=('Dino','Rada')
osoba2=('Goran','Jaran')

print(inicijali(osoba1[0],osoba1[1]))
print(inicijali(osoba2[0],osoba2[1]))


#opet mozemo mjesati, moramo u funciju dodati tuple, a ne odvojeno ime i prezime
#4. kad ona primi tuple, onda je vezamo

def inicijali1(osoba):
    return osoba[0][0]+osoba[1][0]


print(inicijali1(osoba1))
print(inicijali1(osoba2))

#sad dode netko i odluci napraviti ovo... mozemo zloupotrijebiti 
neka_lista=[[1,2],[3,4],[5,6]]
print(inicijali1(neka_lista))

#u igru dolaze klase. Radim tip podatka koji ce glumiti tuple. Objekt cemo spremiti u varijablu
#za nasu klasu ce to biti neka osoba

# class Osoba:
#     def __init__(self,ime,prezime):
#         #print('tu sam')
#u vrijablu dino mi spremi varijable koje ima osoba. Za sad je to samo print'tu sam', pa kad je
#pozovemo, to se ispisuje

#dino=Osoba()

# class Osoba:
#     def __init__(self,ime,prezime):
#         self.ime=ime
#         self.prezime=prezime

##self.ime=ime ...  ime je u argumentu, ali mi cemo nagurati to u objekt
# dino=Osoba('Dino','Rada')
# goran=Osoba('Goran','Jaran')

# print (inicijali1(dino))
# print (inicijali1(goran))
# ne radi jer ne zna funckija sto je sto

def inicijali2(osoba):
    return osoba.ime[0]+osoba.prezime[0]

# print (inicijali2(dino))
# print (inicijali2(goran))
# ako probamo ovo print(inicijali2(10.5)), bit ce greska, ali i dalje je problem sto mozemo ipak pozvati funkciju nad ovim
#moramo dodati funckiju unutar klase, to postaje metoda 

class Osoba:
    def __init__(self,ime,prezime):
        self.ime=ime
        self.prezime=prezime

    def inicijali(self):
        return self.ime[0]+self.prezime[0]
    
dino=Osoba('Dino','Rada')
goran=Osoba('Goran','Jaran')

print(dino.inicijali())
print(goran.inicijali())

#moramo jos staviti da ime i prezime moraju biti stringovi, da ne bi netko dodao listu ili brojeve