def flower_beds(array):
    array.sort()
    result = [array[0]]
    for item in array[1:]:
        if item[0] > result[-1][1]:
            result.append(item)
        else:
            if result[-1][1] < item[1]:
                result[-1][1] = item[1]
    return result


def main():
    n = int(input())
    fields = flower_beds([list(map(int, input().split())) for _ in range(n)])
    for item in flower_beds(fields):
        print(*item)


if __name__ == '__main__':
    main()
