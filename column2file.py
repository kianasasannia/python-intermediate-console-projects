f=open("f.txt")
l=f.readlines()
f.close()

f1=open("f.txt")
for x in range(len(l)):
    s=f1.readline()
    l2=s.split()
    print(l2[len(l2)-1])


