#positional_argument
def say_hello(username, status):

  print(f'Hello {username} your status is: {status}')

say_hello("Alice", "developer")

say_hello("Mark", "manager")

def say_hello(username, status):

  print(f'Hello {username} your status is: {status}')

say_hello("developer", "Alice")
say_hello("manager", "Mark")

#keyword argument

def say_hello(username, status):

  print(f'Hello {username} your status is: {status}')

say_hello(status="developer", username="Alice")

say_hello(status="manager", username="Mark")

say_hello(status="PR", username="Tylor")

def Factorial(N:int):
    if N == 0 or N == 1:
        F = 1
    else:
        F = 1
        for i in range(1, N+1):
            F *= i
    print(F)        
    return F

Factorial(5)

def average( *vals ):
    total = 0
    for v in vals:
        total += v
    return total/len(vals)

a=average(14,80,54)
print(a)



def add( a, b ):
    return a + b

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
result = add(a,b)
print(result)

##docstring
def sum(num1, num2):

  '''

  This function adds two numbers together

  '''

  return num1 + num2

sum()

help(sum)

##even_number

def even_number(num_list):
  even=[]
  for x in num_list:
    if(x%2==0):
      even.append(x)
    else:
      pass
  return even
      
print(even_number([3,6,8,9,5]))



