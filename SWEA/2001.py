t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    lst = []
    # print(arr)


    # 행
    for r in range(n-m+1):
        for c in range(n-m+1):
            sm = 0
            # print()
            for i in range(m):
                for j in range(m):
                    # print(f'{r+i} {c+j}')
                    sm += arr[r+i][c+j]
            lst.append(sm)
    print(f'#{tc} {max(lst)}')