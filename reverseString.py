
def str_reverse (s):
    result=""
    last=len(s)
    while last>0:
        result+=s[last-1]
        last=last-1   #last-=1
    return result
print(str_reverse("python"))

