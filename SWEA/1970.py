t = int(input())
for tc in range(1, t+1):
    money = int(input())
    cash = [0]*8
    if money >= 50000:
        cnt = 0
        while money >= 50000:
            money -= 50000
            cnt += 1
        cash[0] = cnt
    if money >= 10000:
        cnt = 0
        while money >= 10000:
            money -= 10000
            cnt += 1
        cash[1] = cnt
    if money >= 5000:
        cnt = 0
        while money >= 5000:
            money -= 5000
            cnt += 1
        cash[2] = cnt
    if money >= 1000:
        cnt = 0
        while money >= 1000:
            money -= 1000
            cnt += 1
        cash[3] = cnt
    if money >= 500:
        cnt = 0
        while money >= 500:
            money -= 500
            cnt += 1
        cash[4] = cnt
    if money >= 100:
        cnt = 0
        while money >= 100:
            money -= 100
            cnt += 1
        cash[5] = cnt
    if money >= 50:
        cnt = 0
        while money >= 50:
            money -= 50
            cnt += 1
        cash[6] = cnt
    if money >= 10:
        cnt = 0
        while money >= 10:
            money -= 10
            cnt += 1
        cash[7] = cnt


    print(f'#{tc}')
    print(*cash)