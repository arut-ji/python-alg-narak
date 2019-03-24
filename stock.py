# Use Kadane's algorithm
from typing import List

arr = [1082.47, 1008.46, 1059.81, 1075.8, 1073.73, 1055, 1039.48,
       1069, 1091.38, 1073.99, 1061.39, 1043.29, 1050, 1044.71, 1059.41,
       1057.2, 1000, 1036.76, 1030, 1038.35, 1041, 1048.76, 1076.08]

benefits = []
for i in range(1, len(arr)):
    benefits += [arr[i] - arr[i - 1]]

ans = benefits[0]
temp_sum = benefits[0]
n = len(benefits)

for i in range(1, n):
    temp_sum += benefits[i]
    ans = max(benefits[i], temp_sum)

print(ans)

def max_range(arr: List[int]) -> int:
    n = len(arr)
    ans = arr[0]
    temp_sum = arr[0]
    for i in range(1, n):
        temp_sum += arr[i]
        ans = max(arr[i], temp_sum)
    return ans

print(max([1,2,-3,4,-5,6]))