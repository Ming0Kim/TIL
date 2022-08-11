# 정렬함수
def bub(numbers):
    for i in range(N -1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return numbers