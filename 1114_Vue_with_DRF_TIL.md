## 0. 목차

---

1. Vue with DRF

2. CORS

3. DRF Auth System

4. DRF Auth with Vue

5. DRF-spectacular

## 1. Vue with DRF

----

1. Server & Client
   
   * 서버(server)란?
     
     * 클라이언트에게 정보와 서비스를 제공하는 컴퓨터 시스템
     
     * 서비스 전체를 제공 == Django Web Service
     
     * 정보를 제공 == DRF API Service
       
       * Django를 통해 관리하는 정보만을 클라이언트에게 제공
       
       * DRF를 사용하여 JSON으로 변환
   
   * 클라이언트(Client)란?
     
     * Server가 제공하는 서비스에 적절한 요청을 통해 Server로부터 반환 받은 응답을 사용자에게 표현하는 기능을 가진 프로그램 혹은 시스템
   
   * 정리
     
     * Server는 정보와 서비스를 제공 -> DRF
     
     * Client는 사용자의 정보 요청을 처리, server에게 응답 받은 정보를 표현 -> Vue

2. Again DRF
   
   * Skeleton code 확인

3. Back to Vue
   
   * Skeleton code 확인

4. Vue with DRF
   
   * AJAX 요청 준비
     
     * axios 설정
       
       * 설치: \$ npm install axios
       
       * store/index.js에서 불러오기
         
         * 요청 보낼 API server 도메인 변수에 담기
   
   * 요청 결과 확인
     
     * Server에서는 200을 반환하였으나 Client Console에서는 Error를 확인
     
     * 데이터를 확인할 수 없는 이유? CORS policy에 의해 blocked 되었기 때문

## 2. CORS

----

1. **Cross-Origin Resouce Sharing**
   
   * What Happened?
     
     * 브라우저가 요청을 보내고 서버의 응답이 브라우저에 도착
       
       * Server의 log는 200(정상) 반환
       
       * 즉, Server는 정상적으로 응답, 브라우저가 막은 것
     
     * 보안상의 이유로 브라우저는 **동일 출처 정책(SOP)** 에 의해 다른 출처의 리소스와 상호작용하는 것을 제한함
   
   * **SOP (Same - Origin Policy)**
     
     * 동일 출처 정책
     
     * 불러온 문서나 스크립트가 다른 출처에서 가져온 리소스와 상호작용하는 것을 제한하는 보안 방식
     
     * 잠재적으로 해로울 수 있는 문서를 분리함으로써 공격받을 수 있는 경로를 줄임
   
   * **Origin - 출처**
     
     * URL의 Protocol, Host, Port를 모두 포함하여 출처라고 부름
       
       * Same Origin 예시
       
       * Scheme / Protocol : http
       
       * Host : localhost
       
       * Port : 3000
   
   * **CORS - 교차 출처 리소스 공유**
     
     * 추가 **HTTP Header**를 사용하여, 특정 출처에서 실행 중인 웹 어플리케이션이 **다른 출처의 자원에 접근할 수 있는 권한**을 부여하도록 브라우저에 알려주는 체제
       
       * 어떤 출처에서 자신의 컨텐츠를 불러갈 수 있는지 서버에 지정할 수 있는 방법
     
     * 리소스가 자신의 출처와 다를 때 교차 출처 HTTP 요청을 실행
       
       * 다른 출처의 리소스를 가져오기 위해서는 이를 제공하는 서버가 브라우저에게 다른 출처지만 접근해도 된다는 사실을 알려야 함
       
       * 교차 출처 리소스 공유 정책 (CORS policy)
   
   * **CORS policy - 교차 출처 리소스 공유 정책**
     
     * 다른 출처에서 온 리소스를 공유하는 것에 대한 정책
     
     * CORS policy에 위배되는 경우 브라우저에서 해당 응답 결과를 사용하지 않음
       
       * Server에서 응답을 주더라도 브라우저에서 거절
     
     * 다른 출처의 리소스를 불러오려면 그 출처에서 **올바른 CORS header**를 포함한 응답을 반환해야 함

