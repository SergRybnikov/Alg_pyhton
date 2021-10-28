# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
# Использовал литературу от сюда https://www.bestprog.net/ru/2019/10/21/python-bitwise-operators-ru/

bit_and = 5 & 6
bit_or = 5 | 6
bit_xor = 5 ^ 6
bit_not_5 = ~ 5
bit_not_6 = ~ 6
bit_right = 5 >> 2
bit_left = 5 << 2

print(f'Выполним логические побитовые операции над числами 5 и 6:\n'
      f'5 & 6 = {bit_and}\n'
      f'5 | 6 = {bit_or}\n'
      f'5 ^ 6 = {bit_xor}\n'
      f'5 = ~ 6 = {bit_not_5}\n'
      f'6 = ~ 6 = {bit_not_6}\n'
      f'5 >> 2 = {bit_right}\n'
      f'5 << 2 = {bit_left}')
