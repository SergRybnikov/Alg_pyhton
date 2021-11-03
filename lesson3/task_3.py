"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random

SIZE = 10
r = [random.randint(0, 100) for _ in range(SIZE)]
print(f'Массив до изменения: \n{r}')

idx_min = 0
idx_max = 0

for i in range(SIZE):
    if r[i] < r[idx_min]:
        idx_min = i
    elif r[i] > r[idx_max]:
        idx_max = i

r[idx_min], r[idx_max] = r[idx_max], r[idx_min]
print(f'Массив после изменения: \n{r}')
