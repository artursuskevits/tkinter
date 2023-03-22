
from minumoodul import *
from tkinter import*
from random import*

global sonastiklist
sonastik={}
sonastik2={}
deleatefromtest={}
koik=[]
vastuvoetud=[]
eisoobi=[]
sonastiklist = list(sonastik)
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
        if not hasattr(countdown_timer, 'timer_id'):
            countdown_timer.timer_id = None
        else:
            timerlbl.after_cancel(countdown_timer.timer_id)
        countdown_timer.timer_id = timerlbl.after(1000, countdown_timer) 
    else:
        timerlbl.config(text="Time's up!")
        choice_question()


def rese_timer():
    global time_remaining
    time_remaining=0

def choice_question():
    global sonastiklist
    print(sonastiklist)
    global strforlbl
    global oige
    rese_timer()
    global time_remaining
    time_remaining=100
    countdown_timer()
    global global_attempta
    global question
    global resultaken
    global_attempta+=1
    if global_attempta <=9 :
        a_list=[]
        sonastiklist=list(sonastik)
        question=choice(sonastiklist)
        quetionlbl.configure(text=f"{global_attempta}. {question}")
        a_list.append(str(sonastik[question]))
        for jj2 in range(3):
            answer=choice(list(sonastik2))
            a_list.append(answer)
        sonastiklist.remove(question)
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
        vastuvoetud_string="".join([
            ""
            if item == "(" or item == ")" or item == "'" or item ==","
            else item 
            for item in vastuvoetud_string
        ])
        print(vastuvoetud_string)
        akenfortest.destroy()
        resultaken=Toplevel()
        resultaken.title("Test")
        resultaken.iconbitmap("images.ico")
        resultaken.state('zoomed')
        resultaken.configure(bg='#6d6875')
        leavebtn=Button(resultaken, text="leave", font="Arial 40",command=newleave,bg="#b5838d")
        oigelbl=Label(resultaken, font="Arial 50 bold",bg='#6d6875',text=f"{strforlbl} your result is {oige}/9")
        accepted_list=Label(resultaken, font="Arial 40",bg='#fca311')
        tahvel3=Canvas(resultaken,width=100,height=100,bg="white")
        tahvel3.create_image(1,1,image=img,anchor=NW)
        oigelbl.configure()
        accepted_list.configure(text=f"VASTUVOETUD ON: {vastuvoetud_string}")
        oigelbl.place(relx = 0.5, rely = 0.1, anchor = CENTER)
        accepted_list.place(relx = 0.5, rely = 0.55, anchor = CENTER)
        leavebtn.place(relx = 0.5, rely = 0.9, anchor = CENTER)
        tahvel3.place(anchor = NW)
        
        
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
    akenfortest.configure(bg='#6d6875')
    quetionlbl=Label(akenfortest, text="do you want to do a test?", font="Arial 40 bold",bg="#6d6875")
    timerlbl=Label(akenfortest,text="Good Luck!",  font="Arial 40 bold",bg="#6d6875")
    newaken.destroy()
    testbutton1=Button(akenfortest,  font="Arial 17",relief=RAISED,command=lambda:[check_answer(testbutton1),choice_question()],height= 4, width=70,wraplength=600, justify=CENTER,bg="#fca311")
    testbutton2=Button(akenfortest, font="Arial 17",relief=RAISED,command=lambda:[check_answer(testbutton2),choice_question()],height= 4, width=70, wraplength=600,justify=CENTER,bg="#ffcdb2")
    testbutton3=Button(akenfortest, font="Arial 17",relief=RAISED,command=lambda:[check_answer(testbutton3),choice_question()],height= 4, width=70,wraplength=600, justify=CENTER,bg="#ffb4a2")
    testbutton4=Button(akenfortest,  font="Arial 17",relief=RAISED,command=lambda:[check_answer(testbutton4),choice_question()],height= 4, width=70,wraplength=600, justify=CENTER,bg="#e5989b")
    tahvel3=Canvas(akenfortest,width=100,height=100,bg="white")
    tahvel3.create_image(1,1,image=img,anchor=NW)
    if global_attempta <= 5:
        answer_list = choice_question()
       
        tahvel3.place(anchor = NW)
        akenfortest.update()
        timerlbl.place(relx = 0.2, rely = 0.1, anchor = CENTER)
        quetionlbl.place(relx = 0.5, rely = 0.1, anchor = CENTER)
        testbutton1.place(relx = 0.25, rely = 0.4, anchor = CENTER)
        testbutton2.place(relx = 0.75, rely = 0.4, anchor = CENTER)
        testbutton3.place(relx = 0.25, rely = 0.6, anchor = CENTER)
        testbutton4.place(relx = 0.75, rely = 0.6, anchor = CENTER)
        akenfortest.update()


