def chk(bracket):
    stk = []
    for i in range(n):
        if bracket[i] in ['(', '[', '{', '<']:
            stk.append(bracket[i])
        elif bracket[i] == ')':
            if stk and stk[-1] == '(':
                stk.pop()
                continue
            else:
                return 0
        elif bracket[i] == ']':
            if stk and stk[-1] == '[':
                stk.pop()
                continue
            else:
                return 0
        elif bracket[i] == '}':
            if stk and stk[-1] == '{':
                stk.pop()
                continue
            else:
                return 0
        elif bracket[i] == '>':
            if stk and stk[-1] == '<':
                stk.pop()
                continue
            else:
                return 0
    if not stk:
        return 1
    else:
        return 0


t = 10
for tc in range(1, t+1):
    n = int(input())
    brac = list(input())
    print(f'#{tc} {chk(brac)}')