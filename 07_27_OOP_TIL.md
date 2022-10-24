# OOP

# 1. 객체지향 프로그래밍(OOP)

----

1. 객체 지향 프로그래밍이란?
   
   * **객체 지향 프로그래밍(Object-Oriented Programming, OOP)**: 컴퓨터 프로그래밍의 **패러다임(방법론)** 중 하나
   
   * 컴퓨터 프로그램을 <u>명령어의 목록</u>으로 보는 시각에서 벗어나 <u>여러 개의 독립된 단위</u>, 즉 '**객체'들의 모임**으로 파악하고자 하는 것
   
   * 각각의 객체는 <u>메시지</u>를 주고받고, <u>데이터</u>를 처리할 수 있다.
   
   * 프로그램을 **여러 개의 독립된 객체들**과 그 **객체 간의 상호작용**으로 파악하는 프로그래밍 방법
   
   * 객체 -> <u>정보(변수)와 행동(함수)</u>으로 표현 가능한 것
   
   * 절차지향 프로그래밍 -> 하나의 데이터와 여러 함수의 연결 -> 수정이 어려움
   
   * 데이터와 기능(메서드) 분리, 추상화된 구조(인터페이스)
   
   * 객체지향 프로그래밍이 **필요한 이유**
     
     * **현실 세계**를 프로그램 설계에 **반영**(**추상화**): 복잡한 내용 숨기고 필요한 것만
   
   * **장점**
     
     * <u>클래스 단위</u>로 **모듈화시켜 개발**할 수 있다. -> 많은 인원이 참여하는 <u>대규모 소프트웨어 개발</u>에 적합
     
     * <u>필요한 부분만</u> **수정하기 쉽다.** -> 프로그램의 **유지보수가 쉬움**
   
   * **단점**
     
     * 설계 시 **많은 노력과 시간** 필요
       
       * 다양한 객체들의 **상호 작용 구조**를 만들기 위해 많은 시간과 노력 필요
     
     * **실행 속도**가 상대적으로 **느림**
       
       * 절차 지향 프로그래밍이 컴퓨터의 처리구조와 비슷해서 실행 속도 빠름

2. OOP 기초
   
   * **객체(object)**
     
     * 클래스에서 정의한 것을 토대로 메모리(실제 저장공간)에 할당된 것
     
     * **속성**(정보,**변수**)과 **행동**(동작, **함수-메서드**) 으로 구성된 모든 것
     
     * 객체는 특정 타입의 인스턴스이다.
       
       * ex. 123, 900, 5는 모두 int의 인스턴스
   
   * **클래스와 객체**
     
     * **클래스(설계도)**, **객체(실제 사례)**
     
     * 클래스를 만든다 == **타입**을 만든다
   
   * **객체와 인스턴스**
     
     * **클래스로 만든 객체**를 **인스턴스**라고도 함
     
     * **특정 타입/클래스의 인스턴스**라고 표현
     
     * ex. 이찬혁은 가수의 인스턴스다(O), 이찬혁은 인스턴스다(X)
   
   * **파이썬**은 **모든 것**이 **객체(Object)**
     
     * 파이썬의 모든 것엔 **속성과 행동**이 존재
   
   * **객체의 특징**
     
     * **타입(type)**: 어떤 연산자(operator)와 조작(method)이 가능한가?
       
       * ex. 문자열+문자열과 숫자+숫자는 결과가 다름
     
     * **속성(attribute)**: 어떤 **상태(데이터)** 를 가지는가?
     
     * **조작법(method)**: 어떤 **행위(함수)** 를 할 수 있는가?
     
     * 객체 = 속성(Attribute, 상태, 정보) + 기능(Method)

3. **객체와 클래스 문법**
   
   * 기본 문법
     
     ```python
     # 1. 클래스 정의
     class MyClass:
         pass
     # 2. 인스턴스 생성
     my_instance = MyClass()
     # 3. 메서드 호출
     my_instance.my_method()
     # 4. 속성
     my_instance.my_attribute
     print(isinstance(my_instance, MyClass))  # True
     ```
   
   * 객체 비교하기
     
     * **==**
       * 동등한(**equal**)
       * 변수가 참조하는 객체가 동등한(**내용이 같은**) 경우 **True**
       * 두 객체가 같아 보이지만 실제로 **동일한 대상**을 가리키고 있다고 **확인X**
     * **is**
       * 동일한(**identical**)
       * 두 변수가 **동일한 객체**를 가리키는 경우 **True**
     
     ```python
     a = [1, 2, 3]
     b = [1, 2, 3]
     print(a == b, a is b) # True False
     
     a = [1, 2, 3]
     b = a
     print(a == b, a is b) # True True
     ```

