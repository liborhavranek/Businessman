from tkinter import *
from tkinter import ttk

def update():
    if button:
        window.update()
    elif button1:
        window.update()


def valBarra(m):
    cont = 0
    etapas = m/100
    while cont < etapas:
        cont = cont + 1
        i = 0
        while i < 1000000:
            i = i + 1
        varBarra.set(cont)
        update()



def valBarra1(m):
    cont = 0
    etapas = m/100
    while cont < etapas:
        cont = cont + 1
        i = 0
        while i < 1000000:
            i = i + 1
        varBarra1.set(cont)
        update()


window = Tk()
window.title("program")
window.geometry("500x300")

varBarra = DoubleVar()
varBarra1 = DoubleVar()
varBarra.set(0)

pb = ttk.Progressbar(window,variable=varBarra,maximum=100)
pb.pack()

button = Button(window,text="play", command=lambda:valBarra(10000)).pack()

pb1 = ttk.Progressbar(window,variable=varBarra1,maximum=100)
pb1.pack()

button1 = Button(window,text="play", command=lambda:valBarra1(10000)).pack()


window.mainloop()