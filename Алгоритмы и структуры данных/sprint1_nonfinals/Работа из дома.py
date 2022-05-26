l = []


def convert(b):
    if (b == 0):
        return l
    dig = b % 2
    l.append(dig)
    convert(b // 2)


a = int(input())
convert(a)
l.reverse()
for i in range(len(l)):
    print(l[i], end='')
