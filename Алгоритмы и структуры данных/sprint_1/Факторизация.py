number = int(input())
d = 2

while d * d <= number:
    if number % d == 0:
        print(d, end=' ')
        number //= d
    else:
        d += 1
if number > 1:
    print(number)
