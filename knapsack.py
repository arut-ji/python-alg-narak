def knapsack(weight, values, W, mem):
    n = len(weight)
    if mem[n][W] is not None:
        return mem[n][W]

    if len(weight) == 0 or W == 0:
        return 0

    if weight[-1] > W:
        return knapsack(weight[:-1], values[:-1], W, mem)

    mem[n][W] = max(values[-1] + knapsack(weight[:-1], values[:-1], W - weight[-1], mem),
                    knapsack(weight[:-1], values[:-1], W, mem))

    return mem[n][W]


v = [130, 100, 120]
w = [1, 1, 1]

number_of_item = len(v)
limit_weight = 2

mem = [[None for i in range(limit_weight + 1)] for i in range(number_of_item + 1)]
print(knapsack(w, v, limit_weight, mem))
