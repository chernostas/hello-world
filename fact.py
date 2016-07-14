#ilovebuiltinfunctions
import inspect
import sys


def value_check(n):
    if n < 0:
        raise ValueError('{} is incorrect number for factorial calculation'.
                         format(n))


def fact_00(n):
    from math import factorial
    return factorial(n)


def fact_01(n):
    value_check(n)
    if n == 0:
        return 1
    return reduce(lambda _, _2: _*_2, xrange(1, n + 1))


def fact_02(n):
    value_check(n)
    res = 1
    for _ in xrange(1, n + 1):
        res *= _
    return res


def fact_03(n):
    value_check(n)
    if n == 0:
        return 1
    return n*fact_03(n - 1)


def fact_04_01(n):
    value_check(n)
    res = 1
    while n != 0:
        res *= n
        n -= 1
    return res


def fact_04_02(n):
    value_check(n)
    res = 1
    i = 1
    while i <= n:
        res *= i
        i += 1
    return res


def fact_05_01(n):
    value_check(n)
    if n == 0:
        return 1
    return eval('*'.join(str(_) for _ in xrange(1, n + 1)))


def fact_05_02(n):
    value_check(n)
    if n == 0:
        return 1
    return eval('*'.join(map(str, xrange(1, n + 1))))


def fact_06_01(n):
    value_check(n)
    if n == 0:
        return 1
    res = 1
    seq = iter(xrange(1, n + 1))
    try:
        while True:
            res *= next(seq)
    except StopIteration:
        pass
    return res


def fact_06_02(n):
    value_check(n)
    res = 1
    seq = iter(xrange(n, 0, -1))
    i = next(seq, 1)
    while i > 1:
        res *= i
        i = next(seq, 1)
    return res


def fact_07(n):
    value_check(n)
    if n < 2:
        return 1
    i = n%2 + 1
    seq_1 = xrange(i, n/2 + i)
    seq_2 = xrange(n/2 + i, n + 1)
    pair = reduce(lambda _, _2: (_[0]*_2[0], _[1]*_2[1]), zip(seq_1, seq_2))
    return pair[0]*pair[1]


if __name__ == '__main__':
    output_str = 'Function: {}; i: {}, result: {}'
    fset = [obj for name, obj in inspect.getmembers(sys.modules[__name__]) if
            inspect.isfunction(obj) and obj.__name__.startswith('fact')]
    for func in fset:
        for _ in (0, 1, 5, 10):
            print(output_str.format(func.__name__, _, func(_)))
        print('-'*10)


