def tree(n):
    if n == 0:
        return 1
    return tree(n-1) * n


n = int(input())
print(int(tree(2*n)/(tree(n)*tree(n+1))))
