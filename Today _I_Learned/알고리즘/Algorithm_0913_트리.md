# 트리

강의날짜: 2022/09/13
공부유형: 강의
복습: No
분야: 알고리즘
작성일시: 2022년 9월 13일 오전 10:48
태그: 이진탐색트리, 이진트리, 트리, 힙
편집일시: 2022년 9월 13일 오후 12:17

## 트리

---

### 트리의 개념

- 비선형 구조
- 원소들 간에 1:N 관계를 가지는 자료구조
- 원소들 간에 계층관계를 가지는 계층형 자료구조
- 상위원소에서 하위 원소로 내려가면서 확장되는 트리(나무)모양의 구조

### 정의

- 한 개 이상의 노드로 이루어진 유한 집합이며 다음 조건을 만족한다.
    - 노드 중 최상위 노드를 루트(root)라 한다
    - 나머지 노드들은 ㅜ(≥0)개의 분리 집합 T1,…,TN으로 분리될 수 있다
- 이들 T1,…,TN은 각각 하나의 트리가 되며(재귀적 정의) 루트의 부 트리(subtree)라 한다

![Untitled](%E1%84%90%E1%85%B3%E1%84%85%E1%85%B5%2046fcb3e432774c30bc82f1d61f6ada84/Untitled.png)

### 용어정리

- 노드(`node`) : 틀의 원소
    - 트리 T의 노드 : A,B,C,D,E,F,G,H,I,J,K
- 간선(`edge`) : 노드를 연결하는 선/ 부모 노드와 자식노드를 연결
- 루트 노드(`root node`) : 트리의 시작 노드
    - 트리 T의 루트노드 - A

![Untitled](%E1%84%90%E1%85%B3%E1%84%85%E1%85%B5%2046fcb3e432774c30bc82f1d61f6ada84/Untitled%201.png)

- 형제 노드(`sibling node`) : 같은 부모 노드의 자식 노드들
    - B, C, D는 형제 노드
- 조상 노드 : 간선을 따라 루트 노드까지 이르는 경로에 있는 모든 노드들
    - K의 조상노드 : F, B, A
- 서브 트리(`subtree`) : 부모 노드와 연결된 간선을 끊었을 때 생성되는 트리
- 자손 노드 : 서브 트리에 있는 하위 레벨의 노드들
    - B의 자손노드 : E, F, K
    
    ![Untitled](%E1%84%90%E1%85%B3%E1%84%85%E1%85%B5%2046fcb3e432774c30bc82f1d61f6ada84/Untitled%202.png)
    
- 차수(`degree`)
    - 노드의 차수 : 노드에 연결된 자식 노드의 수
        - B의 차수 : 2, C의 차수 : 1
    - 트리의 차수 : 트리에 있는 노드의 차수 중에서 가장 큰 값
        - 트리 T의 차수 : 3
    - 단말 노드(리프 노드) : 차수가 0인 노드 자식 노드가 없는 노드
- 높이
    - 노드의 높이 : 루트에서 노드에 이르는 간선의 수, 노드의 레벨
        - B의 높이 : 1, F의 높이 : 2
    - 트리의 높이: 트리에 있는 노드의 높이 중에서 가장 큰 값. 최대 레벨
        - 트리 T의 높이 : 3
        
        ![Untitled](%E1%84%90%E1%85%B3%E1%84%85%E1%85%B5%2046fcb3e432774c30bc82f1d61f6ada84/Untitled%203.png)
        

## 이진트리

---

- 모든 노드들이 2개의 서브트리를 갖는 특별한 형태의 트리
- 각 노드가 자식 노드를 최대한 2개 까지만 가질 수 잇는 트리
    - 왼쪽 자식 노드(`left child node`)
    - 오른쪽 자식 노드(`right child node`)
- 이진 트리의 예

![Untitled](%E1%84%90%E1%85%B3%E1%84%85%E1%85%B5%2046fcb3e432774c30bc82f1d61f6ada84/Untitled%204.png)

### 특성

- 레벨 i에서 노드의 최대 개수는 2^i개
- 높이가 h인 이진 트리가 가질 수 있는 노드의 최소 개수는 (h+1)개가 되며, 최대 개수는 (2^(h+1) -1)개가 된다.

![Untitled](%E1%84%90%E1%85%B3%E1%84%85%E1%85%B5%2046fcb3e432774c30bc82f1d61f6ada84/Untitled%205.png)

### 종류

