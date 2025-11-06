def histogram (items):
    for n in items:
        result = ""
        times = n
        while times>0:
            result+= "*"
            times=times-1
        print(result)

histogram([20,3,1,13])
        
