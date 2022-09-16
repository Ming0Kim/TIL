```python
from collections import deque

n, m, start = map(int, input().split())
visited = [0]*(n+1)
arr = [[] for _ in range(n+1)]
# print(arr)

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
# print(arr)

for i in range(n+1):
    arr[i].sort()

def dfs(start):
    print(start, end=' ')
    visited[start] = 1
    for i in arr[start]:
        if not visited[i]:
            dfs(i)
            visited[i] = 1

def bfs(start):
    q = deque([start])
    visited[start] = 1
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in arr[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1

dfs(start)
visited = [0]*(n+1)
print()
bfs(start)
```