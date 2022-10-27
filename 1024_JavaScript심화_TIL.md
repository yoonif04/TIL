## 0. 목차

----

1. DOM

2. Event

3. this

## 1. DOM

----

0. 개요
   
   * 브라우저에서의 JavaScript
     
     * 웹 페이지에서 복잡한 기능을 구현하는 스크립트 언어
     
     * 정적인 정보만 보여주는 것 x 주기적으로 갱신되거나, 사용자와 상호 작용이 가능하거나, 애니메이션이 적용된 그래픽 등에 관여
   
   * [참고] 스크립트 언어 (Script Language)
     
     * 응용 소프트웨어를 제어하는 컴퓨터 프로그래밍 언어

1. **Browser APIs**
   
   * 웹 브라우저에 내장된 API로, 현재 컴퓨터 환경에 관한 데이터를 제공하거나 오디오 재생 등 여러가지 유용하고 복잡한 일을 수행
   * JavaScript로 Browser API들을 사용해서 여러가지 기능 사용 가능
   * **종류**
     * DOM
     * Geolocation API
     * WebGL 등

2. **DOM**
   
   * 문서 객체 모델(Document Objects Model)
   
   * 문서의 구조화된 표현을 제공하며 프로그래밍 언어가 DOM 구조에 접근할 수 있는 방법을 제공
     
     * 문서 구조, 스타일, 내용 등을 변경할 수 있게 도움
     
     * HTML 콘텐츠를 추가, 제거, 변경하고, 동적으로 페이지에 스타일을 추가하는 등   HTML/CSS를 조작할 수 있음
   
   * 문서가 구조화되어 있으며 <u>각 요소는 객체(object)로 취급</u>
   
   * 단순한 속성 접근, 메서드 활용 뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작 가능
   
   * 문서를 논리 트리로 표현
   
   * DOM 메서드를 사용하면 프로그래밍적으로 트리에 접근할 수 있고, 이를 통해 문서의 구조, 스타일, 컨텐츠를 변경 가능
   
   * 웹 페이지는 일종의 문서(document)
   
   * 이 문서는 웹 브라우저를 통해 그 내용이 해석되어 웹 브라우저 화면에 나타나거나 HTML 코드 자체로 나타나기도 함
   
   * DOM은 동일한 문서를 표현하고, 저장하고, 조작하는 방법을 제공
   
   * DOM은 <u>웹 페이지의 객체 지향 표현</u>이며, JavaScript와 같은 <u>스크립트 언어</u>를 이용해 DOM 수정 가능
   
   * DOM에 접근하기
     
     * 모든 웹 브라우저는 스크립트 언어가 접근할 수 있는 웹페이지를 만들기 위해 DOM을 항상 사용함
     
     * DOM의 주요 객체들을 활용하여 문서를 조작하거나, 특정 요소들을 얻을 수 있음
   
   * DOM의 **주요 객체**
     
     * **window**
     
     * **document**
     
     * navigator, location, history, screen 등
   
   * **window** object
     
     * DOM을 표현하는 창
     
     * 가장 <u>최상위</u> 객체(작성시 생략 가능)
     
     * 탭 기능이 있는 브라우저 -> 각각의 탭을 각각의 window 객체로 나타냄
   
   * **window의 메서드 예시**
     
     * 새 탭 열기: **window.open()**
     
     * 경고 대화 상자 표시: **window.alert()**
     
     * 인쇄 대화 상자 표시: **window.print()**
   
   * **document** object
     
     * 브라우저가 불러온 웹 페이지
     
     * 페이지 컨텐츠의 진입점 역할을 하며, \<body> 등과 같은 수많은 다른 요소 포함
     
     * window.document와 같음(window 생략 가능)
   
   * **document의 속성 예시**
     
     * 현재 문서의 제목 (HTML의 **\<title>** 값): document.title
     
     * 제목 수정하기: document.title = "제목"
   
   * [참고] document는 window의 속성
   
   * [참고] 파싱 (Parsing)
     
     * 구문 분석, 해석
     
     * 브라우저가 문자열 해석 -> DOM Tree로 만드는 과정

