## 0. 문자열

----

1. 문자열

2. 패턴 매칭

3. 문자열 암호화

4. 문자열 압축

5. 정수론

## 1. 문자의 표현

----

1. 컴퓨터에서의 문자표현
   
   * 각 문자에 대해서 대응되는 숫자 - 이것을 메모리에 저장
   
   * 영어 - 대소문자 합쳐서 52 - 6비트면 모두 표현 가능 -> 이를 코드체계라고 함
   
   * 각 지역 별 코드체계 - 네트워크 발전 - 서로 정보를 주고 받을 때 다르게 해석
   
   * 혼동을 피하기 위해 표준안 만듦
   
   * ASCII(American Standard Code for Information Interchange)
     
     * 7bit 인코딩, 128문자 표현, 33개의 출력 불가능한 제어 문자, 공백을 비롯한 95개의 출력 가능한 문자
   
   * 확장 아스키
   
   * 유니코드

2. 16진수 계산하기
   
   * 0 1 2 3 4 5 6 7 8 9 A(10) B(11) C(12) D(13) E(14) F(15)
   
   * AB01 = 16^3*10 + 16^2\*11 + 16^1*0 + 1
   
   * 16진수 = 2^4 -> 2진수 4칸과 같다.

## 2. 문자열

----

1. 문자열
   
   * 문자열의 분류
     
     * fixed length
     
     * variable length
       
       * length controlled
       
       * delimited
   
   * java에서 String 클래스에 대한 메모리 배치 예
   
   * c언어에서 문자열 처리
   
   * strlen() 함수 만들어 보기("\0"을 만나기 전까지의 글자수)
     
     ```python
     def strlen(a):
         cnt = 0
         idx = 0
         while True:
             if a[idx] != "\0":
                 cnt += 1
                 idx += 1
             else:
                 break
         return cnt
     
     def strlen(a):
         idx = 0
         while a[idx] != "\0":
             idx += 1
         return idx
     
     a = ['a', 'b', 'c', '\0']
     print(strlen(a))
     ```
   
   * java에서의 문자열 처리
   
   * python에서의 문자열 처리
     
     * char 타입X
     
     * 텍스트 데이터의 취급방법 통일
     
     * 문자열 기호
       
       * ', ", ''', """
       
       * +연결: 문자열 이어 붙여주는 역할
       
       * *반복: 문자열 반복
     
     * 문자열 -> 시퀀스 자료형 -> 인덱싱, 슬라이싱 연산 가능
     
     * 메소드: replace(), split(), isalpha(), find()
     
     * immutable
   
   * C와 Java의 String 처리의 기본적인 차이점

2. 문자열 뒤집기
   
   * 자기 문자열에서 뒤집기
     
     ```python
     def my_reverse2(s):
         list_s = list(s)  # 리스트로 바꾸기
         for i in range(len(s)//2):  # -(i+1)과 len(s)-i-1 동일
             list_s[i], list_s[-(i+1)] = list_s[-(i+1)], list_s[i]
         new_s = ''.join(list_s)
         # for chr in list_s:
         #     new_s += chr
         return new_s
     ```
   
   * 새로운 빈 문자열을 만들기
     
     ```python
     def my_reverse(s):
         reverse = ''  # 새로 만들 문자열
         for i in range(len(s)-1, -1, -1):
             reverse += s[i]
         return reverse
     ```

3. 문자열 비교
   
   * == 연산자: 값이 같은지
     
     * 내부적으로 \_eq\_() 호출 
   
   * is 연산자: 메모리 같은지
     
     ```python
     s1 = 'abc'
     s2 = 'abc'
     s3 = 'def'
     s4 = s1
     s5 = s1[:2] + 'c'
     # == 값이 같은지, is 메모리 같은지
     print(s1 == s2)  # True
     # 파이썬 문자열 저장할 때 똑같은 문자열 -> 같은 메모리 사용
     print(s1 is s2)  # True
     print(s1 == s3)  # False
     print(s1 is s3)  # False
     print(s1 == s4)  # True
     print(s1 is s4)  # True
     print(s1 == s5)  # True
     print(s1 i
     ```
   
   * 사전 순서: 같으면 0, str1이 앞서면 -1, str2이 앞서면 1 리턴
     
     ```python
     def my_strcmp(str1, str2):
         if str1 == str2:
             return 0
         elif str1 < str2:
             return -1
         else:
             return 1
     def my_strcmp2(str1, str2):
          if str1 == str2:
              return 0
          idx = 0
          while idx < len(str1) and idx < len(str2):
              if ord(str1[idx]) < ord(str2[idx]):
                  return -1
              elif ord(str1[idx]) > ord(str2[idx]):
                  return 1
              idx += 1
          if len(str1) < len(str2):
              return -1
          elif len(str1) > len(str2):
              return 1
          else:
              return 0
      def my_strcmp3(str1, str2):
           idx = 0
           while idx < len(str1):
               if str1[idx] != str2[idx]:
                   break
               idx += 1
           return ord(str1[idx]) - ord(str2[idx])
     ```

4. 문자열 숫자를 정수로 변환하기
   
   * atoi
     
     ```python
     def atoi(s):
              i = 0
              for word in s:
                  i = i*10 + ord(word)-ord('0')
              return i
     ```
   
   * itoa
     
     ```python
     def itoa(a):
              i = 10
              s = ""  # 숫자를 문자열로 바꾼 결과
              while a > 0:
                  mod = a % i
                  s += chr(ord('0') + mod)
                  a //= 10
              return s
     ```

## 3. 패턴 매칭

---

1. 패턴 매칭
   
   - 알고리즘
     
     - 고지식한 패턴 검색 알고리즘
     
     - 카프-라빈 알고리즘
     
     - KMP 알고리즘
     
     - 보이어-무어 알고리즘

2. **고지식한 알고리즘(Brute Force)**
   
   - 문자열을 처음부터 끝까지 차례대로 순회, 패턴 내의 문자들을 일일이 비교
   
   - **구현**
     
     ```python
     def BruteForce(p, t):
        idx_t, idx_p = 0, 0   # t,p의 인덱스
        while idx_p < len(p) and idx_t < len(t):
            if t[idx_t] != p[idx_p]:
                idx_t -= idx_p
                idx_p = -1
            idx_t += 1
            idx_p += 1
        if idx_p == len(p):
            return idx_t - len(p)  # 일치 인덱스
        else:
            return -1
     ```
   
   - **시간 복잡도** : **O(MN)**, 패턴길이N, 문자열M
     
     - 최악의 경우 텍스트의 모든 위치에서 패턴을 비교해야함

3. **KMP 알고리즘**
   
   - 불일치가 발생한 텍스트 스트링의 앞부분에 어떤 문자가 있는지 미리 알고 있음 -> 불일치 발생한 앞 부분에 대하여 다시 비교하지 않고 매칭 수행
   
   - 패턴을 전처리 -> 배열 next[M] 을 구해서 잘못된 시작 최소화
     
     - **next[M]** : 불일치 발생했을 경우 **이동할 다음 위치**
   
   - **시간 복잡도** : **O(M+N)**
   
   - 아이디어 설명
     
     - abcdabc까지는 매치되고, e에서 실패한 상황.
     
     - 패턴의 맨 앞의 abc와 실패 직전의 abc는 동일함 이용
     
     - 매칭이 실패했을 때 돌아갈 곳을 계산
       
       ```python
       abcdabcd
       abcdabcef
          abcdabcef   #d부터 비교
       ```
   
   - 알고리즘
     
     ```python
     def kmp(t, p):
         N = len(t)
         M = len(p)
         lps = [0] * (M+1)
         # preprocessing, 전처리
         # 패턴 중에 중복되는 부분을 찾는다.
         # 일치했었다 라는 정보를 이용해 중복되는 부분을 통해 어디까지 건너뛸지 계산하기 위함
         j = 0 # 일치한 개수== 비교할 패턴 위치
         lps[0] = -1
         for i in range(1, M):
             lps[i] = j          # p[i]이전에 일치한 개수
             if p[i] == p[j]:
                 j += 1
             else:
                 j = 0
         lps[M] = j
         print(lps)
         # search
         i = 0   # 비교할 텍스트 위치
         j = 0   # 비교할 패턴 위치
         while i < N and j <= M:
             if j==-1 or t[i]== p[j]:     # 첫글자가 불일치했거나, 일치하면 일치하지 않을때까지 쭉
                 i += 1
                 j += 1
             else:               # 일치하지 않는 순간 j는 돌아갈 위치를 찾아서 간다.
                 j = lps[j]
             if j==M:    # 패턴을 찾을 경우 ( 비교할 패턴 위치가 돌아가지 않고 무사히 마지막위치까지 왔다!! )
                 print(i-M, end = ' ')    # 패턴의 인덱스 출력
                 j = lps[j]
     ```

4. **보이어-무어 알고리즘**
   
   * **오른쪽 -> 왼쪽**으로 비교
   
   * 대부분의 상용 소프트웨어에서 채택하고 있는 알고리즘
   
   * 패턴의 **오른쪽 끝**에 있는 **문자가 불일치**하고 이 문자가 **패턴 내에 존재하지 않**는 경우, **이동 거리는 패턴의 길이만큼**
   
   * 오른쪽 끝에 있는 문자가 불일치하고, 이 문자가 패턴 내에 존재할 경우
     
     * 패턴에서 일치하는 문자를 찾아서 점프
   
   * 알고리즘
     
     ```python
     # skip 배열 사용하지 않고 건너뛸 때마다 계산하는 방법 사용
     def boyer_moore(pattern, text):
         M = len(pattern)
         N = len(text)
         i = 0 # text에서 비교할 문자의 인덱스
         res = [] # 찾은 문자열 위치를 저장할 리스트
         # 반복은 최대 긴텍스트 길이 - 작은텍스트 길이
         while i <= N-M:
             # 보이어 무어 알고리즘은 뒤에서부터 접근하므로 pattern길이의 -1을 해준다.
             # -1을 해주는 이유는 인덱스 범위 때문이다.
             j = M - 1 # pattern 에서 비교할 문자의 인덱스
             # 뒤에서부터 검사하고 인덱스를 감소하는 형식이므로 0 이상일때만 동작한다.
             while j >= 0:
                 # 마지막 글자부터 비교하면서 같은 글자가 나오면 추가로 하나씩 감소하면서 비교한다.
                 if pattern[j] != text[i+j]:
                     # 글자가 틀리다면 얼마나 점프할지 정해야 하므로
                     # 제일마지막 글자 기준으로 find 함수를 호출한다.
                     move = find(pattern, text[i + M - 1])
                     break
                 j = j - 1
             # 인덱스가 -1이라는 뜻은 패턴의 모든 글자가 같다는 말이다.
             if j == -1
                 # 일치하는 패턴을 찾았으므로
                 # 인덱스 추가하고 패턴 길이만큼 점프
                 res.append(i)
                 i += M
             else:
                 # -1이 아니라면 글자를 못찾은 것이므로 find에서 넘겨준 값만큼 옆으로 이동한다.
                 i += move
     
         return res
     
     # 건너뛰기 위한 함수
     def find(pattern, char):
         # 마지막 부분과 일치하는 부분이 있는지 검색한다.
         # 마지막 부분은 이미 가능성이 없으므로 그전부터 검사한다.
         for i in range(len(pattern)-2, -1, -1):
             # 마지막글자와 패턴중 일치하는 글자가 있다면 그만큼 이동한다.
             if pattern[i] == char:
                 return len(pattern) -i -1
         # 일치하는 글자가 없다면 패턴의 길이만큼 이동한다.
         return len(pattern)
     
     print(boyer_moore("abc" , "zzabcababczzabc"))
     ```

5. 문자열 매칭 알고리즘 비교
   
   * 문자열 매칭 알고리즘 비교
     
     * 찾고자 하는 문자열 패턴의 길이: m, 총 문자열 길이: n
     
     * 고지식한 패턴 검색 알고리즘 : O(mn)
     
     * 카프-라빈 알고리즘 : 세타(n)
     
     * KMP 알고리즘 : 세타(n)
     
     * 두 알고리즘들의 공통점 : 문자열의 문자를 적어도 한번씩 훑음 -> 최선의 경우에도 옴(n)
     
     * 보이어-무어 알고리즘
       
       * 텍스트 문자를 다 보지 않아도 됨
       
       * 발상의 전환 : 패턴의 오른쪽부터 비교
       
       * 최악의 경우 : 세타(mn)
       
       * 입력에 따라 다르지만, 일반적으로 세타(n)보다 시간이 덜 든다.

## 4. 문자열 암호화

----

1. 시저 암호

## 5. 정수론

----

1. 최대공약수 구하기
   
   * 최대공약수: 두 수에 서로 공통으로 존재하는 약수(공약수) 중 큰수
   
   * 유클리드 호제법: 2개의 자연수 a, b(a>b)에 대해서 a를 b로 나눈 나머지가 r일때, a와 b의 최대공약수는 b와 r의 최대 공약수와 같다.
     
     * 이를 반복해서 나머지가 0이 되었을 때, 이때 나누는 수가 a와  b의 최대공약수
     
     ```python
     # gcd: greatest common divisor
     def gcd(a, b):  # a > b
         r = 0  # 나머지
         # a를 나누어 떨어질 때까지 나눈다
         while b != 0:
             r = a % b
             a = b
             b = r
         return a
     ```

2. 최소공배수 구하기
   
   * 최소공배수: 두 수에 서로 공통으로 존재하는 배수(공배수) 중 작은수
   
   * 성질: 두 수  a와b의 최소공배수는 a*b를 최대공약수로 나눈 것과 같다.
     
     ```python
     # lcm: least common multiple
     def lcm(a, b):
         return int(a*b/gcd(a, b))
     ```

3. 소수 구하기
   
   * 소수: 약수가 1 또는 자기 자신밖에 없는 숫자(prime number)
     
     ```python
     def is_prime(n):
         if n <2:
             return False
         else:
             for i in range(2, n):
                 if n % i == 0:
                     return False
             return True
     ```

4. 에라토스테네스의 체
   
   * 체로 치듯이 수를 걸러낸다고해서 붙여진 이름
     
     ```python
     def get_prime(n):  # n까지의 숫자 중에서 소수를 구한다.
         arr = [True] * (n+1)  # 일단 n까지의 숫자를 다 소수라고 표시
         # n의 제곱근까지만 검사해서 최적화
         # 제곱근을 쓰는 이유: n = a*b로 나타낼 수 있다.
         # n' 를 n의 제곱근이라고 하자
         # n=n'*n' 여기서 a>=n'일때, a*b=n=n'*n' <=> b<=n'
         # n'까지만 검사를 하면 두 수 ab중에 작은수 b까지만 체크해봐도(a는 검사안해도)소수판별가능
         # 16 => 1, 2, 4, 8, 16
         m = int((n+1)**0.5)
         for i in range(2, m+1):
             if arr[i]:  # 만약 i번째 수가 소수다
                 # 소수의 배수를 모두 소수가 아니라고 체크
                 for j in range(i+i, n+1, i):
                     arr[j] = False
         return [i for i in range(2, n+1) if arr[i] == True]
     ```
