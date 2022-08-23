def dfs(n, sm):
    global ans

    # 가지치기는 제일 위에서, 제일 마지막 순서로
    if sm > K:  # 이미 K값 초과해서 답을 찾을 가능성이 없는 경우
        return

    # 종료조건
    if n == N:
        if sm == K:
            ans += 1
        return

    # dfs(n+1) 호출
    dfs(n + 1, sm + lst[n])  # 사용하는 경우
    dfs(n + 1, sm)  # 사용하지 않는 경우


# T = 10
T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = 0

    dfs(0, 0)

    print(f'#{test_case} {ans}')