2. **How to set CORS**
   
   * How to set CORS
     
     * CORS 표준에 의해 추가된 HTTP Response Header를 통해 이를 통제 가능
     
     * HTTP Response Header 예시
       
       * Access-Control-Allow-Origin / Access-Control-Allow-Credentials / Access-Control-Allow-Headers / Access-Control-Allow-Methods
     
     * Access-Control-Allow-Origin
       
       * 단일 출처를 지정하여 브라우저가 해당 출처가 리소스에 접근하도록 허용
   
   * **django-cors-headers library 사용하기**
     
     * 응답에 CORS header를 추가해주는 라이브러리
     
     * 다른 출처에서 Django 애플리케이션에 대한 브라우저 내 요청을 허용함
     
     * **라이브러리 설치 및 requirements.txt 업데이트**
       
       * \$ pip install django-cors-headers
       
       * \$ pip freeze > requirements.txt
     
     * App 추가 및 MIDDLEWARE 추가 주석 해제
       
       * 주의 ) CorsMiddleware는 가능한 CommonMiddleware 보다 먼저 정의되어야함
     
     * CORS_ALLOWED_ORIGINS에 **교차 출처 자원 공유를 허용할 Domain 등록**
       
       * CORS_ALLOWED_ORIGINS = [ 'http://localhost:8080' ]
       
       * 모든 Origin을 허용 -> CORS_ALLOWED_ORIGINS = True

3. **Vue with DRF (feat.CORS)**
   
   * Article Read
   
   * Article Create
   
   * [참고] 지금의 요청 방식은 효율적인가?
     
     * 비효율적인 부분이 존재
       
       * 전체 게시글 정보를 요청해야 새로 생성된 게시글을 확인 할 수 있음
       
       * 만약  vuex state를 통해 전체 게시글 정보를 관리하도록 구성한다면?
       
       * 나 이외의 유저들이 새롭게 생성한 게시글은 언제 불러 와야 할까?
       
       * 무엇을 기준으로 새로운 데이터가 생겼다는 것을 확인할 수 있을까?
     
     * 내가 구성하는 서비스에 따라 데이터 관리 방식을 고려해 보아야 함
   
   * Article Detail

## 3. DRF Auth System

----

1. Authentication & Authorization
   
   * Authentication - 인증, 입증
     
     * 사용자가 누구인지 확인하는 행위
     
     * 모든 보안 프로세스의 첫번째 단계 (가장 기본 요소)
     
     * 401 Unauthorized
       
       * HTTP 표준에서는 미승인(unauthorized)을 명확히 하고 있지만, 의미상 이 응답은 비인증(unauthenticated)을 의미
   
   * Authorization - 권한 부여, 허가
     
     * 사용자에게 특정 리소스 또는 기능에 대한 액세스 권한을 부여하는 과정(절차)
     
     * 보안 환경에서 권한 부여는 항상 인증이 먼저 필요함
       
       * 사용자는 조직에 대한 액세스 권한을 부여 받기 전에 먼저 자신의 ID가 진짜인지 먼저 확인해야 함
     
     * 403 Forbidden
       
       * 401과 다른 점 -> 서버는 클라이언트가 누구인지 알고 있음
   
   * Authentication and authorization work together
     
     * 회원가입 후, 로그인 시 서비스를 이용할 수 있는 권한 생성
       
       * 인증 이후에 권한이 따라오는 경우가 많음
     
     * 단, 모든 인증을 거쳐도 권한이 동일하게 부여되는 것은 아님
     
     * 세션, 토큰, 제3자를 활용하는 등의 다양한 인증 방식이 존재

