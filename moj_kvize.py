
def generiraj_pitanje(pitanje,odgovor):
    print(pitanje)
    odgovor_korisnika=input('Odgovor:')
    if odgovor_korisnika== odgovor:
        print('Tocno!')
        return 1
    else:
        print('Netocno!')
        return 0


pitanja_i_odgovori= [("Koja je formula za klorovodik?", "HCl"),("Koji je francuski kemicar prvi protumacio gorenje kao spajanje tvari s kisikom?", "Antoine Lavoisierl"),("Koliko atoma ugljika ima u saharozi?", "12")]


print("Pozdrav! Za pocetak nam reci svoje ime:")
ime=input()
print(f"Pozdrav {ime}")
bodovi=0

while True:
    for(pitanje,odgovor) in pitanja_i_odgovori:
        bodovi+= generiraj_pitanje(pitanje,odgovor)

    print("Zelis li igrati ponovno?")
    ponovno=input()
    if ponovno != "da":
        break
    else:
        bodovi=0
        
print(f"{ime}, osvojili ste {bodovi} bodova!")
