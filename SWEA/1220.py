t = 10
for tc in range(1, t+1):
    n = input()
    arr = [list(input().split()) for _ in range(100)]

    slst = []
    for r in range(100):
        lst = []
        for c in range(100):
            lst.append(arr[c][r])
        slst.append(lst)

    cnt = 0
    for row in slst:
        string = ''.join([r for r in row if r != '0'])
        cnt += string.count('12')
    print(f'#{tc} {cnt}')