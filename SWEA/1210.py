# 입력
T = 10
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 마지막 줄 2인 값 찾아서 열 인덱스 반환
    for i in range(100):
        if arr[99][i] == 2:
            c = i

    # 마지막 열부터 시작
    r = 99

    # 빈 인덱스 만들어 이미 온 길 표시 / 왔던 길 중복 피하기 위해
    visit = [[0]*100 for _ in range(100)]
    visit[99][c] = 1

    # 양 옆에 1이 없을 시 1칸씩 올라오기
    while r != 0:
        if 0 <= c-1 < 100 and arr[r][c-1] == 1 and visit[r][c-1] == 0:
            c = c-1
            visit[r][c] = 1
            print(f'{r} {c}')
        elif 0 <= c+1 < 100 and arr[r][c+1] == 1 and visit[r][c+1] == 0:
            c = c+1
            visit[r][c] = 1
            print(f'{r} {c}')
        else:
            r = r-1
            visit[r][c] = 1
            print(f'{r} {c}')

    print(f'#{N} {c}')