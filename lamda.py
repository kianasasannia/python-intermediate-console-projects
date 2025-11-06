
x = lambda a : a + 10
print(x(13))

double = lambda x: x * 2
print(double(28))

x = lambda a, b : a * b
print(x(5, 6))

#example
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 != 0) , my_list))

print(new_list)

# Program to double each item in a list using map()
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2 , my_list))
print(new_list)

