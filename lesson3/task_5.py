"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""

import random

SIZE = 10
array = [random.randint(-100, 100) for _ in range(SIZE)]
print(array)

num = float('-inf')
index = -1
for i, item in enumerate(array):
    if 0 > item > num:
        num = item
        index = i
print(f'Число {num} на позиции {index}')
