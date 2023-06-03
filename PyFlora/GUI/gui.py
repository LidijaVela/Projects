import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)


from Simulator_senzora.skripta import generiraj_sve_podatke


class GlavnaAplikacija:

    image_width = 200
    image_height = 200

    def __init__(self, name='PyFlora-main', geometry='630x600', database=None):
        self.database=database

        self.glavni_prozor=tk.Tk()
        self.glavni_prozor.title(name)

        self.slike=[]
        self.posude=[]
        self.podatci_senozra = {}
        self.generiraj_podatke()

        self.tab_control=ttk.Notebook(self.glavni_prozor)
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab1, text=' PyPosude ')
        self.tab_control.add(self.tab2, text='   Biljke   ')
        self.tab_control.pack(expand=1, fill='both')

        self.prijava=tk.Toplevel(self.glavni_prozor)
        self.prijava.title('PyFlora')
        # self.prijava.geometry('300x150')


        self.username = tk.Label(self.prijava, text='Username:',font=("Arial", 10))
        self.username.grid(column=0, row=7, padx=5, pady=5)
        self.box_username=tk.Entry(self.prijava,background='orchid1')
        self.box_username.grid(column=1, columnspan=1, row=7)

        self.password = tk.Label(self.prijava, text='Password:',font=("Arial", 10))
        self.password.grid(column=0, row=8, padx=5, pady=5)
        self.box_password=tk.Entry(self.prijava,background='orchid1', show='*')
        self.box_password.grid(column=1, columnspan=1, row=8)

        self.prijava.attributes('-topmost', 1)

        self.entry=tk.Button(self.prijava,text='Prijava', font=("Arial", 10), background='magenta2',command=self.check)
        self.entry.grid(column=2, row=9, padx=5, pady=5)

        self.top_tipke_frame = ttk.Frame(self.tab1, relief=tk.RAISED, borderwidth=1)
        self.top_tipke_frame.grid(row=0, padx=4, pady=4, sticky=tk.W)

        self.odjava=tk.Button(self.top_tipke_frame, text='Odjava', font=("Arial", 10), command=self.odjava)
        self.odjava.grid(column=0, row=0, padx=5, pady=5)

        self.tipke_frame = ttk.Frame(self.tab1, relief=tk.RAISED, borderwidth=1)
        self.tipke_frame.grid(column=2, row=1, padx=4, pady=4)

        sync = tk.Button(self.tipke_frame, text='Sync', font=("Arial", 10), command=self.generiraj_podatke)
        sync.grid(column=0, row=1, padx=5, pady=5)

        dodaj = tk.Button(self.tipke_frame, text='Dodaj +', font=("Arial", 10), command=self.dodaj_posudu)
        dodaj.grid(column=0, row=9, padx=5, pady=5)

        self.iscrtaj_posude()
        self.iscrtaj_biljke()

    def iscrtaj_biljke(self):
        pass

    def generiraj_podatke(self):
        sve_posude = self.database.dohvati_sve_posude(join_biljke=False)
        for posuda in sve_posude:
            self.podatci_senozra[posuda['naziv']] = generiraj_sve_podatke()


    def odjava(self):
        self.glavni_prozor.withdraw()
        self.prijava.deiconify()

    def iscrtaj_posude(self):
        sve_posude_iz_baze = self.database.dohvati_sve_posude()
        for index, p in enumerate(sve_posude_iz_baze):
            p_frame = tk.Frame(
                self.tab1, relief=tk.RAISED, borderwidth=1
            )
            p_frame.grid(column=index % 2, row=1 + index // 2 , padx=40, pady=40)
            im = Image.open(f"./slike/{p['slika']}")
            im = im.resize((self.image_width, self.image_height), Image.ANTIALIAS)
            image = ImageTk.PhotoImage(im)

            # onemoguciti da se izbrise slike prije prikaza
            self.slike.append(image)

            image_label = tk.Label(p_frame, image=image)
            image_label.grid(row=0, column=0, rowspan=2, padx=10, pady=10,
                             sticky=tk.W + tk.E + tk.N + tk.S)

            naziv_posude = tk.Label(p_frame, text=f"Naziv posude: {p['naziv']}")
            naziv_posude.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

            ime_biljke = tk.Label(p_frame, text=f"Ime biljke: {p['ime_biljke']}")
            ime_biljke.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

            otvori_posudu = tk.Button(p_frame, text='...', command=lambda: self.otvori_prozor_posude(p))
            otvori_posudu.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

    def otvori_prozor_posude(self, posuda):

        posuda_window = tk.Toplevel(self.tab1)
        posuda_window.title(f'Posuda: {posuda["naziv"]}')
        # lijevo slika, ime biljke i graf
        p_frame = tk.Frame(
            posuda_window, relief=tk.RAISED, borderwidth=1
        )
        p_frame_opis = tk.Frame(
            posuda_window, relief=tk.RAISED, borderwidth=1
        )

        p_frame.grid(column=0, row=0, padx=40, pady=40)
        p_frame_opis.grid(column=1, row=0, padx=40, pady=40)
        im = Image.open(f"./slike/{posuda['slika']}")
        im = im.resize((self.image_width, self.image_height), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(im)

        # onemoguciti da se izbrise slike prije prikaza
        self.slike.append(image)

        image_label = tk.Label(p_frame, image=image)
        image_label.grid(row=0, column=0, rowspan=2, padx=10, pady=10,
                         sticky=tk.W + tk.E + tk.N + tk.S)

        naziv_biljke = tk.Label(p_frame, text=f'Ime biljke: {posuda["ime_biljke"]}')
        naziv_biljke.grid(row=2, column=0)

        vlaznost = tk.Label(p_frame_opis, text='Vlaznost: ')
        vlaznost.grid(column=1, row=1)
        vlaznost_box = tk.Label(p_frame_opis, background='plum1', text=self.podatci_senozra[posuda['naziv']][1])
        vlaznost_box.grid(column=2, row=1, padx=5, pady=5)
        pH = tk.Label(p_frame_opis, text='pH: ')
        pH.grid(column=1, row=2)
        pH_box = tk.Label(p_frame_opis, background='plum1', text=self.podatci_senozra[posuda['naziv']][2])
        pH_box.grid(column=2, row=2, padx=5, pady=5)
        salinitet = tk.Label(p_frame_opis, text='Salinitet: ')
        salinitet.grid(column=1, row=3)
        salinitet_box = tk.Label(p_frame_opis, background='plum1', text=self.podatci_senozra[posuda['naziv']][3])
        salinitet_box.grid(column=2, row=3, padx=5, pady=5)
        svjetlina = tk.Label(p_frame_opis, text='Svjetlina: ')
        svjetlina.grid(column=1, row=4)
        svjetlina_box = tk.Label(p_frame_opis, background='plum1', text=self.podatci_senozra[posuda['naziv']][4])
        svjetlina_box.grid(column=2, row=4, padx=5, pady=5)
        temp = tk.Label(p_frame_opis, text='Temperatura: ')
        temp.grid(column=1, row=5)
        temp_box = tk.Label(p_frame_opis, background='plum1', text=self.podatci_senozra[posuda['naziv']][0])
        temp_box.grid(column=2, row=5, padx=5, pady=5)

        ime_posude = tk.Label(p_frame_opis, text='Ime posude: ')
        ime_posude.grid(column=1, row=9)
        ime_posude_box = tk.Entry(p_frame_opis, background='plum1')
        ime_posude_box.insert(0, posuda['naziv'])
        ime_posude_box.grid(column=2, row=9, padx=5, pady=5)
        azuriraj = tk.Button(p_frame_opis, text='Azuriraj!', command=lambda: self.azuriraj_ime_posude(posuda_window, posuda, ime_posude_box))
        azuriraj.grid(column=3, row=9)

        self.kreiraj_plotove(posuda_window, posuda)

    def azuriraj_ime_posude(self,posuda_window, posuda, entry_box):
        # zasto se kreira nova posuda
        self.database.update_ime_posude(posuda['id'], entry_box.get())
        posuda = self.database.dohvati_posudu_po_imenu(posuda['naziv'])
        posuda_window.title(posuda['naziv'])


    def kreiraj_plotove(self, posuda_window, posuda):

        p_chart = tk.Frame(
            posuda_window, relief=tk.RAISED, borderwidth=1
        )
        p_chart.grid(row=1, padx=40, pady=40)

        x = [1, 2, 3, 4, 5]
        y = self.podatci_senozra[posuda['naziv']]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot(x, y)

        canvas = FigureCanvasTkAgg(f, p_chart)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0)

        labels = ['temperatura', 'vlaznost', 'ph', 'salinitet', 'svjetlina']
        sizes = self.podatci_senozra[posuda['naziv']]

        f_pie = Figure(
            figsize=(5,5),
            dpi=100
        )
        ax = f_pie.add_subplot(111)

        ax.pie(sizes, labels=labels)

        canvas = FigureCanvasTkAgg(f_pie, p_chart)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=1)

        #hist

        f_hist = Figure(
            figsize=(5,5),
            dpi=100
        )
        p = f_hist.gca()

        p.hist(self.podatci_senozra[posuda['naziv']])

        canvas = FigureCanvasTkAgg(f_hist, p_chart)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=3)



    def dodaj_posudu(self):
        nova_posuda = tk.Toplevel(self.posuda)
        nova_posuda.geometry('150x100')
        nova_posuda.title('Nova posuda')
        ime_nove_p = tk.Label(nova_posuda, text='Ime posude:')
        ime_nove_p.pack()
        ime_p_box = tk.Entry(nova_posuda, background='plum1')
        ime_p_box.pack()

        kreiraj_p = tk.Button(nova_posuda, text='KREIRAJ')
        kreiraj_p.pack()

    def check(self):
        if self.box_username.get() == 'a' and self.box_password.get() == 'a':
            self.glavni_prozor.deiconify()
            self.prijava.withdraw()

    def run(self):
        self.glavni_prozor.withdraw()
        self.glavni_prozor.mainloop()

   # def azuriraj_posudu():
   #    azururanje=tk.Toplevel(frame2)
   #    azururanje.geometry('200x150')
   #    azururanje.title('Azuriranje posude')

