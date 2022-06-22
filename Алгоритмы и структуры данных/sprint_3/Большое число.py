def big_number(number, array):
    for i in range(number-1):
        for j in range(0, number-i-1):
            x = array[j] + array[j+1]
            y = array[j + 1] + array[j]
            if x < y:
                array[j], array[j+1] = array[j+1], array[j]
    print("".join(array))


def main():
    number = int(input())
    array = input().split(' ')
    big_number(number, array)


if __name__ == '__main__':
    main()
