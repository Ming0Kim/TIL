## 재귀호출

---

### 재귀호출

- 자기 자신을 호출하여 순환 수행되는 것
- 함수에서 실행해야 하는 작업을 특성에 따라 일반적인 호출방식보다 재귀호출방식을 사용하여 함수를 만들면 프로그램의 크기를 줄이고 간단하게 작성
    - 재귀 호출의 예) factorial
    - - n에 대한 factorial: 1부터 n까지의 모든 자연수를 곱하여 구하는 연산
    
    ```python
    n! = n x (n-1)!
    		(n-1)! = (n-1) x (n-2)!
    		(n-2)! = (n-2) x (n-3)!
    ...
    		2! = 2 x 1!
    		1! = 1
    ```
    
    - 마지막에 구한 하위 값을 이용하여 상위 값을 구하는 작업을 반복
- 0, 1로 시작하고 이전의 두 수 합을 다음 항으로 하는 수열 : 피보나치
- 피보나치 수열의 i번 째 값을 계산하는 함수 F를 정의하면 다음과 같다
    - F0 = 0, F1 = 1
    - Fi = Fi-1 + Fi-2 for i ≥ 2
- 위의 정의로부터 피보나치 수열의 i번째 항을 반환하는 함수를 재귀함수로 구현할 수 있음

```python
def f(i, N):   # i 현재 단계, N 목표 단계
    if i ==N:
        print(i)
        return
    else:
        print(i)
        f(i+1, N)

f(0,3)
```

```python
# 크기가 N인 배열의 모든 원소에 접근하는 재귀함수
def f(i, N):
    if i == N:      # 배열을 벗어남
        return
    else:           # 남은 원소가 있는 경우
        f(i+1, N)   # 다음 원소로 이동

N = 3
A = [1, 2, 3]
f(0, N)             # 0번 원소부터 N개의 원소에 접근
print(B)
```

```python
def f(i, N): # i 현재 단계, N 목표 단계
    if i == N:
        print(i)
        return
    else:
        print(i)
        f(i+1, N)
f(0, 1000)

# RecursionError: maximum recursion depth exceeded while calling a Python object
# 재귀문제는 1000번 가량을 넘어가지 않음. 열댓번 정도
```