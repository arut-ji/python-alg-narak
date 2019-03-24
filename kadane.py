def kadane(arr, n, start, stop):
    _sum = [0] * (n + 1)
    _sum[0] = arr[0]
    for i in range(1, stop + 1):
        _sum[i] = _sum[i - 1] + arr[i]
    ans = _sum[stop] - _sum[start - 1]
    return ans


def max_kadane(arr):
    left, right = 0, 0
    n = len(arr)
    ans = arr[0]
    _sum = arr[0]
    for i in range(1, n):

        if _sum + arr[i] <= arr[i]:
            left = i
            right = i
            _sum = arr[i]
        else:
            _sum += arr[i]

        if ans < _sum:
            right = i
            ans = _sum

    return left, right, ans


array = [1, -2, 4, 5, 20, -25, -26, 30]
print(max_kadane(array))
