from minumoodul import *
from tkinter import*

def leave(newaken):
    newaken.destroy()


def first_user_choose(testent):
    if testent.get() != "":
        name=testent.get
        newaken=Toplevel()
        newaken.geometry("500x500")
        newaken.title("Test")
        newaken.iconbitmap("images.ico")
        namelbl=Label(newaken, font="Arial 24")
        questionlbl=Label(newaken, text="do you want to do a test?", font="Arial 24")
        testbutton=Button(newaken, text="take a test", font="Arial 24",relief=RAISED,command=lambda:first_user_choose)
        leavebutton=Button(newaken, text="leave", font="Arial 24",relief=RAISED,command=lambda:leave(newaken))
        strforlbl=testent.get()
        print(strforlbl)
        namelbl.configure(text=f"hello {strforlbl}")
        namelbl.pack()
        questionlbl.pack()
        testbutton.pack()
        leavebutton.pack()
    else:
        testent.configure(bg="red")
    




testaken=Tk()
testaken.geometry("450x450")
testaken.title("Test")
testaken.iconbitmap("images.ico")


testlbl=Label(testaken,text="Kirjuta sinu nimi",font="Arial 24")
testent=Entry(testaken,fg="blue",bg="lightblue",width=15,font="Arial 20", justify=CENTER)
testbtn=Button(testaken, text="registreerimine", font="Arial 24",relief=RAISED,command=lambda:first_user_choose(testent))

testlbl.pack()
testent.pack()
testbtn.pack()
testaken.mainloop()
sonastik={}
sonastik2={}
koik=[]
vastuvoetud=[]
eisoobi=[]
koik = loe_faelist(koik,"koik.txt")
print(koik)


    
txttodictionary(sonastik,sonastik2,"vastus.txt")
nimi=input("kirjuta siinu eesnimi ja perenimi ")
menu=int(input(f"{nimi} te soovite testi teha, \n1-yah \n2-ei"))
if menu==1:
    koik=test(sonastik,sonastik2,nimi,koik)
    sorter(koik,vastuvoetud,eisoobi,"koik.txt","vastuvoetud.txt","eisoobi.txt")
if menu==2:
    sorter(koik,vastuvoetud,eisoobi,"koik.txt","vastuvoetud.txt","eisoobi.txt")

    
print("Vastuvoetud:")
printfile("vastuvoetud.txt")
print("eisoobi:")
printfile("Eisoobi.txt")




