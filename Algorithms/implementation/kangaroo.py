import sys


def kangaroo(x1, v1, x2, v2):
    return ('NO', 'YES')[bool(v1 > v2 and (x2 - x1) % (v1 - v2) == 0)]


x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
