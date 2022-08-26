# 입력
T = int(input())
for tc in range(T):
    arr = [list(map(int, input().split())) for _ in range(9)]

    ox = 0

    # 총 9 개 네모 구간 합
    for i in range(3):
        for j in range(3):
            lsts = []
            for k in range(3):
                for a in range(3):
                    lsts += [arr[3*i+k][3*j+a]]
            for ll in range(1, 10):
                if ll not in lsts:
                    ox += 1

    # 행 합
    for row in arr:
        for rr in range(1, 10):
            if rr not in row:
                ox += 1


    # 열 합
    for r in range(9):
        lst =[]
        for c in range(9):
            lst += [arr[c][r]]
        for cc in range(1, 10):
            if cc not in lst:
                ox += 1

    if ox > 0:
        print(f'#{tc+1} 0')
    else:
        print(f'#{tc+1} 1')