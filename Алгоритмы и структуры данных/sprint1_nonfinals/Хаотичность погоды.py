n = int(input())
sp = input().split()


for i in range(n):
    sp[i] = int(sp[i])
count = 0
sp.insert(0, -273)
sp.append(-273)
i = 1
while i < n + 1:
    if ((sp[i] > sp[i-1]) and (sp[i] > sp[i+1])):
        count += 1
    i += 1
print(count)
