n = int(input())
list_a = []

for i in range(19):
    list_a.append([])
    for j in range(19):
        list_a[i].append(0)

for _ in range(n):
    a, b = map(int,input().split())
    list_a[a-1][b-1] = 1

for i in range(19):
    for j in range(19):
        print(list_a[i][j],end = ' ')
    print()