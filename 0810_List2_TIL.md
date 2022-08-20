## 배열 2(Array 2)

----

1. 배열 : 2차원 배열

2. 부분집합 생성

3. 바이너리 서치 (Binary Search)

4. 셀렉션 알고리즘 (Selection Algorithm)

5. 선택 정렬 (Selection Sort)

## 1. 2차원 배열

-----

1. 2차원 배열의 **선언**
   
   * 1차원 List를 묶어놓은 List
   
   * 2차원 이상의 다차원 List는 차원에 따라 Index를 선언
   
   * 2차원 List의 선언 : 세로길이(행의 개수), 가로길이(열의 개수)를 필요로 함
   
   * Python에서는 데이터의 초기화를 통해 변수선언과 초기화가 가능함
     
     ```python
     arr = [[0,1,2,3],[4,5,6,7]] #2행4열 2차원List
     ```
   
   * 참고
     
     ```python
     N = int(input())
     arr = [list(map(int, input().split())) for _ in range(N)]
     arr = [list(map(int, input()) for _ in range(N)]
     arr = [[0]*M] * N    # 하나의 리스트 N개 참조(얕은 복사)
     ```

2. 2차원 배열의 **접근**
   
   * **배열 순회**: n X m 배열의 n*m개의 모든 원소를 빠짐없이 조사하는 방법
   
   * **행 우선 순회**
     
     ```python
     for i in range(n):
         for j in range(m):
             arr[i][j]
     ```
   
   * **열 우선 순회**
     
     ```python
     for j in range(m):
         for i in range(n):
             arr[i][j]
     ```
   
   * **지그재그 순회**
     
     ```python
     for i in range(n):
         for j in range(m):
             arr[i][j + (m-1-2*j) * (i%2)]
     ```
   
   * **델타를 이용한 2차 배열 탐색**: 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법
     
     * di[] = [0, 0, -1, 1] 
     
     * dj[] = [-1, -1, 0, 0]
     
     * di, dj = [[0,1], [1,0], [0,-1], [-1,0]]
     
     * 여러 칸 이동
       
       ```python
       for i in range(n):
           for j in range(m):
               for k in range(4):
                   for d in range(1, 3):
                       ni = i + di[k]*d
                       nj = j + dj[k]*d
                       if 0 <=ni<N and 0<=nj<M:
                           print(ni, nj)
       ```
   
   * **전치 행렬**
     
     ```python
     for i in range(n):
         for j in range(m):
             if i < j:
                 arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
     ```
   
   * 왼쪽 대각선 합
     
     ```python
     sum_arr = 0
     for i in range(N):
         for j in range(N):
             if i == j:
                 sum_arr += arr[i][j]
     
     for i in range(N):
         sum_arr += arr[i][i]
     ```
   
   * 오른쪽 대각선 합
     
     ```python
     sum_arr = 0
     for i in range(N):
         sum_arr += arr[i][N-i-1]
     ```
   
   * 대각선 양쪽의 합 -> N이 홀수인 경우 중앙 2번 더해짐 -> 빼줘야 함 (N//2, N//2)
   
   * 왼쪽 대각선의 왼쪽, 오른쪽 영역의 합
     
     ```python
     sum_right = 0
     sum_left = 0
     for i in range(N):
         for j in range(N):
             if i < j:
                 sum_right += arr[i][j]
             elif i > j:
                 sum_left += arr[i][j]
     
     for i in range(N):
         for j in range(i+1, N):
             sum_right += arr[i][j]
             sum_left += arr[j][i]
     ```
   
   * 오른쪽 대각선의 왼쪽, 오른쪽 영역의 합
     
     ```python
     sum_left = 0
     sum_right = 0
     for i in range(N):
         for j in range(N-i-1):
             sum_left += arr[i][j]
             sum_right += arr[N-j-1][N-i-1]
         # for j in range(N-i, N):
         #     sum_right += arr[j][i]
     ```
   
   * 같은 사선 상의 합
     
     ```python
     s = [0]*(2*N-1)   # 사선의 개수: 2*N-1개
     for i in range(N):
         for j in range(N):
             s[i+j] += arr[i][j]  # 같은 사선 -> i+j의 합 같음
     ```

3. 연습문제1
   
   * 5X5 2차원 배열에 25개 숫자 무작위 초기화 후
   
   * 각 요소와 이웃한 요소와의 차의 절댓값 구하기
   
   * 25개의 요소에 대해서 모두 조사해 총합 구하기
   
   ```python
   T = int(input())
   for test_case in range(1, T+1):
       N = int(input())
       nums = [list(map(int, input().split())) for _ in range(N)]
   
       di = [-1, 1, 0, 0]
       dj = [0, 0, -1, 1]
   
       # 절대값 차이 저장 변수
       sum_vals = 0
       # 각 요소 순회
       for i in range(N):
           for j in range(N):
               for d in range(4):
                   ni = i + di[d]
                   nj = j + dj[d]
                   # 이동 위치가 범위 내인지 확인
                   if 0<=ni<N and 0<=nj<N:
                       if nums[i][j] - nums[ni][nj] < 0:
                           sum_vals += -(nums[i][j] - nums[ni][nj])
                       else:
                           sum_vals += nums[i][j] - nums[ni][nj]
       print(f"#{test_case} {sum_vals}")
   ```

## 2. 부분집합 합(Subset Sum) 문제

---

1. 부분집합 합 문제
   
   * 유한개의 정수로 이루어진 집합, 이 집합의 부분집합 중에서 그 집합의 원소를 모두 더한 값이 0이 되는 경우가 있는지
   
   * 완전검색 기법으로 부분집합 합 문제 풀기 : 모든 부분집합 생성 후 각 부분집합의 합 계산

2. 부분집합의 수
   
   * 집합의 원소 n개 -> 공집합을 포함한 **부분집합의 수는 2^n개**
   
   * 이는 각 원소를 부분집합에 **포함시키거나 포함시키지 않는 2가지 경우**를 **모든 원소에 적용한 경우의 수**와 같다.
   
   * 각 원소가 부분집합에 포함되었는지를 loop 이용하여 확인하고 부분집합을 생성하는 방법

3. **비트 연산자**
   
   | 연산자 | 설명                       |
   | --- | ------------------------ |
   | &   | 비트 단위로 **AND 연산**        |
   |     |                          |
   | <<  | 피연산자의 **비트 열을 왼쪽**으로 이동  |
   | >>  | 피연산자의 **비트 열을 오른쪽**으로 이동 |
   
   * << 연산자
     
     * **1<<n** : **2^n** 즉, 원소가 n개일 경우의 **모든 부분집합의 수**를 의미
   
   * & 연산자
     
     * i & (1<<j) : i의 j번째 비트가 1인지 아닌지를 검사
   
   * 부분집합 생성하기
     
     ```python
     for i in range(1<<n):
         for j in range(n):
             if i & (1<<j):
                 print(arr[j], end=",")
         print()
     ```

4. 연습문제 2
   
   * 10개의 정수 입력 받아 부분집합의 합이 0이 되는 것이 존재하는지 계산하는 함수
     
     ```python
     T = int(input())
     for tc in range(1, T + 1):
         arr = list(map(int, input().split()))
     
         N = len(arr)  # 원소 개수
         # 공집합 -> 무조건 부분집합의 합 0
         exist = 0  # 부분집합의 합이 0이 될 때가 존재하면 1 아니면 0
         for i in range(1, 1 << N):   # 부분집합개수만큼(공집합 제외->1부터시작)
             subset_sum = 0  # 부분집합의 합
             for j in range(N):    # j = 0, 1, 2, ..., N-1
                 if i & (1 << j):
                     # i의 비트를 j와 비교 list의 j번째 인덱스에 있는 원소가
                     # 부분 집합에 포함되어 있는지 검사
                    subset_sum += arr[j]
             exist = 1 if subset_sum == 0 else exist
         print(f"#{tc} {exist}")
     ```

## 3. 검색(Search)

---

1. **검색**: 저장되어 있는 자료 중에서 **원하는 항목**을 찾는 작업
   
   * 목적하는 탐색 키를 가진 항목을 찾는 것
     
     * **탐색 키(search key)** : 자료를 **구별**하여 **인식**할 수 있는 키
   
   * 검색의 **종류**
     
     * 순차 검색(sequential search)
     
     * 이진 검색(binary search)
     
     * 해쉬(hash)

2. **순차 검색(Sequential Search)**
   
   * 일렬로 되어 있는 자료를 순서대로 검색하는 방법
     
     * 가장 간단, 직관적
     
     * 배열이나 연결 리스트 등 **순차구조**로 구현된 자료구조에서 원하는 항목을 찾을 때 유용
     
     * 알고리즘 **단순 -> 구현 쉬움** but, 검색 대상의 수가 많은 경우 -> 수행시간 급격히 증가하여 **비효율적**
   
   * 2가지 경우: 정렬X, 정렬O
   
   * 정렬되어 있지 않은 경우
     
     * 검색 과정
       
       * 첫번째 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는지 비교
       
       * 키 값이 동일한 원소를 찾으면 그 원소의 인덱스를 반환
       
       * 자료구조의 마지막까지 검색 대상을 찾지 못하면 검색 실패
     
     * 찾고자 하는 **원소의 순서**에 따라 **비교횟수**가 결정됨
       
       * 평균 비교 횟수 = (1+2+3+...+n)/n = (n+1)/2
       
       * 시간 복잡도 : O(n)
     
     * 구현 예
      ```python
      def sequentialSearch(a, n, key):
         # a: list, n: 길이
         i = 0
         while i < n and a[i] != key:
            i += 1
         if i < n:
            return i
         else:
            return -1
      ```
   
   * 정렬되어 있는 경우
     
     * 검색 과정
       
       * 자료가 **오름차순으로 정렬**된 상태에서 검색 실시 가정
       
       * 자료 순차 검색하면서 키 값 비교, 원소의 키 값이 검색 대상의 키 값보다 크면 찾는 원소X -> 더 이상 검색X 검색 종료
     
     * 찾고자 하는 원소의 순서에 따라 비교횟수가 결정됨
       
       * 정렬되어 있으므로, 검색 실패를 반환하는 경우 평균 비교 회수가 반으로 줄어듦
       
       * 시간 복잡도 : O(n)
     
     * 구현 예
      ```python
      def sequentialSearch2(a, n, key):
         # a:list, n:길이
         i = 0
         while i < n and a[i] < key:
            i += 1
         if i < n and a[i] == key:
            return i
         else:
            return -1
      ```

3. **이진 검색(Binary Search)**
   
   * 자료의 **가운데에 있는 항목의 키 값**과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
   
   * 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 **검색 범위를 반으로 줄여가면서** 보다 빠르게 검색을 수행함
   
   * 이진 검색을 하기 위해서는 자료가 정렬된 상태여야 한다.
   
   * **검색 과정**
     
     * 자료의 중앙 원소를 고른다
     
     * 중앙 원소의 값과 찾고자 하는 목표 값 비교
     
     * 목표 값이 중앙 원소의 값보다 작으면 -> 자료의 왼쪽 반에 대해서 새로 검색, 크다면 -> 자료의 오른쪽 반에 대해서 새로 검색 수행
   
   * 구현
     
     * 검색 범위의 시작점과 종료점을 이용하여 검색을 반복 수행
     
     * 이진 검색의 경우, 자료에 삽입이나 삭제가 발생했을 때 배열의 상태를 항상 정렬 상태로 유지하는 추가 작업 필요
   
   * 반복문 이용 구현
     
     ```python
     def binarySearch(arr, N, key):
         start = 0
         end = N-1
         while start <= end:
             middle = (start + end)//2
             if arr[middle] == key:
                 return True
             elif arr[middle] > key:
                 end = middle - 1
             else:
                 start = middle + 1
         return False
     ```
   
   * 재귀 함수 이용 구현
     
     ```python
     def binarySearch(arr, low, high, key):
         if low > high:
             return False
         else:
             middle = (low + high)//2
             if key == arr[middle]:
                 return True
             elif key < arr[middle]:
                 return binarySearch(arr, low, middle-1, key)
             else:
                 return binarySearch(arr, middle+1, high, key)
     ```

## 4. 인덱스

---

1. 인덱스
   
   * Database에서 유래, 테이블에 대한 동작 속도를 높여주는 자료 구조를 일컫는다.
   
   * Database 분야가 아닌 곳에서는 Look up table등의 용어를 사용하기도 함
   
   * 인덱스를 저장하는데 필요한 디스크 공간은 보통 테이블을 저장하는데 필요한 디스크 공간보다 작다.
   
   * 보통 인덱스는 키-필드만 갖고 있고, 테이블의 다른 세부 항목들은 갖고 있지X
   
   * 배열을 사용한 인덱스
     
     * 대량의 데이터를 매번 정렬 -> 프로그램의 반응 느려질 수 밖에 없음
     
     * 이러한 대량 데이터의 성능 저하 문제 해결을 위해 배열 인덱스를 사용할 수 있음

## 5. 선택 정렬

---

1. **선택 정렬**
   
   * 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식
     
     * 셀렉션 알고리즘을 전체 자료에 적용한 것
   
   * 정렬 과정
     
     * 주어진 리스트 중 최소값을 찾는다.
     
     * 그 값을 리스트의 맨 앞에 위치한 값과 교환
     
     * 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위 과정 반복
   
   * 시간 복잡도: O(n^2)
   
   * 구현
     
     ```python
     def selectionSort(arr, N):
         for i in range(N-1):
             minIdx = i
             for j in range(i+1, N):
                 if arr[minIdx] > arr[j]:
                     minIdx = j
             arr[minIdx], arr[i] = arr[i], arr[minIdx]
     ```

2. **셀렉션 알고리즘(Selection Algorithm)**
   
   * 저장되어 있는 자료로부터 **k번째로 큰 혹은 작은 원소**를 찾는 방법
     
     * 최소값, 최대값 혹은 중간값을 찾는 알고리즘을 의미하기도 함
   
   * 선택 과정
     
     * 정렬 알고리즘을 이용하여 자료 정렬하기
     
     * 원하는 순서에 있는 원소 가져오기
   
   * k번째로 작은 원소를 찾는 알고리즘
     
     * 1번부터 k번째까지 작은 원소들을 찾아 배열의 앞쪽으로 이동시키고, 배열의 k번째를 반환
     
     * k가 비교적 작을 때 유용, **O(kn)** 의 수행시간 필요
     
     ```python
     def select(arr, k):
         for i in range(0, k):
             minIdx = i
             for j in range(i+1, len(arr)):
                 if arr[minIdx] > arr[j]:
                     minIdx = j
             arr[i], arr[minIdx] = arr[minIdx], arr[i]
         return arr[k-1]
     ```

3. 정렬 알고리즘 비교

4. 연습문제3
   
   * 2차 배열 초기화한 후 달팽이 배열로
     
     ```python
     # 2차 배열 입력받은 것 -> 달팽이 순회 적용
     N = int(input())
     arr = [list(map(int, input().split())) for _ in range(N)]
     
     # 새로운 배열
     new_arr = [[0]*N for _ in range(N)]
     
     # 2차원 배열의 값들만 가져와서 1차원으로
     nums = []
     for i in range(N):
         for j in range(N):
             nums.append(arr[i][j])
     
     # 1차원 배열 정렬
     for i in range(len(nums) - 1):
         minIdx = i
         for j in range(i+1, len(nums)):
             if nums[minIdx] > nums[j]:
                 minIdx = j
         nums[minIdx], nums[i] = nums[i], nums[minIdx]
     
     # 새로운 배열에 값 채우기
     dx = [0, 1, 0, -1]    # 우,하,좌,상
     dy = [1, 0, -1, 0]
     
     d = 0
     x, y = 0, 0
     idx = 0
     
     while idx < len(nums):
         new_arr[x][y] = nums[idx]
         idx += 1
     
         # 새로운 방향
         nx = x + dx[d]
         ny = y + dy[d]
         # 새로운 방향이 가능한지 여부
         if 0<=nx<N and 0<=ny<N and new_arr[nx][ny] == 0:
             x, y = nx, ny
         else: # 그게 아니라면
             d = (d+1) % 4     # 새로운 방향
             x += dx[d]        # 바꾼방향을 x로
             y += dy[d]        # 바꾼방향을 y로
     
     for i in range(N):
         for j in range(N):
             print(new_arr[i][j], end=" ")
         print()
     ```
