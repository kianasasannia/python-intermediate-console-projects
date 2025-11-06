
s=input("enter a number: ")
try:
    i=int(s)
    print("valid",i)
except ValueError as err:
    print(err)


print("num:")
t=0
c=0
while True :
    line=input("enter a num: ")
    if line:
        try:
            num=int(line)
        except ValueError as err:
            print(err)
            continue
        t+=num
        c+=1
    else:
        break

import random
x=random.randint(1,6)
y=random.choice(['a','b'])
print(x,y)
