## 0. 큐(Queue)

----

1. 선형큐

2. 원형큐

3. 우선순위 큐

4. 큐의 활용 : 버퍼

5. BFS

6. BFS 예제

## 1. 큐

----

1. 큐(Queue)의 **특성**
   
   * 스택과 마찬가지로 **삽입과 삭제의 위치가 제한적**인 자료구조
     
     * 큐의 **뒤에서는 삽입**만, 큐의 **앞에서는 삭제만** 이루어지는 구조
   
   * **선입선출구조(FIFO : First In First Out)**
     
     * 큐에 삽입한 순서대로 원소가 저장 - 가장 먼저 삽입된 원소는 가장 먼저 삭제

2. 큐의 구조 및 기본 연산
   
   * 큐의 선입선출 구조
   
   * 큐의 기본 연산
     
     * 삽입 : enQueue
     
     * 삭제 : deQueue

3. 큐의 **주요 연산**
   
   | 연산                | 기능                           |
   | ----------------- | ---------------------------- |
   | **enQueue(item)** | 큐의 뒤쪽(rear 다음)에 원소 **삽입**    |
   | **deQueue()**     | 큐의 앞쪽(front)에 원소를 **삭제, 반환** |
   | **createQueue()** | 공백 상태의 큐 생성                  |
   | **isEmpty()**     | 큐가 **공백상태**인지 확인             |
   | **isFull()**      | 큐가 **포화상태**인지 확인             |
   | **Qpeek()**       | 큐의 앞쪽(front)에서 원소를 삭제 없이 반환  |

4. 큐의 연산 과정

5. 큐의 구현
   
   * **선형큐**
     
     * 1차원 배열을 이용한 큐
     
     * 큐의 크기 = 배열의 크기
     
     * front : 저장된 첫번째 원소의 인덱스
     
     * rear : 저장된 마지막 원소의 인덱스
   
   * 상태 표현
     
     * **초기** 상태 : **front = rear = -1**
     
     * **공백** 상태 : **front == rear**
     
     * **포화** 상태 : **rear == n-1** (n : 배열의 크기, n-1: 배열의 마지막 인덱스)
   
   * 초기 공백 큐 생성
     
     * 크기 n인 1차원 배열 생성
     
     * front와 rear를 -1로 초기화
   
   * **삽입 : enQueue(item)**
     
     * 마지막 원소 뒤에 새로운 원소를 삽입하기 위해
       
       * rear값을 하나 증가시켜 새로운 원소를 삽입할 자리 마련
       
       * 그 인덱스에 해당하는 배열원소 Q[rear]에 item을 저장
       
       ```python
       def enQueue(item):
           global rear
           if isFull():
               print("Queue Full")
           else:
               rear += 1
               Q[rear] = item
       ```
   
   * **삭제 : deQueue()**
     
     * 가장 앞에 있는 원소를 삭제하기 위해
       
       * front 값을 하나 증가시켜 큐에 남아있게 될 첫번째 원소 이동
       
       * 새로운 첫번째 원소를 리턴함으로써 삭제와 동일한 기능을 함
       
       ```python
       def deQueue():
           global front
           if isEmpty():
               print("Queue Empty")
           else:
               front += 1
               return Q[front]
       ```
   
   * 공백상태 및 포화상태 검사 : **isEmpty(), isFull()**
     
     * **공백**상태 : **front == rear**
     
     * **포화**상태 : **rear == n-1**
       
       ```python
       def isEmpty():
           return front == rear
       def isFull():
           return rear == len(Q) - 1
       ```
   
   * **검색 : Qpeek()**
     
     * 가장 앞에 있는 원소를 검색하여 반환하는 연산
     
     * 현재 front의 한자리 뒤(front + 1)에 있는 원소, 즉 큐의 첫번째에 있는 원소 반환
       
       ```python
       def Qpeek():
           if isEmpty():
               print("Queue Empty")
           else:
                return Q[front + 1]
       ```

6. 연습문제1
   
   ```python
   for i in range(5):
       enQueue(i)
   for i in range(5):
       print(deQueue())
   ```

