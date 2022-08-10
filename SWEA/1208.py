for j in range(1, 11):
    dump = int(input())
    lst = list(map(int,input().split()))
    for _ in range(dump):
        lst[lst.index(max(lst))] = max(lst) - 1
        lst[lst.index(min(lst))] = min(lst) + 1
    print(f'#{j} {max(lst) - min(lst)}')