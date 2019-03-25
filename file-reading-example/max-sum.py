file = open('max-sum-input.txt', 'r')

n = int(file.readline())

matrix = []
for line in file:
    row = list(map(lambda item: int(item), line.split(' ')))
    matrix.append(row)
print(matrix)

