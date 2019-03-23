from typing import List, Any

def edit_distance(first: str, second: str) -> int:

    n, m = len(first), len(second)

    dp = [[0] * (m + 1) for k in range(n + 1)]
    for item in dp:
        print(item)
    for i in range(n):
        for j in range(m):
            if first[i] == second[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

    lcs = dp[n][m]
    return n - lcs + m - lcs


print(edit_distance('algorithm', 'rhythm'))
print(edit_distance('rhythm', 'algorithm'))


def lcs(first: List[Any], second: List[Any]) -> int:
    n, m = len(first), len(second)

    dp = [[0] * (m + 1) for k in range(n + 1)]

    for i in range(n):
        for j in range(m):
            if first[i] == second[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    return dp[n][m]

