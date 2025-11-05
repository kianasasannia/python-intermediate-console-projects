##int
number=5
n=28
N=0
complex = 5+3j
print(number,n,N,complex)

q=w=e = 17
print(q,w,e)

print(number+n)
print(number*n)
print(number * 5)
print(number**3)
print(type(n))
print((float(n)))

##float
f=21.5
o=19.456
x=8e5
print(f,o,x)

p1,p2,p3,n1 = 'mark','jack','alice',13
print(p1,p2,p3,n1)

print(f+o)
print(type(o))
print(int(o))

##string
text='hello'
i="wlecome  "
p="""
this is a 
multiline
 text """
print(text,i,p)

##Type casting
print("hi"+str(15))
print(text+str(8))
print(i+str(number))

##format
b="test{}"
print(b.format(n))

print(text+i)

##length
print(len(i))

##pow
print(i*3)

##index
print(i[3]) 
print(i[1:4])
print(i[-4:-2])

##find
print(text.find("e"))
print(text.upper()) #lower() 

##delete extra spaces
print(i.strip())

print(text.replace('e','a'))

##exsist
print("text" in p) #boolean

##del text
print(text) #Error

print(p.split())

##Boolean
print(10>8) 
print(2>100)
print(4==9)
print(bool('hi'))
print(bool(0))
print(isinstance(n,int))

##list
list=['a','b','c']
print(list)
print(len(list))
list2=['hi',39,True,4.67]
print(list2)

list.remove('a')
print(list)

list[2]='h'
print(list)

list.insert(2,'y')
print(list)
