T = int(input())
for i in range(T):
    num=map(int,input().split())
    A = sum(n for n in num if n%2 ==1)
    print(f"#{i+1} {A}")