#
# def dodaj_biljku():
#     nova_biljka=tk.Toplevel(tab2)
#     nova_biljka.geometry('300x200')
#     nova_biljka.title('Nova biljka')
#     ime_nove_b=tk.Label(nova_biljka,text='Ime biljke:')
#     ime_nove_b.grid(row=0,column=0)
#     ime_b_box=tk.Entry(nova_biljka,background='plum1')
#     ime_b_box.grid(row=1,column=0,columnspan=2)
#     slika_nove_b=tk.Label(nova_biljka,text='Slika:')
#     slika_nove_b.grid(row=2,column=0)
#     slika_b_box=tk.Entry(nova_biljka,background='plum1')
#     slika_b_box.grid(row=3,column=0,columnspan=2)
#     vlaznost_nove=tk.Label(nova_biljka,text='Vlaznost:')
#     vlaznost_nove.grid(row=4,column=0)
#     vlaznost_n_box=tk.Entry(nova_biljka,background='plum1')
#     vlaznost_n_box.grid(row=4,column=1,padx=2,pady=2,columnspan=4)
#     svjetlo_nove=tk.Label(nova_biljka,text='Svjetlost:')
#     svjetlo_nove.grid(row=5,column=0)
#     svjetlo_n_box=tk.Entry(nova_biljka,background='plum1')
#     svjetlo_n_box.grid(row=5,column=1,columnspan=4)
#     supstrat_nove=tk.Label(nova_biljka,text='Supstrat:')
#     supstrat_nove.grid(row=6,column=0)
#     suptrat_n_box=tk.Entry(nova_biljka,background='plum1')
#     suptrat_n_box.grid(row=6,column=1,columnspan=4)
#     kreiraj_b=tk.Button(nova_biljka,text='KREIRAJ')
#     kreiraj_b.grid(row=7,column=3)
#
#
# dodaj_b=tk.Button(tab2,text='Dodaj +', font=("Arial",10),command=dodaj_biljku)
# dodaj_b.grid(column=9,row=9,padx=5,pady=5)
#
# def otvori_biljku():
#    global biljka_window
#    global azurir
#    biljka_window=tk.Toplevel(biljka1)
#    biljka_window.geometry('500x250')
#    biljka_window.title('Naziv biljke')
#
#    #lijevo slika
#    frame1=tk.Frame(biljka_window)
#    frame1.pack(side='left', fill='both',expand=True)
#    slika=tk.Text (frame1,height = 5, width = 10)
#    slika.pack()
#    label=tk.Label(slika,text='   SLIKA   ')
#    label.pack()
#
#
#    #desno podaci o njezi
#
#    frame2=tk.Frame(biljka_window)
#    frame2.pack(side='left',fill='both',expand=True)
#    njega=tk.Label(frame2, text='NJEGA ')
#    njega.grid(column=1,row=0)
#    vlaznost=tk.Label(frame2, text='Vlaznost: ')
#    vlaznost.grid(column=1,row=1)
#    vlaznost_box=tk.Entry(frame2,background='plum1')
#    vlaznost_box.grid(column=2,row=1, padx=5,pady=5)
#    svjetlina=tk.Label(frame2,text='Svjetlina: ')
#    svjetlina.grid(column=1,row=4)
#    svjetlina_box=tk.Entry(frame2,background='plum1')
#    svjetlina_box.grid(column=2,row=4,padx=5,pady=5)
#
#    supstrat=tk.Label(frame2,text='Supstrat: ')
#    supstrat.grid(column=1,row=5)
#    sup_box=tk.Entry(frame2,background='plum1')
#    sup_box.grid(column=2,row=5,padx=5,pady=5)
#    prazno=tk.Label(frame2,text=' ')
#    prazno.grid(column=1,row=6)
#    prazno2=tk.Label(frame2,text=' ')
#    prazno2.grid(column=1,row=7)
#    prazno3=tk.Label(frame2,text=' ')
#    prazno3.grid(column=1,row=8)
#    azurir=tk.Button(frame2,text='Azuriraj')#command=azuriraj_biljku
#    azurir.grid(column=3,row=9)
# #biljka 1
# biljka1=tk.Frame(tab2,relief=tk.RAISED,borderwidth=1)
# biljka1.grid(row=1, column=1,padx=40,pady=40)
# naziv=tk.Label(biljka1,text='Orhideja')
# tipkica=tk.Button(biljka1,text=' ... ',background='plum2',command=otvori_biljku).pack()
#
