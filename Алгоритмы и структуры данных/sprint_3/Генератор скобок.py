def gen_binary(count, left, right, prefix):
    if left == 0 and right == 0:
        print(prefix)
    else:
        if left > 0:
            gen_binary(count + 1, left - 1, right, prefix + '(')
        if (count > 0 and right > 0):
            gen_binary(count - 1, left, right - 1, prefix + ')')


n = int(input())
count = 0
left = n
right = n
gen_binary(count, left, right, '')
