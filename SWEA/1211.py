# 입력
T = 10
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 마지막 줄 2인 값 찾아서 열 인덱스 저장
    idx = []
    for i in range(100):
        if arr[99][i] == 1:
            idx.append(i)

    # idx 각각의 요소들의 대하여
    cnt = []
    cnt_idx = []
    for c in idx:
        cn = 0

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
                cn += 1
            elif 0 <= c+1 < 100 and arr[r][c+1] == 1 and visit[r][c+1] == 0:
                c = c+1
                visit[r][c] = 1
                cn += 1
            else:
                r = r-1
                visit[r][c] = 1
                cn += 1
        # 이동 거리 수 cnt 리스트에 저장
        cnt.append(cn)
        cnt_idx.append(c)

    # 출력 : min값의 인덱스를 반환
    print(f'#{N} {cnt_idx[cnt.index(min(cnt))]}')