import tkinter as tk
from tkinter import ttk
class GUI:
    def __init__(self,state):

        self.state=state
        
        root = tk.Tk()
        root.title('SmartHome')
        root.geometry('700x400')
        self.root=root

        frame=tk.Frame(root)
        frame.pack()
        self.frame=frame

        frame2=tk.Toplevel(root)
        frame2.geometry('700x300')
        frame2.title('Promjene')
        self.frame2=frame2

        #VLAGA
        vlaga = tk.Label(frame, text='VLAGA',font=("Arial", 11))
        vlaga.grid(column=2, row=0, padx=5, pady=5)

        unutarnja_vlaga = tk.Label(frame, text='Unutarnja vlaga [%]:',font=("Arial", 10))
        unutarnja_vlaga.grid(column=0, row=1, padx=5, pady=5)      
        box_uvlaga=tk.Entry(frame,background='hot pink')
        box_uvlaga.grid(column=1, columnspan=1, row=1)

        vanjska_vlaga = tk.Label(frame, text='Vanjska vlaga [%]:',font=("Arial", 10))
        vanjska_vlaga.grid(column=3, row=1, padx=5, pady=5)
        box_vvlaga=tk.Entry(frame,background='hot pink')
        box_vvlaga.grid(column=4,columnspan=1, row=1)


        #TEMPERATURA
        temperatura = tk.Label(frame, text='TEMPERATURA',font=("Arial", 11))
        temperatura.grid(column=2, row=2, padx=5, pady=5)

        unutarnja_temp = tk.Label(frame, text='Unutarnja temperatura [°C]:',font=("Arial", 10))
        unutarnja_temp.grid(column=0, row=3, padx=5, pady=5)      
        box_utemp=tk.Entry(frame,background='hot pink')
        box_utemp.grid(column=1, columnspan=1, row=3)

        vanjska_temp = tk.Label(frame, text='Vanjska temperatura [°C]:',font=("Arial", 10))
        vanjska_temp.grid(column=3, row=3, padx=5, pady=5)
        box_vtemp=tk.Entry(frame,background='hot pink')
        box_vtemp.grid(column=4,columnspan=1, row=3)

        #TLAK
        tlak = tk.Label(frame, text='TLAK',font=("Arial", 11))
        tlak.grid(column=2, row=4, padx=5, pady=5)

        unutarnja_temp = tk.Label(frame, text='Talk zraka [Pa]:',font=("Arial", 10))
        unutarnja_temp.grid(column=0, row=5, padx=5, pady=5)      
        box_utemp=tk.Entry(frame,background='hot pink')
        box_utemp.grid(column=1, columnspan=1, row=5)

        #ZARULJE
        zarulje = tk.Label(frame, text='SNAGA ŽARULJA',font=("Arial", 11))
        zarulje.grid(column=2, row=6, padx=5, pady=5)

        zarulja_d = tk.Label(frame, text='Dnevna soba [W]:',font=("Arial", 10))
        zarulja_d.grid(column=0, row=7, padx=5, pady=5)      
        box_zaruljad=tk.Entry(frame,background='hot pink')
        box_zaruljad.grid(column=1, columnspan=1, row=7)

        zarulja_s = tk.Label(frame, text='Spavaća soba [W]:',font=("Arial", 10))
        zarulja_s.grid(column=3, row=7, padx=5, pady=5)
        box_zaruljas=tk.Entry(frame,background='hot pink')
        box_zaruljas.grid(column=4,columnspan=1, row=7)


        zarulja_w = tk.Label(frame, text='WC [W]:',font=("Arial", 10))
        zarulja_w.grid(column=0, row=8, padx=5, pady=5)      
        box_zaruljaw=tk.Entry(frame,background='hot pink')
        box_zaruljaw.grid(column=1, columnspan=1, row=8)

        zarulja_k = tk.Label(frame, text='Kuhinja [W]:',font=("Arial", 10))
        zarulja_k.grid(column=3, row=8, padx=5, pady=5)
        box_zaruljak=tk.Entry(frame,background='hot pink')
        box_zaruljak.grid(column=4,columnspan=1, row=8)

        promjeni=tk.Button(frame,text='PROMJENI', font=("Arial", 11), background='maroon1',command=self.show_change)
        promjeni.grid(column=2, row=10, padx=5, pady=5)



        #PROMJENI PROZOR
        zarulje = tk.Label(frame2, text='PROMJENI VRIJEDNOSTI',font=("Arial", 11))
        zarulje.grid(column=2, row=0, padx=5, pady=5)
        #Temp i tlak

        zeljena_temp = tk.Label(frame2, text='Željena temperatura [°C]:',font=("Arial", 10))
        zeljena_temp.grid(column=0, row=1, padx=5, pady=5)      
        box_temp=tk.Entry(frame2,background='light pink')
        box_temp.grid(column=1, columnspan=1, row=1)
        self.zeljena_temp=box_temp

        zeljena_vlaga = tk.Label(frame2, text='željena vlaga [%]:',font=("Arial", 10))
        zeljena_vlaga.grid(column=3, row=1, padx=5, pady=5)
        box_vlaga=tk.Entry(frame2,background='light pink')
        box_vlaga.grid(column=4,columnspan=1, row=1)
        self.zeljena_vlaga=box_vlaga
        #zarulje
        zarulje2 = tk.Label(frame2, text='SNAGA ŽARULJA',font=("Arial", 11))
        zarulje2.grid(column=2, row=2, padx=5, pady=5)

        zarulja_dn = tk.Label(frame2, text='Dnevna soba [W]:',font=("Arial", 10))
        zarulja_dn.grid(column=0, row=3, padx=5, pady=5)      
        box_zaruljadn=tk.Entry(frame2,background='light pink')
        box_zaruljadn.grid(column=1, columnspan=1, row=3)

        zarulja_so = tk.Label(frame2, text='Spavaća soba [W]:',font=("Arial", 10))
        zarulja_so.grid(column=3, row=3, padx=5, pady=5)
        box_zaruljaso=tk.Entry(frame2,background='light pink')
        box_zaruljaso.grid(column=4,columnspan=1, row=3)


        zarulja_wc = tk.Label(frame2, text='WC [W]:',font=("Arial", 10))
        zarulja_wc.grid(column=0, row=4, padx=5, pady=5)      
        box_zaruljawc=tk.Entry(frame2,background='light pink')
        box_zaruljawc.grid(column=1, columnspan=1, row=4)

        zarulja_ku = tk.Label(frame2, text='Kuhinja [W]:',font=("Arial", 10))
        zarulja_ku.grid(column=3, row=4, padx=5, pady=5)
        box_zaruljaku=tk.Entry(frame2,background='light pink')
        box_zaruljaku.grid(column=4,columnspan=1, row=4)

        spremi=tk.Button(frame2,text='SPREMI PROMJENE', font=("Arial", 11), background='maroon1',command=self.change)
        spremi.grid(column=2, row=5, padx=5, pady=5)

        frame2.withdraw()

    def show_change(self):
        self.frame2.deiconify()

    def change(self):
        self.frame2.withdraw()
    
    # def zelim_temp(self,event):
    #     temperature=self.zeljena_temp.get() #pitamo kucicu sto je upisano u njoj
    #     self.state.wanted_temperature(temperature) #saljemo mainu informaciju
    #kaze dino treba ovo staviti kao comand na button spremi pormene, ali ne moze imati vise komanda, nego jedan
    # s toga treba napraviti funkciju koja je i za vlagu i za temperaturu ista. Ako netko hoce mjenjati samo jedan
    #Onda treba biti neka defoult vrijednosti, pa ako nismo upisali zeljeno nesto onda nek bude dofault


    def zelim_vlagu(self,event):
        humidity=self.zeljena_vlaga.get()
        self.state.wanted_humidity(humidity)



    def mainloop(self):
        self.root.mainloop()