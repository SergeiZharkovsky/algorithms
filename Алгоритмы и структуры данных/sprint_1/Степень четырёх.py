number = int(input())
while True:
    if number == 1:
        flag = True
        break

    number = number / 4
    if (number % 4 > 0 and number != 1):
        flag = False
        break

print(flag)
