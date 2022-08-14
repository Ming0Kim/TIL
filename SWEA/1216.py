# 입력
T = 10
for tc in range(T):
    N = int(input())
    arr = [list(input()) for _ in range(100)]
    mx = []

    for x in range(100):
        # 주어진 문자열 내 N 길이 만큼의 회문이 몇 개 있는지 세기
        sm = 0

        # 행에서 찾기
        for row in arr:
            for i in range(101-x):
                word = row[i:i+x]
                if word == word[::-1]:
                    if len(word) > sm:
                        sm = len(word)

        # 열 lst 만들기
        cols = []
        for r in range(100):
            lst = []
            for c in range(100):
                lst.append(arr[c][r])
            cols.append(lst)

        # 열에서 찾기
        for col in cols:
            for k in range(101-N):
                word = col[k:k+x]
                if word == word[::-1]:
                    if len(word) > sm:
                        sm = len(word)

        # mx에 sm의 최대값 저장
        mx.append(sm)

    print(f'#{tc+1} {max(mx)}')
