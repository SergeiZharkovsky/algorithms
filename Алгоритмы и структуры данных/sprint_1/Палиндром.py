import string

word = (input()).lower()
word = word.replace(' ', '')
for p in string.punctuation:
    if p in word:
        word = word.replace(p, '')
i = 0
flag = 1
while i < len(word) // 2:
    if (word[i] != word[len(word) - i - 1]):
        flag = 0
        break
    i += 1
if (flag == 0):
    print('False')
else:
    print('True')
