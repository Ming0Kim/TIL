## 연결리스트 (Linked List)

---

### 기본 개념

- **연결 리스트**란 선형 자료구조 중 배열과 함께 가장 기본이 되는 개념

<aside>
💡 **물리 메모리 어딘가에 흩뿌려진 노드(node)들이 서로 연결된 형태로 구성된 자료구조**

</aside>

- `노드(node)` : **데이터(값) + 다음 노드의 주소(포인터)** 를 담고 있는 형태
- 다음 노드의 주소를 노드 자체에서 담고있기 때문에 물리 메모리 상에서는 데이터가 여기저기 흩어져있더라도 서로 연결된 구조로 사용할 수 있음
- 동적으로 새 노드를 삽입하거나 삭제하기가 편하며, 그 관리 또한 편함

### 노드(node) 생성하기

- 값을 의미하는 data, 다음 노드의 주소를 의미하는 next 값을 모두 파라미터로 받음
- `data`= 0 , `next`= None

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # 값
        self.next = next  # 다음 노드의 주소
```

- 실제 노드 생성과 값과 포인터 출력

```python
# Node 생성 (data = 1)
node1 = ListNode(1)

# node의 값과 포인터 출력
print(node1.val) # 1
print(node1.next) # None
```

### 연결리스트 구현하기

- 위에서 생성한 노드를 바탕으로 연결리스트 클래스를 구현
- `head`란 연결 리스트 중에서도 가장 앞에 있는 노드
- `append`메서드
    - 계속 노드를 헤드부터 반복/ 갱신하면서, 노드의 next값이 None이 나올 때 그 위치 노드의 Next 값에 새로운 데이터 추가
- `print_all`메서드
    - 계속 노드를 헤드부터 반복/갱신하면서, val값을 출력해주는 방식

```python
class LinkedList:
    def __init__(self, data):
        self.head = ListNode(data)
        
    # 새로운 노드 추가
    def append(self, data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = ListNode(data)
        
    # 모든 노드 값 출력
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.val)
            cur = cur.next
```

### 노드 삽입하기 (add_node)

- add_node 함수를 확인하기 전에 노드를 가져올 수 있는 get_node 함수를 먼저 알아야함

```python
def get_node(self, index):
    count = 0
    node = self.head
    while count < index:
        count += 1
        node = node.next
    return node
```

- 1 → 2 → 3으로 되어있는 연결리스트에 노드 4를 추가해서 1 → 2 → 4 → 3으로 구성되어 있는 연결리스트를 만들고 싶을 때

✅ 노드 2 위치 (’내가 삽입하고 싶은 위치-1’의 인덱스)를 파악해서, next를 3에서 4로 바꿔줘야 함

✅ 그리고 새로 추가된 노드 4의 next는 3이 연결되도록 해야함

```python
def add_node(self, index, value):
    new_node = ListNode(value)
    if index == 0:
        new_node.next = self.head
        self.head = new_node
        return
    node = self.get_node(index-1)
    next_node = node.next
    node.next = new_node
    new_node.next = next_node
```

### 노드 삭제하기 (delete_note)

✅ 삭제하고 싶은 위치의 인덱스를 받으면, ‘그 위치-1’의 노드를 찾아가 next값을 삭제하고 싶은 위치의 다음 노드로 연결을 시켜줘야함

```python
def delete_node(self, index):
    if index == 0:
        self.head = self.head.next
        return
    node = self.get_node(index-1)
    node.next = node.next.next
```

### 연결 리스트의 시간

- 연결리스트는 배열과는 달리 특정 인덱스에 접근하기 위해 전체를 순서대로 읽어야함
- 따라서 상수 시간 내 접근이 불가능
- 연결리스트의 탐색시간 : `O(n)`
- 하지만, 연결리스트 노드의 삽입/삭제 : `O(1)`