2. How to authentication determined
   
   * 인증 여부 확인 방법
     
     * DRF 공식문서에서 제안하는 인증 절차 방법
     
     * settings.py에 작성하여야 할 설정
       
       * 기본적인 인증 절차를 어떠한 방식으로 둘 것인지 설정
     
     * DRF가 기본으로 제공해주는 인증 방식 중 하나인 TokenAuthentication 사용
     
     * 모든 상황에 대한 인증 방식을 정의 -> 각 요청에 따라 다른 인증 방식을 거치고자 한다면 다른 방식 필요
     
     * view 함수마다 (각 요청마다) 다른 인증 방식을 설정하고자 한다면 decorator 활용
     
     * [참고] permission_classes
       
       * 권한 관련 설정
       
       * 권한 역시 특정 view 함수마다 다른 접근 권한을 요구할 수 있음
   
   * 다양한 인증 방식
     
     * BasicAuthentication
       
       * 가장 기본적인 수준의 인증 방식
       
       * 테스트에 적합
     
     * SessionAuthentication
       
       * Django에서 사용하였던 session 기반의 인증 시스템
       
       * DRF와 Django의 session 인증 방식은 보안적 측면을 구성하는 방법에 차이가 있음
     
     * RemoteUserAuthentication
       
       * Django의 Remote user 방식을 사용할 때 활용하는 인증 방식
     
     * TokenAuthentication
       
       * 매우 간단하게 구현 가능
       
       * 기본적인 보안 기능 제공
       
       * 다양한 외부 패키지 존재
     
     * (중요) settings.py에서 DEFAULT_AUTHENTICATION_CLASSES를 정의
       
       * TokenAuthentication 인증 방식을 사용할 것임을 명시
   
   * TokenAuthentication **사용 방법**
     
     * INSATALLED_APPS에 rest_framework.authtoken 등록
       
       * migrate 추가로 진행해야함
     
     * 각 User 마다 고유 Token 생성
     
     * 생성한 Token을 각 User에게 발급
       
       * User는 발급받은 Token을 요청과 함께 전송
       
       * Token을 통해 User 인증 및 권한 확인
     
     * Token 발급 방법
     
     * User는 발급 받은 Token을 headers에 담아 요청과 함께 전송
       
       * 단, 반드시 Token 문자열 함께 삽입
         
         * 삽입해야 할 문자열은 각 인증 방식마다 다름 (ex.Bearer, Auth, JWT 등)
       
       * 주의) Token 문자열과 발급받은 실제 token 사이를 ' '(공백)으로 구분
     
     * Authorization HTTP headers 작성 방법
   
   * 토큰 생성 및 관리 문제점
     
     * 기본 제공 방식에서 고려하여야 할 사항들
       
       * Token 생성 시점
       
       * 생성한 Token 관리 방법
       
       * User와 관련된 각종 기능 관리 방법
         
         * 회원가입, 로그인, 회원 정보 수정, 비밀 번호 변경 등

