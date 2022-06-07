class MyQueueSized:
    def __init__(self, max_size):
        self.queue = [None for _ in range(n)]
        self.max_n = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        if self.size < self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
            return 'OK'
        else:
            return 'error'

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.head]

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x


n = int(input())
queue_length = int(input())
s = MyQueueSized(queue_length)

res = []
for i in range(n):
    command = input().split()
    if command[0] == 'push':
        a = s.push(command[1])
        if a == 'error':
            res.append(a)
    if command[0] == 'pop':
        res.append(s.pop())

    if command[0] == 'peek':
        res.append(s.peek())

    if command[0] == 'size':
        res.append(s.size)

for x in res:
    print(x)
