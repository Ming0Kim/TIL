# 90도씩 회전하는 함수!!
def rot(array):
    N = len(array)
    new = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            new[c][N-r-1] = array[r][c]
    return new

# 입력 초기화
T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    total = [[0]*3 for _ in range(N)]

    # 90도 회전
    arr90 = rot(arr)

    a = []
    for row in arr90:
        string = ''.join(row)
        a.append(string)

    for i in range(N):
        total[i][0] = a[i]

    # 180도 회전
    arr180 = rot(arr90)

    b = []
    for row in arr180:
        string = ''.join(row)
        b.append(string)

    for i in range(N):
        total[i][1] = b[i]

    # 270도 회전
    arr270 = rot(arr180)

    c = []
    for row in arr270:
        string = ''.join(row)
        c.append(string)

    for i in range(N):
        total[i][2] = c[i]

    print(f'#{tc+1}')
    for row in total:
        print(*row)