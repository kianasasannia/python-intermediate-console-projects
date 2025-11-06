f=open("text.txt")
print(f.read(10))
print(f.readline())
list1=f.readlines()
print(list1[3])
print(f.readable())

f1=open("asghar2.txt","w")
f1.write("hello\n")

f1=open("asghar2.txt","a")
f1.write("hello\n","a1212")

u=input("enter your username: ")
p=input("enter your password: ")

f=open("info.txt",'w')
f.write(u+"\n"+p)

try:
    f=open("info1.txt",'x')
except FileExistsError:
    print("this username exist")
    print("do you have an account?")
    a=input("yes / no")
    if a=="no":
        print("ple")
    else:
        input("login:")

print("login: ")
u=input("enter your username: ")
p=input("enter your password: ")

f=open("info.txt")
l1=f.readline().split("\n")[0]
l2=f.readline()

if u==l1 and p== l2:
    print("welcome")
else:
    print("wrong")

f=open("info.txt")
list1=f.readlines()

for x in list1:
    n=x.split()
    print(n[0])

with open("info.txt",'r') as f:  #f=open("info.txt",'r')
    list1=f.readlines()
    list1.reverse()
    print(list1)

l=['apple','banana','peach','pear','cherry','grape']
last=0
for _ in l:
    last+=1
    print(last)
for _ in range(last):
    last-=1
    print(l[last])
    