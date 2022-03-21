from tkinter import *
from tkinter.ttk import *

def naamkrijgen():

    global naaminvullen 
    print("hallo {}".format(naaminvullen.get()))

    global nameLabel 
    nameLabel.configure(text=f'welkom {naaminvullen.get()}')

    
    

def main():

    global naaminvullen, nameLabel
    window = Tk()
    
    naam = Label(window, text='Vul uw naam:')
    naam.grid(row=0, column=0)
    naaminvullen = Entry(window)
    naaminvullen.grid(row=1, column=3)
    button = Button(window, text='Hallo', command=naamkrijgen, padding=5, color="L")
    button.grid(row=1, column=0, columnspan=2,)

    nameLabel = Label(window, text=' ') 
    nameLabel.grid(row=2)
 
    window.mainloop()

        
main()