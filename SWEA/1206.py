
for i in range(1,11):
    N = int(input())
    building = list(map(int,input().split()))

    house = 0
    for j in range(2, N-2):
        if building[j] > max(building[j-2], building[j-1], building[j+1], building[j+2]):
            house += building[j] - max(building[j-2], building[j-1], building[j+1], building[j+2])
    print(f'#{i} {house}')
