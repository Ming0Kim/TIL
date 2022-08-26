# 검사 함수
def check(array):
    global ans
    for i in range(n-5+1):
        if array[i:i+5] == 'ooooo':
            ans = 'YES'
    return
 
t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(input())
    ans = 'NO'
    # 행
    for row in arr:
        check(row)
 
    # 열
    arrcol = []
    for r in range(n):
        col = ''
        for c in range(n):
            col += arr[c][r]
        arrcol.append(col)
    for coll in arrcol:
        check(coll)
 
    # 대각선
    dia = []
    for r in range(n-5+1):
        for c in range(n-5+1):
            diag = ''
            for k in range(5):
                diag += arr[r+k][c+k]
            dia.append(diag)
    for a in dia:
        check(a)
    # 대각선
    dia1 = []
    for c in range(n-5+1):
        for r in range(4, n):
            diag1 = ''
            for k in range(5):
                diag1 += arr[c+k][r-k]
            dia1.append(diag1)
    for c in dia1:
        check(c)
    print(f'#{tc} {ans}')