7. 선형 큐 이용시의 **문제점**
   
   * **잘못된 포화상태 인식**
     
     * 배열의 앞부분에 활용할 수 있는 공간이 있음에도 불구하고, rear=n-1인 상태 즉, 포화상태로 인식하여 더 이상의 삽입 수행X
   
   * 해결방법1
     
     * 매 연산이 이루어질 때마다 저장된 원소들 - 배열의 **앞부분으로** 모두 이동
     
     * 원소 이동에 많은 시간 소요 - 큐의 **효율성 급격히 떨어짐**
   
   * 해결방법2
     
     * 1차원 배열을 사용하되, 논리적으로는 배열의 처음과 끝이 연결되어 **원형 형태**의 큐를 이룬다고 가정하고 사용

## 2. 원형 큐

----

1. 원형 큐의 구조
   
   * **초기 공백 상태**
     
     * **front = rear = 0**
   
   * Index의 순환
     
     * front와 rear의 위치 - n-1를 가리킨 후 - 배열의 처음 인덱스인 0으로 이동
     
     * 이를 위해 나머지 연산자 mod 사용
   
   * front 변수
     
     * **공백 상태와 포화 상태 구분을 쉽게** 하기 위해 **front가 있는 자리는 사용X** 항상 빈자리로 둠
   
   * **삽입 위치 및 삭제 위치**
     
     |     | 삽입 위치                   | 삭제 위치                     |
     | --- | ----------------------- | ------------------------- |
     | 선형큐 | rear = rear + 1         | front = front + 1         |
     | 원형큐 | rear = (rear + 1) mod n | front = (front + 1) mod n |

2. 원형 큐의 연산 과정

3. 원형 큐의 **구현**
   
   * 초기 공백 큐 생성
     
     * 크기 n인 1차원 배열 생성
     
     * **front와 rear를 0으로** 초기화
   
   * 공백상태 및 포화상태 검사 : **isEmpty(), isFull()**
     
     * **공백**상태 : **front == rear**
     
     * **포화**상태 : 삽입할 **rear의 다음 위치 == 현재 front**
       
       * (rear+1) mod n == front
       
       ```python
       def isEmpty():
           return front == rear
       def isFull():
              return (rear + 1) % len(cQ) == front
       ```
* 삽입 : **enQueue(item)**
  
  * 마지막 원소 뒤에 새로운 원소를 삽입하기 위해
    
    * rear값을 조정하여 새로운 원소를 삽입할 자리 마련
      
      * rear = (rear + 1) mod n
    
    * 그 인덱스에 해당하는 배열원소 cQ[rear]에 item을 저장
    
    ```python
    def enQueue(item):
        global rear
        if isFull():
            print("Queue Full")
        else:
            rear = (rear + 1) % len(cQ)
            cQ[rear] = item
    ```

* 삭제 : **deQueue(), delete()**
  
  * 가장 앞에 있는 원소를 삭제하기 위해
    
    * front 값을 조정하여 삭제할 자리 준비
    
    * 새로운 front 원소를 리턴함으로써 삭제와 동일한 기능을 함
    
    ```python
    def deQueue():
        global front
        if isEmpty():
            print(Queue Empty)
        else:
            front = (front + 1) % len(cQ)
            return cQ[front]
    ```

## 3. 우선순위 큐(Priority Queue)

----

1. 우선순위 큐의 **특성**
   
   * 우선순위를 가진 항목들을 저장하는 큐
   
   * FIFO 순서가 아니라 **우선순위가 높은 순서대로 먼저** 나가게 된다.

2. 우선순위 큐의 **적용 분야**
   
   * 시뮬레이션 시스템
   
   * 네트워크 트래픽 제어
   
   * 운영체제의 테스크 스케줄링

3. 우선순위 큐의 **구현**
   
   * **배열**을 이용한 우선순위 큐
   
   * **리스트(동적할당)** 를 이용한 우선순위 큐

4. 우선순위 큐의 **기본 연산**
   
   * 삽입 : enQueue
   
   * 삭제 : deQueue

5. **배열을 이용한 우선순위 큐**
   
   * 배열을 이용하여 자료 저장
   
   * 원소를 삽입하는 과정에서 우선순위를 비교 - 적절한 위치에 삽입하는 구조
   
   * 가장 앞에 최고 우선순위의 원소 위치
   
   * **문제점**
     
     * 배열 사용 - 삽입, 삭제 연산이 일어날 때 **원소의 재배치** 발생
     
     * 이에 소요되는 **시간이나 메모리 낭비**가 큼

