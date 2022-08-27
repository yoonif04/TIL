## 0. 트리

----

1. 트리

2. 이진 트리

3. 이진탐색 트리

4. 힙

## 1. 트리

----

1. 트리의 **개념**
   
   * 비선형 구조
   
   * 원소들 간에 **1:n 관계**를 가지는 자료구조
   
   * 원소들 간 계층관계를 가지는 계층형 자료구조
   
   * 상위 원소 -> 하위 원소로 내려가면서 확장되는 트리모양의 구조

2. 트리 - **정의**
   
   * 한 개 이상의 노드로 이루어진 유한 집합, 다음 조건 만족
     
     * 최상위 노드 : 루트(root)
     
     * 나머지 노드 -> n(>=0)개의 분리 집합 T1,...,TN으로 분리될 수 있다.
   
   * 이들 T1,...,TN은 각각 하나의 트리가 됨(재귀적 정의), 루트의 부트리(subtree)라고함
   
   * 용어
     
     - 정점(node, vertex)
     
     - 단말노드 또는 잎(leaf)노드

3. 트리 - **용어정리**
   
   * **노드(node)** : 트리의 원소
   
   * **간선(edge)** : 노드를 연결하는 선. 부모 노드와 자식 노드 연결
   
   * **루트 노드(root node)** : 트리의 시작 노드
   
   * **형제 노드(sibling node)** : 같은 부모 노드의 자식 노드들
   
   * **조상 노드** : 간선을 따라 루트 노드까지 이르는 경로에 있는 모든 노드들
   
   * **서브 트리(subtree)** : 부모 노드와 연결된 간선을 끊었을 때 생성되는 트리
   
   * **자손 노드** : 서브 트리에 있는 하위 레벨의 노드들
   
   * **차수(degree)**
     
     * **노드의 차수** : 노드에 **연결된 자식 노드**의 수
     
     * **트리의 차수** : 트리에 있는 노드의 차수 중에서 **가장 큰 값**
     
     * **단말 노드(리프 노드)** : **차수가 0**인 노드. 자식 노드가 없는 노드
   
   * **높이**
     
     * **노드의 높이** : **루트~노드**에 이르는 **간선의 수**. 노드의 **레벨**
     
     * **트리의 높이** : 트리에 있는 노드의 높이 중에서 **가장 큰 값**. **최대 레벨**

## 2. 이진트리

----

1. 이진트리
   
   * 모든 노드들이 2개의 서브트리를 갖는 특별한 형태의 트리
   
   * 각 노드가 **자식 노드를 최대 2개까지만** 가질 수 있는 트리
     
     * 왼쪽 자식 노드(left child node)
     
     * 오른쪽 자식 노드(right child node)

2. 이진트리 - **특성**
   
   * **레벨 i**에서의 **노드의 최대 개수**는 **2^i**개
   
   * **높이가 h**인 이진 트리가 가질 수 있는 **노드의 최소 개수는 (h+1)** 개, **최대 개수**는 **(2^(h+1) - 1)** 개

3. 이진트리 - **종류**
   
   * **포화 이진 트리(Full Binary Tree)**
     
     * 모든 레벨에 노드가 포화상태로 차 있는 이진 트리
     
     * 높이가 h일때, 최대 노드 개수인 (2^(h+1) - 1)의 노드를 가진 이진 트리
     
     * 루트를 1번으로 하여 (2^(h+1) - 1)까지 정해진 위치에 대한 노드 번호를 가짐
   
   * **완전 이진 트리(Complete Binary Tree)**
     
     * 높이가 h이고 노드 수가 n개일 때 (단, h+1<=n<(2^(h+1) - 1)), 포화 이진 트리의 **노드 번호 1번부터 n번까지 빈 자리가 없는** 이진 트리
   
   * **편향 이진 트리(Skewed Binary Tree)**
     
     * 높이  h에 대한 **최소 개수의 노드**를 가지면서, **한쪽 방향의 자식 노드만**을 가진 이진트리

