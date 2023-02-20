#Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.

a, b = map(int, input().split())
c = 0
for i in range(a + b):
    if c:
        break
    for j in range(a + b):
        if i + j == a and i * j == b:
            c = 1
            print(*sorted([i, j]))
            break