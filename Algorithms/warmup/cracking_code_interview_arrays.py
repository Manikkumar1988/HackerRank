def array_left_rotation(a, n, k):
    temp = []
    for _i in range(n):
        temp[_i] = a[(_i + k) % n]
    return temp



n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')