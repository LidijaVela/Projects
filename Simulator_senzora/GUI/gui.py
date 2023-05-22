import tkinter as tk
from tkinter import ttk

class GUI:
    def __init__(self,state):

        self.state=state 

        root = tk.Tk()
        root.title('Senzor')
        root.geometry('410x350')

        root.after(2,self.update_display) #2 sekunde nakon sto se porene root on ce pokrneuti nasu funkciju update desplay

        self.root=root 

        vlaga = tk.Label(root, text='Vlaga:',font=("Arial", 10))
        vlaga.grid(column=0, row=0, padx=5, pady=5)
        slider_vlaga = tk.Scale(orient = 'horizontal', length = 300, from_ = 0, to=100,bg='hot pink',command=self.hum_change)
        slider_vlaga.grid(column=1, columnspan=3, row=0)
        self.slider_vlaga=slider_vlaga

        temperatura = tk.Label(root, text='Temperatura:',font=("Arial", 10))
        temperatura.grid(column=0, row=1, padx=5, pady=5)
        slider_temperatura = tk.Scale(orient = 'horizontal', length = 300, from_ = -20, to=50,bg='white',command=self.temp_change) 
        slider_temperatura.grid(column=1, columnspan=3, row=1)
        self.slider_temperatura=slider_temperatura

        tlak = tk.Label(root, text='Tlak:',font=("Arial", 10))
        tlak.grid(column=0, row=2, padx=5, pady=5)
        slider_tlak = tk.Scale(orient = 'horizontal', length = 300, from_ = 800, to=1100,bg='maroon1',command=self.press_change)
        slider_tlak.grid(column=1, columnspan=3, row=2)
        self.slider_tlak=slider_tlak

        tipkice = tk.Frame(root).grid(column=0, columnspan=5, row=3, ipadx=50, ipady=50, padx=40, pady=40)
            
        btn_generiraj = tk.Button(tipkice,height=1, width=3,bg='violet red',command=self.button_click_1)
        btn_generiraj.grid(column=0, row=3)
        
        
        btn_kopiraj = tk.Button(tipkice,height=1, width=3,bg='violet red',command=self.button_click_2)
        btn_kopiraj.grid(column=1, row=3)
            
        btn_resetiraj = tk.Button(tipkice,height=1, width=3,bg='violet red',command=self.button_click_3)
        btn_resetiraj.grid(column=0, row=4)

        btn_resetira = tk.Button(tipkice, height=1, width=3,bg='violet red',command=self.button_click_4)
        btn_resetira.grid(column=1, row=4)


        textbox= tk.Text(tipkice, height = 10, width = 25,bg ="white")
        textbox.grid(column=3,row=3)
        self.textbox=textbox


    def temp_change(self, event): 
        temperature=self.slider_temperatura.get() 
        self.state.set_temperature(temperature) 
        

    def press_change(self,event):
        pressure=self.slider_tlak.get()
        self.state.set_pressure(pressure)

    def hum_change(self,event):
        humidity=self.slider_vlaga.get()
        self.state.set_humidity(humidity)

    def button_click_1(self):
        self.state.set_light(0)

    def button_click_2(self):
        self.state.set_light(1)
    
    def button_click_3(self):
        self.state.set_light(2)

    def button_click_4(self):
        self.state.set_light(3)

    def update_display(self):
        text=self.state.read_display()
        self.textbox.delete('1.0',tk.END)
        self.textbox.insert(tk.END,text)
        self.root.after(2000,self.update_display) #pozovi mene nakon 2 sekunde

    def mainloop(self):
        self.root.mainloop()
