"""Дек.
Гоша реализовал структуру данных Дек,
максимальный размер которого определяется заданным числом.
Методы push_back(x), push_front(x), pop_back(), pop_front() работали корректно.
Но, если в деке было много элементов,
программа работала очень долго.
Дело в том, что не все операции выполнялись за O(1). Помогите Гоше!
Напишите эффективную реализацию.
Внимание: при реализации используйте кольцевой буфер.
"""


class NoItemsException(Exception):
    def __init__(self):
        pass


class MaxItemsException(Exception):
    def __init__(self):
        pass


class Deque:
    def __init__(self, max_size):
        self._array = [None] * max_size
        self._max_size = max_size
        self._head = 0
        self._tail = 0
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def _get_index_by_method(self, name):
        results = {
            'push_front': self._head - 1,
            'push_back': self._tail + 1,
            'pop_front': self._head + 1,
            'pop_back': self._tail - 1
        }
        index = results.get(name) % self._max_size
        return index

    def _push(self, idx, value):
        if self._size >= self._max_size:
            raise MaxItemsException

        self._array[idx] = value
        self._size += 1

    def push_back(self, value):
        self._push(self._tail, value)
        self._tail = self._get_index_by_method(self.push_back.__name__)

    def push_front(self, value):
        new_head = self._get_index_by_method(self.push_front.__name__)
        self._push(new_head, value)
        self._head = new_head

    def _pop(self, idx):
        if self.is_empty():
            raise NoItemsException

        self._size -= 1
        x = self._array[idx]
        self._array[idx] = None
        return x

    def pop_front(self):
        x = self._pop(self._head)
        self._head = self._get_index_by_method(self.pop_front.__name__)
        return x

    def pop_back(self):
        new_tail = self._get_index_by_method(self.pop_back.__name__)
        x = self._pop(new_tail)
        self._tail = new_tail
        return x


def main():
    command_length = int(input())
    max_size = int(input())
    deque = Deque(max_size)
    for _ in range(command_length):
        command, *value = input().split()
        result = getattr(deque, command)
        try:
            output = result(*value)
        except (MaxItemsException, NoItemsException):
            output = 'error'
        if output is not None:
            print(output)


if __name__ == '__main__':
    main()
