def sift_down(heap, idx):
    left = 2 * idx
    right = left + 1

    last_idx = len(heap) - 1

    if last_idx < left:
        return idx

    if right <= last_idx and heap[left] < heap[right]:
        index_largest = right
    else:
        index_largest = left

    if heap[idx] < heap[index_largest]:
        heap[idx], heap[index_largest] = heap[index_largest], heap[idx]
        return sift_down(heap, index_largest)
    return idx


def test():
    sample = [-1, 12, 1, 8, 3, 4, 7]
    res = sift_down(sample, 2)
    print(res)
    assert res == 5

    sample = [-1, 12, 9, 6, 2, 4, 1]
    sift_down(sample, 3)


if __name__ == '__main__':
    test()
