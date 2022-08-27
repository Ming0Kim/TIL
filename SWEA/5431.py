t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    lst = set(list(map(int, input().split())))
    slst = set(range(1,n+1))
    result = slst-lst
    print(f'#{tc}',end=' ')
    print(*result)