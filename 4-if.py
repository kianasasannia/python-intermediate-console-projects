##if
a = 33
b = 200
if b > a:
  print("b is greater than a")

##if_else
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

##elif
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

##one_line_if
if a > b: print("a is greater than b")

##And
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

##Or
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

##Pass
a = 33
b = 200

if b > a:
  pass

##nested_if
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


m='male'
f='female'
ad='adult'
t='teenager'

input='male'
age=28

if(input=='male'):
    if(age<=18):
        print("you are a teenage Boy")
    else:
        print('you are an adult male')

elif(input=="female"):
    if(age<=18):
        print("you are a teenage girl")
    else:
        print('you are an adult female')
else:
    print('the input that you entered is wrong!')
