t = int(input())
for i in range(1, t + 1) :
    n = int(input())
    result = ''
    for j in range(n) :
        al, count = input().split()
        result += al * int(count)

    num = 0
    print('#%d' % i)
    for j in range(len(result)) :
        print(result[j], end='')
        num += 1
        if num == 10 :
            num = 0
            print()