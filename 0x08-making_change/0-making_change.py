#!/usr/bin/python3

def makeChange(coins, total):
    min_ch = [float('inf')] * (total + 1)
    min_ch[0] = 0;

    if total <= 0:
        return 0;

    for v in range(1, total + 1):
        for coin in coins:
            if coin <= v:
                min_ch[v] = min((min_ch[v - coin] + 1), min_ch[v])


    if min_ch[total] != float('inf'):
        return min_ch[total]
    else:
        return -1


print(makeChange([1,2,5], 11))