4. **OOP 속성**
   
   * **속성**(데이터, 정보, 상태 -> 변수)
     
     * 특정 데이터 타입/클래스의 **객체들**이 가지게 될 **상태/데이터**를 의미
     
     * **클래스 변수** / **인스턴스 변수**가 존재
   
   * **인스턴스 변수**
     
     * 인스턴스가 **개인적**으로 가지고 있는 **속성**(attribute)
     
     * 각 인스턴스들의 **고유한 변수**
     
     * 생성자 메서드(_____init______)에서 **self.<name>** 으로 정의
     
     * 인스턴스가 생성된 이후 <instance>.<name>으로 접근 및 할당
     
     ```python
     class Person:
         def __init__(self, name):
             self.name = name
     
     john = Person('john')
     print(john.name)  # john
     ```
   
   * **클래스 변수**
     
     * 클래스 선언 내부에서 정의
     
     * <classname>.<name>으로 접근 및 할당
     
     * 인스턴스로도 클래스 변수 조회 가능: <instance>.<name> 인스턴스 변수 찾아보고 없으면 -> 클래스 변수 찾아본다.
     
     ```python
     class Circle():
         pi = 3.14   # 클래스 변수 정의
     
         def __init__(self, r):
             self.r = r   # 인스턴스 변수
     
     c1 = Circle(5)
     print(Circle.pi)  # 3.14
     print(c1.pi)      # 3/14
     ```
   
   * **클래스 변수 활용**하기
     
     * 사용자가 몇 명인지 확인하고 싶다면?
     
     * 인스턴스가 생성 될 때마다 클래스 변수가 늘어나도록 설정하면 됨
     
     ```python
     class Person:
         count = 0
         def __init__(self, name):
             self.name = name
             Person.count += 1
     
     person1 = Person('아이유')
     person2 = Person('이찬혁')
     print(Person.count)   # 2
     ```
   
   * 클래스 변수와 인스턴스 변수
     
     * **클래스 변수 변경**: <u>항상</u> **클래스.클래스변수** 형식으로 변경

5. **OOP 메서드**
   
   * **메서드**: 특정 데이터 타입/클래스의 객체에 **공통적**으로 적용 가능한 **행위**(**함수**)
   
   * 메서드의 **종류**: 인스턴스 메서드, 클래스 메서드, 정적 메서드

6. **인스턴스 메서드**
   
   * 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메서드
   
   * **클래스 내부**에 정의되는 메서드의 기본
   
   * **호출 시**, **첫번째 인자**로 인스턴스 **자기자신(self)** 이 전달됨
   
   * self가 있으면 -> 인스턴스 메서드
   
   * **self**
     
     * 인스턴스 자기자신
     
     * 인스턴스 메서드는 호출 시 자기자신이 전달되는 **파이썬 암묵적 규칙**
   
   * **생성자(constructor)메서드**
     
     * 인스턴스 **객체가 생성**될 때 **자동으로 호출**되는 메서드
     
     * 인스턴스 변수들의 **초기값**을 설정
       
       * 인스턴스 생성
       
       * __init__메서드 자동 호출
     
     ```python
     class Person:
         def __init__(self, name):
             print(f'인스턴스 생성 {name}')
     
     person1 = Person('지민')  # 인스턴스 생성 지민
     ```
   
   * **매직 메서드(스페셜 메서드)**
     
     * Double underscore(____)가 있는 메서드는 **특수한 동작**을 위해 만들어진 메서드
     
     * 특정 상황에 자동으로 불리는 메서드
     
     * 예시
       
       * 객체의 특수 조작 행위를 지정(함수, 연산자 등)
       
       * ______str_____ : 해당 객체의 출력 형태를 지정
         
         * 프린트 함수 호출할 때, 자동으로 호출
         
         * 어떤 인스턴스를 출력하면 ____str_____의 return 값 출력
       
       * ______gt_____:  부등호 연산자(>, greater than)
       
       ```python
       class Circle:
           def __init__(self, r):
               self.r = r
       
           def area(self):
               return 3.14 * self.r * self.r
       
           def __str__(self):
               return f'[원] radius: {self.r}'
       
           def __gt__(self, other):
               return self.r > other.r
       
           def __eq__(self, other):
               return self.r == other.r
       
       c1 = Circle(10)
       c2 = Circle(1)
       
       print(c1)     # [원] radius: 10
       print(c2)     # [원] radius: 1
       print(c1 > c2) # True
       print(c1 < c2) # False
       print(c1 == c2) # False
       ```
   
   * **소멸자(destructor) 메서드**
     
     * 인스턴스 객체가 **소멸(파괴)** 되기 직전에 **호출**되는 메서드
     
     ```python
     class Person:
         def __del__(self):
             print('인스턴스 소멸')
     
     person1 = Person()
     del person1   # 인스턴스 소멸, person1.__del__() 동일
     ```

