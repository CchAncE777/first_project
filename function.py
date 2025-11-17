def function_1():
    print('1')
print(function_1())

def sum(a, b):
    return a + b
print(sum(1, 5))

ord('a') #-> to ascii code
chr(65) #-> to str symbol

def variable_1(a, b):
    diff = len(a) - len(b)
    if diff == 0:
        for i in range(len(a)):
            result =+ chr(abs((ord(a[i])) - ord(b[i])))
    return result
print(variable_1('awsd', 'asdw'))
