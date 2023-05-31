import tkinter as tk
from tkinter import ttk

#fali mi azuriranje biljke i posude

def prazna_kucica(): #provjeravamo je li korisnik unio podatke 
    if box_username.get():
        pass
    if box_password.get():
        pass
    else:
        print ('Unesite podatak')

#login
root = tk.Tk()
root.title('PyFlora')
root.geometry('300x150')

prijava=tk.Frame(root)
prijava.pack()

glavni_prozor=tk.Toplevel(root)
glavni_prozor.geometry('630x600')
glavni_prozor.title('PyFlora-main')
tab_control=ttk.Notebook(glavni_prozor)

username = tk.Label(prijava, text='Username:',font=("Arial", 10))
username.grid(column=0, row=7, padx=5, pady=5)      
box_username=tk.Entry(prijava,background='orchid1')
box_username.grid(column=1, columnspan=1, row=7)

password = tk.Label(prijava, text='Password:',font=("Arial", 10))
password.grid(column=0, row=8, padx=5, pady=5)      
box_password=tk.Entry(prijava,background='orchid1', show='*')
box_password.grid(column=1, columnspan=1, row=8)

entry=tk.Button(prijava,text='Prijava', font=("Arial", 10), background='magenta2',command=prazna_kucica)
entry.grid(column=2, row=9, padx=5, pady=5)

# glavni prozor

#POSUDE

tab1=ttk.Frame(tab_control)
tab2=ttk.Frame(tab_control)

tab_control.add(tab1,text=' PyPosude ')
tab_control.add(tab2,text='   Biljke   ')
tab_control.pack(expand=1,fill='both')

#tipka za sinkroniziranje podataka sa senzora
sync=tk.Button(tab1,text='  Sync  ', font=("Arial",10), background='medium orchid1')
sync.grid(column=9,row=0,padx=5,pady=5)

#tipka za dodavanje nove posude
def dodaj_posudu():
    nova_posuda=tk.Toplevel(posuda)
    nova_posuda.geometry('150x100')
    nova_posuda.title('Nova posuda')
    ime_nove_p=tk.Label(nova_posuda,text='Ime posude:')
    ime_nove_p.pack()
    ime_p_box=tk.Entry(nova_posuda,background='plum1')
    ime_p_box.pack()
    
    kreiraj_p=tk.Button(nova_posuda,text='KREIRAJ')
    kreiraj_p.pack()



dodaj=tk.Button(tab1,text='Dodaj +', font=("Arial",10), background='medium orchid1',command=dodaj_posudu)
dodaj.grid(column=9,row=9,padx=5,pady=5)

# otvorimo posudu pritiskom na tipku ...
def otvori_posudu():
   global posuda_window
   global azuriraj
   posuda_window=tk.Toplevel(tab1)
   posuda_window.geometry('500x250')
   posuda_window.title('Posuda n | Naziv')
   #lijevo slika, ime biljke i graf
   frame1=tk.Frame(posuda_window)
   frame1.pack(side='left', fill='both',expand=True)
   slika=tk.Text (frame1,height = 5, width = 10)
   slika.pack()
   label=tk.Label(slika,text='   SLIKA   ')
   label.pack()
   naziv_biljke=tk.Label(frame1,text='Ime biljke')
   naziv_biljke.pack()
   graf=tk.Text(frame1,height=7,width=22)
   graf.pack(side='bottom')
   #desno podaci sa senzora
   frame2=tk.Frame(posuda_window)
   frame2.pack(side='left',fill='both',expand=True)
   vlaznost=tk.Label(frame2, text='Vlaznost: ')
   vlaznost.grid(column=1,row=1)
   vlaznost_box=tk.Entry(frame2,background='plum1')
   vlaznost_box.grid(column=2,row=1, padx=5,pady=5)
   pH=tk.Label(frame2,text='pH: ')
   pH.grid(column=1,row=2)
   pH_box=tk.Entry(frame2,background='plum1')
   pH_box.grid(column=2,row=2,padx=5,pady=5)
   salinitet=tk.Label(frame2,text='Salinitet: ')
   salinitet.grid(column=1,row=3)
   salinitet_box=tk.Entry(frame2,background='plum1')
   salinitet_box.grid(column=2,row=3,padx=5,pady=5)
   svjetlina=tk.Label(frame2,text='Svjetlina: ')
   svjetlina.grid(column=1,row=4)
   svjetlina_box=tk.Entry(frame2,background='plum1')
   svjetlina_box.grid(column=2,row=4,padx=5,pady=5)
   temp=tk.Label(frame2,text='Temperatura: ')
   temp.grid(column=1,row=5)
   temp_box=tk.Entry(frame2,background='plum1')
   temp_box.grid(column=2,row=5,padx=5,pady=5)
   prazno=tk.Label(frame2,text=' ')
   prazno.grid(column=1,row=6)
   prazno2=tk.Label(frame2,text=' ')
   prazno2.grid(column=1,row=7)
   prazno3=tk.Label(frame2,text=' ')
   prazno3.grid(column=1,row=8)
   azuriraj=tk.Button(frame2,text='Azuriraj',background='medium orchid1')#command=azuriraj_posudu
   azuriraj.grid(column=3,row=9)
   
