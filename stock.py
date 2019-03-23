# Use Kadane's algorithm


arr = [1082.47, 1008.46, 1059.81, 1075.8, 1073.73, 1055, 1039.48,
       1069, 1091.38, 1073.99, 1061.39, 1043.29, 1050, 1044.71, 1059.41,
       1057.2, 1000, 1036.76, 1030, 1038.35, 1041, 1048.76, 1076.08]

length = len(arr)

day = dict()

for i in range(length):
    day[arr[i]] = i

# print(day)

bound = [arr[0]]


for i in range(1, length):
    if arr[i] < bound[0]:
        bound = [arr[i]] + bound
    elif arr[i] > bound[-1]:
        bound += [arr[i]]

while day[bound[0]] > day[bound[-1]]:
    bound = bound[1:]

print(bound[0], bound[-1])
