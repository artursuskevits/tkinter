from tkinter import *
k=0
k2=0
def klikker(event):
    global k
    k+=1
    btn.configure(text=k)
    if k> 20:
        k+=5
        if k >= 100:
            k=0
            btn2.pack()
            btn2.bind("<Button-1>",klikker3)
    if k%2==0:
        tahvel.itemconfig(img_cast,image=img2)
    else:
        tahvel.itemconfig(img_cast,image=img)


def klikker2(event):
    global k
    k-=5
    btn.configure(text=k)

def klikker3(event):
    global k2
    k2+=15
    btn2.configure(text=k2)

def text_to_lbl(event):
    t=ent.get()
    lbl.configure(text=t)
    ent.delete(0,END)

def valik():
    val=var.get()
    ent.insert(END,val)

def checklist_to_l(event):
    v1=var1.get()
    v2=var2.get()
    jarjend=[v1,v2]
    l.delete(0,1)#read.
    for item in jarjend:
        l.insert(END,item)


aken=Tk()
#aken.geometry("800x600")
aken.title("Minu esimine aken")
aken.iconbitmap("images.ico")
f=Frame(aken,bg="lightblue")

lbl=Label(f,text="kliker",bg="yellow",fg="#7465b8",font="times_new_roman 20",height=2,width=40)
btn=Button(f, text="Vajuta siia", font="Arial 24",relief=RAISED) #SUNKEN, RAISED, GROOVE
ent=Entry(f,fg="blue",bg="lightblue",width=15,font="Arial 20", justify=CENTER)

var=IntVar() #StringVar()
r1=Radiobutton(f,text="Esimine",bg="white",font="Arial 20",variable=var, value=1,command=valik)
r2=Radiobutton(f,text="Teine",bg="white",font="Arial 20",variable=var, value=2,command=valik)
r3=Radiobutton(f,text="Kolmas",bg="white",font="Arial 20",variable=var, value=3,command=valik)
var1=StringVar()
var2=StringVar()
c1=Checkbutton(f, text="Esimene",font="Arial 20",variable=var1,onvalue="Esimine on valitud", offvalue="Esimine on peidetud")
c2=Checkbutton(f, text="Teine",font="Arial 20",variable=var2,onvalue="Teine on valitud", offvalue="Teine on peidetud")
l=Listbox(f,height=2,width=20)
tahvel=Canvas(aken,width=260,height=260,bg="white")
img=PhotoImage(file="hello-kitty-icon-29.png")
img2=PhotoImage(file="images.png")
img_cast=tahvel.create_image(2,2,image=img,anchor=NW)
#tahvel.create_image(256,2,image=img2,anchor=NW)

btn2=Button(f, text=k, font="Arial 24",relief=RAISED)
btn.bind("<Button-1>",klikker)#lkm
btn.bind("<Button-2>",checklist_to_l)#lkm
btn.bind("<Button-3>",klikker2)#pkm)
ent.bind("<Return>",text_to_lbl)#Enter
c1.deselect()
c2.deselect()
ob=[lbl,btn,ent,r1,r2,r3,l,c1,c2]
for i in range(len( ob)):
    ob[i].pack()
f.grid(row=0, column=0)
tahvel.grid(row=0, column=1)

aken.mainloop()
