## 0. Django

----

1. Django Intro

2. Django 구조 이해하기 (MTV Design Pattern)

3. Django Quick start

4. Django Template

5. Sending and Retrieving form data

6. Django URLs

7. 마무리

## 1. Django Intro

----

1. Django 시작하기
   
   * Framework 이해하기
     
     * 프레임워크(Framework): 서비스 개발에 필요한 기능들을 미리 구현해서 모아 놓은 것
   
   * 여러가지 WebFramework

2. Web 이해하기
   
   * WWW (World Wide Web)

3. 클라이언트와 서버
   
   * 클라이언트-서버 구조
     
     * 대부분의 웹 서브스는 클라이언트-서버 구조 기반
     
     * 클라이언트와 서버 역시 하나의 컴퓨터 
     
     * CLIENT --requests--> SERVER
     
     * CLIENT <--responses-- SERVER
   
   * 클라이언트
     
     * 웹 사용자의 인터넷에 연결된 장치 (ex. wi-fi에 연결된 컴퓨터 또는 모바일)
     
     * 웹 브라우저 (Chrome 또는 Firefox 등)
     
     * 서비스를 요청하는 주체
   
   * 서버
     
     * 웹 페이지, 사이트 또는 앱을 저장하는 컴퓨터
     
     * 클라이언트가 웹 페이지에 접근하려고 할 때, 서버에서 클라이언트 컴퓨터로 웹 페이지 데이터를 응답해 사용자의 웹 브라우저에 표시됨
     
     * 요청에 대해 서비스를 응답하는 주체
   
   * 정리
     
     * 웹: 클라이언트 - 서버 구조로 이루어짐
     
     * Django는 서버를 구현하는 웹 프레임워크

4. Web browser와 Web page
   
   * 웹 브라우저란?
     
     * 웹에서 페이지를 찾아서 보여주고, 사용자가 하이퍼링크를 통해 다른 페이지로 이동할 수 있도록 하는 프로그램
     
     * 웹 페이지 파일 -> 우리가 보는 화면으로 바꿔주는(렌더링, rendering) 프로그램
     
     * 예시
   
   * 웹 페이지란?
     
     * 웹에 있는 문서: 우리가 보는 화면 각각 한 장 한 장이 웹 페이지
     
     * 웹 페이지 종류: 정적 웹 페이지, 동적 웹 페이지
   
   * 정적 웹 페이지 (Static Web page)
     
     * 있는 그대로를 제공하는 것(served as-is)
     
     * 우리가 지금까지 작성한 웹 페이지, **한 번 작성된 HTML 파일의 내용**이 **변하지 않고** 모든 사용자에게 **동일한 모습**으로 전달되는 것
       
       * == 서버에 미리 저장된 HTML 파일 그대로 전달된 웹 페이지
       
       * == 같은 상황에서 모든 사용자에게 동일한 정보를 표시
   
   * 동적 웹 페이지 (Dynamic Web page)
     
     * 사용자의 요청에 따라 웹 페이지에 추가적인 수정(웹 페이지가 동작)이 되어 클라이언트에게 전달되는 웹페이지
     
     * 웹 페이지의 내용을 바꿔주는 주체 == 서버
       
       * 서버에서 동작하고 있는 프로그램이 웹 페이지를 변경해줌
       
       * 사용자의 요청을 받아서 적절한 응답을 만들어주는 프로그램을 쉽게 만들 수 있게 도와주는 프레임워크 -> Django
     
     * 다양한 서버 사이드 프로그래밍 언어(python, java, c++ 등) 사용 가능
     
     * 파일을 처리하고 데이터베이스와의 상호작용이 이루어짐

## 2. Django 구조 이해하기 (MTV Design Pattern)

-----

1. Design Pattern
   
   * 소프트웨어 디자인 패턴
   
   * 소프트웨어 디자인 패턴의 목적
   
   * 소프트웨어 디자인 패턴의 장점

