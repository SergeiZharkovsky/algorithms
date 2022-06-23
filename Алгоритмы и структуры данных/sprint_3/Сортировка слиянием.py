def merge(arr, lf, mid, rg):
    l, r = lf, mid

    merged = []

    while l < mid and r < rg:
        if arr[l] <= arr[r]:
            merged.append(arr[l])
            l += 1
        else:
            merged.append(arr[r])
            r += 1

    for i in range(l, mid):
        merged.append(arr[i])

    for i in range(r, rg):
        merged.append(arr[i])

    return merged


def merge_sort(arr, lf, rg):
    if rg - lf == 1:
        pass
    elif rg - lf == 2:
        if arr[lf] > arr[rg - 1]:
            arr[lf], arr[rg - 1] = arr[rg - 1], arr[lf]
    else:
        mid = lf + (rg - lf) // 2
        merge_sort(arr, lf, mid)
        merge_sort(arr, mid, rg)

        tmp = merge(arr, lf, mid, rg)

        for i in range(lf, rg):
            arr[i] = tmp[i - lf]


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    assert merge([1, 0], 0, 1, 2) == [0, 1]
    assert merge([1, 2, 1, 3, 5], 0, 2, 5) == [1, 1, 2, 3, 5]
    assert merge([1, 2, 1, 3, 5], 0, 2, 4) == [1, 1, 2, 3]

    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


if __name__ == '__main__':
    test()
