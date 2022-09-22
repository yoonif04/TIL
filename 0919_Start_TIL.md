## 0. 목차

---

1. SW 문제 해결

2. 복잡도 분석

3. 표준 입출력 방법

4. 비트 연산

5. 진수

6. 실수

## 1. SW 문제 해결

---

1. SW 문제 해결 역량이란 무엇인가?
   
   * 프로그램을 하기 위한 많은 제약 조건과 요구사항을 이해하고 최선의 방법을 찾아내는 능력
   
   * 프로그래머가 사용하는 언어나 라이브러리, 자료구조, 알고리즘에 대한 지식을 적재적소에 퍼즐을 배치하듯 이들을 연결하여 큰 그림을 만드는 능력
   
   * 문제 해결 역량은 추상적인 기술이다.
   
   * 문제 해결 역량을 향상시키기 위해서 훈련이 필요하다.

## 2. 복잡도 분석

----

1. **알고리즘**: 유한한 단계를 통해 문제를 해결하기 위한 절차나 방법
   
   * 어떠한 문제를 해결하기 위한 절차

2. **알고리즘의 효율**
   
   * 공간적 효율성과 시간적 효율성
     
     * **공간적 효율성**: 연산량 대비 얼마나 적은 **메모리 공간**을 요하는지
     
     * **시간적 효율성**: 연산량 대비 얼마나 적은 **시간**을 요하는지
     
     * 효율성 <-> 복잡도
     
     * 복잡도가 높을수록 효율성 저하
   
   * 시간적 복잡도 분석
     
     * 하드웨어 환경에 따라 처리시간이 달라짐
       
       * 부동소수 처리 프로세서 존재유무, 나눗셈 가속기능 유무
       
       * 입출력 장비의 성능, 공유여부
     
     * 소프트웨어 환경에 따라 처리시간 달라짐
       
       * 프로그램 언어의 종류
       
       * 운영체제, 컴파일러의 종류
     
     * 이러한 환경적 차이로 인해 분석 어려움
   
   * **복잡도의 점근적 표기**
     
     * 시간(또는 공간)복잡도는 입력 크기에 대한 함수로 표기하는데, 이 함수는 주로 여러개의 항을 가지는 다항식이다.
     
     * 이를 단순한 함수로 표현하기 위해 점근적 표기(Asymptotic Notation) 사용
     
     * 입력 크기 n이 무한대로 커질 때의 복잡도를 간단히 표현하기 위해 사용하는 표기법
       
       * Big-Oh 표기
       
       * Big-Omega 표기
       
       * Big-Theta 표기
   
   * **O(Big-Oh) 표기**
     
     * O-표기는 복잡도의 **점근적 상한**을 나타낸다
   
   * **Big-Omega 표기**
     
     * 복잡도의 **점근적 하한**을 의미
     
     * 복잡도 다항식의 최고차항만 계수 없이 취하면 됨
   
   * **Theta 표기**
     
     * big-oh 표기와 big-omega 표기가 같은 경우
   
   * 자주 사용하는 O-표기
   
   * 왜 효율적인 알고리즘이 필요한가

## 3. 표준 입출력 방법

---

1. **Python3 표준입출력**
   
   * **입력**
     
     * Raw 값의 입력: **input()**
       
       * 받은 입력값을 문자열로 취급
     
     * Evaluated된 값 입력: **eval(input())**
       
       * 받은 입력값을 평가된 데이터 형으로 취급
   
   * **출력**
     
     * **print()**: 표준 출력 함수. 마지막에 개행 문자 포함
     * **print('text', end='')**: 출력 시 마지막에 개행문자 제외할 시
     * **print('%d' %number)**: Formatting된 출력
   
   * 파일의 내용을 **표준 입력**으로 읽어오는 방법
     
     * import sys
     
     * sys.stdin = open("이름.txt", "r")

## 4. 비트 연산

---

