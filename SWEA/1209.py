for n in range(1, 11):
    # 입력
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    lst = []

    # 행 저장
    for i in range(100):
        lst.append(sum(arr[i]))

    # 열 저장
    for k in range(100):
        cnt = 0
        for j in range(100):
            cnt += arr[j][k]
        lst.append(cnt)

    # 대각선 \
    diag = 0
    for l in range(100):
        diag += arr[l][l]
    lst.append(diag)

    # 대각선 /
    onal = 0
    for m in range(100):
        onal += arr[m][100-m-1]
    lst.append(onal)
    
    print(f'#{n} {max(lst)}')