2. Django's Design Pattern
   
   * Django에서의 디자인 패턴
     
     * MTV 패턴
     
     * MVC(Model View Controller) 디자인 패턴을 기반으로 조금 변형된 패턴
   
   * MVC 소프트웨어 디자인 패턴
     
     * Model - View - Controller
     
     * 데이터 및 논리 제어를 구현하는데 널리 사용되는 소프트웨어 디자인 패턴
     
     * 하나의 큰 프로그램을 세가지 역할로 구분한 개발 방법론
     
     * Model : 데이터와 관련된 로직을 관리
     
     * View : 레이아웃과 화면을 처리
     
     * Controller : 명령을 model과 view 부분으로 연결
   
   * MVC 소프트웨어 디자인 패턴의 목적
     
     * 관심사 분리
     
     * 각 부분 독립적 개발, 수정할 부분만 건들이면 됨
       
       * == 개발 효율성 및 유지보수 쉬워짐
       
       * == 다수의 멤버로 개발하기 용이
   
   * Django에서의 디자인 패턴
     
     * MVC 패턴을 기반으로 한 MTV 패턴을 사용
       
       * 두 패턴 크게 다른 점 X, 일부 역할에 대해 부르는 이름이 다름
       
       | MVC        | MTV      |
       | ---------- | -------- |
       | Model      | Model    |
       | View       | Template |
       | Controller | View     |
   
   * MTV 디자인 패턴
     
     * Model
       
       * MVC 패턴에서 Model의 역할에 해당
       
       * 데이터와 관련된 로직 관리
       
       * 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록 관리
     
     * Template
       
       * 레이아웃과 화면을 처리
       
       * 화면상의 사용자 인터페이스 구조와 레이아웃을 정의
       
       * MVC 패턴에서 View의 역할에 해당
     
     * View
       
       * Model & Template과 관련한 로직 처리해서 응답 반환
       
       * 클라이언트의 요청에 대해 처리를 분기하는 역할
       
       * 동작 예시
         
         * 데이터 필요 -> model에 접근해서 데이터 가져옴
         
         * 가져온 데이터를 template로 보내 화면 구성
         
         * 구성된 화면을 응답으로 만들어 클라이언트에게 반환
       
       * MVC 패턴에서 Controller의 역할에 해당
     
     * 정리
       
       * Django는 MTV 디자인 패턴을 가지고 있음
         
         * Model : 데이터 관련
         
         * Template : 화면 관련
         
         * View : Model&Template 중간 처리 및 응답 반환

## 3. Django Quick start

-----

1. 기본 설정
   
   * Django 설치
   
   * Django Project
   
   * 프로젝트 구조
     
     * \_\_init\_\_.py : 파이썬에게 이 디렉토리를 하나의 파이썬 패키지로 다루도록 지시
       
       * 별도로 추가 코드 작성X
     
     * asgi.py
       
       * Asynchronous Server Gateway Interface
       
       * Django 애플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 도움
       
       * 추후 배포 시에 사용하며 지금은 수정 X
     
     * settings.py : Django 프로젝트 설정을 관리
     
     * urls.py : 사이트의 url과 적절한 views의 연결을 지정
     
     * wsgi.py
       
       * Web Server Gateway Interface
       
       * Django 애플리케이션이 웹서버와 연결 및 소통하는 것 도움
       
       * 추후 배포 시에 사용하며 지금은 수정 X
     
     * manage.py
       
       * Django 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티
   
   * Django Application
   
   * 애플리케이션 구조
     
     * admin.py : 관리자용 페이지를 설정하는 곳
     
     * apps.py : 앱의 정보가 작성된 곳
       
       * 별도로 추가 코드 작성 X
     
     * models.py : 애플리케이션에서 사용하는 Model을 정의하는 곳
       
       * MTV패턴의 M에 해당
     
     * tests.py : 프로젝트의 테스트 코드를 작성하는 곳
     
     * views.py : view 함수들이 정의 되는 곳
       
       * MTV패턴의 V에 해당
   
   * 애플리케이션 등록
     
     * 프로젝트에서 앱 사용 -> 반드시 INSTALLED_APPS 리스트에 반드시 추가
     
     * INSTALLED_APPS : Django installation에 활성화 된 모든 앱 지정하는 문자열 목록
   
   * Project & Application
     
     * Project
       
       * 앱의 집합
       
       * 여러 앱이 포함될 수 있음
       
       * 앱은 여러 프로젝트에 있을 수 있음
     
     * Application
       
       * 실제 요청을 처리하고 페이지를 보여주는 등의 역할 담당
       
       * 일반적으로 앱은 하나의 역할 및 기능 단위로 작성하는 것 권장
   
   * 애플리케이션 주의사항

