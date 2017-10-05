#!/bin/python3

import sys

def solve(year):
    leap_day = 0
    if 1700 <= year <1918:
        if year%4 ==0:
            leap_day = 1
    if 1918<year<=2017:
        if year%4==0 and year%100!=0:
            leap_day = 1
    if year == 1918:
        leap_day = 13

    nums = (13-leap_day),"09",year

    return ".".join(map(str, nums))


year = int(input().strip())
result = solve(year)
print(result)
