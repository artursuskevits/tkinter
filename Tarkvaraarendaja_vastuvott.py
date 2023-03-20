from typing import ItemsView
from minumoodul import *
from tkinter import*
from random import*

sonastik={}
sonastik2={}
koik=[]
vastuvoetud=[]
eisoobi=[]
global_attempta=0
txttodictionary(sonastik,sonastik2,"vastus.txt")
koik = loe_faelist(koik,"koik.txt")


def check_answer(button):
    global oige
    answer = button["text"]
    
    check = str(sonastik[question])
    if str(answer) == str(check):
        oige+=1
    else:
        oige=oige
        

   

def countdown_timer():
    global time_remaining
    if time_remaining > 0:
        time_remaining -= 1
        timerlbl.config(text=f"{time_remaining}")
        timerlbl.after(1000, countdown_timer) # call this function again in 1 second
    else:
        timerlbl.config(text="Time's up!")

def rese_timer():
    global time_remaning
    time_remaning=0

def choice_question():
    global strforlbl
    global oige
    rese_timer()
    global time_remaining
    time_remaining=30
    countdown_timer()
    global global_attempta
    global question
    global resultaken
    global_attempta+=1
    if global_attempta <=5 :
        a_list=[]
        question=choice(list(sonastik))
        quetionlbl.configure(text=f"{global_attempta}. {question}")
        a_list.append(str(sonastik[question]))
        for jj2 in range(3):
            answer=choice(list(sonastik2))
            a_list.append(answer)
        #user_answer=int(input("vali oige vastus, sisetades numbrid 1-4"))
        answer_list=a_list 
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
        return answer_list
    else:
        vastuvoetud_string=""
        koik.append((f'{strforlbl}',f"{oige}"))
        sorter(koik,vastuvoetud,eisoobi,"koik.txt","vastuvoetud.txt","eisoobi.txt")
        for tuple in vastuvoetud:
            vastuvoetud_string += str(tuple) + " "
        vastuvoetud_string="".join([
            "\n" + item
            if item == "("
            else item 
            for item in vastuvoetud_string
        ])
        print(vastuvoetud_string)
        akenfortest.destroy()
        resultaken=Toplevel()
        resultaken.title("Test")
        resultaken.iconbitmap("images.ico")
        resultaken.state('zoomed')
        leavebtn=Button(resultaken, text="leave", font="Arial 24",command=newleave)
        oigelbl=Label(resultaken, font="Arial 24")
        accepted_list=Label(resultaken, font="Arial 24")
        oigelbl.configure(text=f"{strforlbl} your result is {oige}/5")
        print(vastuvoetud_string)
        accepted_list.configure(text=f"vastuvoetud on {vastuvoetud_string}")
        oigelbl.pack()
        accepted_list.pack()
        leavebtn.pack()
        
        
def newleave ():
    resultaken.destroy()
    testaken.destroy()

def leave(newaken,testaken):
    newaken.destroy()
    testaken.destroy()


def testvisual(newaken,testaken):

    
    global akenfortest
    global testbutton1
    global testbutton2
    global testbutton3
    global testbutton4
    global timerlbl
    global quetionlbl
    global global_attempta
    global oige
    global_attempta = 0
    oige=0
    
    
    akenfortest=Toplevel()
    akenfortest.geometry("1920x1080")
    akenfortest.state('zoomed')
    akenfortest.title("Test")
    akenfortest.iconbitmap("images.ico")
    quetionlbl=Label(akenfortest, text="do you want to do a test?", font="Arial 24")
    timerlbl=Label(akenfortest,text="Good Luck!",  font="Arial 24")
    newaken.destroy()
    testbutton1=Button(akenfortest,  font="Arial 10",relief=RAISED,command=lambda:[check_answer(testbutton1),choice_question()])
    testbutton2=Button(akenfortest, font="Arial 10",relief=RAISED,command=lambda:[check_answer(testbutton2),choice_question()])
    testbutton3=Button(akenfortest, font="Arial 10",relief=RAISED,command=lambda:[check_answer(testbutton3),choice_question()])
    testbutton4=Button(akenfortest,  font="Arial 10",relief=RAISED,command=lambda:[check_answer(testbutton4),choice_question()])
    answer_list=[]
    questioncounter=0
    if global_attempta <= 5:
        answer_list = choice_question()
       

        akenfortest.update()
        timerlbl.pack()
        quetionlbl.pack()
        testbutton1.pack()
        testbutton2.pack()
        testbutton3.pack()
        testbutton4.pack()
        akenfortest.update()


def first_user_choose(testent,testaken):
    
    global strforlbl
    if testent.get() != "":
        name=testent.get
        newaken=Toplevel()
        newaken.geometry("500x500")
        newaken.title("Test")
        newaken.iconbitmap("images.ico")
        namelbl=Label(newaken, font="Arial 24")
        questionlbl=Label(newaken, text="do you want to do a test?", font="Arial 24")
        testbutton=Button(newaken, text="take a test", font="Arial 24",relief=RAISED,command=lambda:testvisual(newaken,testaken))
        leavebutton=Button(newaken, text="leave", font="Arial 24",relief=RAISED,command=lambda:leave(newaken,testaken))
        strforlbl=testent.get()
        namelbl.configure(text=f"hello {strforlbl}")
        questionlbl.pack()
        namelbl.pack()
        testbutton.pack()
        leavebutton.pack()
    else:
        testent.configure(bg="red")
    

        


global testaken
testaken=Tk()
testaken.geometry("450x450")
testaken.title("Test")
testaken.iconbitmap("images.ico")


testlbl=Label(testaken,text="Kirjuta sinu nimi",font="Arial 24")
testent=Entry(testaken,fg="blue",bg="lightblue",width=15,font="Arial 20", justify=CENTER)
testbtn=Button(testaken, text="alustada", font="Arial 24",relief=RAISED,command=lambda:first_user_choose(testent,testaken))

testlbl.pack()
testent.pack()
testbtn.pack()
testaken.mainloop()

koik = loe_faelist(koik,"koik.txt")


    

nimi=input("kirjuta siinu eesnimi ja perenimi ")
menu=int(input(f"{nimi} te soovite testi teha, \n1-yah \n2-ei"))
#if menu==1:
#    koik=test(sonastik,sonastik2,nimi,koik)
    
#if menu==2:
#    sorter(koik,vastuvoetud,eisoobi,"koik.txt","vastuvoetud.txt","eisoobi.txt")

    
print("Vastuvoetud:")
printfile("vastuvoetud.txt")
print("eisoobi:")
printfile("Eisoobi.txt")




