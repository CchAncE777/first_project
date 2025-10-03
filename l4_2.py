l = (input('Список чисел: ')).split()
b = 0
for a in range(0, len(l)):
    l [a] = int(l[a])
    Ch = int(input('Выберите операцию: '))
match Ch:
    case 0:
        for a in range(0, len(l)):
         l [a] = 0
    case 1:
        for a in range(0, len(l)):
         l [a] = l [a] * 2
    case 2:
        for a in range(0, len(l), 2):
         l [a] = l [a] + 10
    case 3:
        for a in range(0, len(l), 3):
         if l[a] >= 0:
          l [a] = l [a] ** (1/2)
         else:
          l[a] = 0
    case _: 
         b = sum(l)
print(l)
print(b)
