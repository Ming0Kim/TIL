# 입력
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # N이 M보다 작을 때,
    if N < M:
        total = 0
        for i in range(M-N+1):
            sm = 0
            for j in range(N):
                sm += A[j]*B[i+j]
            if sm > total:
                total = sm
        print(f'#{tc+1} {total}')

    elif N > M:
        total = 0
        for i in range(N-M+1):
            sm = 0
            for j in range(M):
                sm += A[i+j]*B[j]
            if sm > total:
                total = sm
        print(f'#{tc+1} {total}')