import sys
import operator

def migratoryBirds(n, ar):
    birds = [0]*n
    for a in ar:
        b = a - 1
        birds[b] = birds[b] + 1
    print(birds)
    print(max(birds))
    print (birds.index(max(birds)))
    return birds.index(max(birds))+1


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)