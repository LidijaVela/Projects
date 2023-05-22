# random Module
# racunalo izabere
# pa korisnik izabere pomocu menija (1 2 3 )
# ispisi jel jednako, pobjedilo racunalo ili korisnik

# racunalo generira slucajno p s k 
# korisnik uspisuje svoj odbabir
# ispis pobjednika

import random

random_number = random.randint(1,3)

print('Izaberi svoju opciju:\n 1. Kamen \n 2. Skare \n 3. Papir')
while True:
    korisnik=input()
    if korisnik.isnumeric() and int(korisnik) in [1,2,3]:
        korisnik=int(korisnik)
        break
    print('Molim izabeerite valjanu opciju')

print (f'Odabir racunala: {random_number}, Odabir korisnika: {korisnik}')

if random_number==korisnik:
    print('Izjednaceno')
elif random_number== 1:
    if korisnik==2:
        print('Kamen je potukao skare! Izgubili ste')
    else: 
        print('Papir poklapa kamen! Pobjedili ste')  
elif random_number==2: 
    if korisnik==3:
        print('Skare su presjekle papair! Izgubili ste')
    else: 
        print('Kamen je potukao skare!. Pobjedili ste')
elif random_number==3:
    if korisnik==1:
        print('Papir poklapa kamen! Izgubili ste')
    else: 
        print('Skare su presjekle papir! Pobjedili ste')
    