7. **클래스 메서드**
   
   * **클래스 메서드**
     
     * 클래스가 사용할 메서드
     
     * **@classmethod** 데코레이터를 사용하여 정의
     
     * 호출 시, **첫번째 인자**로 클래스(**cls**)가 전달됨
     
     ```python
     class Person:
         count = 0
         def __init__(self, name):
             self.name = name
             Person.count += 1
     
         @classmethod
         def number_of_population(cls):
             print(f'인구수 {cls.count}')
     
     person1 = Person('아이유')
     person2 = Person('이찬혁')
     Person.number_of_population()  # 인구수 2
     ```
   
   * **데코레이터**
     
     * 함수를 **어떤 함수로 꾸며서 새로운 기능**을 부여
     
     * **@데코레이터(함수명)** 형태로 함수 위에 작성
     
     * 순서대로 적용되기 때문에 **작성 순서가 중요**
     
     * 데코레이터를 활용하면 **쉽게 여러 함수**를 원하는대로 **변경 가능**
     
     ```python
     # 데코레이팅 함수
     def add_print(original):
         def wrapper():
             print('시작')
             original()
             print('끝')
         return wrapper   # 함수 return
     
     @add_print
     def print_hello():
         print('hello')
     
     print_hello()
     # 시작
     # hello
     # 끝
     ```

8. **클래스 메서드와 인스턴스 메서드**
   
   * **클래스 메서드** -> **클래스 변수 사용**
   
   * **인스턴스 메서드** -> **인스턴스 변수 사용**
   
   * 인스턴스 변수, 클래스 변수 **모두 사용**하고 싶다면?
     
     * **클래스**는 **인스턴스 변수** **사용**이 **불가능**
     
     * **인스턴스 메서드**는 클래스 변수, 인스턴스 변수 **둘 다 사용 가능**

9. **스태틱 메서드**
   
   * **스태틱 메서드**: 인스턴스 변수, 클래스 변수를 **전혀 다루지 않는** 메서드
   
   * **언제 사용**하는가?
     
     * 속성을 다루지 않고 단지 **기능(행동)만**을 하는 메서드를 정의할 때
   
   * 인스턴스 변수, 클래스 변수 아무것도 사용하지 않을 경우 사용
     
     * 즉, **객체 상태**나 **클래스 상태**를 **수정할 수 없음**
   
   * **@staticmethod** 데코레이터를 사용하여 정의
   
   * **일반 함수처럼** 동작하지만, **클래스의 이름공간에 귀속**됨
     
     * 주로 **해당 클래스로 한정**하는 용도로 사용
   
   ```python
   class Person:
       count = 0
       def __init__(self, name):
           self.name = name
           Person.count += 1
   
       @staticmethod
       def check_rich(money): # cls, self사용X
           return money > 10000
   
   person1 = Person('아이유')
   person2 = Person('이찬혁')
   print(Person.check_rich(100000)) # 클래스로 접근가능
   print(person1.check_rich(100000)) # 인스턴스로 접근가능
   ```

