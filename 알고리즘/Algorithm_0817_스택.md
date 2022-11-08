## 스택(stack)

---

### 스택의 특성

- 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조이다
- 스택에 저장된 자료는 선형 구조를 갖는다
    - 선형구조: 자료 간의 관계가 1대1의 관계
    - 비선형구조: 자료 간의 관계가 1대N의 관계 (예: 트리)
- 스택에 자료를 삽입하거나 스택에서 자료를 꺼낼 수 있다
- 마지막에 삽입한 자료를 가장 먼저 꺼냄
- **후입선출**
- 1, 2, 3 순으로 자료 삽입 / 꺼내면 역순으로 3, 2, 1

### 스택의 구현

스택을 프로그램에서 구현하기 위해서 필요한 자료구조와 연산

- 자료구조: 자료를 선형으로 저장할 저장소
    - 배열을 사용할 수 있다
    - 저장소 자체를 스택이라 부르기도 한다
    - 스택에서 마지막 삽입된 원소의 위치를 top이라 부른다
- 연산
    - `push` 삽입 : 저장소에 자료를 저장한다
    - `pop` 삭제 : 저장소에서 자료를 꺼낸다 꺼낸 자료는 삽입한 자료의 역순으로 꺼낸다
    - `isEmpty` : 스택이 공백인지 아닌지를 확인
    - `peek` : 스택의 top 에 잇는 item(원소)를 반환하는 연산
- 스택의 `push` 알고리즘
    - `append` 메소드를 통해 리스트의 마지막에 데이터를 삽입
    
    ```python
    def push(item):
    		s.append(item)
    
    # 참고
    def push(item, size):
    		global top
    		top += 1
    		if top==size:
    				print('overflow!')
    		else:
    				stack[top] = item
    
    size = 10
    stack = [0] * size
    top = -1
    
    push(10, size)
    top += 1         # push(20)
    stack[top] = 20
    ```
    
- 스택의 `pop` 알고리즘
    
    ```python
    def pop():
    		if len(s0 == 0 :
    				# underflow
    				return
    		else :
    				return s.pop(-1);
    
    # 참고
    def pop() :
    		global top
    		if top == -1:
    				print('underflow')
    				return 0
    		else :
    				top -= 1
    				return stack[top+1]
    print(pop())
    
    if top > -1:    #pop()
    		top -= 1
    		print(stack[top])
    ```
    

### 연습문제 1

- 스택을 구현해 봅니다.
- 구현한 스택을 이용하여 3개의 데이터를 스택에 저장하고 다시 3번 꺼내서 출력

```python
# 1
stackSize = 10
stack = [0] * stackSize
top = -1

top += 1
stack[top] = 1

top += 1
stack[top] = 2

top -= 1
temp = stack[top + 1]
print(temp)

temp = stack[top]
top -= 1
print(temp)

# 2
stack2 = []
stack2.append(10)
stack2.append(20)
print(stack2.pop())
print(stack2.pop())
```

### 스택 구현 고려 사항

- 1차원 배열을 사용하여 구현할 경우 구현이 용이하다는 장점이 있지만 스택의 크기를 변경하기가 어렵다는 단점
- 이를 해결하기 위한 방법으로 저장소를 동적으로 할당하여 스택을 구현하는 방법이 있다