## 0. 목차

----

1. UX&UI

2. Vue Router

3. Navigation Guard

4. Articles app with Vue

## 1. UX&UI

-----

1. UX (User Experience)
   
   * 유저와 가장 가까이에 있는 분야, 데이터를 기반으로 유저를 조사하고 분석해서 개발자, 디자이너가 이해할 수 있게 소통
   
   * 유저가 느끼는 느낌, 태도 그리고 행동을 디자인
   
   * 좋은 UX를 설계하기 위해서는
     
     * 유저 리서치, 데이터 설계 및 정제, 유저 시나리오, 프로토타입 설계 등이 필요

2. UI (User Interface)
   
   * 유저에게 보여지는 화면을 디자인
   
   * UX를 고려한 디자인을 반영, 기능 개선 혹은 추가가 필요한 경우 Front-end 개발자와 가장 많이 소통
   
   * 좋은 UI를 설계하기 위해서는
     
     * 심미적인 부분 + 사용자가 보다 쉽고 편리하게 사용할 수 있도록 하는 부분까지 고려되어야 함
     
     * 통일된 디자인을 위한 디자인 시스템, 소통을 위한 중간 산출물, 프로토타입 등 필요
     
     * UI 디자인에 있어 가장 중요한 것은 협업

3. [참고] Interface
   
   * 서로 다른 두 개의 시스템, 장치 사이에서 정보나 신호를 주고받는 경우의 접점
     
     * 즉, 사용자가 기기를 쉽게 동작 시키는데 도움을 주는 시스템
   
   * 인터페이스 예시
     
     * CLI(command-line interface)나 GUI(Graphic User Interface)를 사용해서 컴퓨터를 조작

4. 디자이너와 기획자 그리고 개발자

5. 생각하는 UX & UI 디자인

6. Prototyping
   
   * Software prototyping
     
     * 애플리케이션의 프로토타입을 만드는 것
     
     * 개발 중인 sw 프로그램의 완성되기 전 버전을 만드는 것
   
   * Prototyping Tool 시장
   
   * Figma
     
     * 인터페이스 디자인을 위한 협업 웹 애플리케이션
     
     * 협업에 중점을 두면서 UI/UX 설계에 초점
     
     * 웹 기반 시스템 -> 매우 가벼운 환경에서 실행 가능, 모든 작업 내역 웹에 저장
     
     * 실시간으로 팀원들이 협업할 수 있는 기능 제공
     
     * 직관적이고 다양한 디자인 툴 제공
     
     * Figma 사용자들이 만든 다양한 플러그인이 존재
     
     * 대부분의 기능 무료
   
   * 프로젝트를 시작하기 전
     
     * 개발 시작 전 반드시 충분한 기획을 거칠 것
     
     * 완성하고자 하는 대략적인 모습을 그려보는 과정이 필요 (프로토타입)
     
     * 이러한 과정을 통해서 기획에서 빠진 화면이나 API등을 확인 가능
     
     * 설계와 기획이 끝난 후 개발을 시작해야 체계적인 진행 가능
   
   * 프로젝트와 협업

## 2. Vue Router

---

1. Routing
   
   * 네트워크에서 경로를 선택하는 프로세스
   
   * 웹 서비스에서의 라우팅
     
     * 유저가 방문한 URL에 대해 적절한 결과를 응답하는 것
   
   * Routing in SSR
     
     * Server가 모든 라우팅을 통제
     
     * URL로 요청이 들어오면 응답으로 완성된 HTML 제공
       
       * Django로 보낸 요청의 응답 HTML은 완성본인 상태였음
     
     * 결론적으로, Routing(URL)에 대한 결정권을 서버가 가짐
   
   * Routing in SPA / CSR
     
     * 서버는 하나의 HTML(index.html)만을 제공
     
     * 이후에 모든 동작 -> 하나의 HTML 문서 위에서 JsavaScript 코드 활용
       
       * DOM을 그리는데 필요한 추가적인 데이터가 있다면 axios와 같은 AJAX 요청을 보낼 수 있는 도구를 사용하여 데이터를 가져오고 처리
     
     * 즉, 하나의 URL만 가질 수 있음
   
   * Why routing??
     
     * 동작에 따라 URL이 반드시 바뀌어야 하나? -> X -> 단, 유저의 사용성 관점에서는 필요
     
     * Routing이 없다면
       
       * 유저가 URL을 통한 페이지의 변화를 감지X
       
       * 페이지가 무엇을 렌더링 중인지에 대한 상태 알 수 없음
         
         * 새로고침 시 처음 페이지로 돌아감
         
         * 링크 공유 시 처음 페이지만 공유 가능
       
       * 브라우저의 뒤로 가기 기능 사용할 수 X

