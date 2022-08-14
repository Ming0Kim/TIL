# 딕셔너리 컴프리헨션을 이용해 인덱스 값 부여
numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

dict_idx = {v:k for k, v in enumerate(numbers)}

# 입력 값 초기화
T = int(input())
for _ in range(T):
    tc, N = input().split()
    lst = input().split()

    # 입력된 lst를 딕셔너리를 통해 index값만 도출
    numlist = []
    for i in lst:
        numlist.append(dict_idx[i])

    # numlist를 정렬
    numlist.sort()

    # 정렬된 numlist에서 다시 키 값 반환
    dict_idx1 = {v:k for k,v in dict_idx.items()}
    print(tc)
    for j in numlist:
        print(dict_idx1[j], end=' ')