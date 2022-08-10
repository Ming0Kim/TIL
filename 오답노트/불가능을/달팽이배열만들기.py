T = int(input())

# 우 하 좌 상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for tc in range(T):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    i, j = 0, 0
    cnt = 0

    for k in range(1, N*N+1):
        arr[i][j] = k
        i += di[cnt]
        j += dj[cnt]

        # arr의 범위를 벗어나면,
        if i < 0 or j < 0 or i > N-1 or j > N-1 or arr[i][j] != 0:
            #실행취소
            i -= di[cnt]
            j -= dj[cnt]
            # %4 안하면 5678이런식으로 늘어남
            cnt = (cnt+1)%4
            i += di[cnt]
            j += dj[cnt]

    print(f'#{tc+1}')
    for row in arr:
        print(*row)
