def remove_duplicate(alist):
    return list(set(alist))


def solution(A):
    A = remove_duplicate(A)
    A.sort()
    B = []
    for i in A:
        if i > 0:
            B.append(i)
    l = 1
    for k in range(len(B)):
        if B[k] != l:
            return l
        l = l + 1
    return l
    pass


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = solution(ar)
print(result)