3. **DOM 조작**
   
   * **DOM 조작 순서**
     
     * **선택 (Select)**
     
     * **조작 (Manipulation)**
       
       * 생성, 추가, 삭제 등
   
   * **선택 관련 메서드**
     
     * document.**querySelector(selector)**
       
       * 제공한 선택자와 일치하는 **element 한 개** 선택
       
       * 제공한 CSS selector를 만족하는 <u>첫번째 element</u> 객체 반환 (<u>없다면 null</u> 반환)
     
     * doocument.**querySelectorAll(selector)**
       
       * 제공한 선택자와 일치하는 **여러 element** 선택
       
       * 매칭할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음
       
       * 제공한 CSS selector를 만족하는 **NodeList** 반환
   
   * 선택 관련 메서드 실습
   
   * **[참고] NodeList**
     
     * **index**로만 각 항목에 접근 가능
     
     * 배열의 forEach 메서드 및 다양한 배열 메서드 사용 가능
     
     * querySelectorAll()에 의해 반환되는 NodeList -> DOM의 변경사항을 <u>실시간으로 반영X</u>
   
   * **조작 관련 메서드 (생성)**
     
     * document.**createElement(tagName)**
       
       * 작성한 tagName의 HTML 요소를 생성하여 반환
   
   * **조작 관련 메서드 (입력)**
     
     * Node.**innerText**
       
       * Node 객체와 그 자손의 텍스트 컨텐츠(DOMString)를 표현 (해당 요소 내부의 raw test)
       
       * 사람이 읽을 수 있는 요소만 남김
       
       * 줄 바꿈 인식, 숨개진 애용 무시 등 최종적으로 스타일링이 적용된 모습으로 표현
   
   * **조작 관련 메서드 (추가)**
     
     * Node.**appendChild()**
       
       * 한 Node를 특정 부모 Node의 자식 중 NodeList 중 마지막 자식으로 압십
       
       * 한번에 <u>오직 하나의 Node</u>만 추가 가능
       
       * 추가된 Node 객체를 <u>반환</u>
       
       * 주어진 Node가 이미 문서에 존재하는 다른 Node를 참조 -> 현재 위치에서 새로운 위치로 이동
   
   * **조작 관련 메서드 (삭제)**
     
     * Node.**removeChild()**
       
       * DOM에서 자식 Node 제거
       
       * 제거된 Node를 반환
   
   * **조작 관련 메서드 (속성 조회 및 설정)**
     
     * Element.**getAttribute(attributeName)**
       
       * 해당 요소의 지정된 값(문자열)을 반환
       
       * 인자(attributeName)는 값을 얻고자 하는 속성의 이름
     
     * Element.**setAttribute(name, value)**
       
       * 지정된 요소의 값을 설정
       
       * 속성이 이미 존재 -> 값 갱신
       
       * 존재 x -> 지정된 이름과 값으로 새 속성 추가
   
   * DOM 조작 정리

## 2. Event

----

0. 개요
   
   * Event: 프로그래밍하고 있는 시스템에서 일어나는 사건(action) 혹은 발생(occurrence)

1. Event Intro
   
   * Event object
     
     * 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체
     
     * DOM 요소는 Event를 받고("수신")
     
     * 받은 Event를 "처리"할 수 있음
       
       * 처리는 주로 addEventListener()라는 Event처리기(Event handler)를 다양한 html 요소에 "부착"해서 처리함
   
   * Event 발생
   
   * Event handler - **addEventListener()**
     
     * 대상에 특정 Event가 발생하면, 할 일을 등록
       
       * **EventTarget.addEventListener(type, listener[, options])**
         
         * 지정한 Event가 대상에 전달될 때마다 호출할 함수 설정
         
         * Event를 지원하는 모든 객체(Element, Document, Window 등)를 대상으로 지정 가능
         
         * **type**: 반응할 Event 유형을 나타내는 대소문자 구분 문자열
           
           * 대표 이벤트
             
             * **input**, **click**, **submit**
         
         * **listener**: 지정된 타입의 Event를 수신할 객체
           
           * JavaScript function 객체(콜백 함수)여야 함
           
           * 콜백 함수는 발생한 Event의 데이터를 가진 Event 객체를 유일한 매개변수로 받음
   
   * addEventListener 정리
     
     * "\~하면 \~한다."
       
       * 클릭하면, 경고창을 띄운다.
       
       * 특정 Event가 발생하면, 할 일(콜백 함수)을 등록한다.

