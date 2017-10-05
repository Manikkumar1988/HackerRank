def bonAppetit(n, k, b, ar):
    b_actual = 0
    b_charged = b
    for price_index in range(n):
        #print(price_index)
        if k!=price_index:
            #print("m",price_index)
            b_actual = b_actual + ar[price_index]
    #print(b_actual)
    b_actual = b_actual/2
    if b_actual == b_charged:
        return "Bon Appetit"
    else:
        return int(b_charged - b_actual)


n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
