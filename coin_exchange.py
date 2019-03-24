from typing import List


def coin_changing(coins: List[int], target, mem) -> int:

    n = len(coins)
    if mem[n][target] is not None:
        return mem[n][target]

    if target == 0 or len(coins) == 0:
        return 0

    if coins[-1] > target:
        return coin_changing(coins[:-1], target, mem)


    mem[n][target] = min(coin_changing(coins[:-1], target, mem), 1 + coin_changing(coins[:], target - coins[-1], mem))

    return mem[n][target]

coins = [1, 10, 21, 34, 70, 100, 250, 1295, 1500]

value = 140

print(coin_changing(coins, value, [[None for i in range(value + 1)] for i in range(len(coins) + 1)]))