1. **비트 연산자**
   
   | 연산자    | 연산자의 기능                            |
   | ------ | ---------------------------------- |
   | **&**  | 비트단위로 **AND** 연산                   |
   | **\|** | 비트단위로 **OR** 연산                    |
   | **^**  | 비트단위로 **XOR** 연산 (**같으면 0 다르면 1**) |
   | **\~** | 단항 연산자로서 피연산자의 모든 비트를 **반전**시킨다.   |
   | **<<** | 피연산자의 비트 열을 **왼쪽으로** 이동            |
   | **>>** | 피연산자의 비트 열을 **오른쪽으로** 이동           |
   
   * ^연산자 -> 특정 bit 반전시키는 효과
   
   * **1<<n**
     
     * 2의 n제곱 값을 갖는다.
     
     * 원소가 n개일 경우의 **모든 부분집합의 수** 의미
     
     * Power set (모든 부분 집합)
       
       * 공집합과 자기 자신을 포함한 모든 부분집합
       
       * 각 원소가 포함되거나 포함되지 않는 2가지 경우의 수를 계산하면 모든 부분집합의 수가 계산된다.
   
   * **i & (1<<j)** : 계산 결과는 **i의 j번째 비트**가 **1인지 아닌지**를 의미
   
   * 비트 연산 예제1
     
     ```python
     def Bbit_print(i):
         output = ""
         for j in range(7, -1, -1):
             output += '1' if i & (1 << j) else '0'
         print(output)
      for i in range(-5, 6):
          print("%3d = " % i, end="")
          Bbit_print(i)
     ```
   
   * 비트 연산 예제2
     
     ```python
     def Bbit_print(i):
         output = ""
         for j in range(7, -1, -1):
             output += "1" if i & (1<<j) else "0"
         print(output, end=" ")
     a = 0x10
     x = 0x01020304
     print("%d = " %a, end="")
     Bbit_print(a)
     print()
     print("0%X = " %x, end="")
     for i in range(0, 4):
         Bbit_print((x >> i*8) & 0xff)
     print()
     ```

2. 연습문제1: 0과 1로 이루어진 1차 배열에서 7개 bit를 묶어서 10진수로 출력하기
   
   ```python
   nums = input()
   binary_list = [0] * 7
   for i in range(7):
       binary_list[7-1-i] = 2**i
   
   for i in range(0, len(nums)-1, 7):
       num = nums[i:i+7]
       result = 0
       for i in range(7):
           result += int(num[i]) * binary_list[i]
       print(result)
   ```

3. **엔디안(Endianness)**
   
   * 컴퓨터의 메모리와 같은 1차원의 공간에 여러 개의 **연속된 대상을 배열하는 방법**을 의미하며 HW 아키텍처마다 다르다.
   
   * 주의: 속도 향상을 위해 바이트 단위와 워드 단위를 변환하여 연산할 때 올바로 이해하지 않으면 오류를 발생 시킬 수 있다.
   
   * **빅 엔디안(Bit-endian)**: 보통 큰 단위가 앞에 나옴. 네트워크.
   
   * **리틀 엔디안(Little-endian)**: 작은 단위가 앞에 나옴. 대다수 데스크탑 컴퓨터.
   
   * 엔디안 확인 코드
     
     * import sys
     
     * print(sys.byteorder)
   
   * 비트 연산 예제3, 4
     
     ```python
     def ce(n):
         p = []
         for i in range(0, 4):
             p.append((n >> (24 - i * 8)) & 0xff)
         return p
     def ce1(n):
         return (n << 24 & 0xff000000) | (n << 8 & 0xff0000) | (n >> 8 & 0xff00) | (n >> 24 & 0xff)
     x = 0x01020304
     p = []
     for i in range(0, 4):
         p.append((x >> (i * 8)) & 0xff)
     print("x = %d%d%d%d" % (p[0], p[1], p[2], p[3]))
     p = ce(x)
     print("x = %d%d%d%d" % (p[0], p[1], p[2], p[3]))
     ce1(x)
     print("x = %d%d%d%d" % (p[0], p[1], p[2], p[3]))
     ```
   
   * 비트 연산 예제5: 비트 연산자 ^를 두 번 연산 -> 처음 값을 반환
     
     ```python
     def Bbit_print(i):
         output = ""
         for j in range(7, -1, -1):
             output += "1" if i & (1 << j) else "0"
         print(output)
     a = 0x86
     key = 0xAA
     print("a       ==> ", end="")
     Bbit_print(a)
     print("a^=key  ==> ", end="");
     a ^= key;
     Bbit_print(a)
     print("a^=key  ==> ", end="");
     a ^= key;
     Bbit_print(a)
     ```

