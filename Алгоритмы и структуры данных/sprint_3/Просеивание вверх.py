def sift_up(heap: list, sift_idx: int) -> int:
    if sift_idx <= 1:
        return sift_idx

    parent_idx = sift_idx // 2

    if heap[parent_idx] < heap[sift_idx]:
        heap[parent_idx], heap[sift_idx] = heap[sift_idx], heap[parent_idx]
        return sift_up(heap, parent_idx)
    else:
        return sift_idx


def test():
    sample = [-1, 12, 6, 8, 3, 15, 7]
    assert sift_up(sample, 5) == 1
