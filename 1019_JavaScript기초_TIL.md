## 0. 목차

---

1. JavaScript 시작하기
2. JavaScript 기초 문법
3. 함수
4. Array와 Object

## 1. JavaScript 시작하기

---

1. JavaScript를 배워야 하는 이유
   
   * **Web 기술의 기반**이 되는 언어
     
     * HTML 문서의 콘텐츠를 **동적으로 변경**할 수 있는 언어
     * Web이라는 공간에서 채팅, 게임 등 다양한 동작을 할 수 있게 된 기반
   
   * **다양한 분야로 확장**이 가능한 언어
     
     * 단순히 Web 조작을 넘어서 서버 프로그래밍, 모바일 서비스, 컴퓨터 응용프로그래밍, 블록체인, 게임 개발 등 다양한 분야에서 활용이 가능한 언어가 됨
   
   * 2022년 현재, 가장 인기있는 언어

2. JavaScript의 **역사**
   
   * Web을 조작하기 위한 언어인 만큼 **Web Browser와도 깊은 연관 관계**가 있음
   
   * **웹 브라우저의 역할**
     
     * URL을 통해 Web(WWW)을 탐색
     * HTML/CSS/JavaScript를 **이해한 뒤 해석** -> 사용자에게 하나의 화면으로 보여줌
     * 웹 서비스 이용시 클라이언트의 역할을 함
     * 웹 페이지 코드 이해, 보여주는 역할 -> 웹 브라우저
   
   * 웹 브라우저와 스크립트 언어
     
     * 웹 브라우저에 탑재해서 웹 페이지를 동적으로 바꿔줄 Script 언어 개발 필요
     
     * Script 언어: 소스 코드를 기계어로 바꿔주는 컴파일러 없이 바로 실행 가능한 언어
       
       * 속도가 느리다는 단점이 있음
   
   * 정리

3. JavaScript **실행환경 구성**
   
   * Web Browser로 실행하기
     
     * 개발자도구
     
     * .js 확장자를 가진 파일에 JavaScript를 작성하고, 해당 파일을 HTML에 포함 가능
     
     * 웹 브라우저의 console에서 바로 JavaScript를 입력해도 됨(엔진이 있으니까)
     
     * 특별하게 웹 브라우저에서 바로 실행할 수 있는 JavaScript 문법들을 **Vanilla JavaScript**라고 부름
       
       * 순수한 JavaScript라는 의미
   
   * Node.js로 실행하기
     
     * 웹 브라우저를 이용하지 않고 JavaScript를 실행할 수 있음(엔진이 있으니까)
     * Node.js 설치 확인
       * \$ node -v
       * \$ npm -v

## 2. JavaScript 기초 문법

---

