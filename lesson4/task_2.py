"""
Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна
принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
"""
import timeit
import cProfile


def eratosthenes(n):
    _range = list(range(2, n + 1))
    for i in _range:
        if i != 0:
            for candidate in range(2 * i, n + 1, i):
                _range[candidate - 2] = 0
    return list(filter(lambda x: bool(x), _range))


# print(timeit.timeit('eratosthenes(10)', number=1000, globals=globals()))
# print(timeit.timeit('eratosthenes(100)', number=1000, globals=globals()))
# print(timeit.timeit('eratosthenes(1000)', number=1000, globals=globals()))
# print(timeit.timeit('eratosthenes(10000)', number=1000, globals=globals()))

# 0.0066805999995267484
# 0.0485683999977482
# 0.563883499999065
# 6.25143830000161

# cProfile.run('eratosthenes(10000)')
# 10003 function calls in 0.011 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.011    0.011 <string>:1(<module>)
#        1    0.008    0.008    0.011    0.011 task_2.py:15(eratosthenes)
#     9999    0.002    0.000    0.002    0.000 task_2.py:21(<lambda>)
#        1    0.000    0.000    0.011    0.011 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

def simple(n):
    _range = list(range(2, n + 1))
    for i in _range:
        for j in list(range(2, i)):
            if i % j == 0:
                _range[i - 2] = 0
                break
    return list(filter(lambda x: bool(x), _range))

# print(timeit.timeit('simple(10)', number=1000, globals=globals()))
# print(timeit.timeit('simple(100)', number=1000, globals=globals()))
# print(timeit.timeit('simple(1000)', number=1000, globals=globals()))

# 0.010594400002446491
# 0.23879999999917345
# 17.58573350000006

# cProfile.run('simple(10000)')

# 10003 function calls in 1.940 seconds

# Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    1.940    1.940 <string>:1(<module>)
#        1    1.938    1.938    1.940    1.940 task_2.py:45(simple)
#     9999    0.002    0.000    0.002    0.000 task_2.py:52(<lambda>)
#        1    0.000    0.000    1.940    1.940 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
