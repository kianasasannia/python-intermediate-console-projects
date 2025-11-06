import os
import random
a=True
s1=0
s2=0
while a:
    p1=input("choose r ,p ,s ?")
    os.system("cls")
    p2=input("choose r ,p ,s ?")
    os.system("cls")
    if p1=="r" and p2=="s" or p1=="p" and p2=="r" or p1=="s" and p2 =="p":
        s1+=1
        print("player one wins\n","scores: Player one-->",s1,"Computer-->",s2)
    elif p1==p2:
        print("tie\n","scores: Player one-->",s1,"Computer-->",s2)
    else:
        s2+=1
        print("Computer wins\n","scores: Player one-->",s1,"Computer",s2)
    if s1==2 or s2==2:
        a=False

a=True
s1=0
s2=0
while a:
    l=["r","p","s"]
    p2=random.choice(l)
    p1=input("choose r ,p ,s ?")
    if p1=="r" and p2=="s" or p1=="p" and p2=="r" or p1=="s" and p2 =="p":
        s1+=1
        os.system("cls")
        print("player one wins\n","computer choise:",p2,"\nscores: Player one-->",s1,"Computer-->",s2)
    elif p1==p2:
        os.system("cls")
        print("tie\n","computer choise:",p2,"\nscores: Player one-->",s1,"Computer-->",s2)
    else:
        s2+=1
        os.system("cls")
        print("Computer wins\n","computer choise:",p2,"\nscores: Player one-->",s1,"Computer",s2)
    if s1==2 or s2==2:
        a=False
