N,M = map(int, raw_input().split())
coins = map(int, raw_input().split())
minCoin = min(coins)

ways = {}

def solution(amt,coin):
    if len(coin) ==0:
        return 0
    elif amt==0:
        return 1
    elif amt < 0:
        return 0
    elif len(coin) ==1:
        if coin[0] < amt:
            return 0
        else:
            return solution(amt-coin[0],coin)
    else:
        inp = amt-coin[0]
        ans = solution(inp,coin) + solution(amt, coin[1:])
        if not ways.has_key(amt):
            ways[amt] = [[set(coin),ans]]
        else:
            ways[amt] = ways[amt].append([set(coin),ans])
        return ans



ans = solution(N,coins)
print ans
