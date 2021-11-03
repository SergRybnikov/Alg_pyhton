"""
Определить, какое число в массиве встречается чаще всего.
"""
import random

SIZE = 10
r = [random.randint(0, SIZE // 2) for _ in range(SIZE)]
print(r)
diction = {}
for item in r:
    if item in diction.keys():
        diction[item] += 1
    else:
        diction[item] = 1
print(diction)
