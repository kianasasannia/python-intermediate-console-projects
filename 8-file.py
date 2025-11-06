import os 

f = open("demofile.txt")
print(f.read())

f = open("demofile.txt", "r")
print(f.read(30))

f=open("f.txt","r")
print(f.readable())

f = open("f.txt", "r")
print(f.readline())

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

f = open("demofile.txt", "r")
for x in f:
  print(x)

f = open("demofile.txt", "r")
print(f.readlines())
f.close()

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

f = open("demofile2.txt", "r")
print(f.read())

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())

f = open('demofile3.txt', "w")
f.writelines( ["hello world!\n", "test line",'\n salam asghar'] )
f.close()

f = open("myfile.txt", "x")
f = open("myfile.txt", "w")

with open("demofile3.txt") as f:  #f = open('demofile3.txt', "r")
  data =f.read()
  
