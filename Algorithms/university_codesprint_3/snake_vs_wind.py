import sys

if __name__ == "__main__":
    n = int(input().strip())
    d = input().strip()
    x, y = input().strip().split(' ')
    x, y = [int(x), int(y)]

    if d == "n":
        up = -1
        right = 0
    elif d == "e":
        up = 0
        right = 1
    elif d == "s":
        up = 1
        right = 0
    else:
        up = 0
        right = -1



    zeros = [[0 for _ in range(n)] for _ in range(n)]
    zeros[x][y] = 1
    for i in range(2, n * n + 1):
        if x + up >= 0 and x + up < n and y + right >= 0 and y + right < n and not zeros[x + up][y + right]:
            zeros[x + up][y + right] = i
            x, y = x + up, y + right
        elif y + up >= 0 and y + up < n and x + right >= 0 and x + right < n and not zeros[x + right][y + up]:
            zeros[x + right][y + up] = i
            x, y = x + right, y + up
        elif y - up >= 0 and y - up < n and x - right >= 0 and x - right < n and not zeros[x - right][y - up]:
            zeros[x - right][y - up] = i
            x, y = x - right, y - up
        else:
            zeros[x - up][y - right] = i
            x, y = x - up, y - right
    for row in zeros:
        print(*row)










