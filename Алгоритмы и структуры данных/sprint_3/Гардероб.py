def wardrobe(colors):
    values = [0] * 3
    for value in colors:
        values[value] += 1
    return [0] * values[0] + [1] * values[1] + [2] * values[2]


n = int(input())
colors = list(map(int, input().strip().split()))
print(*wardrobe(colors))
