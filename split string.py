sentence = 'This is a sentence'
split_value = []
tmp = ''
for c in sentence:
    if c == ' ':
        split_value.append(tmp)
        tmp = ''
        
    else:
        tmp += c
if tmp:
    split_value.append(tmp)
print(split_value)