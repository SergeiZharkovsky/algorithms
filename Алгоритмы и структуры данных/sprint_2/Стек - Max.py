class StackMax:
    def __init__(self):
        self.items = []
        self.max = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if len(self.items) == 0:
            self.max.append(int(item))
        elif int(item) > self.max[len(self.items)-1]:
            self.max.append(int(item))
        else:
            self.max.append(self.max[len(self.items)-1])
        self.items.append(item)


def pop(self):
    if self.isEmpty():
        return 'error'
    self.max.pop()
    return self.items.pop()


def get_max(self):
    if self.isEmpty():
        return 'None'
    return self.max[len(self.items) - 1]


s = StackMax()
n = int(input())
result = []
for i in range(n):
    command = input().split()
    if command[0] == 'push':
        s.push(command[1])
    if command[0] == 'pop':
        if pop(s) == 'error':
            result.append('error')
    if command[0] == 'get_max':
        result.append(get_max(s))
for i in result:
    print(i)
