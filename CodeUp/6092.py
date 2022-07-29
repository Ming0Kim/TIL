N = int(input())
num = list(map(int,input().split()))
empty_list = [0]*23

for i in num:
    empty_list[i-1] += 1

result = ' '.join(map(str, empty_list))
print(result)