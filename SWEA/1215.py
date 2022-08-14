# 입력
T = 10
for tc in range(T):
    N = int(input())
    arr = [list(input()) for _ in range(8)]

    # 주어진 문자열 내 N 길이 만큼의 회문이 몇 개 있는지 세기
    sm = 0

    # 행에서 찾기
    for row in arr:
        for i in range(9-N):
            word = row[i:i+N]
            if word == word[::-1]:
                sm += 1

    # 열 lst 만들기
    cols = []
    for r in range(8):
        lst = []
        for c in range(8):
            lst.append(arr[c][r])
        cols.append(lst)

    # 열에서 찾기
    for col in cols:
        for k in range(9-N):
            word = col[k:k+N]
            if word == word[::-1]:
                sm += 1

    print(f'#{tc+1} {sm}')