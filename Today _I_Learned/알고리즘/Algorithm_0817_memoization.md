## Memoization

---

- 앞의 예에서 피보나치 수를 구하는 함수를 재귀함수로 구현한 알고리즘 문제점 : 엄청난 중복 호출이 존재

### 메모이제이션

- 컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술
- **동적 계획법의 핵심이 되는 기술**
- 앞의 예에서 피보나치 수를 구하는 알고리즘에서 fibo(n)의 값을 계산하자마자 저장하면(memoize), 실행시간을 O(n)으로 줄일 수 있다

```python
# memo를 위한 배열을 할당하고 모두 0으로 초기화한다;
# memo[0]을 0으로 memo[1]는 1로 쵝화한다;

def fibo1(n) :
		if n >= 2 and len(memo) <= n:
				memo.append(fibo1(n-1) + fibo1(n-2))
		return memo[n]

memo = [0, 1]
```

## DP(Dynamic Programming)

---

### 동적 계획 알고리즘

- 그리디 알고리즘과 같이 **최적화 문제**를 해결하는 알고리즘이다
- 먼저 입력 크기가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여, 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘

### 피보나치 수 DP 적용

- 피보나치 수는 부분 문제의 답으로부터 본 문제의 답을 얻을 수 있으므로 최적 부분 구조로 이루어져 있다
1. 문제를 부분 문제로 분할한다
    1. Fibonacci(n)은 Fibonacci(n-1) 등등의 부분집하으로 나뉜다
2. 부분 문제로 나누는 일을 끝냈으면 가장 작은 부분 문제부터 해를 구한다
3. 그 결과는 테이블에 저장하고, ㅔㅌ이블에 저장된 부분 문제의 해를 이용하여 상위 문제의 해를 구한다

```python
# 재귀 함수
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

for i in range(101):
    print(i, fibo(i))

# 0 0
# 1 1
# 2 1
# 3 2
# 4 3
# 5 5
```

```python
# 동적 계획법
def fibo(n):
    if memo[n] == -1:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

memo = [-1]*101
memo[0] = 0
memo[1] = 1
for i in range(101):
    print(i, fibo(i))
```

```python
def fibo_dp(n):
    table[0] = 0
    table[1] = 1
    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]
    return

table = [0]*101
fibo_dp(100)
print(table[20])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc} {table[N]}')
```

### DP 구현방식

- recursive 방식 : fib1()
- iterative 방식 : fib2()
- memoization을 재귀적 구조에 사용하는 것보다 반복적 구조로 DP를 구현한 것이 성능 면에서 보다 효율적이다
- 재귀적 구조는 내부에 시스템 호출 스택을 사용하는 오버헤드가 발생하기 때문

## DFS(깊이우선탐색)

- 비선형구조인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요
- 두가지 방법
    - 깊이 우선 탐색(Depth First Search, DFS)
    - 너비 우선 탐색(Breadth First Search, BFS)
- 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회방법
- 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 후입선출 구조의 스택 사용
    1. 시작 정점 v를 결정하여 방문한다
    2. 정점 v에 인접한 정점 중에서
        1. 방문하지 않은 정점 w가 있으면, 정점 v를 스택에 push하고 정점 w를 방문한다. 그리고 w를 v로 하여 다시 2를 반복한다
        2. 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해서 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 2를 반복한다
    3. 스택이 공백이 될 때까지 2를 반복한다.

```markdown
visited[], stack[] 초기화
DFS(v)
		시작점 v 방문;
		visited[v] <-true;
		while {
				if ( v의 인접 정점 중 방문 안 한 정점 w가 있으면)
						push(v);
						v <- w; (w에 방문)
						visited[w] <- true;
				else
						if (스택이 비어있지 않으면)
								v <- pop(stack);
						else
								beak
		}
end DFS()
```