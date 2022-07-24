from tkinter import *
from tkinter.ttk import *

import time
coin = 0


def lemon_bar_click():
    global coin
    meter  = 100
    fill_meter = 0
    speed = 10
    while(fill_meter<meter):
        time.sleep(0.05)
        lemon_bar['value']+=(speed/meter)*100
        fill_meter+=speed
        window.update_idletasks()
    lemon_bar["value"] = 0
    coin += 1
    money_label.config(text=f"{coin}")




def paper_business_click():
    global coin
    meter  = 100
    fill_meter = 0
    speed = 10
    while(fill_meter<meter):
        time.sleep(0.05)
        paper_bar['value']+=(speed/meter)*100
        fill_meter+=speed
        window.update_idletasks()
    paper_bar["value"] = 0
    coin += 5
    money_label.config(text=f"{coin}")



window = Tk()
window.config(background="pale green")

business_label = Label(text="Capitalist Business", font=('Arial', 40), background="yellow")
business_label.grid(column=0, row=0, columnspan=5, pady=20)

lemon_label = Label(text="Lemon bar")
lemon_label.grid(column=0, row=1)

lemon_bar = Progressbar(orient=HORIZONTAL,length=300)
lemon_bar.grid(column=0, row=2 ,padx=10, pady=10)


lemon_button = Button(text="buy", command=lemon_bar_click)
lemon_button.grid(column=0, row=3, pady=10, padx=10)

lemon_piecis = 0
lemon_piecis_label = Label(text=f"{lemon_piecis}", font=('Arial', 20))
lemon_piecis_label.grid(column=1, row=1, rowspan=2, sticky=W, padx=60)


paper_bar = Label(text="paper bar")
paper_bar.grid(column=2, row=1)

paper_bar = Progressbar(orient=HORIZONTAL,length=300)
paper_bar.grid(column=2, row=2 ,padx=10, pady=10)

paper_button = Button(text="buy", command=paper_business_click)
paper_button.grid(column=2, row=3, pady=10, padx=10)

paper_piecis = 0
paper_piecis_label = Label(text=f"{paper_piecis}", font=('Arial', 20))
paper_piecis_label.grid(column=4, row=1, rowspan=2, sticky=W, padx=60)

pizza_label = Label(text="pizza")
pizza_label.grid(column=0, row=4)

pizza_bar = Progressbar(orient=HORIZONTAL,length=300)
pizza_bar.grid(column=0, row=5 ,padx=10, pady=10)

pizza_button = Button(text="buy")
pizza_button.grid(column=0, row=6, pady=10, padx=10)

pizza_piecis = 0
pizza_piecis_label = Label(text=f"{paper_piecis}", font=('Arial', 20))
pizza_piecis_label.grid(column=1, row=4, rowspan=2, sticky=W, padx=60)


donut_bar = Label(text="donut bar")
donut_bar.grid(column=2, row=4)

donut_bar = Progressbar(orient=HORIZONTAL,length=300)
donut_bar.grid(column=2, row=5 ,padx=10, pady=10)

donut_button = Button(text="buy")
donut_button.grid(column=2, row=6, pady=10, padx=10)

donut_piecis = 0
donut_piecis_label = Label(text=f"{paper_piecis}", font=('Arial', 20))
donut_piecis_label.grid(column=4, row=4, rowspan=2, sticky=W, padx=60)

money_label = Label(text=f"{coin}", font=('Arial', 40), background="yellow")
money_label.grid(column=0, row=7, columnspan=5, pady=20)


window.mainloop()
