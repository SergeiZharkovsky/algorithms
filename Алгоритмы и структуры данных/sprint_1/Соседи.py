def neighbors(matrix, y, x):
    h = []
    if x + 1 < len(matrix[0]):
        h.append(matrix[y][x + 1])
    if x - 1 >= 0:
        h.append(matrix[y][x - 1])
    if y + 1 < len(matrix):
        h.append(matrix[y + 1][x])
    if y - 1 >= 0:
        h.append(matrix[y - 1][x])
    return h


n = int(input())
m = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
y, x = int(input()), int(input())
print(*sorted(neighbors(matrix, y, x)))
