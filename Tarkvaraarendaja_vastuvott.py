from minumoodul import *
from tkinter import*
from random import*
import time
import datetime

sonastik={}
sonastik2={}
koik=[]
vastuvoetud=[]
eisoobi=[]
txttodictionary(sonastik,sonastik2,"vastus.txt")

def leave(newaken):
    newaken.destroy()

def testvisual():
    akenfortest=Toplevel()
    akenfortest.geometry("1920x1080")
    akenfortest.title("Test")
    akenfortest.iconbitmap("images.ico")
    quetionlbl=Label(akenfortest, text="do you want to do a test?", font="Arial 24")
    timerlbl=Label(akenfortest,  font="Arial 24")
    testbutton1=Button(akenfortest,  font="Arial 10",relief=RAISED,command=leave)
    testbutton2=Button(akenfortest, font="Arial 10",relief=RAISED,command=leave)
    testbutton3=Button(akenfortest, font="Arial 10",relief=RAISED,command=leave)
    testbutton4=Button(akenfortest,  font="Arial 10",relief=RAISED,command=leave)
    a_list=[]
    oige=0
    questioncounter=0
    
    questioncounter+=1
    a_list.clear()
    question=choice(list(sonastik))
    quetionlbl.configure(text=f"{questioncounter}. {question}")
    a_list.append(str(sonastik[question]))
    for jj2 in range(3):
        answer=choice(list(sonastik2))
        a_list.append(answer)
    #user_answer=int(input("vali oige vastus, sisetades numbrid 1-4"))
    answer_list=a_list
    print(answer_list)
    print(len(answer_list))
    texttobutton=choice(answer_list)
    testbutton1.configure(text=f"{texttobutton}")
    answer_list.remove(texttobutton)
    texttobutton=choice(answer_list)
    testbutton2.configure(text=f"{texttobutton}")
    answer_list.remove(texttobutton)
    texttobutton=choice(answer_list)
    testbutton3.configure(text=f"{texttobutton}")
    answer_list.remove(texttobutton)
    texttobutton=choice(answer_list)
    testbutton4.configure(text=f"{texttobutton}")
    answer_list.remove(texttobutton)
    akenfortest.update()
     
    quetionlbl.pack()
    testbutton1.pack()
    testbutton2.pack()
    testbutton3.pack()
    testbutton4.pack()
    akenfortest.update()

    total_seconds = 30
    while total_seconds > 0:
        timer = datetime.timedelta(seconds = total_seconds)
        timerlbl.configure(text=str(timer))
        timerlbl.pack()
        akenfortest.update()
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1
    
    #    if str(answer_list[user_answer-1]) == str(sonastik[question]):
    #        oige +=1
    #        print("Oige vastus!")
    #        sonastik.pop(question)
    #    else:
    #        print("Vale vastus.")
    #        sonastik.pop(question)
    #print(f"{nimi} sinu resultat on {oige}/5")
    #koik.append((f'{nimi}',f"{oige}"))
    #print(koik)
    #koik.sort(key=lambda a: a[1])
    #koik.reverse()
    #print(koik)

def first_user_choose(testent):
    if testent.get() != "":
        name=testent.get
        newaken=Toplevel()
        newaken.geometry("500x500")
        newaken.title("Test")
        newaken.iconbitmap("images.ico")
        namelbl=Label(newaken, font="Arial 24")
        questionlbl=Label(newaken, text="do you want to do a test?", font="Arial 24")
        testbutton=Button(newaken, text="take a test", font="Arial 24",relief=RAISED,command=testvisual)
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

koik = loe_faelist(koik,"koik.txt")
print(koik)


    

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




