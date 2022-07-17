A = int(input())
B = list(map(int, input().split()))
A = int((A-1)/2)
B.sort()
print(B[A])