- 포화 이진 트리(`Full Binary Tree`)
    - 모든 레벨에 노드가 포화상태로 차있는 이진트리
    - 높이가 h일때, 최대의 노드 개수인(2^(h+1)-1)의 노드를 가진 이진트리
        - 높이 3일때 2^(3+1)-1 = 15개의 노드
    - 루트를 1번으로 하여 2^(h+1)-1까지 정해진 위치에 대한 노드 번호를 가짐
    
    ![Untitled](%E1%84%90%E1%85%B3%E1%84%85%E1%85%B5%2046fcb3e432774c30bc82f1d61f6ada84/Untitled%206.png)
    
- 완전 이진 트리(`Complete Binary Tree)
    - 높이가 h이고 노드 수가 n개일 때 (단, h+1 ≤ n < 2^(h+1)-1), 포화 이진 트리의 노드 번호 1번부터 n번까지 빈 자리가 없는 이진 트리
    - 노드가 10개인 완전 이진 트리
    
    ![Untitled](%E1%84%90%E1%85%B3%E1%84%85%E1%85%B5%2046fcb3e432774c30bc82f1d61f6ada84/Untitled%207.png)
    
- 편향 이진 트리(`Skewed binary Tree`)
    - 높이 h에 대한 최고 개수의 노드를 가지면서 한쪽 방향의 자식 노드만을 가진 이진 트리
        - 왼쪽 편향 이진트리, 오른쪽 편향 이진트리
        
        ![Untitled](%E1%84%90%E1%85%B3%E1%84%85%E1%85%B5%2046fcb3e432774c30bc82f1d61f6ada84/Untitled%208.png)
        

### 순회

- 순회(`traversal`) : 트리의 노드들을 체계적으로 방문하는 것
- 3가지의 기본적인 순회방법
    - 전위순회(`preorder traversal`) : VLR
        - 부모노드 방문 후, 자식노드를 좌, 우 순서로 방문한다
    - 중위순회(`inorder traversal`) : LVR
        - 왼쪽 자식노드, 부모노드, 오른쪽 자식노드 순으로 방문한다
    - 후위순회(`postorder raversal`) : LRV
        - 자식노드를 좌우 순서로 방문한 후, 부모노드로 방문한다
        
        ![Untitled](%E1%84%90%E1%85%B3%E1%84%85%E1%85%B5%2046fcb3e432774c30bc82f1d61f6ada84/Untitled%209.png)
        

### 전위 순회(preorder traversal)

- 수행 방법
    1. 현재 노드 n을 방문하여 처리한다 → **V**
    2. 현재 노드 n의 왼쪽 서브트리로 이동한다 → **L**
    3. 현재 노드 n의 오른쪽 서브트리로 이동한다 → **R**
- 전위 순회 알고리즘

![Untitled](%E1%84%90%E1%85%B3%E1%84%85%E1%85%B5%2046fcb3e432774c30bc82f1d61f6ada84/Untitled%2010.png)

- 전위순회 예

![Untitled](%E1%84%90%E1%85%B3%E1%84%85%E1%85%B5%2046fcb3e432774c30bc82f1d61f6ada84/Untitled%2011.png)

### 중위 순회(inorder traversal)

- 수행 방법
    1. 현재 노드 n의 왼쪽 서브트리로 이동한다 → **L**
    2. 현재 노드 n을 방문하여 처리한다 → **V**
    3. 현재 노드 n의 오른쪽 서브트리로 이동한다 → **R**
- 중위 순회 알고리즘

![Untitled](%E1%84%90%E1%85%B3%E1%84%85%E1%85%B5%2046fcb3e432774c30bc82f1d61f6ada84/Untitled%2012.png)

- 중위 순회의 예

![Untitled](%E1%84%90%E1%85%B3%E1%84%85%E1%85%B5%2046fcb3e432774c30bc82f1d61f6ada84/Untitled%2013.png)

### 후위 순회(postorder traversal)

- 수행 방법
    1. 현재 노드 n의 왼쪽 서브트리로 이동한다 → **L**
    2. 현재 노드 n의 오른쪽 서브트리로 이동한다 → **R**
    3. 현재 노드 n을 방문하여 처리한다 → **V**
- 후위 순회 알고리즘

![Untitled](%E1%84%90%E1%85%B3%E1%84%85%E1%85%B5%2046fcb3e432774c30bc82f1d61f6ada84/Untitled%2014.png)

- 후위 순회의 예

![Untitled](%E1%84%90%E1%85%B3%E1%84%85%E1%85%B5%2046fcb3e432774c30bc82f1d61f6ada84/Untitled%2015.png)

### 순회 연습 문제

![Untitled](%E1%84%90%E1%85%B3%E1%84%85%E1%85%B5%2046fcb3e432774c30bc82f1d61f6ada84/Untitled%2016.png)

## 이진트리의 표현

---

### 배열을 이용한 이진 트리의 표현

- 이진 트리에 각 노드 번호를 다음과 같이 부여
- 루트의 번호를 1로 함
- 레벨 n에 있는 노드에 대하여 왼쪽부터 오른쪽으로 2^n부터 2^(n+1)-1까지 번호를 차례로 부여

![Untitled](%E1%84%90%E1%85%B3%E1%84%85%E1%85%B5%2046fcb3e432774c30bc82f1d61f6ada84/Untitled%2017.png)

- 노드 번호의 성질

![Untitled](%E1%84%90%E1%85%B3%E1%84%85%E1%85%B5%2046fcb3e432774c30bc82f1d61f6ada84/Untitled%2018.png)

![Untitled](%E1%84%90%E1%85%B3%E1%84%85%E1%85%B5%2046fcb3e432774c30bc82f1d61f6ada84/Untitled%2019.png)

![Untitled](%E1%84%90%E1%85%B3%E1%84%85%E1%85%B5%2046fcb3e432774c30bc82f1d61f6ada84/Untitled%2020.png)

### 이진트리의 저장

![Untitled](%E1%84%90%E1%85%B3%E1%84%85%E1%85%B5%2046fcb3e432774c30bc82f1d61f6ada84/Untitled%2021.png)

![Untitled](%E1%84%90%E1%85%B3%E1%84%85%E1%85%B5%2046fcb3e432774c30bc82f1d61f6ada84/Untitled%2022.png)

![Untitled](%E1%84%90%E1%85%B3%E1%84%85%E1%85%B5%2046fcb3e432774c30bc82f1d61f6ada84/Untitled%2023.png)

### 배열을 이용한 이진 트리의 표현의 단점

- 편향 이진 트리의 경우에 사용하지 않는 배열 원소에 대한 메모리 공간 낭비 발생
- 트리의 중간에 새로운 노드를 삽입하거나 기존의 노드를 삭제할 경우 배열의 크기 변경 어려워 비효율적

```python
'''
정점 번호 V = 1~(E+1)
간선 수
부모-자식 수
4
1 2 1 3 3 4 3 5
'''
def find_root(V):
    for i in range(1, V + 1):
        if par[i] == 0:  # 부모가 없으면 root
            return i

def preorder(n):    # 전위순회
    if n:
        print(n)    # visit(n)
        preorder(ch1[n])
        preorder(ch2[n])

def inorder(n):     # 중위순회
    if n:
        inorder(ch1[n])
        print(n)    # visit(n)
        inorder(ch2[n])

def postorder(n):   # 후위순회
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n)    # visit(n)
E = int(input())
arr = list(map(int, input().split()))
V = E + 1
root = 1
# 부모를 인덱스로 자식 번호 저장
ch1 = [0]*(V + 1)
ch2 = [0]*(V + 1)
# 자식을 인덱스로 부모 번호 저장
par = [0]*(V + 1)
for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0:   # 아직 자식이 없으면
        ch1[p] = c    # 자식 1로 저장
    else:
        ch2[p] = c
    par[c] = p
root = find_root(V)
print(root)
# print(ch1)
# print(ch2)
#
# preorder(root)
# inorder(root)
# postorder(root)
```

### 트리의 표현 - 연결리스트

- 배열을 이용한 이진 트리의 표현의 단점을 보완하기 위해 연결리스트를 이용하여 트리를 표현할 수 있다
- 연결 자료구조를 이용한 이진트리의 표현
    - 이진 트리의 모든 노드는 최대 2개의 자식 노드를 가지므로 일정한 구조의 단순 연결리스트노드를 사용하여 구현
    
    ![Untitled](%E1%84%90%E1%85%B3%E1%84%85%E1%85%B5%2046fcb3e432774c30bc82f1d61f6ada84/Untitled%2024.png)
    
- 완전이진트리의 연결리스트 표현

![Untitled](%E1%84%90%E1%85%B3%E1%84%85%E1%85%B5%2046fcb3e432774c30bc82f1d61f6ada84/Untitled%2025.png)

```python
def pre(n):
    if n <= size:
        print(tree[n])
        pre(2*n)
        pre(2*n+1)

tree = [0, 'A', 'B', 'C', 'D', 'E', 'F']   # 완전이진트리
size = len(tree) - 1                       # 마지막 정점 번호
pre(2)
```