def count(arr, m, n):
    table = [[0 for x in range(m)] for x in range(n + 1)]
    for i in range(m):
        table[0][i] = 1

    for i in range(1, n + 1):
        for j in range(m):
            x = table[i - arr[j]][j] if i - arr[j] >= 0 else 0
            y = table[i][j - 1] if j >= 1 else 0
            table[i][j] = x + y
    return table[n][m - 1]


print(count([2, 5, 3, 6], 4, 10))
