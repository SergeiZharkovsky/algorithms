"""
Улица, на которой хочет жить Тимофей, имеет длину n, то есть состоит
из n одинаковых идущих подряд участков.
На каждом участке либо уже построен дом, либо участок пустой.
Тимофей ищет место для строительства своего дома.
Он очень общителен и не хочет жить далеко от других людей,
живущих на этой улице.
Чтобы оптимально выбрать место для строительства, Тимофей хочет для каждого
участка знать расстояние до ближайшего пустого участка.
(Для пустого участка эта величина будет равна нулю —
расстояние до самого себя).
Ваша задача –— помочь Тимофею посчитать искомые расстояния.
Для этого у вас есть карта улицы.
Дома в городе Тимофея нумеровались в том порядке, в котором строились,
поэтому их номера на карте никак не упорядочены.
Пустые участки обозначены нулями.
"""


def get_distances(street, length_street):
    distance = []

    zero_index = None
    for i, house_num in enumerate(street):
        if house_num == 0:
            zero_index = i
            distance.append(0)
            continue
        if (house_num != 0 and zero_index is not None):
            distance.append(i - zero_index)
        else:
            distance.append(length_street)

    zero_index = None
    for i, house_num in reversed(list(enumerate(street))):
        if house_num == 0:
            zero_index = i
            continue
        if (
            house_num != 0 and zero_index is not None
            and distance[i] > zero_index - i
        ):
            distance[i] = (zero_index - i)

    return distance


def main():
    length_street = int(input())
    street = [int(num) for num in input().strip().split()]
    print(*get_distances(street, length_street))


if __name__ == '__main__':
    main()