10. **인스턴스와 클래스 간의 이름 공간(namespace)**
    
    * 클래스 정의 -> 클래스와 해당하는 이름 공간 생성
    
    * 인스턴스 만들면 -> 인스턴스 객체 생성되고 이름 공간 생성
    
    * **인스턴스**에서 특정 속성 접근 -> **인스턴스-클래스 순 탐색**

11. **메서드 정리**
    
    * **인스턴스 메서드**: 호출한 인스턴스를 의미하는 **self** 매개 변수를 통해 인스턴스 조작
    
    * **클래스 메서드**: 클래스를 의미하는 **cls** 매개 변수를 통해 클래스를 조작
    
    * **스태틱 메서드**: 클래스 변수나 인스턴스 변수를 사용하지 않는 경우에 사용
      
      * **객체 상태**나 **클래스 상태**를 **수정할 수 없음.**
    
    * **클래스 자체**에서 각 메서드를 호출하는 경우: **인스턴스 메서드는 호출X**
    
    * **인스턴스**는 **클래스 메서드**와 **스태틱 메서드** **모두 접근** 가능
      
      * 인스턴스에서 클래스 메서드와 스태틱 메서드는 호출X (가능하다 != 사용한다)

# 2. 객체지향의 핵심 개념

----

1. **추상화**(변수, 함수, 클래스)
   
   * 현실 세계를 프로그램 설계에 반영
     
     * 복잡한 것은 숨기고, 필요한 것만 들어내기
   
   * 세부적인 내용은 감추고 필수적인 부분만 표현하는 것
   
   * 여러 클래스가 공통적으로 사용할 속성 및 메서드를 추출하여 기본 클래스로 작성하여 활용

2. **상속**
   
   * 상속이란: **두 클래스** 사이 **부모 - 자식** 관계를 정립하는 것
   
   * 클래스는 상속이 가능함
     
     * 모든 파이썬 클래스는 object를 상속 받음
   
   * 하위 클래스는 **상위 클래스**에 정의된 속성, 행동, 관계 및 제약 조건을 **모두 상속받음**
   
   * 부모클래스의 속성, 메서드가 자식 클래스에 상속됨 -> **코드 재사용성**이 높아짐
   
   * 상속 관련 **함수와 메서드**
     
     * **isinstance(object, classinfo)**: classinfo의 **instance**거나 **subclass**인 경우 **True**
     
     * **issubclass(class, classinfo)**: classinfo의 **subclass**면 **True**
       
       * classinfo는 클래스 객체의 튜플일 수 있으며, classinfo의 모든 항목 검사
       
       ```python
       print(issubclass(bool, int)) # True
       print(issubclass(float, int)) # False
       ```
     
     * **super()**: 자식클래스에서 **부모클래스를 사용**하고 싶은 경우
       
       ```python
       class Person:
           def __init__(self, name, age, number, email):
               self.name = name
               self.age = age
               self.number = number
               self.email = email 
       
           def greeting(self):
               print(f'안녕, {self.name}')
       
       class Student(Person):
           def __init__(self, name, age, number, email, student_id):
               super().__init__(name, age, number, email)
               self.student_id = student_id
       ```
     
     * **mro 메서드(Method Resolution Order)**
       
       * 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인
       
       * 기존의 인스턴스 -> 클래스 순으로 이름 공간을 탐색하는 과정에서 상속 관계에 있으면 **인스턴스 -> 자식 클래스 -> 부모 클래스**로 확장
       
       ```python
       ClassName.__mro__
       
       # 또는
       ClassName.mro()
       ```
   
   * **상속 정리**
     
     * 파이썬의 모든 클래스는 object로부터 상속됨
     
     * 부모 클래스의 **모든 요소(속성, 메서드)** 가 상속됨
     
     * **super()** 를 통해 부모 클래스의 요소를 호출할 수 있음
     
     * **메서드 오버라이딩**을 통해 자식 클래스에서 **재정의 가능**함
     
     * 상속관계에서의 **이름 공간**은 **인스턴스-자식클래스-부모클래스** 순으로 탐색
   
   * **다중 상속**
     
     * **두 개 이상**의 클래스를 상속 받는 경우
     
     * 상속받은 **모든 클래스의 요소**를 활용 가능함
     
     * **중복된 속성이나 메서드**가 있는 경우 **상속 순서**에 의해 결정됨

