def getRecord(s):
    min1 = []
    max1 = []

    max1.append(s[0])
    min1.append(s[0])

    maxValue = max1[0]
    minValue = min1[0]
    for i in range(len(s)-1):
        maxValue = max(s[i+1],maxValue)
        minValue = min(s[i+1],minValue)
        max1.append(maxValue)
        min1.append(minValue)

    maxCounter = 0
    minCounter = 0
    for i in range(len(s)-1):
        if max1[i+1] > max1[i]:
            maxCounter = maxCounter + 1
        if min1[i+1] < min1[i]:
            minCounter = minCounter + 1
    print(s)
    print(max1)
    print(min1)
    return [maxCounter,minCounter]

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))