"""
1). Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания
первых трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.
"""
# Выбрал задачу номер 5 из урока 3

import random
import timeit
import cProfile


def max_zero(size):
    array = [random.randint(size * -10, size * 10) for _ in range(size)]

    i = 0
    index = -1

    while i < size:
        if array[i] < 0 and index == -1:
            index = i
        elif array[i] < 0 and array[i] > array[index]:
            index = i
        i += 1
    return f'Число {array[index]} на позиции {index}'

# print(timeit.timeit('max_zero(10)', number=100, globals=globals()))
# print(timeit.timeit('max_zero(100)', number=100, globals=globals()))
# print(timeit.timeit('max_zero(1000)', number=100, globals=globals()))
# print(timeit.timeit('max_zero(10000)', number=100, globals=globals()))

# 0.0024278999990201555
# 0.02242389999992156
# 0.2341070000002219
# 2.1509334000002127

# При увеличении массива в 10 раз, время также увеличивается примерно в 10 раз. Это говорит, что алгоритм линейный (Оn)

# cProfile.run('max_zero(10)')
#             87 calls in 0.000 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      10    0.000    0.000    0.000    0.000 random.py:239(_randbelow_with_getrandbits)
#      10    0.000    0.000    0.000    0.000 random.py:292(randrange)
#      10    0.000    0.000    0.000    0.000 random.py:366(randint)
#       1    0.000    0.000    0.000    0.000 task_1.py:16(max_zero)
#       1    0.000    0.000    0.000    0.000 task_1.py:17(<listcomp>)
#      30    0.000    0.000    0.000    0.000 {built-in method _operator.index}
#       1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      12    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# cProfile.run('max_zero(100)')
#             807 calls in 0.001 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#      100    0.000    0.000    0.000    0.000 random.py:239(_randbelow_with_getrandbits)
#      100    0.000    0.000    0.000    0.000 random.py:292(randrange)
#      100    0.000    0.000    0.000    0.000 random.py:366(randint)
#        1    0.000    0.000    0.001    0.001 task_1.py:16(max_zero)
#        1    0.000    0.000    0.001    0.001 task_1.py:17(<listcomp>)
#      300    0.000    0.000    0.000    0.000 {built-in method _operator.index}
#        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#      100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      102    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# cProfile.run('max_zero(1000)')
#              8 631 calls in 0.006 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.006    0.006 <string>:1(<module>)
#     1000    0.001    0.000    0.002    0.000 random.py:239(_randbelow_with_getrandbits)
#     1000    0.002    0.000    0.004    0.000 random.py:292(randrange)
#     1000    0.001    0.000    0.005    0.000 random.py:366(randint)
#        1    0.000    0.000    0.006    0.006 task_1.py:16(max_zero)
#        1    0.001    0.001    0.006    0.006 task_1.py:17(<listcomp>)
#     3000    0.000    0.000    0.000    0.000 {built-in method _operator.index}
#        1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
#     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     1626    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# cProfile.run('max_zero(10000)')
#              82 977 calls in 0.060 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.060    0.060 <string>:1(<module>)
#    10000    0.011    0.000    0.016    0.000 random.py:239(_randbelow_with_getrandbits)
#    10000    0.020    0.000    0.041    0.000 random.py:292(randrange)
#    10000    0.008    0.000    0.048    0.000 random.py:366(randint)
#        1    0.004    0.004    0.060    0.060 task_1.py:16(max_zero)
#        1    0.007    0.007    0.056    0.056 task_1.py:17(<listcomp>)
#    30000    0.005    0.000    0.005    0.000 {built-in method _operator.index}
#        1    0.000    0.000    0.060    0.060 {built-in method builtins.exec}
#    10000    0.002    0.000    0.002    0.000 {method 'bit_length' of 'int' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    12972    0.003    0.000    0.003    0.000 {method 'getrandbits' of '_random.Random' objects}
