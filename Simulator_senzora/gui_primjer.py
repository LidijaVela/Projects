import tkinter as tk

def show_login():
    login_window.deiconify() #otvori login prozor kad se pozove ova kunkcija

def check():

    if username.get() =='Dino' and password.get() =='12345':
        frame.pack_forget()         #zaboravi prozor Niste logirani
        success_frame.pack()        #prikazi nam Dobrodisli prozor
    
    login_window.withdraw()


main_window=tk.Tk()
main_window.title('Glavni prozor')
main_window.geometry('370x370')

frame=tk.Frame(main_window)
frame.pack()

success_frame=tk.Frame(main_window)
dobrodosli=tk.Label(success_frame,text='Dobrodošli!')
dobrodosli.pack()

label=tk.Label(frame,text='Niste logirani')
label.pack()

login_button=tk.Button(frame, text='Login',command=show_login)
login_button.pack()


#u tkinteru postoji element koji se zove top level, to je novi prozor. root je glavni porozor, a toplevel mozemo otvarati posebno, istovremeno
login_window=tk.Toplevel(main_window)
login_window.geometry('200x100')
login_window.title('Login')

username=tk.Entry(login_window)
username.pack()

password=tk.Entry(login_window,show='*')
password.pack()

submit=tk.Button(login_window,text='Submit', command=check)
submit.pack()

login_window.withdraw() #ne pokaze se na pocetku

main_window.mainloop()