## 4.큐의 활용 : 버퍼(Buffer)

----

1. **버퍼**
   
   * 데이터를 한곳에서 다른 한 곳으로 전송하는 동안 **일시적으로 그 데이터를 보관**하는 메모리의 영역
   
   * **버퍼링** : 버퍼를 **활용하는 방**식 또는 **버퍼를 채우는 동작** 의미

2. 버퍼의 **자료구조**
   
   * 일반적으로 입출력 및 네트워크와 관련된 기능에서 이용됨
   
   * 순서대로 입력/출력/전달되어야 하므로 FIFO방식의 자료구조인 **큐 활용**

3. 키보드 버퍼

4. 연습문제2
   
   ```python
   # 마이쮸
   p = 1  # 처음 줄 설 사람 번호
   # q = []
   q = deque()
   N = 20  # 초기 마이쮸 개수
   m = 0  # 나눠준 개수
   v = 0
   
   while m < N:
       # input()
       q.append((p, 1, 0))  # 처음 줄 서는 사람
       # print(q)
       # c: 받아갈 사탕 수, m:나눠준 사탕 수
       # v, c, my = q.pop(0)
       v, c, my = q.popleft()
       m += c
       # 마이쮸를 받고 다시 서는 사람
       q.append((v, c + 1, my + c))
       p += 1  # 처음 줄서는 사람 번호
   print(f"마지막 받은 사람 : {v}")
   ```

## 5. BFS(Breadth First Search)

----

1. 그래프를 탐색하는 2가지
   
   * 깊이 우선 탐색(Depth First Search, DFS)
   
   * 너비 우선 탐색(Breadth First Search, BFS)

2. 너비우선탐색
   
   * 탐색 시작점의 **인접한 정점들을 먼저 모두 차례로 방문**한 후, 방문했던 정점을 시작점으로 다시 인접한 정점들을 차례로 방문
   
   * 인접한 정점 탐색 후, 차례로 다시 너비우선탐색 진행 - 선입선출 형태의 큐 활용

3. BFS 알고리즘

4. 연습문제3
   
   ```python
   def bfs(g, v, n):  # g:그래프(인접리스트), v:시작지점, n:정점개수
       # 중복 탐색 방지를 위한 방문 배열
       visited = [False] * (n + 1)  # 정점 번호가 1부터 시작하면 n+1
       queue = []  # 큐로 사용할 배열 선언
       queue.append(v)  # 탐색을 시작할 초기 위치 큐에 추가
       visited[v] = True  # 초기 위치는 방문했다고 체크
       # 반복
       while queue:
           t = queue.pop(0)
           print(f"{t}", end=" ")
           for i in g[t]:
               if not visited[i]:
                   queue.append(i)
                   visited[i] = True
   adjList = [[],
              [2, 3],
              [1, 4, 5],
              [1, 7],
              [2, 6],
              [2, 6],
              [4, 5, 7],
              [3, 6]]
   bfs(adjList, 1, 7)
   ```