1. 코드 작성법
   
   * **세미콜론(semicolon)**
     
     * 자바스크립트는 세미콜론을 선택적으로 사용 가능
     
     * 세미콜론이 없으면 -> ASI에 의해 자동으로 세미콜론 삽입됨
       
       * **ASI**(Automatic Semicolon Insertion, 자동 세미콜론 삽입 규칙)
   
   * 들여쓰기와 코드 블럭
     
     * **2칸 들여쓰기** 사용
     
     * **블럭(block)** 은 if, for, 함수에서 **중괄호 {}** 내부를 말함
       
       * 중괄호 {}를 사용해 코드 블럭을 구분
   
   * 코드 스타일 가이드
     
     * 수업에서는 Airbnb Style Guide를 기반으로 사용
   
   * [참고] 다양한 JavaScript 코드 스타일 가이드
   
   * **주석**
     
     * 한 줄 주석(//)과 여러 줄(/**/) 주석

2. **변수와 식별자**
   
   * **식별자 정의와 특징**
     
     * **식별자(identifier)**: 변수를 구분할 수 있는 변수명
     
     * 반드시 **문자, 달러(\$) 또는 밑줄(\_)** 로 시작
     
     * **대소문자 구분**, 클래스명 외에는 모두 **소문자로 시작**
     
     * **예약어 사용X**: for, if, function 등
     
     * **카멜 케이스(camelCase, loser-camel-case)**: 변수, 객체, 함수에 사용
     
     * **파스칼 케이스(PascalCase, upper-camel-case)**: 클래스, 생성자에 사용
     
     * **대문자 스네이크 케이스(SNAKE_CASE)**
       
       * 상수(constants)에 사용
       * 상수: 개발자의 의도와 상관없이 변경될 가능성 없는 값
   
   * **변수 선언 키워드**
     
     * **let** : 블록 스코프 **지역 변수**를 선언 (추가로 동시에 값을 초기화)
     * **const** : 블록 스코프 **읽기 전용 상수**를 선언 (추가로 동시에 값을 초기화)
     * **var** : 변수를 선언 (추가로 동시에 값을 초기화)
   
   * **[참고] 선언, 할당, 초기화**
     
     * **선언 (Declaration)** : **변수를 생성**하는 행위 또는 시점
     * **할당 (Assignment)** : 선언된 변수에 **값을 저장**하는 행위 또는 시점
     * **초기화 (Initialization)** : 선언된 변수에 **처음으로 값을 저장**하는 행위 또는 시점
   
   * **[참고] 블록 스코프 (block scope)**
     
     * if, for, 함수 등의 **중괄호({}) 내부**를 가리킴
     * 블록 스코프를 가지는 **변수** -> 블록 **바깥에서 접근 X**
   
   * **변수 선언 키워드 - let**
     
     * let : **재할당 가능** & **재선언 불가능**
     * **블록 스코프**를 갖는 지역 변수를 선언, 선언과 동시에 원하는 값으로 초기화 가능
   
   * **변수 선언 키워드 - const**
     
     * const : **재할당 불가능** & **재선언 불가능**
     * 선언 시 **반드시 초기값 설정** , 이후 값 변경 불가능
     * let과 동일하게 **블록 스코프**를 가짐
   
   * **변수 선언 키워드 - var**
     
     * var : **재할당 가능** & **재선언 가능**
     
     * ES6 이전에 변수를 선언할 때 사용되던 키워드
     
     * "호이스팅"되는 특성 -> 예기치 못한 문제 발생 가능
       
       * ES6 이후부터는 var 대신 const와 let을 사용하는 것을 권장
     
     * **함수 스코프(function scope)** 를 가짐
     
     * 변수 선언 시 var, const, let 키워드 중 하나를 사용하지 않으면 -> **자동으로 var로 선언**
   
   * **[참고] 함수 스코프(function scope)**
     
     * 함수의 **중괄호 내부**
     * 함수 스코프를 가지는 **변수** -> 함수 **바깥에서 접근 불가능**
   
   * **[참고] 호이스팅(hoisting)**
     
     * 변수를 **선언 이전에 참조**할 수 있는 현상
     * **var**로 선언된 변수 -> 선언 이전에 참조할 수 있다.
     * 변수 선언 이전의 위치에서 접근 시 undefined를 반환
     * 실제 실행시에 **코드의 최상단으로** 끌어 올려지게 됨, var로 선언된 변수는 선언시에 undefined로 값이 초기화되는 과정이 동시에 일어남
     * let, const -> 호이스팅이 일어나면 에러 발생
   
   * **변수 선언 키워드 정리**
     
     | 키워드       | 재선언 | 재할당 | 스코프    | 비고       |
     | --------- | --- | --- | ------ | -------- |
     | **let**   | X   | O   | 블록 스코프 | ES6부터 도입 |
     | **const** | X   | X   | 블록 스코프 | ES6부터 도입 |
     | **var**   | O   | O   | 함수 스코프 | 사용X      |

3. **데이터 타입**
   
   * 데이터 타입
     
     * JavaScript의 모든 값은 특정한 데이터 타입을 가짐
     * 크게 **원시 타입(Primitive type)** 과 **참조 타입(Reference type)** 으로 분류됨
     * **Primitive type**: **Number, String, Boolean, undefined, null, Symbol**
     * **Reference type**: Objects - Array, Function, ...
   
   * **Number**
     
     * 정수 또는 실수형 숫자를 표현하는 자료형
     
     * **NaN** : Not-A-Number
       
       * Number.isNaN()의 경우 주어진 값의 유형이 Number이고 값이 NaN이면 true, 아니면 false를 반환
     
     * **NaN을 반환하는 경우**
       
       * 숫자로서 읽을 수 없음
       * 결과가 허수인 수학 계산식
       * 피연산자가 NaN (7 \*\* NaN )
       * 정의할 수 없는 계산식 (0 \* Infinity)
       * 문자열을 포함하면서 덧셈이 아닌 계산식
   
   * **String**
     
     * 문자열을 표현하는 자료형
     * **작은 따옴표 또는 큰 따옴표** 모두 가능
     * 곱셈, 나눗셈, 뺄셈은 안되지만 **덧셈을 통해 문자열 붙일 수 있음**
     * **Quote를 사용**하면 **선언 시 줄 바꿈이 안됨**
     * 대신 **escape sequence를 사용 가능 -> \n을 사용**해야 함
     * **Template Literal**을 사용하면 **줄 바꿈**이 되며, 문자열 사이에 변수도 삽업 가능
       * (단, escape sequence를 사용할 수 없다)
   
   * **Template Literals (템플릿 리터럴)**
     
     * 내장된 표현식을 허용하는 문자열 작성 방식
     * ES6+부터 지원
     * **Backtick(``)** 을 이용, 여러 줄에 걸쳐 문자열을 정의할 수도 있고 JavaScript의 변수를 문자열 안에 바로 연결할 수 있는 이점이 생김
     * 표현식을 넣을 수 있음 -> \$와 중괄호( \$ {expression} ) 로 표기
   
   * **Empty Value**
     
     * 값이 존재하지 않음 표현하는 값 -> **null**, **undefined**가 존재
     * 두개의 키워드가 존재하는 이ㄴ유 -> 단순한 설계 실수
   
   * **null**
     
     * null값을 나타내는 키워드
     * 변수의 값이 없음을 **의도적으로 표현**할 때 사용
   
   * **undefined**
     
     * 값이 정의되어 있지 않음을 표현하는 값
     * 변수 선언 이후 직접 값을 할당하지 않으면 **자동으로 할당**됨
   
   * **null과 undefined**
     
     * 가장 대표적인 차이점 -> **typeof** 연산자를 통해 타입을 확인했을 때 나타남
     * **null**이 원시 타입임에도 불구하고 **object**로 출력됨 -> 설계 당시의 버그
   
   * **Boolean**
     
     * true와 false
     
     * 참과 거짓을 표현하는 값
     
     * 조건문 또는 반복문에서 유용하게 사용
       
       * 조건문 또는 반복문에서 boolean이 아닌 데이터 타입 -> **자동 형변환 규칙**에 따라 true 또는 false로 변환됨
   
   * ToBoolean Conversions(자동 형변환)
     
     | 데이터 타입    | false      | true    |
     | --------- | ---------- | ------- |
     | undefined | 항상 false   | X       |
     | null      | 항상 false   | X       |
     | Number    | 0, -0, NaN | 나머지     |
     | String    | 빈 문자열      | 나머지     |
     | Object    | X          | 항상 true |

4. **연산자**
   
   * **할당 연산자**
     
     * **Increment** 및 **Decrement** 연산자
       
       * ++
       * --
       * += 또는 -=와 같이 더 분명한 표현으로 적을 것을 권장
     
     * 오른쪽에 있는 피연산자의 평가 결과를 왼쪽 피연산자에 할당하는 연산자
     
     * 다양한 연산에 대한 단축 연산자 지원
   
   * **비교 연산자**
     
     * 피연산자들(숫자, 문자, Boolean 등)을 비교하고 결과값을 boolean으로 반환하는 연산자
     * 문자열 -> 유니코드 값 사용 표준 사전 순서 기반 비교
       * 알파벳끼리 비교시
         * 알파벳 순서상 후순위가 더 크다
         * 소문자 > 대문자
   
   * **동등 연산자 (==)**
     
     * 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
     * 비교할 때 **암묵적 타입 변환**을 통해 타입을 일치시킨 후 같은 값인지 비교
     * **두 피연산자가 모두 객체**일 경우 메모리의 **같은 객체를 바라보는지** 판별
     * 예상치 못한 결과가 발생할 수 있으므로 특별한 경우를 제외하고 사용X
   
   * **일치 연산자(===)**
     
     * 두 피연산자의 **값과 타입**이 모두 같은 경우 true를 반환
     
     * **같은 객체**를 가리키거나, **같은 타입이면서 같은 값인지**를 비교
     
     * 엄격한 비교가 이뤄지며, **암묵적 타입 변환 발생X**
       
       * 엄격한 비교 : 두 비교 대상의 타입과 값 모두 같은지 비교
   
   * **논리 연산자**
     
     * 세가지 논리 연산자
       
       * and 연산 : '**&&**'
       * or 연산: '**||**'
       * not 연산 '**!**'
     
     * 단축 평가 지원
   
   * **삼항 연산자 (Ternary Operator)**
     
     * 3개의 피연산자를 사용하여 조건에 따라 값을 반환하는 연산자
     * **조건식 ? 값1 : 값2**
     * 가장 앞의 조건식이 참이면 :(콜론) 앞의 값, 반대일 경우 뒤의 값 반환
     * 삼항 연산자의 결과 값이기 때문에 **변수에 할당 가능**

5. **조건문**
   
   * 조건문의 종류와 특징
     
     * if statement
       
       * 조건 표현식의 결과값을 boolean 타입으로 변환 후 참/거짓을 판단
     
     * switch statement
       
       * 조건 표현식의 결과값이 어느 값(case)에 해당하는지 판별
       * 주로 특정 변수의 값에 따라 조건을 분기할 때 활용
         * 조건이 많아질 경우 if문보다 가독성이 나을 수 있음
   
   * **if statement**
     
     * **if, else if, else**
       
       * **조건**은 **소괄호(condition)** 안에 작성
       * 실행할 코드는 **중괄호 {}** 안에 작성
       * 블록 스코프 생성
   
   * **switch statement**
     
     * 표현식의 결과값을 이용한 조건문
     * 표현식의 결과값과 case문의 오른쪽 값을 비교
     * break 및 default문은 [선택적]으로 사용 가능
     * break문이 없는 경우 -> break문을 만나거나 default문을 실행할 때까지 다음 조건문 실행
     * 블록 스코프 생성
   
   * if / switch
     
     * 조건이 많은 경우 -> switch문을 통해 가독성 향상 기대할 수 있음
     * 일반적으로 중첩 else if문은 유지보수하기 힘들다는 문제도 있음

6. **반복문**
   
   * 반복문 종류
     
     * while
     * for
     * for...in
     * for...of
   
   * **while** : 조건문이 참이기만하면 문장을 계속해서 수행
   
   * **for** : 특정한 조건이 거짓으로 판별될 때까지 반복
     
     ```javascript
     for ([초기문]; [조건문]; [증감문]){
         // do something
     }
     ```
   
   * **for...in**
     
     * 객체(object)의 **속성을 순회**할 때 사용
     * 배열도 순회 가능하지만 **인덱스 순으로 순회한다는 보장이 없**으므로 권장X
   
   * **for...of**
     
     * **반복 가능한 객체**를 순회할 때 사용
     * 반복 가능한 객체의 종류: **Array, Set, String 등**
   
   * **for...in과 for...of 차이**
     
     * **for...in** : 속성 **이름**을 통해 반복
     * **for...of** : 속성 **값**을 통해 반복
     
     ```javascript
     const arr = [3, 5, 7]
     for (const i in arr){
         console.log(i) // 0 1 2
     }
     for (const i of arr){
         console.log(i) // 3 5 7
     }
     ```
   
   * **[참고] for...in, for...of와 const**
     
     * for문
       * 재할당이 아니라, **매 반복 시 해당 변수를 새로 정의**하여 사용 -> **에러X**
     * for...in, for...of
       * 일반적인 for문의 경우에는 **최초 정의한 i를 재할당 const 사용 -> 에러**
   
   * 조건문과 반복문 정리
     
     | 키워드      | 종류  | 연관 키워드               | 스코프    |
     | -------- | --- | -------------------- | ------ |
     | if       | 조건문 | -                    | 블록 스코프 |
     | switch   | 조건문 | case, break, default | 블록 스코프 |
     | while    | 반복문 | break, continue      | 블록 스코프 |
     | for      | 반복문 | break, continue      | 블록 스코프 |
     | for...in | 반복문 | 객체 순회                | 블록 스코프 |
     | for...of | 반복문 | Iterable 순회          | 블록 스코프 |

## 3. 함수

---

0. 개요
   
   * 참조 타입 중 하나, **function 타입**에 속함
   
   * JavaScript에서 함수를 정의하는 **2가지 방법**
     
     * 함수 선언식 (function declaration)
     * 함수 표현식 (function expression)

1. **함수의 정의**
   
   * **함수 선언식 (Function delaration)**
     
     * 일반적인 프로그래밍 언어의 함수 정의 방식
     
     ```javascript
     function function_name() {
         // do something
     }
     ```
   
   * **함수 표현식 (Function expression)**
     
     * 표현식 내에서 함수를 정의하는 방식
     * **함수의 이름을 생략**한 익명 함수로 정의 가능
     * **함수 이름을 명시**하는 것도 가능
     * 다만 이 경우 함수 이름은 호출에 사용되지 못하고 -> **디버깅 용도**로 사용됨
     
     ```javascript
     변수키워드 함수명 = function() {
         // do something
     }
     ```
   
   * **기본 인자 (Default arguments)**
     
     * 인자 작성 시 '=' 문자 뒤 기본 인자 선언 가능
   
   * **매개변수와 인자의 개수 불일치 허용**
     
     * 매개변수 < 인자의 개수
     * 매개변수 > 인자의 개수
       * 부족한 인자 -> undefined
   
   * **Spread syntax(...)**
     
     * 전개 구문
     
     * 전개 구문을 사용하면 배열이나 문자열과 같이 반복 가능한 객체를 **배열의 경우는 요소, 함수의 경우는 인자로 확장** 가능
       
       * **배열**과의 사용
         
         ```javascript
         let parts = ['shoulders', 'knees']
         let lyrics = ['head', ...parts, 'and', 'toes']
         // ['head', 'shoulders', 'knees', 'and', 'toes']
         ```
       
       * **함수**와의 사용 (**Rest parameters**)
         
         * The rest parameter syntax를 사용하여 **정해지지 않은 수의 매개변수**를 배열로 받을 수 있음
         
         ```javascript
         function func_name(a, b, ...theArgs){
             //
         }
         ```

2. **선언식과 표현식**
   
   * 호이스팅 - 선언식
     
     * **함수 선언식**으로 정의한 함수는 -> var로 정의한 변수처럼 **호이스팅**이 발생
     * 함수 호출 이후에 선언해도 동작
     * **함수 표현식**으로 선언한 함수 -> 함수 **정의 전에 호출 시 에러**
     * 함수 표현식으로 정의된 함수 -> 변수로 평가되어 **변수의 scope 규칙**을 따름
   
   * 선언식과 표현식 정리
     
     |         | 선언식 (declaration)               | 표현식 (expression)                |
     | ------- | ------------------------------- | ------------------------------- |
     | **공통점** | 데이터 타입, 함수 구성 요소 (이름, 매개변수, 바디) | 데이터 타입, 함수 구성 요소 (이름, 매개변수, 바디) |
     | **차이점** | 익명 함수 불가능<br>호이스팅 있음            | 익명 함수 가능<br>호이스팅 없음             |
     | 비고      |                                 | Airbnb Style Guide 권장 방식        |

3. **Arrow Function**
   
   * **화살표 함수 (Arrow Function)**
     
     * 함수를 비교적 간결하게 정의할 수 있는 문법
     
     * function 키워드와 중괄호를 이용한 **구문을 짧게** 사용하기 위해 탄생
       
       * **function** 키워드 **생략**가능
       * 함수의 **매개변수가 하나** -> **'()' 생략** 가능
       * **함수**의 내용이 **한 줄** -> **'{}'와 'return' 도 생략** 가능
     
     * 화살표 함수는 항상 익명 함수 --> **함수 표현식**에서만 사용가능
     
     * 화살표 함수 (Arrow Function) 예시
       
       ```javascript
       const arrow1 = function (name) {
           return `hello, ${name}`
       }
       // 1. function 키워드 삭제
       const arrow2 = (name) => {return `hello, ${name}`}
       // 2. 인자가 1개일 경우에만 () 생략 가능
       const arrow3 = name => {return `hello, ${name}`}
       // 3. 함수 바디가 return을 포함한 표현식 1개일 경우에 {} & return 삭
       const arrow4 = name => `hello, ${name}`
       ```
     
     * 응용
       
       * 인자가 없다면 () 혹은 \_ 로 표시
       
       * **object를 return**한다면
         
         * return을 명시적으로 적어준다.
         * **return 적지 않으려면 ()** 를 붙여야 함
   
   * **즉시 실행 함수(IIFE, Immediately Invoked Function Expression)**
     
     * 선언과 동시에 실행되는 함수
     * **함수의 선언 끝에 '()'** 를 추가하여 선언되자마자 실행하는 형태
     * '()'에 **값을 넣어 인자로** 넘겨줄 수 있음
     * 즉시 실행 함수는 **선언과 동시에 실행** -> 같은 함수를 **다시 호출X**
     * 초기화 부분에 많이 사용
     * **일회성 함수**이므로, **익명함수로 사용하는 것이 일반적**
     
     ```javascript
     (function(num) {return num ** 3})(2) // 8
     (num => num ** 3)(2) // 8
     ```

## 4. Array와 Object

---

0. 개요
   
   * 참조 타입, 해당하는 타입은 Array, Object이며 객체라고도 말함
   * 객체 -> 속성들의 모음

1. **배열 (Array)**
   
   * **키와 속성**들을 담고 있는 참조 타입의 객체
   
   * **순서 보장**
   
   * **대괄호([])를 이용하여 생성**, 0을 포함한 **양의 정수 인덱스**로 특정 값에 접근 가능
   
   * 배열의 길이는 **array.length** 형태로 접근 가능
     
     * 마지막 원소는 array.length-1로 접근

2. **배열 메서드 기초**
   
   * 배열 메서드 기초
     
     | 메서드                 | 설명                                   | 비고                  |
     | ------------------- | ------------------------------------ | ------------------- |
     | **reverse**         | **원본 배열**의 요소들의 순서를 반대로 정렬           |                     |
     | **push & pop**      | 배열의 **가장 뒤**에 요소를 **추가 또는 제거**       |                     |
     | **unshift & shift** | 배열의 **가장 앞**에 요소를 **추가 또는 제거**       |                     |
     | **includes**        | 배열에 **특정 값**이 존재하는지 판별 후 **참/거짓** 반환 |                     |
     | **indexOf**         | 배열에 **특정 값**이 존재하는지 판별 후 **인덱스 반환**  | 요소가 **없을 경우 -1** 반환 |
     | **join**            | 배열의 **모든 요소를 구분자를 이용하여 연결**          | 구분자 **생략 시 쉼표** 기준  |
   
   ```javascript
   const numbers = [1, 2, 3, 4, 5]
   numbers.reverse()
   console.log(numbers) // [5, 4, 3, 2, 1]
   const numbers = [1, 2, 3, 4, 5]
   numbers.push(100)
   console.log(numbers) // [1, 2, 3, 4, 5, 100]
   numbers.pop()
   console.log(numbers) // [1, 2, 3, 4, 5]
   console.log(numbers.includes(1)) // true
   console.log(numbers.includes(100)) // false
   console.log(numbers.indexof(3)) // 2
   console.log(numbers.indexof(100)) // -1
   console.log(numbers.join()) // 1, 2, 3, 4, 5
   ```

3. **배열 메서드 심화**
   
   * Array Helper Methods
     
     * 배열을 순회하며 특정 로직을 수행하는 메서드
     
     * 메서드 호출 시 인자로 **callback 함수**를 받는 것이 특징
       
       * **callback 함수**: 어떤 **함수의 내부에서 실행될 목적**으로 인자로 넘겨받는 함수
     
     | 메서드         | 설명                                             | 비고    |
     | ----------- | ---------------------------------------------- | ----- |
     | **forEach** | 배열의 각 요소에 대해 콜백 함수를 한번씩 실행                     | 반환 값X |
     | **map**     | **콜백 함수의 반환 값**을 요소로 하는 **새로운 배열 반환**          |       |
     | **filter**  | **콜백 함수의 반환 값**이 **참인 요소들**만 모아서 **새로운 배열 반환** |       |
     | **reduce**  | **콜백 함수의 반환 값**들을 **하나의 값(acc)에 누적** 후 반환      |       |
     | **find**    | **콜백 함수의 반환 값**이 **참이면 해당 요소를 반환**             |       |
     | **some**    | 배열의 요소 중**하나라도 판별 함수를 통과**하면 **참**을 반환         |       |
     | **every**   | 배열의**모든 요소가 판별 함수를 통과**하면 **참**을 반환            |       |
   
   * **Array Helper Methods - forEach**
     
     * array.forEach(callback(element[, index[,array]]))
     
     * 인자로 주어지는 함수(콜백 함수)를 배열의 각 요소에 대해 한번씩 실행
       
       * 콜백 함수는 3가지 매개변수로 구성
         
         * element: 배열의 요소
         * index: 배열 요소의 인덱스
         * array: 배열 자체
     
     * 반환 값(return) 없음
     
     ```javascript
     const colors = ['red', 'blue', 'green']
     colors.forEach((color) => {
         return console.log(color) 
     })
     ```
   
   * **Array Helper Methods - map**
     
     * array.map(callback(element[, index[,array]]))
     
     * 배열의 각 요소에 대해 콜백 함수를 한번씩 실행
     
     * 콜백 함수의 **반환값을 요소로 하는 새로운 배열 반환**
     
     * 기존 배열 전체를 다른 형태로 바꿀 때 유용
       
       * **forEach + return**
     
     ```javascript
     const numbers = [1, 2, 3]
     const doubleNumbers = numbers.map((number) => {
         return number * 2
     })
     console.log(doubleNumbers) // [2, 4, 6]
     ```
   
   * **Array Helper Methods - filter**
     
     * array.filter(callback(element[, index[,array]]))
     * 배열의 각 요소에 대해 콜백 함수를 한번씩 실행
     * 콜백 함수의 반환값이 **참인 요소들만 모아서 새로운 배열 반환**
     * 기존 배열의 요소들을 필터링할 때 유용
     
     ```javascript
     const products = [
         {name: 'cucumbre', type: 'vegetable'},
         {name: 'banana', type: 'fruit'},
         {name: 'carrot', type: 'vegetable'},
         {name: 'apple', type: 'fruit'},
     ]
     const fruits = products.filter((product) => {
         return product.type === 'fruit'
     })
     ```
   
   * **Array Helper Methods - reduce**
     
     * array.reduce(callback(acc, element, [index[, array]]) [, initialValue])
     
     * 인자로 주어지는 함수(콜백 함수)를 배열의 각 요소에 대해 한번씩 실행해서, 하나의 결과 값을 반환
     
     * 즉, 배열을 하나의 값으로 계산하는 동작이 필요할 때 사용 (총합, 평균 등)
     
     * map, filter등 여러 배열 메서드 동작
     
     * 주요 매개변수
       
       * **acc** : 이전 callback 함수의 반환 값이 **누적**되는 변수
       
       * **initialValue (optional)**
         
         * 최초 callback 함수 호출 시 acc에 할당되는 값, default값은 배열의 첫번째 값
     
     * reduce의 첫번째 매개변수인 콜백함수의 첫번째 매개변수(acc)는 누적된 값(전 단계까지의 결과)
     
     * reduce의 두번째 매개변수인 initialValue는 누적될 값의 초기값, 지정하지 않을 시 첫번째 요소의 값이 됨
     
     * **빈 배열의 경우 initialValue를 제공하지 않으면 에러 발생**
     
     ```javascript
     const tests = [90, 90, 80, 77]
     const sum = tests.reduce((total, x) => total + x, 0)
     const avg = tests.reduce((total, x) => total + x, 0) / tests.length
     ```
   
   * **Array Helper Methods - find**
     
     * array.find(callback(element[, index[, array]]))
     * 배열의 각 요소에 대해 콜백 함수를 한번씩 실행
     * 콜백 함수의 반환 값이 **참이면, 조건을 만족하는 첫번째 요소 반환**
     * 찾는 값이 배열에 **없으면 -> undefined** 반환
     
     ```javascript
     const avengers = [
         {name: 'Tony Stark', age: 45},
         {name: 'Steve Rogers', age: 32},
         {name: 'Thor', age: 40},
     ]
     const avenger = avengers.find((avenger) => {
         return avenger.name === 'Tony Stark'
     })
     ```
   
   * **Array Helper Methods - some**
     
     * array.some(callback(element[, index[, array]]))
     * 배열의 **요소 중 하나라도** 주어진 판별 함수를 통과하면 참을 반환
     * 모든 요소가 통과하지 못하면 거짓 반환
     * **빈 배열은 항상 false 반환**
     
     ```javascript
     const arr = [1, 2, 3, 4, 5]
     const result = arr.some((elem) => {
         return elem % 2 === 0
     })
     ```
   
   * **Array Helper Methods - every**
     
     * array.every(callback(element[, index[, array]]))
     * 배열의 **모든 요소**가 주어진 판별 함수를 통과하면 참을 반환
     * 하나의 요소라도 통과X -> 거짓 반환
     * **빈 배열 -> 항상 true 반환**
     
     ```javascript
     const arr = [1, 2, 3, 4, 5]
     const result = arr.every((elem) => {
         return elem % 2 === 0
     })
     ```
   
   * **배열 순회 비교**
     
     | 방식       | 특징                                                                             | 비고                          |
     | -------- | ------------------------------------------------------------------------------ | --------------------------- |
     | for loop | - 모든 브라우저 환경에서 지원<br>- 인덱스를 활용하여 배열의 요소에 접근<br>- break, continue 사용 가능         |                             |
     | for...of | - 일부 오래된 브라우저 환경에서 지원X<br>- 인덱스 없이 배열의 요소에 바로 접근 가능<br>- break, continue 사용 가능 |                             |
     | forEach  | - 대부분의 브라우저 환경에서 지원\<br> break, continue 사용 불가능                                | Airbnb Style Guide<br>권장 방식 |

4. **객체 (Object)**
   
   * 개요
     
     * 객체는 속성(property)의 집합이며, 중괄호 내부에 **key와 value의 쌍**으로 표현
     
     * **key**는 **문자열 타입만** 가능
       
       * key 이름에 띄어쓰기 등의 구분자가 있으면 따옴표로 묶어서 표현
     
     * **value**는 **모든 타입(함수포함) 가능**
     
     * 객체 요소 접근은 **점(.) 또는 대괄호([])** 로 가능
       
       * key 이름에 띄어쓰기 같은 **구분자**가 있으면 **대괄호 접근만** 가능
   
   * **객체 관련 문법**
     
     * ES6 문법 익히기
       
       * **속성명 축약**
         
         * 객체를 정의할 때 key와 할당하는 변수의 이름이 같으면 축약 가능
         
         ```javascript
         const books = ['Learning JavaScript', 'Learning Python']
         const magazines = ['Vogue', 'Science']
         const bookShop = {
             books,
             magazines
         }
         // books: books,
         // magazines: magazines
         ```
       
       * **메서드명 축약**
         
         * 메서드 선언 시 **function 키워드 생략** 가능
         
         ```javascript
         const obj = {
             greeting() {
             console.log('Hi!')
             }
         }
         ```
       
       * **계산된 속성명 사용하기(computed property name)**
         
         * 객체를 정의할 때 **key**의 이름을 **표현식을 이용하여 동적으로 생성** 가능
         
         ```javascript
         const key = 'country'
         const value = ['한국', '미국', '일본', '중국']
         const myObj = {
             [key]: value,
         }
         console.log(myObj)
         // {country: ['한국', '미국', '일본', '중국']}
         ```
       
       * **구조 분해 할당(destructing assignment)**
         
         * 배열 또는 **객체를 분해하여 속성을 변수에 쉽게 할당**할 수 있는 문법
         
         ```javascript
         const userInformation = {
             name: 'ssafy kim',
             userId: 'ssafyStudent1234',
             phoneNumber: '010-1234-1234',
             email: 'ssafy@ssafy.com'
         }
         const {name, userId} = userInformation
         ```
       
       * **객체 전개 구문(Spread Operator)**
         
         * 배열과 마찬가지로 전개구문을 사용해 **객체 내부에서 객체 전개** 가능
         * **얕은 복사**에 활용 가능
         
         ```javascript
         const obj = {b:2, c:3, d:4}
         const newObj = {a:1, ...obj, e:5}
         console.log(newObj) // {a:1, b:2, c:3, d:4, e:5}
         ```
     
     * **JSON**
       
       * JavaScript Object Notation
       * Key-Value 형태로 이루어진 자료 표기법
       * JavaScript의 Object와 유사한 구조를 가지고 있지만, **Object는 그 자체로 타입**이고, **JSON은 형식이 있는 "문자열"**
       * JSON을 Object로 사용하기 위해서는 변환 작업 필요
     
     * **JSON 변환**
       
       ```javascript
       const jsObject = {
           coffee: 'Americano',
           iceCream: 'Cookie and cream'
       }
       // Object -> JSON
       const objToJson = JSON.stringify(jsObject)
       // JSON -> Object
       const jsonToObj = JSON.parse(objToJson)
       ```
     
     * **[참고] 배열은 객체다**
       
       * 배열: 키와 속성들을 담고 있는 참조 타입의 객체
       * 배열은 인덱스를 키로 가지며 length 프로퍼티를 갖는 특수한 객체
