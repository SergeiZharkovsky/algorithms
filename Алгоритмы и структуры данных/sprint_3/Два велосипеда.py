def two_bicycles(money, price, left, right):
    # промежуток пуст
    if right <= left and left != 0:
        return -1
    # промежуток не пуст
    mid = (left + right) // 2
    if (money[mid] >= price and (money[mid - 1] < price or mid == 0)):
        return mid + 1
    # искомый элемент меньше центрального
    elif price <= money[mid]:
        # значит ищем в левой половине
        return two_bicycles(money, price, left, mid)
        # потом ищем в правой половине
    else:
        return two_bicycles(money, price, mid + 1, right)

days = int(input())
money = [int(num) for num in input().split(' ')]
price = int(input())
# запускаем двоичный поиск на всей длине массива
print(two_bicycles(money, price, left = 0, right = len(money)), end=' ')
print(two_bicycles(money, price * 2, left = 0, right = len(money)), end=' ')
