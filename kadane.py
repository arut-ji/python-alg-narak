def kadane(arr, n, start, stop):
    _sum = [0] * (n + 1)
    _sum[0] = arr[0]
    for i in range(1, stop + 1):
        _sum[i] = _sum[i - 1] + arr[i]
    ans = _sum[stop] - _sum[start - 1]
    return ans


def max_kadane(arr, n):
    ans = arr[0]
    _sum = arr[0]
    for i in range(1, n):
        _sum = max(arr[i], _sum + arr[i])
        ans = max(_sum, ans)
        # print(sum,ans)
    return ans
