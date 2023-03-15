from module1 import *
from tkinter import *
logins=[]
passwords=[]
aken=Tk()
aken.geometry("600x600")
aken.title("Menu")
aken.iconbitmap("images.ico")

def check_registreerimine(ent1,ent2):
    if ent1.get() != "" and ent2.get() != "":
        login = str(ent1.get())
        print(login)
        password=str(ent2.get())
        logins.append(ent1.get())
        passwords.append(ent2.get())
        print(logins)
        print(passwords)
    else:
        ent1.configure(bg="red")
        ent2.configure(bg="red")


def registreerimine(): 
    dopaken=Toplevel()
    dopaken.geometry("600x600")
    dopaken.title("registreerimine")
    lbl1=Label(dopaken,text="Create login")
    ent1=Entry(dopaken,fg="blue",bg="lightblue",width=15,font="Arial 20", justify=CENTER)
    lbl2=Label(dopaken,text="Create password")
    ent2=Entry(dopaken,fg="blue",bg="lightblue",width=15,font="Arial 20", justify=CENTER)
    Check=Button(dopaken,text="go", font="Arial 24",relief=RAISED,command=lambda:check_registreerimine(ent1,ent2))
    lbl1.pack()
    ent1.pack()
    lbl2.pack()
    ent2.pack()
    Check.pack()
    dopaken.mainloop()



btn1=Button(aken, text="registreerimine", font="Arial 24",relief=RAISED,command=registreerimine)
btn2=Button(aken, text="autoriseerimine", font="Arial 24",relief=RAISED)
btn3=Button(aken, text="nime voi parooli muutmine", font="Arial 24",relief=RAISED)
btn4=Button(aken, text="unustanud parooli taastamine", font="Arial 24",relief=RAISED)
btn5=Button(aken, text="lopetamine", font="Arial 24",relief=RAISED)


ob=[btn1,btn2,btn3,btn4,btn5]
for i in range(len( ob)):
    ob[i].pack()
aken.mainloop()