def first_user_choose(testent,testaken):
    
    global strforlbl
    if testent.get() != "":
        name=testent.get
        newaken=Toplevel()
        newaken.geometry("600x600+200+100")
        newaken.title("Test")
        newaken.iconbitmap("images.ico")
        newaken.configure(bg='#6d6875')
        strforlbl=testent.get()
        questionlbl=Label(newaken, text=f"{strforlbl} kas soovite teha testi?", font="Times_New:_Roman 30 bold",bg="#6d6875")
        testbutton=Button(newaken, text="Teha test", font="Arial 24",relief=RAISED,command=lambda:testvisual(newaken,testaken),bg="#b5838d")
        leavebutton=Button(newaken, text="Jata", font="Arial 24",relief=RAISED,command=lambda:leave(newaken,testaken),bg="#b5838d")
        tahvel2=Canvas(newaken,width=100,height=100,bg="white")
        tahvel2.create_image(1,1,image=img,anchor=NW)
        questionlbl.place(relx = 0.5, rely = 0.3, anchor = CENTER)
        testbutton.place(relx = 0.3, rely = 0.5, anchor = CENTER)
        leavebutton.place(relx = 0.7, rely = 0.5, anchor = CENTER)
        tahvel2.place(anchor = NW)
    else:
        testent.configure(bg="red")
    

        


global testaken
testaken=Tk()
testaken.geometry("600x600+200+100")
testaken.title("Test")
testaken.iconbitmap("images.ico")
testaken.configure(bg='#6d6875')

terelbl=Label(testaken,text="Tere!",font="Times_New_Roman 36 bold",bg="#6d6875")
testlbl=Label(testaken,text="Palun, kirjuta sinu nimi",font="Arial 34",bg="#6d6875")
testent=Entry(testaken,fg="blue",bg="lightblue",width=15,font="Arial 20",background="#b5838d",foreground="black", justify=CENTER)
testbtn=Button(testaken, text="Alustada", font="Arial 24",relief=RAISED,command=lambda:first_user_choose(testent,testaken),bg="#b5838d")
tahvel=Canvas(testaken,width=100,height=100,bg="white")
img=PhotoImage(file="tthk.png")
img_cast=tahvel.create_image(1,1,image=img,anchor=NW)

terelbl.place(relx = 0.5, rely = 0.15, anchor = CENTER)
testlbl.place(relx = 0.5, rely = 0.35, anchor = CENTER)
testent.place(relx = 0.5, rely = 0.5, anchor = CENTER)
testbtn.place(relx = 0.5, rely = 0.6, anchor = CENTER)
tahvel.place(anchor = NW)
testaken.mainloop()

koik = loe_faelist(koik,"koik.txt")


    

#nimi=input("kirjuta siinu eesnimi ja perenimi ")
#menu=int(input(f"{nimi} te soovite testi teha, \n1-yah \n2-ei"))
#if menu==1:
#    koik=test(sonastik,sonastik2,nimi,koik)
    
#if menu==2:
#    sorter(koik,vastuvoetud,eisoobi,"koik.txt","vastuvoetud.txt","eisoobi.txt")

    
#print("Vastuvoetud:")
#printfile("vastuvoetud.txt")
#print("eisoobi:")
#printfile("Eisoobi.txt")




