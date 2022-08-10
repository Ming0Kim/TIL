num = list(map(int,input().split()))
subnum = [[]]
for i in num:
    n = len(subnum)
    for j in range(n):
        subnum += [(subnum[j] + [i])]
print(subnum)