def bubble_sort(number, array):
    flag = 1
    for i in range(number - 1):
        for j in range(0, number-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                flag = 1
        if flag == 1:
            for x in array:
                print(x, end=' ')
            print('')
            flag = 0


def main():
    number = int(input())
    array = [int(num) for num in input().split(' ')]
    bubble_sort(number, array)


if __name__ == '__main__':
    main()