#    def azuriraj_posudu():
#       azururanje=tk.Toplevel(frame2)
#       azururanje.geometry('200x150')
#       azururanje.title('Azuriranje posude')


#posuda 1
posuda=tk.Frame(tab1,relief=tk.RAISED,borderwidth=1)
posuda.grid(row=1, column=1,padx=40,pady=40)
naziv=tk.Label(posuda,text='Posuda 1 | Balkon')
naziv.pack()
tipkica=tk.Button(posuda,text=' ... ',background='plum2',command=otvori_posudu).pack()

#posuda 2
posuda2=tk.Frame(tab1,relief=tk.RAISED,borderwidth=1)
posuda2.grid(row=1, column=2,padx=40,pady=40)
naziv=tk.Label(posuda2,text='Posuda 2 | Soba1')
naziv.pack()
tipkica2=tk.Button(posuda2,text=' ... ',background='plum2',command=otvori_posudu)
tipkica2.pack()

#posuda 3
posuda3=tk.Frame(tab1,relief=tk.RAISED,borderwidth=1)
posuda3.grid(row=1, column=3,padx=40,pady=40)
naziv=tk.Label(posuda3,text='Posuda 3 | WC')
naziv.pack()
tipkica3=tk.Button(posuda3,text='...',background='plum2',command=otvori_posudu)
tipkica3.pack()

#posuda 4
posuda4=tk.Frame(tab1,relief=tk.RAISED,borderwidth=1)
posuda4.grid(row=2, column=1,padx=40,pady=40)
naziv=tk.Label(posuda4,text='Posuda 4 | Dnevni')
naziv.pack()
tipkica4=tk.Button(posuda4,text='...',background='plum2',command=otvori_posudu)
tipkica4.pack()

#posuda 7
posuda7=tk.Frame(tab1,relief=tk.RAISED,borderwidth=1)
posuda7.grid(row=3, column=1,padx=40,pady=40)
naziv=tk.Label(posuda7,text='Posuda 7 | Hodnik')
naziv.pack()
tipkica7=tk.Button(posuda7,text='...',background='plum2',command=otvori_posudu)
tipkica7.pack()

#glavni prozor

#BILJKE
#tipka za dodavanje nove biljke

