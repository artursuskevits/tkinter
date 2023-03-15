from tkinter import *
from tkinter import ttk
def func(i):
    tabs.select(i)

win=Tk()
win.geometry("200x200")

M=Menu(win)
win.config(menu=M)
m1=Menu(M)
M.add_cascade(label="Tabs",menu=m1)
m1.add_command(label="Esimine",accelerator="Ctrl_1",command=lambda:func(0))
m1.add_command(label="Teine",accelerator="Command+2",command=lambda:func(1))
m1.add_command(label="Kolmas",accelerator="Command+3",command=lambda:func(2))
m1.add_command(label="Neljas",accelerator="Command+4",command=lambda:func(3))
m1.add_command(label="Viies",accelerator="Command+5",command=lambda:func(4))
m1.add_separator()

tabs=ttk.Notebook(win)
texts=["Esimine","Teine","Kolmas","Neljas","Viies"]
tab1=Frame(tabs)
tab2=Frame(tabs)
tab3=Frame(tabs)
tab4=Frame(tabs)
tab5=Frame(tabs)

tabs.add(tab1,text=texts[0])
tabs.add(tab2,text=texts[1])
tabs.add(tab3,text=texts[2])
tabs.add(tab4,text=texts[3])
tabs.add(tab5,text=texts[4])

tabs.pack(fill="both")

win.mainloop()