4. **이진트리 - 순회(traversal)**
   
   * 순회(traversal)란 트리의 각 노드를 중복되지 않게 전부 방문(visit)하는 것
   
   * 트리는 비선형 구조 -> 선후 연결관계를 알 수 없다.
   
   * 순회(traversal): 트리의 노드들을 체계적으로 방문하는 것
   
   * **3가지 기본적인 순회방법**
     
     * **전위순회(preorder traversal) : VLR**
       
       * 부모노드 방문 후, 자식노드를 좌,우 순서로 방문
     
     * **중위순회(inorder traversal) : LVR**
       
       * 왼쪽 자식노드, 부모노드, 오른쪽 자식노드 순으로 방문
     
     * **후위순회(postorder traversal) : LRV**
       
       * 자식노드를 좌우 순서로 방문 후, 부모노드 방문
   
   * **전위순회(preorder traversal)**
     
     * 알고리즘
       
       ```python
       def preorder(node):
           if node:
               print(node.data, end=" ")
               preorder(node.left)
               preorder(node.right)
       ```
   
   * **중위순회(inorder traversal)**
     
     * 알고리즘
       
       ```python
       def inorder(node):
           if node:
               inorder(node.left)
               print(node.data, end=" ")
               inorder(node.right)
       ```
   
   * **후위순회(postorder traversal)**
     
     * 알고리즘
       
       ```python
       def postorder(node):
           if node:
               postorder(node.left)
               postorder(node.right)
               print(node.data, end=" ")
       ```
   
   * 연습문제

5. 이진트리의 **표현**
   
   * **배열을 이용한 이진 트리의 표현**
     
     * 이진 트리에 각 노드 번호를 다음과 같이 부여
     
     * **루트의 번호를 1**로 함
     
     * **레벨 n**에 있는 노드에 대하여 왼쪽부터 오른쪽으로 **2^n부터 2^(n+1) -1**까지 번호를 차례로 부여

6. **이진트리의 표현 - 배열**
   
   * 노드 번호의 **성질**
     
     * **노드 번호 i**인 노드의 **부모 노드** 번호: **내림(i/2)**
     
     * **노드 번호가 i**인 노드의 **왼쪽 자식** 노드 번호: **2*i**
     
     * **노드 번호가 i**인 노드의 **오른쪽 자식** 노드 번호: **2*i + 1**
     
     * **레벨 n**의 **노드 번호 시작** 번호: **2^n**
     
     * **레벨 n**의 노드 번호 **마지막** 번호: **2^(n+1) - 1**
   
   * 배열을 이용한 이진 트리의 표현
     
     * 노드 번호 -> 배열의 인덱스로 사용
     
     * **높이가 h**인 이진 트리 **배열의 크기**
       
       * **레벨 i의 최대 노드 수**: **2^i**
       
       * 1 + 2 + 4 + 8 ... + 2^i = **2^(h+1)-1**
   
   * 배열을 이용한 이진 트리 표현의 **단점**
     
     * 편향 이진 트리의 경우 사용하지 않는 배열 원소에 대한 **메모리 공간 낭비**
     
     * 트리의 중간에 새로운 노드 **삽입**, 기존 노드 **삭제**의 경우 **배열의 크기 변경 어려워 비효율적**

7. [참고] 이진 트리의 저장
   
   * 부모 번호를 인덱스로 자식 번호를 저장
     
     * 왼쪽 자식 저장 배열 1개, 오른쪽 자식 저장 배열 1개
   
   * 자식 번호를 인덱스로 부모 번호를 저장
     
     * 부모 번호를 저장할 배열 1개
     
     * 이를 활용하여 루트, 조상을 찾을 수 있음.

