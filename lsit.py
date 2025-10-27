l = [3, 6, 9, 11, 17, 29, 33, 52, 69]
a = len(l)
b = int(a**(1/2))
iskomoe = 3
index = 0
is_found = False

for i  in range(0, a, b):
    if iskomoe <l[i]:
        for j in range(i-a, i):
            if l[j] == iskomoe:
                index = j
                is_found = True
                break
    if l[index] == iskomoe:
         break
for j in range(i, len(l)):
            if l[j] == iskomoe:
                index = j
                is_found = True
                break
print(index)

if is_found:
    print(index)
else:
     print('Not found')