from typing import List, Any


def is_subset_sum(arr: List[Any], result: int, mem: List[Any]) -> bool:
    if mem[result] is not None:
        return mem[result]

    if result == 0:
        return True
    if len(arr) == 0 and result != 0:
        mem[result] = False
        return False

    if arr[-1] > result:
        return is_subset_sum(arr[:-1], result, mem)

    mem[result] = is_subset_sum(arr[:-1], result, mem) or is_subset_sum(arr[:-1], result - arr[-1], mem)
    return mem[result]


def subset_sum(arr: List[Any], result: int) -> bool:
    arr.sort()
    dp = [None for i in range(result + 1)]
    result = is_subset_sum(arr, result, dp)
    return result


array: List[Any] = [3, 34, 4, 12, 5, 2]

print(subset_sum(array, 49))
