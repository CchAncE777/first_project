N = int(input('Введите N: '))
L = 0

if N == 0:
   print('Количество шагов равно нулю')
while N!=0:
     
     if N % 3 == 0:
        N = int((N-10)/2)
        L = L + 1
     elif N % 2 == 0:
        N = int(N*3)
        L = L + 1
     elif N % 5 == 0:
        N = int(N** .5)
        L = L + 1
     elif N % 7 == 0:
        N = int(N**(1/3))
        L = L + 1
     else: N = N - 1
     L = L + 1
     if L > 1_000_000:
        print('Количество шагов бесконечность')
        break
if L < 1_000_000:
 print('Количество шагов :', L)