
import math


def main():
    n = int(input())
    arr = list(map(lambda item: int(item), input().split(' ')))
    result = int(input())

    mem = {}
    for item in arr:
        mem[item] = True
    minn = 1234567
    first, second = 0, 0
    for item in arr:
        if mem.setdefault(result - item, False):
            if math.fabs(result - 2 * item) < minn:
                first = item
                second = result - item
                minn = math.fabs(first - second)

    print("Peter should buy books whose prices are", min(first,second), "and", max(first,second))


if __name__ == '__main__':
    main()