2. **Vue Router**
   
   * Vue의 공식 라우터
   
   * SPA 상에서 라우팅을 쉽게 개발할 수 있는 기능 제공
   
   * 라우트(routes)에 컴포넌트를 매핑한 후, 어떤 URL에서 렌더링 할지 알려줌
     
     * 즉, SPA를 MPA처럼 URL을 이동하면서 사용 가능
     
     * SPA의 단점 중 하나인 "**URL이 변경되지 않는다**"를 **해결**
   
   * [참고] MPA (Multiple Page Application)
     
     * 여러 개의 페이지로 구성된 애플리케이션
     
     * SSR방식으로 렌더링
   
   * Vue Router 시작하기
     
     * \$ vue add router
     
     * history mode 사용여부 -> Yes
     
     * App.vue
       
       * router-link 요소 및 router-view가 추가됨
     
     * router/index.js 생성
     
     * views 폴더 생성
   
   * **History mode**
     
     * 브라우저의 History API를 활용한 방식
       
       * 새로고침 없이 URL 이동 기록을 남길 수 있음
     
     * 우리에게 익숙한 URL 구조로 사용 가능
       
       * 예시) http://localhost:8080/index
     
     * [참고] History mode를 사용하지 않으면 Default 값인 hash mode로 설정됨 ('#'을 통해 URL을 구분하는 방식)
       
       * 예시) http://localhost:8080#index
   
   * **router-link**
     
     * a 태그와 비슷한 기능 -> URL을 이동시킴
       
       * routes에 등록된 컴포넌트와 매핑됨
       
       * 히스토리 모드에서 router-link는 클릭 이벤트를 차단하여 a 태그와 달리 브라우저가 페이지를 다시 로드하지 않도록 함
     
     * 목표 경로는 'to' 속성으로 지정됨
     
     * 기능에 맞게 HTML에서 a 태그로 rendering 되지만, 필요에 따라 다른 태그로 바꿀 수 있음
   
   * **router-view**
     
     * 주어진 URL에 대해 일치하는 컴포넌트를 렌더링 하는 컴포넌트
     
     * 실제 component가 DOM에 부착되어 보이는 자리를 의미
     
     * router-link를 클릭하면 routes에 매핑된 컴포넌트를 렌더링
     
     * Django에서의 block tag와 비슷함
       
       * App.vue는 base.html의 역할
       
       * router-view는 block 태그로 감싼 부분
   
   * **src/router/index.js**
     
     * 라우터에 관련된 정보 및 설정이 작성되는 곳
     
     * Django에서의 urls.py에 해당
     
     * routes에 URL과 컴포넌트를 매핑
   
   * **src/Views**
     
     * router-view에 들어갈 component 작성
     
     * 기존에 컴포넌트를 작성하던 곳은 components 폴더 뿐이었지만 이제 두 폴더로 나뉘어짐
     
     * 각 폴더 안의 .vue 파일들이 기능적으로 다른 것은 아님
     
     * 이제 폴더별 컴포넌트 배치는 다음과 같이 진행
     
     * **views/**
       
       * **routes에 매핑되는 컴포넌트**, 즉 \<router-view\>의 위치에 렌더링 되는 컴포넌트를 모아두는 폴더
       
       * 다른 컴포넌트와 구분하기 위해 View로 끝나도록 만드는 것 권장
     
     * **components/**
       
       * **routes에 매핑된 컴포넌트의 하위 컴포넌트**를 모아두는 폴더

3. Vue Router 실습
   
   * **주소를 이동하는 2가지 방법**
     
     * **선언적 방식 네비게이션**
       
       * router-link의 **'to'** 속성으로 주소 전달
         
         * routes에 등록된 주소와 매핑된 컴포넌트로 이동
       
       * Named Routes
         
         * 이름을 가지는 routes
           
           * Django에서 path 함수의 name 인자의 활용과 같은 방식
       
       * 동적인 값을 사용하기 때문에 **v-bind를 사용**해야 정상적으로 작동
     
     * **프로그래밍 방식 네비게이션**
       
       * Vue 인스턴스 내부에서 라우터 인스턴스에 **\$router**로 접근 가능
       
       * 다른 URL로 이동하려면 **this.\$router.push**를 사용
         
         * history stack에 이동할 URL을 넣는(push) 방식
         
         * history stack에 기록이 남기 때문에 사용자가 브라우저의 뒤로 가기 버튼을 클릭하면 이전 URL로 이동 가능
       
       * \<router-link :to="..."\> 를 클릭하는 것과 \$router.push(...) 를 호출하는 것은 같은 동작
   
   * **Dynamic Route Matching**
     
     * 동적 인자 전달
       
       * URL의 특정 값을 변수처럼 사용 가능
       
       * ex) Django에서의 variable routing
     
     * \$route.params로 변수에 접근 가능
     
     * HTML에서 직접 사용하기 보다는 data에 넣어서 사용하는 것 권장
     
     * params를 이용하여 동적 인자 전달 가능
   
   * route에 컴포넌트를 등록하는 또다른 방법
     
     * **lazy-loading**
       
       * 모든 파일을 한 번에 로드하려고 하면 모든걸 다 읽는 시간이 매우 오래 걸림
       
       * 미리 로드를 하지 않고 특정 라우트에 방문할 때 매핑된 컴포넌트의 코드를 로드하는 방식을 활용할 수 있음
         
         * 모든 파일 한 번에 로드x -> 최초 로드 시간 빨라짐
         
         * 당장 사용하지 않을 컴포넌트는 먼저 로드하지 않는 것이 핵심

## 3. Navigation Guard

----

1. 네비게이션 가드
   
   * Vue router를 통해 특정 URL에 접근할 때 **다른 url로 redirect**를 하거나 **해당 URL로의 접근을 막는** 방법
     
     * ex) 사용자의 인증 정보가 없으면 특정 페이지에 접근하지 못하게 함
   
   * 네비게이션 가드의 **종류**
     
     * **전역 가드**: 애플리케이션 전역에서 동작
     
     * **라우터 가드**: 특정 URL에서만 동작
     
     * **컴포넌트 가드**: 라우터 컴포넌트 안에 정의

2. **전역 가드**
   
   * **Global Before Guard**
     
     * **다른 url 주소로 이동할 때** 항상 실행
     
     * router/index.js에 **router.beforeEach()** 를 사용하여 설정
     
     * 콜백 함수의 값으로 **3개의 인자**를 받음
       
       * **to**: **이동**할 URL 정보가 담긴 Route **객체**
       
       * **from**: **현재** URL 정보가 담긴 Route **객체**
       
       * **next**: **지정한** URL로 이동하기 위해 호출하는 **함수**
         
         * 콜백 함수 내부에서 **반드시 한번만 호출**되어야 함
         
         * 기본적으로 **to**에 해당하는 URL로 이동
     
     * URL이 변경되어 **화면 전환 전** router.beforeEach() 호출
       
       * 화면 전환되지 않고 **대기 상태**
     
     * 변경된 URL로 **라우팅하기 위해서는 next() 호출**해줘야 함
       
       * next()가 호출되기 전까지 화면 전환X
   
   * Global Before Guard 실습
   
   * Login 여부에 따른 라우팅 처리

3. **라우터 가드**
   
   * **특정 route**에 대해서만 가드를 설정하고 싶을 때
   
   * **beforeEnter()**
     
     * route에 진입했을 때 실행됨
     
     * <u>라우터를 등록한 위치에 추가</u>
     
     * 단 매개변수, 쿼리, 해시 값이 변경될 때는 실행되지X, **다른 경로에서 탐색**할 때만 실행됨
     
     * 콜백 함수는 to, from, next를 인자로 받음
   
   * Login 여부에 따른 라우팅 처리

4. **컴포넌트 가드**
   
   * 특정 컴포넌트 내에서 가드를 지정하고 싶을 때
   
   * **beforeRouteUpdate()**
     
     * 해당 컴포넌트를 **렌더링하는 경로가 변경될 때** 실행 
   
   * **params 변화 감지**
     
     * URL은 변하지만 페이지는 변화하지 않음
     
     * 변화하지 않는 **이유**
       
       * **컴포넌트가 재사용**되었기 때문
       
       * 기존 컴포넌트를 지우고 새로 만드는 것보다 효율적
         
         * 단, lifecycle hook이 호출되지 X
         
         * 따라서 \$route.params에 있는 데이터를 새로 가져오지 X
     
     * beforeRouteUpdate()를 사용해서 처리
       
       * userName을 이동할 params에 있는 userName으로 재할당

5. **404 Not Found**
   
   * 사용자가 **요청한 리소스가 존재하지 않을 때** 응답
   
   * 요청한 리소스가 존재하지 않는 경우
     
     * 모든 경로에 대해서 404 page로 redirect 시키기
       
       * 기존에 명시한 경로가 아닌 모든 경로가 404 page로 redirect됨
       
       * 이때, routes에 최하단부에 작성해야 함



## 4. Articles app with Vue

----

1. **Index**

2. **Create**
   
   * **v-on:{event}.prevent**를 활용하여 submit **이벤트 동작 취소**하기
     
     * @submit.prevent=""

3. **Detail**
   
   * **동적인자**를 통해 받은 id는 **str**이므로 형변환을 해서 비교
     
     * Number(id)
   
   * optional chaining(**?.**)을 통해 article 객체가 있을 때만 출력되도록 수정
   
   * **[참고] Optional Chaining**
     
     * Optional Chaining(**?.**) 앞의 평가 대상이 **undefined나 null**이면 -> **에러 발생X**, **undefined 반환**
   
   * **Date in JavaScript**
     
     * JavaScript에서 시간을 나타내는 Date 객체는 1970년 1월 1일 UTC(협정 세계시) 자정과의 시간 차이를 밀리초로 나타내는 정수값을 담음
       
       * **Date().toLocaleString()** 을 사용하여 변환
       
       * new Date(article?.createdAt).toLocaleString()

4. **Delete**

5. **404 Not Found**
   
   * Detail에 대한 route 보다 먼저 등록해줘야 함
     
     * path: '/404-not-found'
     
     * /404로 등록 -> 404번째 게시글과 혼동됨
   
   * 요청한 리소스가 존재하지 않는 경우 404 page로 redirect 시키기
     
     * \$router.push와 마찬가지로 name 이용하여 이동 가능
     
     * redirect: { name: 'NotFound404' }