5. 추가
   
   * 전부 1로 바뀌는데 며칠이 걸릴까?
     
     ```python
     di = [-1, 1, 0, 0]
     dj = [0, 0, -1, 1]
     def bfs(si, sj, N):
         visited = [[0] * N for _ in range(N)]
         queue = []
         queue.append((si, sj))
         visited[si][sj] = 1
         day = 0     # 며칠이 지났는지
     
         while queue:
             # 2차원 배열 모양 출력
             print(f"{day}일차")
             print("=============================")
             for k in range(n):
                 print(visited[k])
             print("=============================")
     
             # 현재 위치에서 방문을 몇번 할건지
             # 방문할 위치는 큐에 들어있고, 그 위치의 개수(큐의 크기)만큼
             # 큐의 길이만큼만 반복
             for _ in range(len(queue)):
                 # 현재 방문 위치 꺼내기
                 i, j = queue.pop(0)
     
                 # 현재 위치에서 갈 수 있는 곳 검사(델타 이용 4방향 탐색)
                 for d in range(4):
                     # 다음 위치 알아내기
                     ni, nj = i + di[d], j + dj[d]
                     # 다음 위치가 탐색가능한 위치인지(배열 범위내, 방문한적 없음)
                     if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                         # 탐색가능한 위치이면 방문체크, 큐에 위치 추가
                         queue.append((ni, nj))
                         visited[ni][nj] = 1
             day += 1
         return day - 1  # 마지막에 한번 더 더해진 것 빼줌
     ```
   
   * dfs로 가능한 모든 경로 돌기
     
     ```python
     def dfs(i, j, N):
         global answer
         if maze[i][j] == 3:
             answer += 1
             return
         else:
             visited[i][j] = 1
             for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                 ni, nj = i + di, j + dj
                 # 벽으로 둘러쌓인 미로
                 if maze[ni][nj] != 1 and visited[ni][nj] == 0:
                     dfs(ni, nj, N)
             visited[i][j] = 0   # 다시 0으로 - 지나갈수있도록
             return
     T = int(input())
     for tc in range(1, T + 1):
         N = int(input())
         maze = [list(map(int, input())) for _ in range(N)]
         # 시작점 찾기
         sti, stj = -1, -1
         for i in range(N):
             for j in range(N):
                 if maze[i][j] == 2:
                     sti, stj = i, j
                     break
             if sti != -1:
                 break
         answer = 0      # 경로의 수
         visited = [[0]*N for _ in range(N)]
         dfs(sti, stj, N)
         print(answer)
     ```
   
   * dfs로 지나온 칸 수 구하기
     
     ```python
     # dfs로 지나온 칸 수
     def dfs(i, j, s, N):
         global minV
         if maze[i][j] == 3:
             if minV > s + 1:
                 minV = s + 1    # 출발~도착까지
             return
         else:
             visited[i][j] = 1
             for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                 ni, nj = i + di, j + dj
                 # 벽으로 둘러쌓인 미로
                 if maze[ni][nj] != 1 and visited[ni][nj] == 0:
                     dfs(ni, nj, s+1, N)
             visited[i][j] = 0   # 다시 0으로 - 지나갈수있도록
             return
     T = int(input())
     for tc in range(1, T + 1):
         N = int(input())
         maze = [list(map(int, input())) for _ in range(N)]
         # 시작점 찾기
         sti, stj = -1, -1
         for i in range(N):
             for j in range(N):
                 if maze[i][j] == 2:
                     sti, stj = i, j
                     break
             if sti != -1:
                 break
         minV = N*N      # 지나온 칸 수 최단
         visited = [[0]*N for _ in range(N)]
         dfs(sti, stj, 0, N)
         print(f"#{tc} {minV}")
     ```
   
   * bfs 최단경로
     
     ```python
     def bfs(i, j, N):
         visited = [[0] * N for _ in range(N)]
         q = []
         q.append((i, j))
         visited[i][j] = 1
         while q:
             i, j = q.pop(0)
             # 3인지 확인
             if maze[i][j] == 3:
                 return visited[i][j]
             for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                 ni, nj = i + di, j + dj
                 if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and not visited[ni][nj]:
                     q.append((ni, nj))
                     visited[ni][nj] = visited[i][j] + 1
         return -1
     T = int(input())
     for tc in range(1, T + 1):
         N = int(input())
         maze = [list(map(int, input())) for _ in range(N)]
         # 시작점 찾기
         sti, stj = -1, -1
         for i in range(N):
             for j in range(N):
                 if maze[i][j] == 2:
                     sti, stj = i, j
                     break
             if sti != -1:
                 break
     
         print(f"#{tc} {bfs(sti, stj, N)}")
     ```
   
   * bfs 출발점 여러개
     
     ```python
     def bfs(N):
         visited = [[0]*N for _ in range(N)]
         q = []
         for i in range(N):
             for j in range(N):
                 if maze[i][j] == 2:
                     q.append((i, j))
                     visited[i][j] = 1
         while q:
             i, j = q.pop(0)
     
             for di, dj in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
                 ni, nj = i + di, j + dj
                 if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and not visited[ni][nj]:
                     q.append((ni, nj))
                     visited[ni][nj] = visited[i][j] + 1
         return
     ```
