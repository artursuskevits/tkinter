import subprocess
from tkinter import *
logins={}
passwords={}
listforupdate=[]
aken=Tk()
aken.geometry("450x450")
aken.title("Menu")
aken.iconbitmap("images.ico")


f=open("dictionary.txt", "r", encoding="utf-8-sig")
for line in f:
    k, v=line.strip().split(":")
    logins[k.strip()] = v.strip()
    f=open("dictionary.txt", "r", encoding="utf-8-sig")
for line in f:
    k, v=line.strip().split(":")
    passwords[v.strip()] = k.strip()
    f=open("dictionary.txt", "r", encoding="utf-8-sig")

def end():
    f=open("dictionary.txt","w",encoding="utf-8-sig")
    for key,vlaue in logins.items():
        line=(f"{key}:{vlaue}")
        listforupdate.append(line)
    f=open("dictionary.txt","w",encoding="utf-8-sig")
    for line in (listforupdate):
        f.write(line+"\n")
    f.close()
    aken.destroy()

def check_autoriseerimine(ent1,ent2,dopaken):
    login = ent1.get()
    password = ent2.get()
    ll=login
    pp=password
    print(ll)
    print(pp)
    print(logins)
    print(passwords)
    if ent1.get() != "" and ent2.get() != "" :
        ##if passwords[pp] == ll and logins[ll] == pp:
        #    lbl4=Label(dopaken,text="You in",height=2,width=40,font="Arial 24")
        #    lbl4.pack()
        for item in logins:
            if logins[item] == password and passwords[password] == login:
                dopaken.destroy()
                aken.destroy()
                subprocess.call(["python", "Tarkvaraarendaja_vastuvott.py"])
            #    lbl4=Label(dopaken,text="You in",height=2,width=40,font="Arial 24")
            #    lbl4.pack()
            #    ent1.configure(bg="lightblue")
            #    ent2.configure(bg="lightblue")
            #    dopaken.destroy()
    else:
        ent1.configure(bg="red")
        ent2.configure(bg="red")

def check_registreerimine(ent1,ent2,dopaken):
    if ent1.get() != "" and ent2.get() != "":
        login = str(ent1.get())
        print(login)
        password = str(ent2.get())
        logins.update({login:password})
        passwords.update({password:login})
        print(logins)
        print(passwords)
        dopaken.destroy()
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
    Check=Button(dopaken,text="go", font="Arial 24",relief=RAISED,command=lambda:check_registreerimine(ent1,ent2,dopaken))
    lbl1.pack()
    ent1.pack()
    lbl2.pack()
    ent2.pack()
    Check.pack()
    dopaken.mainloop()

def autoriseerimine():
    dopaken=Toplevel()
    dopaken.geometry("600x600")
    dopaken.title("autoriseerimine")
    lbl1=Label(dopaken,text="Insert login")
    ent1=Entry(dopaken,fg="blue",bg="lightblue",width=15,font="Arial 20", justify=CENTER)
    lbl2=Label(dopaken,text="Insert password")
    ent2=Entry(dopaken,fg="blue",bg="lightblue",width=15,font="Arial 20", justify=CENTER)
    Check=Button(dopaken,text="go", font="Arial 24",relief=RAISED,command=lambda:check_autoriseerimine(ent1,ent2,dopaken))
    lbl1.pack()
    ent1.pack()
    lbl2.pack()
    ent2.pack()
    Check.pack()
    dopaken.mainloop()

def muuda():
    dopaken=Toplevel()
    dopaken.geometry("600x600")
    dopaken.title("nime voi parooli muutmine")
    lbl1=Label(dopaken,text="What you want change?",font="Arial 24")
    Lobtn=Button(dopaken, text="Login", font="Arial 24",relief=RAISED,command=lambda:lchange(dopaken))
    Pabtn=Button(dopaken, text="Password", font="Arial 24",relief=RAISED,command=lambda:pchange(dopaken))
    lbl1.pack()
    Lobtn.pack()
    Pabtn.pack()

def lchange(dopaken):
    dopaken.destroy()
    dopaken2=Toplevel()
    dopaken2.geometry("600x600")
    lbl1=Label(dopaken2,text="Write old Login",font="Arial 24")
    ent1=Entry(dopaken2,fg="blue",bg="lightblue",width=15,font="Arial 20", justify=CENTER)
    lbl3=Label(dopaken2,text="Write your Pass",font="Arial 24")
    ent3=Entry(dopaken2,fg="blue",bg="lightblue",width=15,font="Arial 20", justify=CENTER)
    lbl2=Label(dopaken2,text="Write new Login",font="Arial 24")
    ent2=Entry(dopaken2,fg="blue",bg="lightblue",width=15,font="Arial 20", justify=CENTER)
    chng=Button(dopaken2, text="Change", font="Arial 24",relief=RAISED,command=lambda:checkl(ent1,ent3,ent2,dopaken2))
    lbl1.pack()
    ent1.pack()
    lbl3.pack()
    ent3.pack()
    lbl2.pack()
    ent2.pack()
    chng.pack()
