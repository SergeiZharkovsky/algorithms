def main():
    a, b, c = map(int, input().split())
    result = (
            (a % 2 == 0 and b % 2 == 0 and c % 2 == 0) or
            (a % 2 == 1 and b % 2 == 1 and c % 2 == 1)
              )
    if result:
        print('WIN')
    else:
        print('FAIL')


if __name__ == '__main__':
    main()
