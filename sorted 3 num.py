a=int(input("enter the first number : ")) #12
b=int(input("enter the second number : ")) #5
c=int(input("enter the third number : ")) #8
if a >b:
    temp= a  #temp=12
    a=b       #a=5
    b=temp     # b=12

if a>c:
    temp= a  #temp= 12
    a=c     #a=8
    c=temp  #c=12

if b>c:
    temp=b
    b=c
    c=temp

print("sorted : ",a, b,c)