8. **트리의 표현 - 연결리스트**
   
   * 연결 자료구조를 이용한 이진트리의 표현
     
     * 이진 트리의 모든 노드는 최대 2개의 자식 노드를 가짐 -> 일정한 구조의 단순 연결 리스트 노드를 사용하여 구현
   
   * 클래스를 활용하여 트리 구현하기
     
     ```python
     # Node class를 통해 이진 트리 표현하기
     class Node:
         def __init__(self, data):
             self.data = data
             self.left = None
             self.right = None
     
     # Node를 사용해서 트리 만들어보기
     root = Node(1)  # root 노드 만들기
     
     # 2, 3을 root의 왼쪽과 오른쪽에 추가
     root.left = Node(2)
     root.right = Node(3)
     
     # 4, 5를 2번의 왼쪽과 오른쪽에 추가
     root.left.left = Node(4)  # Node(2).left
     root.left.right = Node(5)  # Node(2).right
     ```

9. 연습문제
   
   ```python
   # 13
   # 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
   v = int(input())
   tree = [Node(i) for i in range(v+1)]
   edge_list = list(map(int, input().split()))
   # 입력을 두개씩 잘라서 확인
   # 앞 ==> 부모p, 뒤 ==> 자식 c
   while edge_list:
       p = edge_list.pop(0)    # 부모
       c = edge_list.pop(0)    # 자식
       # 트리 만들기
       # 부모를 기준으로 왼쪽이 있는 경우
       if tree[p].left:
           tree[p].right = tree[c]
       # 부모를 기준으로 왼쪽이 없는 경우
       else:
           tree[p].left = tree[c]
   
   preorder(tree[1])
   print()
   ```

10. **수식 트리**
    
    * 수식을 표현하는 이진트리
    
    * **수식이진트리(Expression Binary Tree)** 라고 부르기도 함
    
    * **연산자**: **루트 노드 or 가지노드**
    
    * **피연산자**: 모두 **잎 노드**

11. 수식 트리의 순회
    
    ```python
    # 중위 순회: A / B * C * D + E
    # 후위 순회: A B / C * D * E +
    # 전위 순회 : + * * / A B C D E
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
    exp_root = Node("+")
    exp_root.left = Node("*")
    exp_root.right = Node("E")
    exp_root.left.left = Node("*")
    exp_root.left.right = Node("D")
    exp_root.left.left.left = Node("/")
    exp_root.left.left.right = Node("C")
    exp_root.left.left.left.left = Node("A")
    exp_root.left.left.left.right = Node("B")
    inorder(exp_root)
    print()
    postorder(exp_root)
    print()
    preorder(exp_root)
    ```

## 3. 이진 탐색 트리

----

1. **이진 탐색 트리**
   
   * 탐색을 효율적으로 하기 위한 자료구조
   
   * 모든 원소는 서로 다른 유일한 키를 갖는다.
   
   * key(왼쪽 서브트리) < key(루트 노드) < key(오른쪽 서브트리)
   
   * 왼쪽 서브트리와 오른쪽 서브트리도 이진 탐색 트리다.
   
   * **중위 순회 -> 오름차순으로 정렬된 값** 얻을 수 있음

