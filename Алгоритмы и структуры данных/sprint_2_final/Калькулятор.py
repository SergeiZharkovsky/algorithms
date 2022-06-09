"""Калькулятор
Задание связано с обратной польской нотацией.
Она используется для парсинга арифметических выражений.
Еще её иногда называют постфиксной нотацией.
В постфиксной нотации операнды расположены перед знаками операций.
"""


OPERATORS = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x // y
}


class Stack:
    def __init__(self):
        self._array = []

    def push(self, element):
        self._array.append(element)

    def pop(self):
        if len(self._array) > 0:
            return self._array.pop()
        raise IndexError('Стек пуст')


def calculator(expression):
    stack = Stack()
    for i in expression:
        if i in OPERATORS:
            number_1, number_2 = stack.pop(), stack.pop()
            stack.push(OPERATORS[i](number_2, number_1))
        else:
            stack.push(int(i))
    return stack.pop()


def main():
    expression = input().split()
    print(calculator(expression))


if __name__ == '__main__':
    main()
