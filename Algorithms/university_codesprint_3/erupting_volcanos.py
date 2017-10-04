import sys


def printMatrix(zeros1, n1):
    print('values in zeros')
    for i in range(n1):
        for j in range(n1):
            print(zeros1[i][j], sep='', end=' ', file=sys.stdout)
        print('\n')


if __name__ == "__main__":
    n = int(input().strip())
    m = int(input().strip())
    zeros = [[0] * n for _ in range(n)]
    max1 = zeros[0][0]
    for a0 in range(m):
        x, y, w = input().strip().split(' ')
        x, y, w = [int(x), int(y), int(w)]

        for row in range(n):
            for col in range(n):
                    rowDiff = abs(row - x)
                    colDiff = abs(col - y)
                    if w - max(rowDiff, colDiff) >= 0:
                        zeros[row][col] = zeros[row][col] + w - max(rowDiff, colDiff)

                        print(''.join("{0}-".format(w - max(rowDiff, colDiff))), row, col, sep='', end=' ', file=sys.stdout)
                        if zeros[row][col] > max1:
                            max1 = zeros[row][col]
            print('\n')
        print('**')

    printMatrix(zeros, n)
    print(max1)