def checkl(ent1,ent3,ent2,dopaken2):
    if ent1.get() != "" and ent2.get() != "":
        yourpass=ent3.get()
        oldlogin=ent1.get()
        changelogin=ent2.get()
        if oldlogin in logins and yourpass in passwords and passwords[yourpass]==oldlogin:
            oldpass=logins[oldlogin]
            passwords[oldpass] = changelogin
            logins[changelogin]=logins.pop(oldlogin)
            print(logins)
            print(passwords)
            dopaken2.destroy()
        else:
            ent1.configure(bg="red")
            ent2.configure(bg="red")
            ent3.configure(bg="red")
    else:
        ent1.configure(bg="red")
        ent2.configure(bg="red")
        ent3.configure(bg="red")


def pchange(dopaken):
    dopaken.destroy()
    dopaken2=Toplevel()
    dopaken2.geometry("600x600")
    lbl3=Label(dopaken2,text="Write your login",font="Arial 24")
    ent3=Entry(dopaken2,fg="blue",bg="lightblue",width=15,font="Arial 20", justify=CENTER)
    lbl1=Label(dopaken2,text="Write old Password",font="Arial 24")
    ent1=Entry(dopaken2,fg="blue",bg="lightblue",width=15,font="Arial 20", justify=CENTER)
    lbl2=Label(dopaken2,text="Write new Password",font="Arial 24")
    ent2=Entry(dopaken2,fg="blue",bg="lightblue",width=15,font="Arial 20", justify=CENTER)
    chng=Button(dopaken2, text="Change", font="Arial 24",relief=RAISED,command=lambda:checkp(ent1,ent2,ent3,dopaken2))
    lbl3.pack()
    ent3.pack()
    lbl1.pack()
    ent1.pack()
    lbl2.pack()
    ent2.pack()
    chng.pack()
def checkp(ent1,ent2,ent3,dopaken2):
    if ent1.get() != "" and ent2.get() != "" and ent3 != "":
        yourlogin=ent3.get()
        oldpassword=ent1.get()
        changepassword=ent2.get()
        if oldpassword in passwords and yourlogin in logins and logins[yourlogin] == oldpassword :
            oldlogin=passwords[oldpassword]
            logins[oldlogin] = changepassword
            passwords[changepassword]=passwords.pop(oldpassword)
            print(logins)
            print(passwords)
            dopaken2.destroy()
        else:
            ent1.configure(bg="red")
            ent2.configure(bg="red")
            ent3.configure(bg="red")
    else:
        ent1.configure(bg="red")
        ent2.configure(bg="red")
        ent3.configure(bg="red")

def help():
    dopaken=Toplevel()
    dopaken.geometry("600x600")
    dopaken.title("unustanud parooli taastamine")
    lbl1=Label(dopaken,text="Write your login",font="Arial 24")
    ent3=Entry(dopaken,fg="blue",bg="lightblue",width=15,font="Arial 20", justify=CENTER)
    chck=Button(dopaken, text="show password", font="Arial 24",relief=RAISED,command=lambda:showpassword(ent3,dopaken))
    lbl1.pack()
    ent3.pack()
    chck.pack()

def showpassword(ent3,dopaken):
    yourlogin=ent3.get()
    dopaken.destroy()
    dopaken2=Toplevel()
    dopaken2.geometry("600x600")
    lbl2=Label(dopaken2,text="Your password:",font="Arial 24")
    lbl3=Label(dopaken2,font="Arial 30")
    if yourlogin in logins:
        yourpassword=logins[yourlogin]
        lbl3.configure(text=yourpassword)
        lbl2.pack()
        lbl3.pack()
    else:
        lbl3.configure(bg="red")
        lbl3.configure(text="Wrong Login")
        lbl2.pack()
        lbl3.pack()

        



btn1=Button(aken, text="registreerimine", font="Arial 24",relief=RAISED,command=registreerimine)
btn2=Button(aken, text="autoriseerimine", font="Arial 24",relief=RAISED,command=autoriseerimine)
btn3=Button(aken, text="nime voi parooli muutmine", font="Arial 24",relief=RAISED,command=muuda)
btn4=Button(aken, text="unustanud parooli taastamine", font="Arial 24",relief=RAISED,command=help)
btn5=Button(aken, text="lopetamine", font="Arial 24",relief=RAISED,command=end)



ob=[btn1,btn2,btn3,btn4,btn5]
for i in range(len(ob)):
    ob[i].pack()
aken.mainloop()