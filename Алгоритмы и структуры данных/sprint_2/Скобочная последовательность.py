class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]


stack = Stack()
n = list(input())
seq = {"(": ")", "[": "]", "{": "}"}


def is_correct_bracket_seq(n):
    for i in n:
        if i in seq.keys():
            stack.push(seq[i])
        elif stack.isEmpty():
            return False
        elif stack.peek() == i:
            stack.pop()
        else:
            return False
    return stack.isEmpty()


print(is_correct_bracket_seq(n))
