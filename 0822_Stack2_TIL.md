# 스택2

---

1. 계산기1

2. 계산기2

3. 백트래킹

4. [참고] 부분집합, 순열

5. 분할정복

## 1. 계산기1

----

1. 문자열 수식 계산의 일반적 방법
   
   * step1. 중위 표기법 -> 후위 표기법 (스택 이용)
   
   * step2. 후위 표기법의 수식을 계산 (스택 이용)
   
   * **중위표기법(infix notation)**: 연산자를 피연산자의 가운데 표기하는 방법
   
   * **후위표기법(postfix notation)**: 연산자를 피연산자 뒤에 표기하는 방법

2. step1. 중위표기식의 후위표기식 변환 방법1
   
   * 수식의 각 연산자에 대해서 우선순위에 따라 **괄호를 사용**하여 다시 표현
   
   * 각 연산자를 그에 대응하는 **오른쪽 괄호의 뒤**로 이동시킨다.
   
   * **괄호를 제거**한다.

3. step1. 중위 표기법에서 후위 표기법으로의 변환 알고리즘(스택 이용)2
   
   * 입력 받은 중위 표기식에서 토큰(연산자or피연산자)을 읽는다.
   
   * 토큰 = **피연산자** ==> **출력**
   
   * 토큰 = **연산자(괄호포함)**
     
     * 우선순위: **스택top의 연산자 < 토큰** ==> 스택에 **push**
     
     * 우선순위: **같거나 낮을 경우** ==> 우선순위: **스택 top의 연산자 < 토큰 일 때까지** 스택에서 pop ==> 토큰의 연산자 push
     
     * 만약 top에 연산자가 없으면 ==> push
   
   * **토큰 == ")"** ==> 스택top에 **"("가 올 때까지** pop수행, pop한 연산자 출력
     
     * "("만나면 pop만 하고 출력x
   
   * 중위 표기식에 더 읽을 것이 없다면 중지하고, 더 읽을 것이 있다면 1부터 다시 반복
   
   * **스택에 남아있는 연산자**를 **모두 pop**하여 출력
   
   * 스택 밖의 왼쪽 괄호 -> 우선순위 가장 높음
   
   * 스택 안의 왼쪽 괄호 -> 우선순위 가장 낮음
   
   * **우선순위**
     
     | 토큰   | isp(in-stack priority) | icp(in-coming priority) |
     | ---- | ---------------------- | ----------------------- |
     | )    | -                      | -                       |
     | *, / | 2                      | 2                       |
     | +, - | 1                      | 1                       |
     | (    | 0                      | 3                       |

4. 연습문제1: 후위 표기식
   
   ```python
   # 중위연산식 ==> 후위연산식
   n = int(input())  # 식의 길이(문자 갯수)
   infix = input()  # 중위표기식을 문자열로 입력 받기
   
   stack = [0] * n  # 스택의 길이는 최대 n
   top = -1
   
   # 연산자의 우선순위
   icp = {"+": 1, "-": 1, "/": 2, "*": 2}
   
   postfix = ""
   
   # 중위연산식을 순회하면서 후위연산식으로 바꾸기
   for i in range(n):
       # i번째 문자를 하나 떼와서
       # 피연산자이면 ==> 출력, 연산자이면 우선순위 스택의 top과 비교
       if "0" <= infix[i] <= "9":  # 피연산자, 숫자인경우
           # print(infix[i], end=" ")
           postfix += infix[i]  # 문자열 조합
       else:
           # 연산자인 경우
           # 우선순위를 비교해서 스택의 top의 원소와 지금 떼온 연산자와 우선순위 비교
           # 우선순위 같거나 높으면 pop
           while top > -1 and icp[stack[top]] >= icp[infix[i]]:
               # pop시켜주고 문자열에 출력
               postfix += stack[top]
               top -= 1
           top += 1
           stack[top] = infix[i]
   # 만약 스택 안에 연산자가 남아있는 경우 수식 뒤에 붙여주기
   while top > -1:
       postfix += stack[top]
       top -= 1
   print(postfix)  # 후위 연산식 출력
   ```

## 2. 계산기2

----

1. step2. 후위 표기법의 수식을 스택을 이용하여 계산
   
   * **피연산자**를 만나면 ==> **스택에 push**
   
   * **연산자**를 만나면 ==> 필요한 만큼의 **피연산자를 스택에서 pop하여 연산** ==> **연산결과**를 다시 스택에 **push**
   
   * 수식이 끝나면 ==> 마지막으로 스택을 pop하여 출력

## 3. 백트래킹

----

1. 백트래킹(Backtracking)
   
   * 해를 찾는 도중에 **막히면**(즉, 해가 아니면) **되돌아가서 다시** 해를 찾아가는 기법
   
   * **최적화(optimization)** 문제와 **결정(decision)문제**를 해결할 수 있다.
   
   * **결정문제**: 문제의 조건을 만족하는 해가 존재하는지의 여부를 'yes' 또는 'no'가 답하는 문제
     
     * 미로 찾기
     
     * n-Queen 문제
     
     * Map coloring
     
     * 부분 집합의 합(Subset Sum) 문제 등
   
   * 백트래킹과 **깊이우선탐색과의 차이**
     
     * 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 ==> 더 이상 그 경로를 따라가지 않음으로써 시도의 횟수를 줄임(**prunning 가지치기**)
     
     * 깊이우선탐색: 모든 경로 추적, 백트래킹: 불필요한 경로 조기 차단
     
     * 깊이우선탐색을 가하기에는 경우의 수가 너무 많음.
       
       * N!가지의 경우의 수를 가진 문제에 대해 깊이우선탐색을 가하면 처리 불가능
     
     * 백트래킹 알고리즘을 적용하면 일반적으로 경우의 수가 줄어듦. but, 최악의 경우에는 여전히 지수함수 시간(Exponential Time)을 요하므로 처리 불가능
   
   * 백트래킹 기법
     
     * 어떤 노드의 유망성을 점검 - 유망(promising)하지 않다고 결정되면 - 그 노드의 부모로 되돌아가(backtracking) 다음 자식 노드로 감
     
     * 어떤 노드를 방문하였을 때 - 그 노드를 포함한 경로가 해답이 될 수 없으면 -> 그 노드는 유망하지 않다고 함. 해답의 가능성이 있으면 -> 유망하다
     
     * **가지치기(prunning)**: 유망하지 않는 노드가 포함되는 경로 - 더 이상 고려X
   
   * 백트래킹 이용 **알고리즘 절차**
     
     * 상태 공간 트리의 **깊이 우선 검색** 실시
     
     * 각 노드가 **유망한지** 점검
     
     * 만일 그 노드가 유망하지 않으면 -> 그 노드의 **부모 노드**로 돌아가서 검색 계속
   
   * 일반 백트래킹 알고리즘

2. 백트래킹: 미로찾기
   
   * 입구, 출구가 주어진 미로에서 입구~출구까지의 경로 찾는 문제
   
   * 이동 방향 4방향으로 제한
   
   * 미로찾기 알고리즘

## 3. 부분집합 구하기

---

1. 백트래킹 기법으로 powerset을 구해보자
   
   * 일반적인 백트래킹 접근 방법 이용
   
   * n개의 원소가 들어있는 집합의 2^n개의 부분집합을 만들 때는, True 또는 False값을 가지는 항목들로 구성된 n개의 배열을 만드는 방법 이용
   
   * 배열의 i번째 항목은 i번째의 원소가 부분집합의 값인지 아닌지를 나타내는 값

2. loop를 이용해서 부분집합을 생성하는 방법

3. powerset을 구하는 백트래킹 알고리즘
   
   ```python
   # 부분 집합 구하기
   def f(i, N):
       if i == N:
           for i in range(N):
               if bit[i]:
                   print(A[i], end=" ")
       else:
           bit[i] = 1
           f(i+1, N)
           bit[i] = 0
           f(i+1, N)
   A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
   bit = [0] * 10
   answer = 0
   f(0, 10)
   print(answer)
   ```

## 4. 순열 구하기

---

1. 단순하게 순열을 생성하는 방법

2. 백트래킹을 이용하여 순열 구하기

3. 연습문제2: powerset중 원소의 합이 10인 부분집합 구하기
   
   ```python
   # 부분집합의 합 - 백트래킹
   def f(i, N, s, t):
       global answer
       global cnt
       cnt += 1
       if i == N:
           if s == t:
               answer += 1
           return
       elif s > t:
           return
       else:
           f(i + 1, N, s + A[i], t)  # A[i]가 포함된 경우
           f(i + 1, N, s, t)  # A[i]가 포함되지 않는 경우
   ```

4. [참고] 부분 집합의 합
   
   * 남은 구간의 합을 다 더해도 찾는 값 미만인 경우 중단 가능

5. [참고] 순열
   
   * 사전 순 출력
     
     ```python
     # 순열
     def npr(i):
         if i == n:   #n과 같아지면 출력
             for num in s:
                 print(num, end=" ")
             print()
         else:
             # j번째 자리 구하기
             for j in range(1, n+1):
                 if not visited[j]:
                     visited[j] = True
                     s.append(j)
                     npr(i+1)
                     s.pop()
                     visited[j] = False
     n = int(input())
     s = []
     visited = [False] * (n+1)
     npr(0)
     ```
     
     ```
     
     ```

## 5. 분할 정복

----

1. 유래

2. 설계 전략
   
   * **분할(Divide)** : 해결할 문제를 여러 개의 작은 부분으로 나눈다.
   
   * **정복(Conquer)** : 나눈 작은 문제를 각각 해결한다.
   
   * **통합(Combine)** : (필요하다면) 해결된 해답을 모은다.

3. 분할정복 예제
   
   * 거듭 제곱(Exponentiation)
     
     ```python
     def power(base, e):
         if e == 0 or base == 0:
             return 1
         if e % 2 == 0:
             newbase = power(base, e/2)
             return newbase*newbase
         else:
             newbase = power(base, (e-1)/2)
             return (newbase*newbase)*base
     ```

4. 퀵 정렬
   
   * 주어진 배열을 두 개로 분할하고, 각각을 정렬
   
   * 합병정렬과 다른점
     
     * 합병정렬 -> 그냥 두 부분으로 나눔, 퀵정렬->**기준 아이템(pivot item)중심**으로 이보다 작은것은 왼편, 큰 것은 오른편에 위치시킨다.
     
     * 합병정렬 -> 각 부분 정렬 후 합병이라는 후처리 필요, 퀵정렬 -> **후처리 필요X**
   
   * 수행 과정
   
   * 알고리즘
     
     ```python
     def partition(arr, begin, end):
         pivot = (begin + end)//2
         L = begin
         R = end
         while L < R:
             while L < R and arr[L] < arr[pivot]:
                 L += 1
             while L < R and arr[R] >= arr[pivot]:
                 R -= 1
             if L < R:
                 if L == pivot:
                     pivot = R
                 arr[L], arr[R] = arr[R], arr[L]
         arr[pivot], arr[R] = arr[R], arr[pivot]
         return R
     
      def quicksort(arr, begin, end):
          if begin < end:
              p = partition(arr, begin, end)
              quicksort(arr, begin, p-1)
              quicksort(arr, p+1, end)
     ```
* 추가
  
  ```python
  def quicksort(arr, start, end):
      # 원소 1개인 경우
      if start >= end:
          return
  
      pivot = start
      left, right = start + 1, end
      while left <= right:
          # pivot보다 큰 데이터 찾을 때까지 반복
          while left <= end and arr[left] <= arr[pivot]:
              left += 1
          # pivot보다 작은 데이터를 찾을 때까지 반복
          while right > start and arr[right] >= arr[pivot]:
              right -= 1
          # 엇갈린 경우
          if left > right:
              arr[right], arr[pivot] = arr[pivot], arr[right]
          else:   # 엇갈리지 않은 경우
              arr[right], arr[left] = arr[left], arr[right]
      quicksort(arr, start, right-1)
      quicksort(arr, right+1, end)
  
  arr = [2, 5, 4, 3 ,21, 7, 1, 2, 4]
  quicksort(arr, 0, len(arr)-1)
  print(arr)
  
  def quicksort(arr):
      if len(arr) <= 1:
          return arr
      pivot = arr[0]
      tail = arr[1:]
      left = [x for x in tail if x <= pivot]
      right = [x for x in tail if x > pivot]
  
      return quicksort(left) + [pivot] + quicksort(right)
  ```
