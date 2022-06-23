"""
Алла ошиблась при копировании из одной структуры данных в другую.
Она хранила массив чисел в кольцевом буфере.
Массив был отсортирован по возрастанию, и в нём можно было
найти элемент за логарифмическое время.
Алла скопировала данные из кольцевого буфера в обычный массив,
но сдвинула данные исходной отсортированной последовательности.
Теперь массив не является отсортированным.
Тем не менее, нужно обеспечить возможность находить в нем элемент за
O(log n).Можно предполагать, что в массиве только уникальные элементы.
"""


def broken_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        pivot = (left + right) // 2
        if nums[pivot] == target:
            return pivot

        if nums[left] <= nums[pivot]:
            if nums[left] <= target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        else:
            if nums[pivot] < target <= nums[right]:
                left = pivot + 1
            else:
                right = pivot - 1
    return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6


if __name__ == '__main__':
    test()
