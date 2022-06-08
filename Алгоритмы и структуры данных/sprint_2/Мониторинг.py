def data_input():
    n = int(input())
    m = int(input())
    matrix = ''
    matrix = [input().split(' ') for j in range(n)]
    return n, m, matrix


def calculations():
    n, m, matrix = data_input()
    for i in range(m):
        for j in range(n):
            print(matrix[j][i], end=' ')
        print('')


if __name__ == '__main__':
    calculations()