3. **dj-rest-auth**
   
   * Dj-Rest-Auth
     
     * 회원가입, 인증(소셜미디어 인증 포함), 비밀번호 재설정, 사용자 세부 정보 검색, 회원 정보 수정 등을 위한 REST API end point 제공
     
     * 주의) django-rest-auth는 더 이상 업데이트를 지원하지 않음 dj-rest-auth 사용
   
   * dj-rest-auth 사용 방법
     
     * 패키지 설치
     
     * App 등록
     
     * url 등록
   
   * 시작하기 전에
     
     * auth.User를 accounts.User로 변경 필요
     
     * auth.User로 설정된 DB 제거
     
     * my_api/settings.py 주석 해제
   
   * dj-rest-auth 사용하기
   
   * Registration
     
     * Registration 기능을 사용하기 위해 추가 기능 등록 및 설치 필요
       
       * dj-rest-auth는 소셜 회원가입을 지원
       
       * dj-rest-auth의 회원가입 기능을 사용하기 위해서는 django-allauth 필요
     
     * django-allauth 설치 : \$ pip install 'dj-rest-auth[with_social]'
     
     * my_api/settings.py 주석 해제
       
       * App 등록 및 SITE_ID 설정
     
     * [참고] SITE_ID는 무엇인가요?
       
       * Django는 하나의 컨텐츠를 기반으로 여러 도메인에 컨텐츠를 게시 가능하도록 설계됨
       
       * 다수의 도메인이 하나의 데이터베이스에 등록
       
       * 현재 프로젝트가 첫번째 사이트임을 나타냄
     
     * my_api/urls.py 주석 해제
     
     * migrate -> allauth 추가에 대한 migrate
     
     * /accounts/signup/ 페이지 확인
     
     * Get method는 접근 불가
     
     * 회원가입 POST 요청 양식 제공
       
       * email은 생략 가능
   
   * Sign up & Login
     
     * 회원가입 요청 후 결과 확인
       
       * 요청에 대한 응답으로 Token 발급
     
     * 로그인 시에도 동일한 토큰 발급
     
     * 발급 받은 토큰 테스트를 위해 기록
       
       * b5814836ce39a8dc4a31ca2b3e204dded0775ad5
   
   * **Password change**
     
     * /accounts/password/change/ 기능 확인
       
       * 로그인 되어 있거나, 인증이 필요한 기능
       
       * DRF 자체 제공 HTML form에서는 토큰을 입력할 수 있는 공간이 없음
       
       * Postman 에서 진행
     
     * [참고] Raw data에서 직접 headers 추가 가능
     
     * Postman으로 양식에 맞춰 POST 요청
       
       * body/form-data에 값 입력
         
         * headers에 Token 입력
           
           * Authorization: Token {your token} 형식에 맞춰 입력
     
     * 실패 이유는? 인증 방법이 입증되지 않음
     
     * my_api/settings.py 주석 해제

4. **Permission setting**
   
   * 권한 설정 방법 확인
     
     * DRF 공식 문서 > API Guide > Permissions 확인
   
   * 권한 세부 설정
     
     * 모든 요청에 대해 인증을 요구하는 설정
     
     * 모든 요청에 대해 인증이 없어도 허용하는 설정
   
   * 설정 위치 == 인증 방법을 설정한 곳과 동일
     
     * 우선 모든 요청에 대해 허용 설정
     
     * my_api/settings.py 주석 해제

## 4. DRF Auth with Vue

----

1. Vue Server 요청 정상 작동 여부 확인
   
   * 정상 작동하던 게시글 전체 조회 요청이 작동X
     
     * 401 status code 확인
     
     * 인증X 사용자 -> 조회 요청 불가능

2. SignUp Request
   
   * SignUp Page
   
   * SignUp Request
   
   * 토큰 관리
   
   * [참고] User 인증 정보를 localStorage에 저장해도 되는가?

3. Login Request
   
   * Login Page
     
     * signUp과 다른 점은 password1, password2가 password로 바뀐 것
     
     * 요청을 보내고 응답을 받은 Token을 state에 저장하는 것까지도 동일
       
       * mutations가 처리해야하는 업무 동일
       
       * SIGN_UP mutations를 SAVE_TOKEN mutations로 대체 가능

4. IsAuthenticated in Vue
   
   * 회원가입, 로그인 요청에 대한 처리 후

5. Request with Token



## 5. DRF-spectacular

---

1. swagger란?
   
   * 개발자가 REST 웹 서비스를 설계, 빌드, 문서화, 소비하는 일을 도와주는 오픈 소스 소프트웨어 프레임워크
     
     * 즉, API를 설계하고 문서화 하는데 도움을 주는 라이브러리

2. 다양한 DRF API
   
   * 스웨거(Swagger)를 생성할 수 있도록 도움을 주는 라이브러리
     
     * drf-spectacular
   
   * OpenAPI Specification이 3.0으로 업데이트 되며 새 버전을 지원하지 않는 라이브러리들이 있으니 사용시 유의

3. drf-spectacular
   
   * drf-spectacular
     
     * Open API 3.0을 지원하는 DRF API OpenAPI 생성기
     
     * 지속적인 업데이트와 관리로 최신 Django, DRF 버전 지원
   
   * 설치 : \$ pip install drf-spectacular
   
   * 등록
   
   * 기본 설정
   
   * URL 설정


