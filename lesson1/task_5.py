# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.


print('Ведите две прописные буквы латинского алфавита:')
let1 = input('Первая буква - ')
let2 = input('Вторая буква - ')

letter1 = ord(let1)
letter2 = ord(let2)

pos_let1 = ord(let1) - letter1 + 1
pos_let2 = ord(let2) - letter1 + 1
distance = abs(pos_let1 - pos_let2) - 1
print(f'Буква "{let1}" {pos_let1}-я в алфавите\n'
      f'Буква "{let2}" {pos_let2}-я в алфавите\n'
      f'Между буквами {distance} букв(ы)')
