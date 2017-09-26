#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

sum1 = 0
for d in apple:
    if s <= d+a <= t:
        sum1 += 1
print(sum1)

sum1 = 0
for d in orange:
    if s <= d+b <= t:
        sum1 += 1
print(sum1)



