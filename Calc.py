#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print('-=Калькулятор=-')


# In[ ]:


user_name = input('Введите логин: ')
password = input('Введите пароль: ')
if user_name == 'admin':
    if password == 'admin':
        print(f'Вы вошли, как Администратор')
    else:
        print('Неверный пароль')
else:
    print('Неверный логин')


# In[ ]:


print('Выбери желаемую операцию:')
print('a)Сложение')
print('b)Вычитание')
print('c)Умножение')
print('d)Деление')d


# In[ ]:


answer = input()


# In[ ]:


x = int(input('Введите первое число: '))


# In[ ]:


y = int(input('Введите второе число: '))


# In[ ]:


if answer == 'a':
    itog = x + y
elif answer == 'b':
    itog = x - y
elif answer == 'c':
    itog = x * y
elif answer == 'd':
    itog = x / y


# In[ ]:


if answer == 'a':
    print(f'Сумма чисел {x} и {y} равняется {itog}')
elif answer == 'b':
    print(f'Разница чисел {x} и {y} равняется {itog}')
elif answer == 'c':
    print(f'Произведение чисел {x} и {y} равняется {itog}')
elif answer == 'd':
    print(f'Частное чисел {x} и {y} равняется {itog}')

