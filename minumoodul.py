from random import*
from tkinter import*
def test(sonastik:dict,sonastik2:dict,nimi:str,koik:list):
    answer_list=[]
    oige=0
    for jj in range(5):
        answer_list.clear()
        question=choice(list(sonastik))
        answer_list.append(str(sonastik[question]))
        for jj2 in range(3):
            answer=choice(list(sonastik2))
            answer_list.append(answer)
        print(f"{nimi} {jj+1} kusimus on {question}")
        print('\n'.join(answer_list))
        user_answer=int(input("vali oige vastus, sisetades numbrid 1-4"))
        shuffle(answer_list)
        if str(answer_list[user_answer-1]) == str(sonastik[question]):
            oige +=1
            print("Oige vastus!")
            sonastik.pop(question)
        else:
            print("Vale vastus.")
            sonastik.pop(question)
    print(f"{nimi} sinu resultat on {oige}/5")
    koik.append((f'{nimi}',f"{oige}"))
    print(koik)
    koik.sort(key=lambda a: a[1])
    koik.reverse()
    print(koik)
    return koik

def kirjutafaeli(list:list,file:str):
    f=open(file,"w",encoding="utf-8-sig")
    for line in list:
        f.write(str(line)+"\n")
    f.close()
    return file

def sorter(koik:list,vastuvoetud:list,eisoobi:list,koikfail:str,vastuvoetudfail:str,eisoobifail:str):
    koiklen = len(koik)
    kirjutafaeli(koik,koikfail)
    if koiklen >= 5:
        for jj in range (koiklen):
            if koik[jj][1] <(koik[4][1]):
                eisoobi.append(koik[jj])
                eisoobi.sort(key=lambda a: a[0])

            else:
                vastuvoetud.append(koik[jj])
    kirjutafaeli(eisoobi,eisoobifail)
    kirjutafaeli(vastuvoetud,vastuvoetudfail)
    return vastuvoetud,eisoobi, koikfail,vastuvoetudfail,eisoobifail

def loe_faelist(newlist:list,fail:str):
    f=open(fail,"r",encoding="utf-8-sig")
    for rida in f:
        k, v = rida.strip().split(",")
        rida=rida[1:-1]
        k = k.strip("'")
        v=v[:-2]
        v=v[2:]
        k=k[2:]
        newlist.append((k, v))
    f.close()
    return newlist

def printfile(fail:str):
    f=open(fail,"r",encoding="utf-8-sig")
    lines=f.readlines()
    for line in lines:
        print(line.strip())
    f.close

def txttodictionary(dictionary:dict,dictionary2:dict,fail:str):
    f=open(fail, "r", encoding="utf-8-sig")
    for line in f:
        k, v=line.strip().split("-")
        dictionary[k.strip()] = v.strip()
        f=open("vastus.txt", "r", encoding="utf-8-sig")
    for line in f:
        k, v=line.strip().split("-")
        dictionary2[v.strip()] = k.strip()
        f=open("vastus.txt", "r", encoding="utf-8-sig")
    