2. 요청과 응답
   
   * 요청과 응답
     
     * URL -> VIEW -> TEMPLATE 순의 작성 순서로 코드를 작성해보고 데이터의 흐름 이해하기
     
     * **URLs**
       
       * urls.py 파일
       
       * from 앱이름 import views
       
       * path('경로명/', views.함수명)
     
     * **View**
       
       * 앱이름/views.py 파일
         
         ```python
         def 함수명(request):
             return render(request, '이름.html')
         ```
       
       * **render(request, template_name, context)**
         
         * 주어진 템플릿(보여줄 화면)을 주어진 컨텍스트 데이터(화면에 포함될 데이터들)와 결합하고 렌더링된 텍스트와 함께 **HttpResponse(응답) 객체를 반환**하는 함수
         
         * **request** : 응답을 생성하는데 사용되는 요청 객체
         
         * **template_name** : 템플릿의 전체 이름 또는 템플릿 이름의 경로
         
         * **context** : 템플릿에서 사용할 데이터 (<u>딕셔너리 타입</u>으로 작성)
     
     * **Templates**
       
       * 실제 내용을 보여주는데 사용되는 파일
       
       * 파일의 구조나 레이아웃을 정의
       
       * 파일의 기본 경로
         
         * app 폴더 안의 templates 폴더
         
         * app_name/templates/
     
     * 코드 작성 순서: URL -> View -> Template
     
     * [참고] 추가 설정

## 4. Django Template

----

