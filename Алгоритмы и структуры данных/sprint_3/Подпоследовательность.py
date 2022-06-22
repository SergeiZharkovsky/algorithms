def subsequence(first_string, two_string):
    position = -1
    for i in first_string:
        position = two_string.find(i, position + 1)
        if position == - 1:
            return False
    return True


def main():
    first_string = input()
    two_string = input()
    print(subsequence(first_string, two_string))


if __name__ == '__main__':
    main()
