## 0. 목차

----

1. 동기와 비동기

2. JavaScript의 비동기 처리

3. Axios 라이브러리

4. Callback과 Promise

5. AJAX

## 1. 동기와 비동기

----

1. **동기 (Synchronous)**
   
   * 모든 일을 **순서대로 하나씩** 처리하는 것
   
   * 순서대로 처리 == 이전 작업 끝나면 다음 작업 시작

2. **비동기 (Asynchronous)**
   
   * 작업 시작 후 **결과를 기다리지 않고** 다음 작업 처리 (병렬적 수행)
   
   * 시간이 필요한 작업들은 요청을 보낸 뒤 응답이 빨리 오는 작업부터 처리

3. 비동기(Asynchronous)를 **사용하는 이유**
   
   * **사용자 경험**
     
     * 동기식 처리 -> 특정 로직 실행되는 동안 다른 로직 실행 차단 -> 프로그램이 응답하지 않는 듯한 사용자 경험
     
     * 비동기 처리 -> 먼저 처리되는 부분부터 보여줄 수 있음 -> 사용자 경험에 긍정적인 효과

## 2. JavaScript의 비동기 처리

----

1. **Single Thread 언어, JavaScript**
   
   * 한번에 하나의 일만 수행 가능한 Single Thread 언어 -> 동시에 여러 작업 처리X
   
   * JavaScript는 하나의 작업을 요청한 순서대로 처리할 수 밖에 없음 -> 어떻게 비동기 처리?

2. **JavaScript Runtime**
   
   * 비동기 처리를 할 수 있도록 도와주는 환경 필요
   
   * **런타임(Runtime)**: 특정 언어가 동작할 수 있는 환경
   
   * JavaScript에서 **비동기**와 관련한 작업 -> **브라우저 or Node 환경**에서 처리
   
   * 브라우저 환경에서의 비동기 동작의 **구성요소**
     
     * JavaScript Engine의 **Call Stack**
     
     * **Web Api**
     
     * **Task Queue**
     
     * **Event Loop**

3. **비동기 처리 동작 방식**
   
   * 브라우저 환경에서의 비동기 처리
     
     * **모든 작업** -> **Call Stack**(LIFO)으로 들어간 후 처리
     
     * **오래 걸리는 작업**이 Call Stack으로 들어오면 -> **Web API**로 보내서 별도 처리
     
     * Web API에서 처리가 끝난 작업들 -> **Task Queue**(FIFO)에 순서대로 들어간다
     
     * **Event Loop**가 Call Stack이 비어 있는 것 체크 -> Task Queue에서 가장 오래된 작업 -> Call Stack으로 보냄
   
   * **Call Stack**: 요청이 들어올 때마다 순차적으로 처리하는 Stack(LIFO)
     
     * 기본적인 JavaScript의 Single Thread 작업 처리
   
   * **Web API**: JavaScript 엔진이 아닌 브라우저에서 제공하는 runtime 환경
     
     * 시간이 소요되는 작업 처리 (**setTimeout, DOM Event, AJAX 요청 등**)
   
   * **Task Queue**: 비동기 처리된 Callback 함수가 대기하는 Queue(FIFO)
   
   * **Event Loop**: Call Stack과 Task Queue를 지속적으로 모니터링
     
     * Call Stack이 비어 있는지 확인 -> 비어있다면 -> Task Queue에서 대기 중인 오래된 작업을 Call Stack으로 Push
   
   * 정리

## 3. Axios 라이브러리

----

1. Axios
   
   * JavaScript의 HTTP 웹 통신을 위한 라이브러리
   
   * 인터페이스와 쉽게 사용할 수 있는 비동기 통신 기능 제공

2. Axios 기본 구조
   
   * Axios 사용해보기
     
     * cdn
     
     * get, post 등 여러 method 사용가능
     
     * **then** -> 성공하면 수행할 로직 작성
     
     * **catch** -> 실패하면 수행할 로직 작성
     
     ```html
     axios.get('요청할 URL')
         .then(성공시 콜백함수)
         .catch(실패시 콜백함)
     ```
   
   * 고양이 사진 가져오기
   
   * 정리

## 4. Callback과 Promise

---

1. 비동기 처리의 단점
   
   * Web API로 들어오는 순서X -> 작업이 완료되는 순서에 따라 처리
   
   * 코드 실행 순서 불명확 -> 실행 결과를 예상하면서 코드를 작성하는 것X

