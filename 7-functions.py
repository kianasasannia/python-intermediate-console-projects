def my_function():
  print("Hello from a function")

my_function() #calling

def welcome(fname):
  print( "welcome "+fname)

welcome("alice")
welcome("mark")
welcome("harry")

def fullname(fname, lname):
  print(fname + " " + lname)

fullname("john", "gray")

def youngest(*kids):
  print("The youngest child is " + kids[2])

youngest("alice", "merry", "john","mark","tylor")

def my_function2(country = "Iran"):
  print("I am from " + country)

my_function2("India")
my_function2()
my_function2("Brazil")

def multiple5(x):
  return 5 * x

print(multiple5(3))
print(multiple5(5))
print(multiple5(9))

def my_pow(x,y):
     print( x**y)

a=2
b=3
my_pow(a,b)
















