class CustomNoItemsException(Exception):
    def __init__(self):
        pass


class ListQueue:
    def __init__(self):
        self.__array = []

    def put(self, element):
        self.__array.append(element)

    def size(self):
        return len(self.__array)

    def get(self):
        if self.size() == 0:
            raise CustomNoItemsException
        else:
            return self.__array.pop(0)


n = int(input())
s = ListQueue()

for _ in range(n):
    try:
        command = input().split(' ')
        if len(command) == 1:
            print(getattr(s, command[0])())
        else:
            getattr(s, command[0])(command[1])
    except CustomNoItemsException:
        print('error')
