def sift_down(heap: list, sift_idx: int) -> int:
    left_idx = 2*sift_idx
    right_idx = left_idx + 1

    if len(heap) <= left_idx:
        return sift_idx

    if len(heap) <= right_idx:
        max_idx = left_idx
    else:
        max_idx = max([left_idx, right_idx], key=lambda idx: heap[idx])

    if heap[sift_idx] >= heap[max_idx]:
        return sift_idx
    else:
        heap[sift_idx], heap[max_idx] = heap[max_idx], heap[sift_idx]
        return sift_down(heap, max_idx)


def test():
    sample = [-1, 12, 1, 8, 3, 4, 7]
    assert sift_down(sample, 2) == 5

    sample = [-1, 4, 9, 6, 2, 4, 1]
    assert sift_down(sample, 1) == 2