1. Django Template
   
   * Django Template
     
     * 데이터 표현을 제어하는 도구이자 표현에 관련된 로직
     
     * HTML 정적 부분과 동적 컨텐츠 삽입
     
     * Template System의 기본 목표 숙지
   
   * Django Template System
     
     * 데이터 표현을 제어하는 도구이자 표현에 관련된 로직을 담당
   
   * Django Template Language (DTL)
     
     * Django template에서 사용하는 built-in template system
   
   * DTL Syntax
     
     * Variable
     
     * Filters
     
     * Tags
     
     * Comments
   
   * Variable: {{ variable }}
     
     * 변수명: 영어, 숫자, 밑줄(\_)의 조합
       
       * 밑줄로 시작X
       
       * 공백, 구두점 문자X
     
     * dot(.) -> 변수 속성에 접근 가능
     
     * render()의 세번째 인자로 {'key': value}와 같이 딕셔너리 형태 넘겨줌 -> key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨
   
   * Filter : {{ variable | filter}}
     
     * 표시할 변수를 수정할 때 사용
     
     * 60개의 built-in template filters를 제공
     
     * chained가 가능하며 일부 필터는 인자를 받기도 함
   
   * Tags: {% tag %}
     
     * 출력 텍스트, 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행
     
     * 일부 태그 -> 시작과 종료 태그 필요
     
     * 약 24개의 built-in template tags 제공
   
   * Comments
     
     * {# #} : 한 줄 주석
     
     * {% comment %} {% endcomment%} : 여러 줄 주석

2. Template inheritance
   
   * 템플릿 상속
     
     * 코드의 재사용성
     
     * 사이트의 모든 공통 요소를 포함하고, 하위 템플릿이 재정의(override)할 수 있는 블록을 정의하는 기본 'skeleton' 템플릿을 만들 수 있음
   
   * 템플릿 상속에 관련된 태그
     
     * {% extends '' %}
       
       * 자식(하위)템플릿이 부모 템플릿을 확장한다는 것을 알림
       
       * 반드시 템플릿 최상단에 작성! (즉, 2개 이상 사용X)
     
     * {% block content %}{% endblock content %}
       
       * 하위 템플릿에서 재지정(overridden)할 수 있는 블록을 정의
       
       * 즉, 하위 템플릿이 채울 수 있는 공간
       
       * 가독성을 높이기 위해 선택적으로 endblock 태그에 이름 지정 가능
   
   * 추가 템플릿 경로 추가하기
     
     * 앱 안의 템플릿 디렉토리가 아닌 프로젝트 최상단의 템플릿 디렉토리 안에 위치시키기
     
     * 기본 템플릿 경로 아닌 다른 경로 추가
       
       * 프로젝트의 settings.py의 TEMPLATES 안에 수정하기
         
         ```python
         TEMPLATES = [
             {
             #...생략...
             'DIRS' : [BASE_DIR / 'templates'],
         }
         ]
         ```
       
       * 프로젝트 폴더, 앱 폴더와 동일한 위치에 templates 폴더 만들고 html 파일 추가
       
       * [참고] BASE_DIR



## 5. Sending and Retrieving form data

-----

1. Sending and Retrieving form data
   
   * 데이터를 보내고 가져오기
   
   * Client & Server architecture
     
     * 클라이언트 측에서 HTML form은 HTTP요청을 서버에 보내는 가장 편리한 방법
     
     * 이를 통해 사용자는 HTTP요청에서 전달할 정보를 제공할 수 있음

2. Sending form data (Client)
   
   * HTML <form> element
     
     * 데이터가 전송되는 방법 정의
     
     * 웹에서 사용자 정보를 입력하는 여러 방식(text, button, submit등)을 제공, 사용자로부터 할당된 데이터를 서버로 전송하는 역할 담당
     
     * 데이터를 어디(action)로 어떤 방식(method)으로 보낼지
     
     * 핵심 속성
       
       * action
       
       * method
   
   * HTML form's attributes
     
     * action
       
       * 입력 데이터가 전송될 URL을 지정
       
       * 데이터를 어디로 보낼 것인지 지정하는 것, 반드시 유효한 URL이어야 함
       
       * 이 속성 지정X -> 현재 form이 있는 페이지의 URL로 보내짐
     
     * method
       
       * 데이터를 어떻게 보낼 것인지 정의
       
       * 입력 데이터의 HTTP request methods를 지정
       
       * 2가지 방식: GET 방식(파라미터 노출), POST방식(비노출)
   
   * HTML <input> element
     
     * 사용자로부터 데이터를 입력 받기 위해 사용
     
     * type 속성에 따라 동작 방식 달라짐
       
       * 지정x -> 기본값: text
     
     * 핵심 속성 : name
     
     * name
       
       * form을 통해 데이터를 제출했을 때, name속성에 설정된 값을 서버로 전송하고, 서버는 name 속성에 설정된 값을 통해 사용자가 입력한 데이터 값에 접근 가능
       
       * 주요 용도 : GET/POST 방식으로 서버에 전달하는 파라미터(name은 key, value는 value)로 매핑하는 것
         
         * GET방식에서는 URL에서 '?key=value&key=value/' 형식으로 데이터 전달
   
   * HTTP request methods
     
     * HTTP : HTML 문서와 같은 리소스(데이터, 자원)들을 가져올 수 있도록 해주는 프로토콜(규칙, 규약)
     
     * 웹에서 이루어지는 모든 데이터 교환의 기초
     
     * 자원에 대한 행위(수행하고자 하는 동작)을 정의
     
     * 주어진 리소스(자원)에 수행하길 원하는 행동을 나타냄
     
     * HTTP Method 예시 : GET, POST, PUT, DELETE
   
   * GET
     
     * 서버로부터 정보를 조회하는 데 사용
       
       * 즉, 서버에서 리소스를 요청하기 위해 사용
     
     * 데이터를 가져올 때만 사용해야 함
     
     * 데이터를 서버로 전송할 때 Query String Parameters를 통해 전송
       
       * 데이터는 URL에 포함되어 서버로 보내짐
   
   * Query String Parameters
     
     * 사용자가 입력 데이터를 전달하는 방법 중 하나, url주소에 데이터를 파라미터를 통해 넘기는 것
     
     * 이러한 문자열은 앰퍼샌드(&)로 연결된 key=value 쌍으로 구성, 기본URL과 ?로 구분
     
     * Query String이라고도 함
     
     * 정해진 주소 이후에 물음표를 쓰는 것으로 Query String이 시작함을 알림
     
     * 'key=value'로 필요한 파라미터의 값을 적음
       
       * '='로 key와 value가 구분됨
     
     * 파라미터 여러개 -> &를 붙여 여러 개의 파라미터를 넘길 수 있음

3. Retrieving the data (Server)
   
   * 데이터 가져오기(검색하기)
   
   * 서버는 클라이언트로 받은 key-value쌍의 목록과 같은 데이터를 받게 됨
   
   * 이러한 목록에 접근하는 방법 -> 사용하는 특정 프레임워크에 따라 다름
   
   * catch 작성
   
   * action 작성
   
   * 데이터 가져오기
     
     * form이 보낸 데이터는 어디에 들어 있는 걸까?
     
     * URL에 포함되어 서버로 보내짐
     
     * 모든 요청 데이터는 view 함수의 첫번째 인자 request에 들어있다.
     
     * request 객체 살펴보기
   
   * Request and Response objects
     
     * 요청과 응답 객체 흐름
       
       * 페이지 요청되면 -> Django는 요청에 대한 메타데이터를 포함하는 HttpRequest object 생성
       
       * 해당하는 적절한 view 함수 로드, HttpRequest를 첫번째 인자로 전달
       
       * view 함수는 HttpResponse object를 반환



## 6. Django URLs

-----

1. Django URLs

2. Trailing URL Slashes
   
   * URL 끝에 /가 (Trailing slash) 없다면 자동으로 붙여주는 것이 기본 설정
     
     * 모든 주소가 '/'로 끝나도록 구성되어있음
     
     * 그러나 모든 프레임워크가 이렇게 동작하는 것은 아님
   
   * [참고] URL 정규화

3. Variable routing
   
   * Variable routing의 필요성
     
     * 템플릿의 대부분 중복, 일부분만 변경되는 상황
   
   * Variable routing
     
     * URL 주소를 변수로 사용하는 것을 의미
     
     * URL의 일부를 변수로 지정하여 view 함수의 인자로 넘길 수 있음
     
     * 즉, 변수 값에 따라 하나의 path()에 여러 페이지를 연결 시킬 수 있음
   
   * Variable routing 작성
     
     * 변수는 <>에 정의하며, view 함수의 인자로 할당됨
     
     * 기본 타입은 str, 5가지 타입 명시 가능
   
   * View 함수 작성
     
     * variable routing으로 할당된 변수를 인자로 받고 템플릿 변수로 사용할 수 있음
     
     * 주소 적을때 마지막에 /value
   
   * [참고] Routing(라우팅)

4. App URL mapping
   
   * 앱이 많아졌을 때 urls.py를 각 app에 매핑하는 방법 이해하기
   
   * include()
     
     * 다른 URLconf(app1/urls.py)들을 참조할 수 있도록 돕는 함수
     
     * 함수 include()를 만나게 되면 URL의 그 시점까지 일치하는 부분을 잘라내고, 남은 문자열 부분을 후속 처리를 위해 include된 URLconf로 전달

5. Naming URL patterns
   
   * 필요성
   
   * 링크에 URL 직접 작성 -> path() 함수의 name 인자 정의해서 사용
   
   * DTL의 Tag 중 하나인 URL 태그를 사용해서 path() 함수에 작성한 name을 사용 가능
   
   * [참고] DRY 원칙





## 7. 마무리

----

1. Django의 설계 철학 (Templates System)

2. Framework의 성격
