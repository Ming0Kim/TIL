## BFS(Breadth First Search)

---

- 그래프를 탐색하는 방법 두 가지
    - 깊이우선탐색(DFS)
    - 너비우선탐색(BFS)
- 너비우선탐색은 탐색시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후에, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식
- 인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비우선탐색을 진행해야 하므로, 선입선출 형태의 자료구조인 큐를 활용함
- 입력파라미터 : 그래프 G와 탐색시작점 v

```python
def BFS(G, v) : # 그래프 G, 탐색시작점 v
    visited = [0]*(n+1)                # n : 정점의 개수
    queue = []                         # 큐 생성
    queue.append(v)                    # 시작점 v를 큐에 삽입
    while queue :                      # 큐가 비어있지 않은 경우
        t = queue.pop(0)               # 큐의 첫번째 원소 반환
        if not visited[t]:             # 방문되지 않은 곳이라면
            visited[t] = True          # 방문한 것으로 표시
            visit(t)                   # 정점 t에서 할일
            for i in G[t] :            # t와 연결된 모든 정점에 대해
                if not visited[i] :    # 방문되지 않은 곳이라면
                    queue.append(i)    # 큐에 넣기
```

- 입력파라미터 : 그래프 G와 탐색시작점 v

```python
def BFS(G, v, n) : # 그래프 G, 탐색시작점 v
    visited = [0]*(n+1)                # n : 정점의 개수
    queue = []                         # 큐 생성
    queue.append(v)                    # 시작점 v를 큐에 삽입
    visited[v] = 1
    while queue :                      # 큐가 비어있지 않은 경우
        t = queue.pop(0)               # 큐의 첫번째 원소 반환
        visit(t)
        for i in G[t]:                 # t와 연결된 모든 정점에 대해
            if not visited[i]:         # 방문되지 않은 곳이라면
                queue.append(i)        # 큐에 넣기
                visited[i] = visited[t] + 1  # n으로부터 1만큼 이동
```

```python
def bfs(v, N):   #  v 시작정점, N 마지막 정점
    visited = [0]*(N+1)       # visited 생성
    q = []                    # 큐 생성
    q.append(v)               # 시작점 인큐
    visited[v] = 1            # 시작점 처리 표시
    while q:                  # 큐가 비어있지 않으면
        v = q.pop(0)          # 디큐
        print(v)              # visit(v)
        for w in adjList[v]:  # 인접하고 미방문(인큐되지 않은) 정점 w가 있으면
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1
V, E = map(int, input().split())
N = V+1         # N 정점 개수
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)
bfs(0, V)
```

```python
# SWEA 1219

def bfs(v, N, t) :  # v 시작, N 마지막 정점, t 목표 정점번호
    visited = [0] * (N+1)
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        v = q.pop(0)
        if v == t:        # visit(v)
            return visited[99]    # 목표 발견
        for w in adjList[v]:  # v에 인접하고 방문안한 w 인큐, 표시
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1
    return 0

T = 10
for _ in range(T):
    tc, E = map(int, input().split())
    arr = list(map(int, input().split()))

    adjList = [[] for _ in range(100)]
    for i in range(E):
        a, b = arr[i*2], arr[i*2 + 1]
        adjList[a].append(b)               # 단방향

    print(f'#{tc} {bfs(0, 99, 99)}')     # 시작, 마지막 정점, 목표 정점번호
```

```python
# 연습문제3 미로

def bfs(i ,j, N):
    visited = [[0]*N for _ in range(N)]
    q = []
    q.append((i, j))
    visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        if maze[i][j] == 3:  # 3번인가?? 도착지인가??
            return 1
        for di, dj in [[0, 1],[1, 0],[0, -1],[-1, 0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj] != 1 and visited[ni][nj]==0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return 0

t = int(input())
for tc in range(1, t+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sti, stj = i, j
                break
        if sti != -1:
            break

    print(f'#{tc} {bfs(sti, stj, N)}')
```