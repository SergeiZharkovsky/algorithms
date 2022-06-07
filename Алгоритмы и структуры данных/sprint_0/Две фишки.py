def twosum(numbers, X):
    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == X:
                return numbers[i], numbers[j]
    return None,


n = int(input())
numbers = list(map(int, input().strip().split()))
X = int(input())
print(*twosum(numbers, X))
