from typing import List


def custom_input_main():
    n = int(input())
    mat_input = list(map(lambda item: int(item), input().split(' ')))

    matrix = []

    for i in range(n):
        rows = mat_input[i * n: (i + 1) * n]
        matrix += [rows]

    print(maximum_sum_rectangle(get_sum_rectangle(matrix, n), n))


def fixed_input_main():
    n = 4
    matrix = [
        [0, -2, -7, 0],
        [9, 2, -6, 2],
        [-4, 1, -4, 1],
        [-1, 8, 0, -2]
    ]
    matrix = get_sum_rectangle(matrix, n)
    result = maximum_sum_rectangle(matrix, n)
    print(result)


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


def maximum_sum_rectangle(matrix: List[List[int]], n: int) -> int:
    max_rect = 0
    max_left, max_right, max_down, max_top = 0, 0, 0, 0
    for l in range(1, n + 1):
        for r in range(l, n + 1):
            arr = []
            for row in range(1, n + 1):
                arr += [matrix[row][r] - matrix[row][l - 1]]
                # max_rect = max(max_rect, max_kadane(arr))
                top, down, ans = max_kadane(arr)
                if max_rect < ans:
                    max_left = l
                    max_right = r
                    max_top = top
                    max_down = down
                    max_rect = ans

    # print((max_left, max_right), (max_top, max_down))
    return max_rect


def get_sum_rectangle(matrix: List[List[int]], n: int) -> List[List[int]]:
    sumed_square = [[0 for i in range(n + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            sumed_square[i][j] = matrix[i - 1][j - 1]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            sumed_square[i][j] += sumed_square[i][j - 1]
    return sumed_square


if __name__ == '__main__':
    # fixed_input_main()
    custom_input_main()
