dozvoljena_polja=['1','2', '3', '4','5','6','7','8','9']
pobjeda_x= 'Pobjedio je x!'
pobjeda_o= 'Pobjedio je o!'
izjednaceno= 'Izjednaceno!'

# imamo dvije liste:
#     - lista x- pmatimo polja za igraca x
#     - lista o- pamtimo polja za igraca o

lista_x=[]
lista_o=[]

while True:
    while True:
        # igrac x unosi broj polja
        igrac_x=input('Igra igrac x:')
        if igrac_x in dozvoljena_polja and igrac_x not in lista_x and igrac_x not in lista_o:
            lista_x.append(igrac_x)
            break
        else:
            print('Krivi unos, ponovite!')

    # Provjeri je li igra zavrsila, ako da, ispisi rezultat
    if '1' in lista_x and '2' in lista_x and '3' in lista_x:
        print(pobjeda_x)
        break
    if '4' in lista_x and '5' in lista_x and '6' in lista_x:
        print(pobjeda_x)
        break
    if '7' in lista_x and '8' in lista_x and '9' in lista_x:
        print(pobjeda_x)
        break
    if '1' in lista_x and '4' in lista_x and '7' in lista_x:
        print(pobjeda_x)
        break
    if '2' in lista_x and '5' in lista_x and '8' in lista_x:
        print(pobjeda_x)
        break
    if '3' in lista_x and '6' in lista_x and '9' in lista_x:
        print(pobjeda_x)
        break
    if '1' in lista_x and '5' in lista_x and '9' in lista_x:
        print(pobjeda_x)
        break
    if '3' in lista_x and '5' in lista_x and '7' in lista_x:
        print(pobjeda_x)
        break
    if len(lista_x)+len(lista_o)== 9:
        print(izjednaceno)
        break

    while True:
        igrac_O=input('Igra igrac o:')
        if igrac_O in dozvoljena_polja and igrac_O not in lista_x and igrac_O not in lista_o:
            lista_o.append(igrac_O)
            break
        else:
            print('Krivi unos, ponovite!')

    # Provjeri je li igra zavrsila, ako da, ispisi rezultat
    if '1' in lista_o and '2' in lista_o and '3' in lista_o:
        print(pobjeda_o)
        break
    if '4' in lista_o and '5' in lista_o and '6' in lista_o:
        print(pobjeda_o)
        break
    if '7' in lista_o and '8' in lista_o and '9' in lista_o:
        print(pobjeda_o)
        break
    if '1' in lista_o and '4' in lista_o and '7' in lista_o:
        print(pobjeda_o)
        break
    if '2' in lista_o and '5' in lista_o and '8' in lista_o:
        print(pobjeda_o)
        break
    if '3' in lista_o and '6' in lista_o and '9' in lista_o:
        print(pobjeda_o)
        break
    if '1' in lista_o and '5' in lista_o and '9' in lista_o:
        print(pobjeda_o)
        break
    if '3' in lista_o and '5' in lista_o and '7' in lista_o:
        print(pobjeda_o)
        break
    if len(lista_x)+len(lista_o)== 9:
        print(izjednaceno)
        break

