def Read_Two_Column_File(file_name):
    data  = open(file_name, 'r')
    lines = data.readlines()
    x = []
    y = []
    for line in lines:
        p = line.split()
        x.append((p[0]))
        y.append((p[1]))
    data.close()
    return x, y

a,b = Read_Two_Column_File('demofile3.txt')

print (a)
print (b)