def dodaj_biljku():
    nova_biljka=tk.Toplevel(tab2)
    nova_biljka.geometry('300x200')
    nova_biljka.title('Nova biljka')
    ime_nove_b=tk.Label(nova_biljka,text='Ime biljke:')
    ime_nove_b.grid(row=0,column=0)
    ime_b_box=tk.Entry(nova_biljka,background='plum1')
    ime_b_box.grid(row=1,column=0,columnspan=2)
    slika_nove_b=tk.Label(nova_biljka,text='Slika:')
    slika_nove_b.grid(row=2,column=0)
    slika_b_box=tk.Entry(nova_biljka,background='plum1')
    slika_b_box.grid(row=3,column=0,columnspan=2)
    vlaznost_nove=tk.Label(nova_biljka,text='Vlaznost:')
    vlaznost_nove.grid(row=4,column=0)
    vlaznost_n_box=tk.Entry(nova_biljka,background='plum1')
    vlaznost_n_box.grid(row=4,column=1,padx=2,pady=2,columnspan=4)
    svjetlo_nove=tk.Label(nova_biljka,text='Svjetlost:')
    svjetlo_nove.grid(row=5,column=0)
    svjetlo_n_box=tk.Entry(nova_biljka,background='plum1')
    svjetlo_n_box.grid(row=5,column=1,columnspan=4)
    supstrat_nove=tk.Label(nova_biljka,text='Supstrat:')
    supstrat_nove.grid(row=6,column=0)
    suptrat_n_box=tk.Entry(nova_biljka,background='plum1')
    suptrat_n_box.grid(row=6,column=1,columnspan=4)
    kreiraj_b=tk.Button(nova_biljka,text='KREIRAJ')
    kreiraj_b.grid(row=7,column=3)


dodaj_b=tk.Button(tab2,text='Dodaj +', font=("Arial",10), background='medium orchid1',command=dodaj_biljku)
dodaj_b.grid(column=9,row=9,padx=5,pady=5)

def otvori_biljku():
   global biljka_window
   global azurir
   biljka_window=tk.Toplevel(biljka1)
   biljka_window.geometry('500x250')
   biljka_window.title('Naziv biljke')

   #lijevo slika
   frame1=tk.Frame(biljka_window)
   frame1.pack(side='left', fill='both',expand=True)
   slika=tk.Text (frame1,height = 5, width = 10)
   slika.pack()
   label=tk.Label(slika,text='   SLIKA   ')
   label.pack()
   
   
   #desno podaci o njezi
   
   frame2=tk.Frame(biljka_window)
   frame2.pack(side='left',fill='both',expand=True)
   njega=tk.Label(frame2, text='NJEGA ')
   njega.grid(column=1,row=0)
   vlaznost=tk.Label(frame2, text='Vlaznost: ')
   vlaznost.grid(column=1,row=1)
   vlaznost_box=tk.Entry(frame2,background='plum1')
   vlaznost_box.grid(column=2,row=1, padx=5,pady=5)
   svjetlina=tk.Label(frame2,text='Svjetlina: ')
   svjetlina.grid(column=1,row=4)
   svjetlina_box=tk.Entry(frame2,background='plum1')
   svjetlina_box.grid(column=2,row=4,padx=5,pady=5)

   supstrat=tk.Label(frame2,text='Supstrat: ')
   supstrat.grid(column=1,row=5)
   sup_box=tk.Entry(frame2,background='plum1')
   sup_box.grid(column=2,row=5,padx=5,pady=5)
   prazno=tk.Label(frame2,text=' ')
   prazno.grid(column=1,row=6)
   prazno2=tk.Label(frame2,text=' ')
   prazno2.grid(column=1,row=7)
   prazno3=tk.Label(frame2,text=' ')
   prazno3.grid(column=1,row=8)
   azurir=tk.Button(frame2,text='Azuriraj',background='medium orchid1')#command=azuriraj_biljku
   azurir.grid(column=3,row=9)
#biljka 1
biljka1=tk.Frame(tab2,relief=tk.RAISED,borderwidth=1)
biljka1.grid(row=1, column=1,padx=40,pady=40)
naziv=tk.Label(biljka1,text='Orhideja')
tipkica=tk.Button(biljka1,text=' ... ',background='plum2',command=otvori_biljku).pack()

root.mainloop()