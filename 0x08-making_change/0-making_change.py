#!/usr/bin/python3
"""make change module"""


def makeChange(coins, total):
    """Make change method"""
    min_ch = [float('inf')] * (total + 1)
    min_ch[0] = 0

    if total <= 0:
        return 0

    for v in range(1, total + 1):
        for coin in coins:
            if coin <= v:
                min_ch[v] = min((min_ch[v - coin] + 1), min_ch[v])

    if min_ch[total] != float('inf'):
        return min_ch[total]
    else:
        return -1