2. 이진 탐색 트리 - **연산**
   
   * 탐색연산
     
     * **루트에서 시작**
     
     * **탐색할 키 값 x**를 **루트 노드의 키 값**과 **비교**
       
       * **키 값x = 루트노드 키 값** : 탐색연산 성공
       
       * **키 값x < 루트노드 키 값** : **왼쪽 서브트리**에 대해서 탐색연산
       
       * **키 값x > 루트노드 키 값** : **오른쪽 서브트리**에 대해서 탐색연산
     
     * 서브트리에 대해서 순환적으로 탐색 연산 반복
     
     ```python
     # 이진 탐색 트리
     class Node:
         def __init__(self, data):
             self.data = data
             self.left = None
             self.right = None
     # BinarySearchTree
     class BST:
         def __init__(self):
         self.root = None    # root는 트리의 시작지점
     
         # 탐색 연산
         def search(self, target):
             now = self.root  # 탐색의 시작은 root부터
             cnt = 0
             # 찾을때까지 반복 (노드가 없어질 때까지)
             while now:
                 print(now.data)
                 # 현재 내가 있는 노드의 키값과 찾고있는 값이 같으면 반환
                 if target == now.data:
                     print(cnt)
                     return cnt
                 # 내가 있는 노드의 키값이 찾고있는 값보다 크면 왼쪽으로 이동
                 elif target < now.data:
                     now = now.left
                 # 작으면 오른쪽으로 이동
                 else:
                     now = now.right
                 cnt += 1
             # 만약 반복이 끝남 => 데이터가 이진 탐색트리 안에 없음
             return
     ```
   
   * 삽입연산
     
     * 먼저 탐색 연산 수행
       
       * 같은 원소 -> 트리에 삽입X
       
       * 탐색에서 탐색 실패가 결정되는 위치 -> 삽입 위치
     
     * 탐색 실패한 위치에 원소 삽입
     
     ```python
     # BinarySearchTree
     class BST:
         def __init__(self):
             self.root = None    # root는 트리의 시작지점
     
         # 탐색 연산
         def search(self, target):
             return
     
         # 삽입 연산
         def insert(self, node):
             now = self.root     # 루트부터 탐색 시작
     
             # 루트 노드가 없다면 바로 리턴
             if now == None:
                 self.root = node    # 제일 처음 들어온 노드가 루트 노드
                 return
             # 탐색 진행 - 탐색 실패한 지점에 노드 삽입
             while True:
                 p = now     # now가 바뀌기 전 부모를 기억해놓기
                 print(p.data)
                 # 넣고싶은 데이터가 현재 노드보다 작으면 왼쪽
                 if node.data < now.data:
                     now = now.left  # 왼쪽으로
                     # 왼쪽 노드가 없으면, 부모 노드의 왼쪽에 추가
                     if not now:
                         p.left = node
                         return
                 # 넣고싶은 데이터가 현재 노드보다 크면 오른쪽
                 else:
                     now = now.right     # 오른쪽으로
                     # 오른쪽 노드가 없으면, 부모 노드의 오른쪽에 추가
                     if not now:
                         p.right = node
                         return
     root = Node(9)
     root.left = Node(4)
     root.right = Node(12)
     root.left.left = Node(3)
     root.left.right = Node(6)
     root.right.right = Node(15)
     root.right.right.left = Node(13)
     root.right.right.right = Node(17)
     bst = BST()
     bst.root = root
     # bst.search(13)
     bst.insert(Node(5))
     
     # 위의 트리 만들기를 insert 활용해서
     # 입력을 한줄로 어떻게 줘야 위의 트리가 만들어 질까 - 전위순회
     # 9 4 12 3 6 15 13 17
     bst = BST()
     data_list = list(map(int, input().split()))
     node_list = [Node(i) for i in data_list]
     
     for node in node_list:
         bst.insert(node)
     ```

3. 이진 탐색 트리 - **성능**
   
   * 탐색, 삽입, 삭제 시간 - 트리의 높이 만큼
     
     * O(h), h:BST의 깊이
   
   * 평균의 경우
     
     * 이진 트리가 균형적으로 생성되어 있는 경우 : O(log n)
   
   * 최악의 경우
     
     * 한쪽으로 치우친 경사 이진트리의 경우 : O(n)
     
     * 순차탐색과 같다.
   
   * 검색 알고리즘의 비교

4. 이진 탐색 트리 - 연산 연습
   
   * 삭제 연산

## 4. 힙(heap)

-----

1. 힙
   
   * 완전 이진 트리에 있는 노드 중에서 **키값이 가장 큰 노드**나 키값이 **가장 작은 노드**를 **찾기 위해서 만든 자료구조**
   
   * **최대 힙(max heap)**
     
     * 키값이 가장 큰 노드를 찾기 위한 **완전 이진 트리**
     * 부모 노드의 키 값 > 자식 노드의 키 값
     * 루트 노드 : 키값이 가장 큰 노드
   
   * **최소 힙(min heap)**
     
     * 키값이 가장 작은 노드를 찾기 위한 **완전 이진 트리**
     * 부모 노드의 키 값 < 자식 노드의 키 값
     * 루트 노드 : 키 값이 가장 작은 노드

2. 힙 연산 - 삽입

3. 힙 연산 - 삭제
   
   * 루트 노드의 원소만을 삭제 가능

4. 힙을 이용한 우선순위 큐
