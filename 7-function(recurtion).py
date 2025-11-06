def sum(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sum(list[1:])


print(sum([5, 7, 3, 8, 10]))

"""

sum([5, 7, 3, 8, 10])
5 + sum([7, 3, 8, 10])
5 + 7 + sum([3, 8, 10])
5 + 7 + 3 + sum([8, 10])
5 + 7 + 3 +  8 + sum([10])
5 + 7 + 3 +  8 + 10
5 + 7 + 3 +  18
5 + 7 + 21
5 + 28
33

"""

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(4)


"""
tri_recursion(6) 
 = 6 + tri_recursion(5) 
 = 6 + 5 + tri_recursion(4)
 = 6 + 5 + 4 + tri_recursion(3)
 = 6 + 5 + 4 + 3 + tri_recursion(2)
 = 6 + 5 + 4 + 3 + 2 + tri_recursion(1)
 = 6 + 5 + 4 + 3 + 2 + 1 + tri_recursion(0)

 """


"""

Recursion Example Results
                         start loop k 6
                     start loop k 5
                 start loop k 4
             start loop k 3
         start loop k 2
     start loop k 1
i reached when k = 0
 end loop 0
     i am k( 1 )+previous result( 0 )= 1
     end loop 1
         i am k( 2 )+previous result( 1 )= 3
         end loop 2
             i am k( 3 )+previous result( 3 )= 6
             end loop 3
                 i am k( 4 )+previous result( 6 )= 10
                 end loop 4
                     i am k( 5 )+previous result( 10 )= 15
                     end loop 5
                         i am k( 6 )+previous result( 15 )= 21
                         end loop 6

"""