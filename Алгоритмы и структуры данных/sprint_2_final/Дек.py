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


class Deque:
    def __init__(self, max_size):
        self.elem = [None] * max_size
        self.max_n = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_back(self, value):
        if self.size != self.max_n:
            self.elem[self.tail] = value
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            raise OverflowError

    def push_front(self, value):
        if self.size != self.max_n:
            self.elem[self.head - 1] = value
            self.head = (self.head - 1) % self.max_n
            self.size += 1
        else:
            raise OverflowError

    def pop_front(self):
        if self.is_empty():
            raise IndexError
        x = self.elem[self.head]
        self.elem[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def pop_back(self):
        if self.is_empty():
            raise IndexError
        x = self.elem[self.tail - 1]
        self.elem[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_n
        self.size -= 1
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
        except (OverflowError, IndexError):
            output = 'error'
        if output is not None:
            print(output)


if __name__ == '__main__':
    main()
