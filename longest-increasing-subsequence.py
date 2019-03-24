from typing import List, Any
from sys import maxsize


def _LIS(arr: List[int], index: int, n: int, prev: int, mem: List[Any]) -> int:
    if mem[index] is not None:
        return mem[index]

    if n == index:
        return 0

    exclude = _LIS(arr, index + 1, n, prev, mem)
    include = 0 if prev > arr[index] else _LIS(arr, index + 1, n, arr[index], mem) + 1
    mem[index] = max(max(exclude, include), mem[index]) if mem[index] is not None else max(exclude, include)
    return mem[index]


def LIS(arr: List[int]):
    n = len(arr)
    # print(-maxsize)
    return _LIS(arr, 0, n, -maxsize, [None for i in range(n + 1)])


array = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

print(LIS(array))
