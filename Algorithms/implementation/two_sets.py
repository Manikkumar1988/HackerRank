def getTotalX(a, b):
    sum1 = 0
    min1 = a[0]
    for index in range(min1,100):
        atrue = 1
        for A in a:
            if index % A != 0:
                atrue = 0
                break
            else:
                atrue = 1
        if atrue == 1:
            for A in b:
                if A % index  != 0:
                    atrue = 0
                    break
                else:
                    atrue = 1

        if atrue == 1:
            sum1 += 1

    return sum1


if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)