def get_longest_word(sentence):
    words = sentence.split()
    word_lengths = [len(word) for word in words]
    length_of_longest_word = max(word_lengths)
    index_longest_word = word_lengths.index(length_of_longest_word)
    return length_of_longest_word, words[index_longest_word]


def main():
    input()
    sentence = input()
    length, word = get_longest_word(sentence)
    print(word)
    print(length)


if __name__ == '__main__':
    main()
