def aVeryBigSum(n, ar):
    sum =0
    for a in ar:
        sum += a
    return sum

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)