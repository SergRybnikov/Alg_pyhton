# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).


print('Ведите 3 разных числа:')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

average = a + b + c - max(a, b, c) - min(a, b, c)

print(f'Число {average} - среднее')
