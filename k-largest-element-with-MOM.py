from typing import List, Any


def find_median(arr):
    arr.sort()
    if len(arr) == 0:
        return []
    return [arr[len(arr) // 2]]


def k_largest_elements(arr: List[Any], k: int):
    n = len(arr)
    medians = []
    arr, extra = arr[:(n // 5 * 5)], arr[(n // 5 * 5):]
    for i in range(n // 5):
        medians += find_median(arr[i * 5: i * 5 + 5])

    medians += find_median(extra)

    med_of_meds = find_median(medians)[0]

    left = list(filter(lambda item: item < med_of_meds, arr + extra))
    right = [med_of_meds] + list(filter(lambda item: item > med_of_meds, arr + extra))

    len_right = len(right)

    if len_right < k:
        return k_largest_elements(left, k - len_right) + right
    elif len_right > k:
        return k_largest_elements(right, k)
    else:
        return right


k = 4

k_numbers = k_largest_elements([12, 3, 5, 7, 4, 19, 26] + list(range(150, 100, -1)), k)
print(k_numbers)
print(sum(k_numbers) / k)
