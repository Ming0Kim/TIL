
# 무어 알고리즘 함수
def moore(string, sen):
    m = len(string)
    n = len(sen)
    i = 0
    while i <= n - m:
        # 인덱스가 0부터 시작하므로
        j = m - 1
        while j >= 0:
            if string[j] != sen[i + j]:
                move = find(string, sen[i + m - 1])
                break
            j = j - 1
        if j == -1:
            return '1'
        else:
            i += move
    return '0'

def find(pat, char):
    for i in range(len(pat) - 2, -1, -1):
        if pat[i] == char:
            return len(pat) - i - 1
    return len(pat)