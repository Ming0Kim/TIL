t = int(input())
for tc in range(1, t+1):
    n, p = (map(int, input().split()))
    a = n//p
    b = n%p
    print(f'#{tc} {a**(p-b)*(a+1)**b}')
