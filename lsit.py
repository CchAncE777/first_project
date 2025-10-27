l = [3, 6, 9, 11, 17, 29, 33, 52, 69]
a = len(l)
b = int(a**(1/2))
iskomoe = 69
index = 0
for i  in range(0, a, b):
    if iskomoe <l[i]:
        for j in range(i-a, i):
            if l[j] == iskomoe:
                index = j
                break
    if l[index] == iskomoe:
         break
for j in range(i, len(l)):
            if l[j] == iskomoe:
                index = j
                break
print(index)