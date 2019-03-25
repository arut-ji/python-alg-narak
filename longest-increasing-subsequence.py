from typing import List


def LIS(arr: List[int], n) -> int:
    dp = [arr[0]]

    for i in range(1, n):
        print(dp)
        if arr[i] < dp[0]:
            dp[0] = arr[i]
        elif arr[i] > dp[-1]:
            dp += [arr[i]]
        else:
            dp[lower_bound(dp, arr[i])] = arr[i]

    return len(dp)


def _lower_bound(arr: List[int], left: int, right: int, key: int):
    if left >= right:
        return left + 1 if left > right else left

    mid = (left + right) // 2

    if arr[mid] < key:
        return _lower_bound(arr, mid + 1, right, key)
    elif arr[mid] > key:
        return _lower_bound(arr, left, mid - 1, key)


def lower_bound(arr: List[int], key: int):
    n = len(arr)
    return _lower_bound(arr, 0, n - 1, key)


arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(LIS(arr, len(arr)))
