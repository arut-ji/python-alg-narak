from typing import List, Any
from random import shuffle


def mergeSort(arr: List[Any]) -> List[Any]:
    current_size: int = 1
    while current_size < len(arr):

        left = 0
        while left < len(arr) - 1:
            first_mid: int = left + current_size
            second_mid: int = left + current_size * 2 if left + current_size * 2 < len(arr) else len(arr)
            high: int = left + current_size * 3 if left + current_size * 3 < len(arr) else len(arr)

            arr = merge(arr=arr, low=left, first_mid=first_mid, second_mid=second_mid, high=high)
            left = left + current_size * 3
            print(arr)
        current_size = 3 * current_size

    return arr


def merge(arr: List[Any], low: int, first_mid: int, second_mid: int, high: int) -> List[Any]:
    first: List[Any] = arr[low:first_mid]
    second: List[Any] = arr[first_mid:second_mid]
    third: List[Any] = arr[second_mid:high]

    result: List[Any] = []

    while first != [] and second != [] and third != []:
        if min(first[0], second[0], third[0]) == first[0]:
            result += [first[0]]
            first = first[1:]
        elif min(first[0], second[0], third[0]) == second[0]:
            result += [second[0]]
            second = second[1:]
        else:
            result += [third[0]]
            third = third[1:]

    while first != [] and second != []:
        if min(first[0], second[0]) == first[0]:
            result += [first[0]]
            first = first[1:]
        else:
            result += [second[0]]
            second = second[1:]

    while first != [] and third != []:
        if min(first[0], third[0]) == first[0]:
            result += [first[0]]
            first = first[1:]
        else:
            result += [third[0]]
            third = third[1:]

    while third != [] and second != []:
        if min(third[0], second[0]) == third[0]:
            result += [third[0]]
            third = third[1:]
        else:
            result += [second[0]]
            second = second[1:]

    result += first + second + third

    return arr[:low] + result + arr[high:]


arr = list(range(100))
shuffle(arr)

# arr = [66, 36, 60, 98, 77, 52, 47, 11, 19, 85]

print("Given array is ")
print(arr)

arr = mergeSort(arr)

print("Sorted array is ")
print(arr)