## 5. 진수

---

1. 10진수 -> 타 진수로 변환
   
   * 원하는 타진법의 수로 나눈 뒤 나머지를 거꾸로 읽는다.

2. 타 진수 -> 10진수로 변환

3. 컴퓨터에서의 음의 정수 표현 방법
   
   * **1의 보수**: 부호와 절대값으로 표현된 값을 **부호 비트를 제외**한 나머지 비트들을 **0은 1로, 1은 0으로 변환**한다.
   
   * **2의 보수**: **1의 보수방법**으로 표현된 값의 **최하위 비트에 1을 더한다.**

4. 연습문제2
   
   ```python
   def change_2(n):
       p = [0] * 4
       for i in range(4-1, -1, -1):
           p[i] = n % 2
           n//=2
       for num in p:
           result.append(num)
   words = input()
   result = []
   for word in words:
       if "0" <= word <= "9":
           change_2(int(word))
       else:
           change_2(ord(word) - 55)
   binary_7 = [0] * 7
   for i in range(7):
       binary_7[7-1-i] = 2**i
   for i in range(0, len(result), 7):
       num = result[i: i+7]
       result_num = 0
       for j in range(len(num)-1, -1, -1):
           result_num += num[len(num)-1-j] * binary_7[7-1-j]
       print(result_num, end=" ")
   print()
   ```

## 6. 실수

---

1. 실수의 표현
   
   * 2진 실수를 10진수로 변환하는 방법
   
   * **부동 소수점(floating-point) 표기법**
     
     * **소수점의 위치를 고정**시켜 표현하는 방식
     * 소수점의 위치를 **왼쪽의 가장 유효한 숫자 다음으로** 고정시키고 밑수의 지수승으로 표현
   
   * 실수를 저장하기 위한 형식
     
     * **단정도 실수(32비트)**
     
     * **배정도 실수(64비트)**
     
     * **가수부(mantissa)** : 실수의 유효 자릿수들을 부호화된 고정 소수점으로 표현한 것
     
     * **지수부(exponent)** : 실제 소수점의 위치를 지수 승으로 표현한 것
   
   * 단정도 실수의 가수 부분을 만드는 방법
   
   * 단정도 실수의 지수 부분을 만드는 방법
   
   * 컴퓨터는 실수를 근사적으로 표현한다.
   
   * 실수 자료형의 **유효 자릿수**
     
     * 32비트 실수형 유효자릿수(십진수) -> 6
     
     * 64비트 실수형 유효자릿수(십진수) -> 15
   
   * 파이썬에서의 실수 표현 범위

2. 연습문제 3
   
   ```python
   pattern = {
       "001101": 0, "010011": 1, "111011": 2, "110001": 3, "100011": 4,
       "110111": 5, "001011": 6, "111101": 7, "011001": 8, "101111": 9,
   }
   def decode(c):
       p = ['0'] * 4
       for i in range(3, -1, -1):
           p[i] = str(c % 2)
           c //= 2
       return "".join(p)
   codes = input()
   change_code = ""
   for code in codes:
       if "0" <= code <= "9":
           change_code += decode(int(code))
       else:
           change_code += decode(ord(code) - 55)
   change_code = change_code.rstrip("0")
   result = []
   idx = len(change_code)-1
   while idx >= 0:
       if change_code[idx] == "1":
           result.append(pattern[change_code[idx-5: idx+1]])
           idx -= 6
       else:
           idx -= 1
   for i in range(len(result)-1, -1, -1):
       print(result[i], end=" ")
   print()
   ```
