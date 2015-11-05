from collections import defaultdict

N,M = map(int, raw_input().split())
coins = map(int, raw_input().split())
minCoin = min(coins)

ways = defaultdict(list)

def solution(amt,coin):
    coinSet = set(coin)
    if ways.has_key(amt):
       for ansList in ways[amt]:
           if ansList[0] == coinSet:
               return ansList[1]

    if len(coin) ==0:
        return 0
    elif amt==0:
        return 1
    elif amt < 0:
        return 0
    else:
        inp = amt-coin[0]
        ans = solution(inp,coin) + solution(amt, coin[1:])
        ways[amt].append([set(coin),ans])
        return ans



ans = solution(N,coins)
print ans
