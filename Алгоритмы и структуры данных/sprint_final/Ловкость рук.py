"""
Гоша и Тимофей нашли необычный тренажёр для скоростной печати
и хотят освоить его.
Тренажёр представляет собой поле из клавиш 4× 4,
в котором на каждом раунде появляется конфигурация цифр и точек.
На клавише написана либо точка, либо цифра от 1 до 9.
В момент времени t игрок должен одновременно нажать на все клавиши,
на которых написана цифра t. Гоша и Тимофей могут нажать
в один момент времени на k клавиш каждый.
Если в момент времени t были нажаты все нужные клавиши,
то игроки получают 1 балл.
Найдите число баллов, которое смогут заработать Гоша и Тимофей,
если будут нажимать на клавиши вдвоём.
"""


def data_input():
    k = int(input()) * 2
    symbols = ''.join(input() for i in range(4)).replace('.', '')
    return k, symbols


def calculations():
    k, symbols = data_input()
    numbers = []
    scores = 0
    for i in range(1, 10):
        count = symbols.count(str(i))
        numbers.append(count)

    for i, elem in enumerate(numbers):
        if elem == 0:
            continue
        if int(elem) <= k:
            scores += 1
    print(scores)


if __name__ == '__main__':
    calculations()
