T = int(input())
for i in range(0,T):
    num = list(map(int, input().split()))
    A = round(sum(num)/10)
    print(f"#{i+1} {A}")