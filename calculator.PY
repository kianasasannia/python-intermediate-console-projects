def calculater(num1 , operator, num2):      
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":     
        result = num1 / num2
    elif operator == "%":     
        result = num1 % num2
    elif operator == "^":     
        result = num1 ** num2

    else:
        result = "The operator is not valid!"
    
    print(result)

# function call
try:
    num1 = int(input("Please Enter Number1: "))
    operator = input("Please Enter the operator(+ - * /): ")
    num2 = int(input("Please Enter Number2: "))

except:
    print("Something went wrong!")    
else:
    calculater(num1, operator, num2)






























