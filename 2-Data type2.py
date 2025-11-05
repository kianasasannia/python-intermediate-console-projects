##tuple
my_tuple = (27, "new", 2.821, 9)
empty_tuple = ()
single_tuple = (27,)  # , is necessary!
tpl = (17, 14, 20,5,19,341,963)
print( tpl[2] )
print( tpl[3:7] )

tuple1 = ( "Test", "Element" )
tuple2 = ( 11, 37, 23 )
tuple3 = tuple1 + tuple2
print( tuple3 )

##set
num_set = {17, 81, 4, 11}
num_set.remove(4)
print(num_set)
str_set = {"alice", "mark", "sam"}


print( "alice" in str_set )

lst = ["New york", "Tehran", "Los vegas", "Vashangton"]
cities = set(lst)
print(cities)


site_name = "www.github.com"
site_chars = set(site_name)
print(site_chars)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

A_union_B = A | B
print(A.union(B))
print( A - B )
print( A.difference(B))
print( A & B )
print( A.intersection(B))
##dictionary

person  = {
    "name": "harry",
    "job": "graphist",
    "car": "BMW x6",
    "age": 24,
    "code": 134
}

person["age"] = 23
person["age"] = person["age"] + 1
person["mobile"] = "Samsung S25"
print( person )
person.clear() # delete all keys in Dictionary
print( person )