3. **다형성**
   
   * 다형성(Polymorphism)이란?
     
     * 여러 모양을 뜻하는 그리스어
     * 동일한 메서드가 클래스에 따라 다르게 행동할 수 있음을 의미
     * 즉, **서로 다른 클래스**에 속해있는 **객체들**이 **동일한 메시지**에 대해 **다른 방식**으로 **응답**할 수 있음
   
   * **메서드 오버라이딩**
     
     * **상속받은 메서드를 재정의**
       
       * 클래스 상속 시, 부모 클래스에서 정의한 메서드를 자식 클래스에서 변경
       
       * 부모 클래스의 **메서드 이름과 기본 기능은 그대로** 사용하지만, **특정 기능을 바꾸고 싶을 때** 사용
       
       * 상속받은 클래스에서 **같은 이름의 메서드로 덮어씀**
       
       * _____init_____, ______str_____ 의 메서드를 정의하는 것도 메서드 오바라이딩 
       
       * **부모 클래스의 메서드**를 실행시키고 싶은 경우 **super를 활용**
       
       ```python
       class Person:
           def __init__(self, name):
               self.name = name
           def talk(self):
               print(f'{self.name}입니다.')
       
       class Student(Person):
           def talk(self):
               super().talk()
               print(f'저는 학생입니다.')
       
       s1 = Student('이학생')
       s1.talk()
       # 이학생입니다.
       # 저는 학생입니다.
       ```

4. **캡슐화**
   
   * 객체의 일부 **구현 내용**에 대해 외부로부터의 직접적인 **액세스를 차단**
     
     * ex. 주민등록번호
   
   * 파이썬에서 암묵적으로 존재하지만, 언어적으로는 존재하지 않음.
   
   * **접근제어자 종류**
     
     * Public Access Modifier
     
     * Protected Access Modifier
     
     * Private Access Modifier
   
   * **Public Member**
     
     * **언더바 없이** 시작하는 **메서드나 속성**
     
     * 어디서나 호출이 가능, 하위 클래스 **override 허용**
     
     * 일반적으로 작성되는 메서드와 속성의 **대다수를 차지**
   
   * **Protected Member**
     
     * **언더바 1개**로 시작하는 **메서드나 속성**
     
     * **암묵적 규칙**에 의해 **부모 클래스 내부**와 **자식 클래스에서만 호출** 가능
     
     * 하위 클래스 **override 허용**
     
     ```python
     class Person:
         def __init__(self, name, age):
             self.name = name
             self._age = age
     
         def get_age(self):
             return self._age
     
     p1 = Person('김싸피', 30)
     print(p1.get_age())  # 30, _age에 직접 접근도 가능(암묵적)
     ```
   
   * **Private Member**
     
     * **언더바 2개**로 시작하는 **메서드나 속성**
     
     * **본 클래스 내부에서만** 사용이 가능
     
     * 하위클래스 **상속 및 호출 불가능**(**오류**)
     
     * **외부 호출 불가능**(**오류**)
     
     ```python
     class Person:
         def __init__(self, name, age):
             self.name = name
             self.__age = age
     
         def get_age(self):
             return self.__age
     
     p1 = Person('김싸피', 30)
     print(p1.get_age())  # 30
     print(p1.__age)  # 직접 접근 불가능 error
     ```
   
   * **getter 메서드와 setter 메서드**
     
     * 변수에 **접근**할 수 있는 메서드를 별도로 생성
       
       * **getter 메서드**: 변수의 **값을 읽는** 메서드 -> **@property** 데코레이터 사용
       
       * **setter 메서드**: 변수의 **값을 설정**하는 성격의 메서드 -> **@변수.setter** 사용
     
     ```python
     class Person:
     
         def __init__(self, age):
             self._age = age 
     
         @property
         def age(self):
             return self._age
     
         @age.setter
         def age(self, new_age):
             if new_age <= 19:
                 raise ValueError('Too Young For SSAFY')
                 return
     
             self._age = new_age
     
     p1 = Person(20)
     print(p1.age)  # 20._age = new_age
     ```

# 3. 에러와 예외

-----