2. **콜백 함수 (Callback Function)**
   
   * **콜백 함수**: 다른 함수의 인자로 전달되는 함수
   
   * 동기, 비동기 상관x 사용 가능
   
   * **비동기 콜백(asynchronous callback)**: 비동기 작업이 완료된 후 실행할 작업을 명시하는데 사용되는 콜백함수

3. 콜백 함수를 **사용하는 이유**
   
   * 특정한 조건 혹은 행동에 의해 호출되도록 작성 가능
   
   * **비동기 처리를 순차적으로 동작 가능하게 함**
   
   * 비동기 처리를 위해서는 콜백 함수의 형태 반드시 필요

4. **콜백 지옥(Callback Hell)**
   
   * 콜백 함수 -> **연쇄적으로 발생하는 비동기 작업**을 **순차적으로 동작**할 수 있게 함
   
   * **콜백 지옥(Callback Hell)**: 비동기 처리를 위한 콜백 작성 시 마주하는 문제
     
     * 파멸의 피라미드(Pyramid of doom)라고도 부름

5. **프로미스 (Promise)**
   
   * Callback Hell 문제를 해결한 비동기 처리를 위한 객체
   
   * 작업이 끝나면 실행 시켜줄게라는 약속
   
   * **비동기 작업의 완료 또는 실패를 나타내는 객체**
   
   * Promise 기반의 클라이언트 -> Axios 라이브러리
     
     * 성공에 대한 약속 then()
     
     * 실패에 대한 약속 catch()
   
   * **then(callback)**
     
     * 요청한 작업이 성공하면 callback 실행
     
     * callback은 이전 작업의 **성공 결과**를 인자로 전달 받음
   
   * **catch(callback)**
     
     * then()이 **하나라도 실패**하면 callback 실행
     
     * callback은 이전 작업의 **실패 객체**를 인자로 전달 받음
   
   * then과 catch 모두 **항상 promise 객체 반환** -> 계속해서 **chaining 가능**
   
   * axios로 처리한 비동기 로직이 항상 promise 객체 반환 -> then을 계속 이어 나가면서 작성 가능
   
   * then, catch를 진행할 때 **return 꼭 넣어주기!!**

6. Promise가 보장하는 것 (vs 비동기 콜백)
   
   * callback 함수 -> JS의 Event Loop가 현재 실행 중인 Call Stack을 완료하기 이전에는 절대 호출X
     
     * Promise callback 함수 -> Event Queue에 배치되는 엄격한 순서로 호출됨
   
   * 비동기 작업이 성공하거나 실패한 뒤에 .then() 메서드를 이용하여 추가한 경우에도 위와 똑같이 동작
   
   * .then()을 여러번 사용하여 여러개의 callback 함수 추가 가능(**Chaining**)
     
     * 각각의 callback은 주어진 **순서대로** 하나하나 실행

## 5. AJAX

----

1. **AJAX란?**
   
   * 비동기 통신 웹 개발 기술(Asynchronous Javascript And XML(AJAX))
   
   * AJAX의 **특징**
     
     * 페이지 **새로고침 없이** 서버에 요청
     
     * 서버로부터 **응답(데이터)을 받아 작업을 수행**
   
   * 비동기 웹 통신을 위한 라이브러리 중 하나 -> Axios

2. 비동기 적용하기
   
   * axios로 POST 요청을 보내기 위해 필요한 것
     
     * url에 작성할 user pk (HTML -> JavaScript)
       
       * **data-\* attributes**
         
         * **사용자 지정 데이터 특성**을 만들어 임의의 데이터를 **HTML과 DOM 사이에서 교환** 할 수 있는 방법
         
         * 모든 사용자 지정 데이터는 dataset 속성을 통해 사용 가능
         
         * **data-test-value**라는 이름 특성 지정 -> JS에서는 **element.dataset.testValue**로 접근
         
         * 속성명 작성시 **주의사항**
           
           * 대소문자 여부 상관없이 xml로 시작x
           
           * 세미콜론,대문자 포함 X
     
     * csrftoken
       
       * hidden 타입으로 숨겨져있는 csrf 값을 가진 input 태그 선택
       
       * axios에 headers: {'X-CSRFToken': 값}
   
   * 팔로우가 된 상태인지 여부 확인
     
     * axios 요청을 통해 받는 response 객체 활용 -> view 함수 -> 팔로우 여부 파악할 수 있는 변수 담아 JSON 타입으로 응답
   
   * [참고] XHR
   
   * 팔로워 & 팔로잉 수 비동기 적용
