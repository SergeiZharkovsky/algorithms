symbols = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


def combinations(numbers):
    result = ['']
    for char in numbers:
        letters = symbols.get(char, '')
        result = [prefix+letter for prefix in result for letter in letters]
    print(*result)


numbers = input()
combinations(numbers)
