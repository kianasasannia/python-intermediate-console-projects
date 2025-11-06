##normal
list=[2,4,1,3,5]
total=0
for item in list:
    total+=item
total=total/len(list)
print(total)

##function
def avr_list(list):
    total=0
    for item in list:
         total+=item
    total=total/len(list)
    return total

print(avr_list([2,4,1,3,5]))
