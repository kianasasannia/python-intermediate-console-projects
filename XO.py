from random import shuffle
l=["X","X","O","X"]
shuffle(l)
i= int(input("choose 1 , 2 , 3 , 4:"))
if l[i-1]=="O":
    print("you win :D\n",l)
else:
    print("you lose :(\n",l)

