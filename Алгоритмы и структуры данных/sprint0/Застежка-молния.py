n = int(input())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
for i in zip(a, b):
    print(*i, end=' ')
