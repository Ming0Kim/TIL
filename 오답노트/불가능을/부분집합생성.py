num = list(map(int,input().split()))
subnum = [[]]
for i in num:
    n = len(subnum)
    for j in range(n):
        subnum += [(subnum[j] + [i])]
print(subnum)

A = 12
arr = [i for i in range(1, A+1)]
result=[]

# 비트를 이용한 부분집합 생성
for i in range(1<<len(arr)):
    subset = []
    for j in range(len(arr)):
        if i & (1<<j):
            subset += [arr[j]]
    