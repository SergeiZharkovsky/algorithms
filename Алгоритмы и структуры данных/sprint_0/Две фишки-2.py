def twosum_with_sort(numbers, X):
    numbers.sort()
    left = 0
    right = len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == X:
            return numbers[left], numbers[right]
        if current_sum < X:
            left += 1
        else:
            right -= 1
    return None,


n = int(input())
numbers = list(map(int, input().strip().split()))
X = int(input())
print(*twosum_with_sort(numbers, X))
