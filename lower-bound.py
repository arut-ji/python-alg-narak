from typing import List, Any


def _lower_bound(arr: List[int], k: int, left: int, right: int) -> int:
    if left >= right:
        return arr[left - 1]

    mid = (left + right) // 2

    if arr[mid] > k:
        return _lower_bound(arr, k, left, mid - 1)
    elif arr[mid] < k:
        return _lower_bound(arr, k, mid + 1, right)


def lower_bound(arr: List[int], k: int) -> int:
    n = len(arr)
    return _lower_bound(arr, k, 0, n - 1)


print(lower_bound([0, 1, 2, 4, 7, 8, 10], 6))
