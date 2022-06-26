def polynomial_hash(base, module, string):
    hash = 0
    for char in string:
        hash = (hash * base + ord(char)) % module
    return hash


def main():
    base = int(input())
    module = int(input())
    string = input()
    print(polynomial_hash(base, module, string))


if __name__ == '__main__':
    main()