1. **디버깅**
   
   * **버그란**? 소프트웨어에서 발생하는 문제
   
   * 디버깅의 정의: 잘못된 프로그램을 수정하는 것
     
     * 에러 메시지가 발생하는 경우: 해당하는 위치를 찾아 메시지 해결
     
     * 로직 에러가 발생하는 경우: 명시적인 에러 메시지 없이 예상과 다른 결과
   
   * print 함수 활용: 특정 함수 결과, 반복/조건 결과 등 나눠서 생각
   
   * 개발 환경(text editor, IDE) 등에서 제공하는 기능 활용: breakpoint, 변수 조회 등
   
   * python tutor 활용 (단순 파이썬 코드인 경우)

2. **에러와 예외**
   
   * **문법 에러(Syntax Error)**
     
     * 문법 에러 -> 프로그램 실행 X
     
     * 파일이름, 줄번호, ^문자를 통해 파이썬이 코드를 읽어 나갈 때(parser)문제가 발생한 위치를 표현
     
     * 줄에서 에러가 감지된 가장 앞의 위치를 가리키는 캐럿(caret)기호(^)를 표시
     
     * Invalid syntax: 문법 오류
     
     * assign to literal: 잘못된 할당
     
     * EOL(End of Line)
     
     * EOF(End of File)
   
   * **예외(Exception)**
     
     * 실행 도중 **예상치 못한 상황** -> 프로그램 **실행을 멈춤**
       
       * 문장이나 표현식이 **문법적으로 올바르더라도** 발생하는 에러
     
     * **실행 중에 감지**되는 에러들을 예외라고 부름
     
     * 예외는 **여러 타입(type)** 으로 나타나고, 타입이 메시지의 일부로 출력됨
       
       * NameError, TypeError 등
     
     * 모든 내장 예외는 Exception Class를 상속받아 이뤄짐
     
     * 사용자 정의 예외를 만들어 관리할 수 있음
     
     * **ZeroDivisionError**: 0으로 나누고자 할 때 발생
     
     * **NameError**: namespace 상에 이름이 없는 경우 
     
     * **TypeError**: 타입 불일치, argument 누락/개수 초과/type불일치
     
     * **ValueError**: 타입은 올바르나 **값이 적절하지 않거나 없는** 경우
     
     * **IndexError**: 인덱스가 존재하지 않거나 범위를 벗어나는 경우
     
     * **KeyError**: 해당 키가 존재하지 않는 경우
     
     * **ModulNotFoundError**
     
     * **ImportError**: 모듈은 있으나 존재하지 않는 클래스/함수를 가져오는 경우
     
     * **KeyboardInterrupt**: 임의로 프로그램을 종료하였을 때
     
     * **IndentationError**: Indentation이 적절하지 않는 경우
   
   * 파이썬 내장 예외 (built-in-exceptions)
     
     * 파이썬 내장 예외의 클래스 계층 구조

3. **예외 처리**
   
   * **try문(statement) / except절(clause)** 을 이용하여 예외 처리 할 수 있음
   
   * **try문**
     
     * 오류가 발생할 가능성이 있는 코드를 실행
     
     * 예외 발생X -> except없이 실행 종료
   
   * **except문**
     
     * 예외 발생 -> except절이 실행
     
     * 예외 상황을 처리하는 코드를 받아서 적절한 조치를 취함
   
   * **작성 방법**
     
     ```python
     try:
         try 명령문
     except 예외그룹-1 as 변수-1:
         예외처리 명령문1
     except 예외그룹-2 as 변수-2:
         예외처리 명령문2
     finally:
         finally명령문
     ```
   
   * **에러 메시지 처리 (as)**
     
     * **as 키워드**를 활용하여 원본 에러 메시지를 사용할 수 있음
   
   * 복수의 예외 처리 실습
     
     * 순차적으로 수행됨으로, **가장 작은 범주부터** 예외 처리를 해야함
   
   * **예외 처리 종합**
     
     * **try**: 코드를 실행함
     
     * **except**: try문에서 **예외가 발생 시 실행**함
     
     * **else**: try문에서 **예외가 발생하지 않으면 실행**함
     
     * **finally**: 예외 발생 여부와 관계없이 **항상 실행**
