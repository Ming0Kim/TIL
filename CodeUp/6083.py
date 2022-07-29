a, b, c = map(int,input().split())
s = 0

for i in range(a):
    for j in range(b):
        for k in range(c):
            s +=1
            print(f'{i} {j} {k}')
print(s)