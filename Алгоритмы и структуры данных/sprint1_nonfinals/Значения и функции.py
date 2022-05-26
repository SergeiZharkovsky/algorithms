def main():
    a, x, b, c = map(int, input().split(' '))
    y = a * x ** 2 + b * x + c
    print(y)


if __name__ == '__main__':
    main()
