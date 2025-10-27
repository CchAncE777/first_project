import numpy as np
import pandas as pd
import random

r = {}

for i in range(1,10):   
    name = input('Введите имя: ')
    sname = input('Введите фамилию: ')
    pname = input('Введите отчество: ')
    date = input('Введите дату рождения: ')
    id = random.randint(1000,9999)

    n = {'Имя': name, 'Фамилия': sname, 'Отчество': pname, 'Дата': date}
    
    r.update({id : n})

df = pd.DataFrame(r.values(), index=r.keys())

df.to_csv('d:/1.csv', encoding='utf-8')
df1 = pd.read_csv('D:/1.csv')