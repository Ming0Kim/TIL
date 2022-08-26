def tf(A):
    global ans
    for a in A:
        if a < 0 :
            ans = 'Impossible'
            break
        else:
            ans = 'Possible'
    for ls in lst:
        if ls == 0:
            ans = 'Impossible'
    return
 
t = int(input())
for tc in range(1, t+1):
    n, m, k = map(int, input().split())
    lst = list(map(int, input().split()))
 
    # 사람이 오는 마지막 시간
    last = max(lst)
 
    # 붕어빵이 시간(index)별 개수가 몇 개 있을지
    fish = [0]*11112  # 1초는 1의 인덱스를 가지게 0초에는 0 설정
 
    for i in range(1, last+1):
        if m * i <= last:
            fish[m * i] = k
        fish[i] += fish[i-1]
        for ls in lst:
            if i == ls:
                fish[ls] -= 1
 
    tf(fish)
    print(f'#{tc} {ans}')