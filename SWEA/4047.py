t = int(input())
for tc in range(1, t+1):
    string = input()
    shp = []
    for i in range(len(string)):
        if i%3 ==0:
            shp.append(string[i:i+3])
 
    if len(set(shp)) != len(shp):
        print(f'#{tc} ERROR')
    else:
        a = string.count('S')
        b = string.count('D')
        c = string.count('H')
        d = string.count('C')
        print(f'#{tc} {13-a} {13-b} {13-c} {13-d}')