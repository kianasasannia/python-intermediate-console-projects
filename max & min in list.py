list=[5,2,15,6,3,17,58,35]
max=0
min=list[0]
for item in list:
    if(item<min):
        min=item
    if(item>max):
        max=item

print(min,max)

def min_max(list):
    max=0
    min=list[0]
    for item in list:
        if(item<min):
            min=item
        if(item>max):
            max=item
    return max ,min

print(min_max([5,2,15,6,3,17,58,35]))
