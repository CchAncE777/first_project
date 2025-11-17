def hello():
    print('Hello world!')
hello()

def hello():
    return('Hello world!')
hello()

def hello(name):
    return(f'Hello, {name}')
print(hello('Egor'))

def give_me(name):
    print(f'Hello, {name}')
my_name = input('Введите имя: ')
give_me(my_name)

def hello(age, name ='user'):
    return(f"Hello, {name}. I'm {age} old")
print(hello(18))

def hello(*args):
    data = ''.join(args)
    return(f'Hello {data}')
print(hello('go up', "jjoa"))

def hello(**kwargs):
    return(f"Hello {' '.join(kwargs)}")
print(hello())