2. Event 실습
   
   * 버튼 클릭 -> 특정 변수 값 변경하기
   
   * input에 입력하면 입력 값을 실시간으로 출력하기
   
   * input에 입력하면 입력 값을 실시간으로 출력하고, 버튼을 클릭하면 출력된 값의 클래스를 토글하기

3. Event 취소
   
   * event.**preventDefault()**
     
     * 현재 Event의 기본 동작을 중단
     
     * HTML 요소의 기본 동작을 작동하지 않게 막음
     
     * HTML 요소의 기본 동작 예시
       
       * a 태그: 클릭 시 특정 주소로 이동
       
       * form 태그: form 데이터 전송

4. Event 취소 실습
   
   * 웹 페이지 내용을 복사하지 못하도록 하기

5. Event 종합 실습
   
   * 버튼을 클릭하면 랜덤 로또 번호 6개 출력하기
   
   * [참고] lodash
     
     * 모듈성, 성능 및 추가 기능을 제공하는 JavaScript 유틸리티 라이브러리
     
     * array, objects등 자료구조를 다룰 때 사용하는 유용하고 간편한 유틸리티 함수들을 제공
     
     * 함수 예시
       
       * reverse, sortBy, range, random...
   
   * CREATE, READ 기능을 충족하는 todo app 만들기

## 3. this

----

1. this
   
   * 어떠한 object를 가리키는 키워드
     
     * (java에서의 this와 python에서의 self는 인스턴스 자기자신을 가리킴)
   
   * JavaScript의 함수는 호출될 때 -> this를 암묵적으로 전달 받음
   
   * JavaScript에서의 this는 일반적인 프로그래밍 언어에서의 this와 조금 다르게 동작
   
   * JavaScript는 해당 **함수 호출 방식**에 따라 this에 바인딩되는 객체가 달라짐
   
   * 즉, 함수를 선언할 때 this에 객체 결정x -> **함수가 어떻게 호출 되었는지에 따라 동적으로 결정**
   
   * this INDEX
     
     * 전역 문맥에서의 this
     
     * 함수 문맥에서의 this
       
       * 단순 호출
       
       * Method (객체의 메서드로서)
       
       * Nested
   
   * **전역 문맥에서의 this**
     
     * 브라우저의 전역 객체인 **window**를 가리킴
       
       * 전역객체는 모든 객체의 유일한 **최상위 객체**를 의미
   
   * **함수 문맥에서의 this**
     
     * 함수의 this 키워드 -> 다른 언어와 조금 다르게 동작
     
     * this의 값 -> **함수를 호출한 방법에 의해 결정됨**
     
     * 함수 내부에서 this의 값 -> 함수를 호출한 방법에 의해 좌우됨
     
     * **단순 호출**
       
       * **전역 객체**를 가리킴
       
       * 전역은 **브라우저에서는 window**, **Node.js는 global**을 의미
     
     * **Method (Function in Object, 객체의 메서드로서)**
       
       * 메서드로 선언하고 호출한다면, 객체의 메서드이므로 **해당 객체가 바인딩**
     
     * **Nested (Function 키워드)**
       
       * forEach의 콜백 함수에서의 this가 메서드의 객체를 가리키지 못하고 전역 객체 window를 가리킴
       
       * 단순호출 방식으로 사용되었기 때문
       
       * 이를 해결하기 위해 등장한 함수표현식이 바로 화살표함수
     
     * **Nested (화살표 함수)**
       
       * 메서드의 객체를 잘 가리킴
       
       * 화살표 함수에서 this는 자신을 감싼 정적 범위
       
       * 자동으로 한단계 상위의 scope의 context를 바인딩
     
     * **화살표 함수**
       
       * 호출의 위치와 상관없이 상위 스코프를 가리킴(Lexical scope this)
       
       * Lexical scope
         
         * 함수를 어디서 호출하는지가 아니라 어디에 선언하였는지에 따라 결정
         
         * Static scope라고도하며 대부분의 프로그래밍 언어에서 따르는 방식
       
       * 함수 내의 함수 상황에서 화살표 함수를 쓰는 것을 권장
   
   * **this와 addEventListener**
     
     * **addEventListener**에서의 **콜백 함수** -> **function 키워드**의 경우 -> addEventListener를 **호출한 대상(event.target)** 을 뜻함
     
     * 화살표 함수의 경우 상위 스코프 지칭 -> window 객체 바인딩
     
     * addEventListener의 콜백 함수 -> function 키워드 사용
