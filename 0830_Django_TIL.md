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
     
     * **프레임워크(Framework)**: 서비스 개발에 필요한 기능들을 **미리 구현**해서 모아 놓은 것
     * Frame(뼈대, 틀) + Work(일하다)
       * 일정한 뼈대, 틀을 가지고 일하다
       * 제공받은 도구들과 뼈대, 규약을 가지고 무언가를 만드는 일
       * 특정 프로그램을 개발하기 위한 여러 도구들과 규약을 제공하는 것
       * "소프트웨어 프레임워크"는 복잡한 문제를 해결하거나 서술하는데 사용되는 기본 개념 구조
     * 직접 개발할 필요 없이, 만들고자 하는 본질(로직)에 집중해 개발할 수 있음
     * 소프트웨어의 생산성과 품질을 높임
   
   * 여러가지 WebFramework
   
   * Django를 배워야하는 이유
     
     * python으로 작성된 프레임워크
       
       * python 언어의 강력함과 거대한 커뮤니티
     
     * 수많은 여러 유용한 기능들
     
     * 검증된 웹 프레임워크

2. Web 이해하기
   
   * **WWW (World Wide Web)**: 전 세계에 퍼져있는 거미줄 같은 연결망
   * 인터넷을 이용한다는 건, 전세계의 컴퓨터가 연결되어 있는 하나의 인프라를 이용하는 것

3. **클라이언트와 서버**
   
   * 클라이언트-서버 구조
     
     * 대부분의 웹 서비스는 **클라이언트-서버** 구조 기반
     
     * 클라이언트와 서버 역시 하나의 컴퓨터 
     
     * CLIENT --requests--> SERVER
     
     * CLIENT <--responses-- SERVER
   
   * **클라이언트**
     
     * 웹 사용자의 **인터넷에 연결된 장치** (ex. wi-fi에 연결된 컴퓨터 또는 모바일)
     
     * **웹 브라우저** (Chrome 또는 Firefox 등)
     
     * 서비스를 **요청하는 주체**
   
   * **서버**
     
     * 웹 페이지, 사이트 또는 앱을 저장하는 컴퓨터
     
     * 클라이언트가 웹 페이지에 접근하려고 할 때, 서버에서 클라이언트 컴퓨터로 웹 페이지 데이터를 응답해 사용자의 웹 브라우저에 표시됨
     
     * 요청에 대해 서비스를 **응답하는 주체**
   
   * 정리
     
     * 웹: 클라이언트 - 서버 구조로 이루어짐
     
     * Django는 서버를 구현하는 웹 프레임워크

4. **Web browser와 Web page**
   
   * **웹 브라우저란?**
     
     * 웹에서 **페이지**를 찾아서 **보여주고**, 사용자가 **하이퍼링크**를 통해 다른 페이지로 **이동할 수 있도록** 하는 프로그램
     
     * 웹 페이지 파일을 우리가 보는 화면으로 바꿔주는(**렌더링, rendering**) **프로그램**
     
     * 예시
   
   * **웹 페이지란?**
     
     * **웹에 있는 문서**: 우리가 보는 화면 각각 한 장 한 장이 웹 페이지
     
     * 웹 페이지 **종류**: **정적 웹 페이지, 동적 웹 페이지**
   
   * **정적 웹 페이지 (Static Web page)**
     
     * 있는 그대로를 제공하는 것(served as-is)
     
     * 우리가 지금까지 작성한 웹 페이지, **한 번 작성된 HTML 파일의 내용**이 **변하지 않고** 모든 사용자에게 **동일한 모습**으로 전달되는 것
       
       * == 서버에 미리 저장된 **HTML 파일 그대로** 전달된 웹 페이지
       
       * == 같은 상황에서 **모든 사용자에게 동일한 정보**를 표시
   
   * **동적 웹 페이지 (Dynamic Web page)**
     
     * 사용자의 요청에 따라 웹 페이지에 **추가적인 수정**(웹 페이지가 동작)이 되어 클라이언트에게 전달되는 웹페이지
     
     * 웹 페이지의 **내용을 바꿔주는 주체** == **서버**
       
       * 서버에서 동작하고 있는 프로그램이 웹 페이지를 변경해줌
       
       * 사용자의 요청을 받아서 적절한 응답을 만들어주는 프로그램을 쉽게 만들 수 있게 도와주는 프레임워크 -> Django
     
     * 다양한 서버 사이드 프로그래밍 언어(python, java, c++ 등) 사용 가능
     
     * 파일을 처리하고 데이터베이스와의 상호작용이 이루어짐

## 2. Django 구조 이해하기 (MTV Design Pattern)

-----

1. **Design Pattern**
   
   * **소프트웨어 디자인 패턴**
     
     * 소프트웨어도 자주 사용되는 구조와 해결책이 존재
     
     * 클라이언트-서버 구조도 소프트웨어 디자인 패턴 중 하나
     
     * 자주 사용되는 소프트웨어의 구조를 일반적으로 구조화를 해둔 것
   
   * **소프트웨어 디자인 패턴의 목적**
     
     * 공통적으로 발생하는 문제에 대해 재사용 가능한 해결책을 제시
   
   * **소프트웨어 디자인 패턴의 장점**
     
     * 디자인 패턴을 알고 있다면 서로 복잡한 커뮤니케이션이 매우 간단해짐

2. **Django's Design Pattern**
   
   * **Django에서의 디자인 패턴**
     
     * **MTV 패턴**
     
     * MVC(Model View Controller) 디자인 패턴을 기반으로 조금 변형된 패턴
   
   * **MVC 소프트웨어 디자인 패턴**
     
     * **Model - View - Controller**
     
     * 데이터 및 논리 제어를 구현하는데 널리 사용되는 소프트웨어 디자인 패턴
     
     * 하나의 큰 프로그램을 세가지 역할로 구분한 개발 방법론
     
     * **Model** : **데이터와 관련된 로직**을 관리
     
     * **View** : **레이아웃과 화면**을 처리
     
     * **Controller** : 명령을 **model과 view** 부분으로 연결
   
   * **MVC 소프트웨어 디자인 패턴의 목적**
     
     * 관심사 분리
     
     * 각 부분 **독립적 개발**, 수정할 부분만 건들이면 됨
       
       * == 개발 효율성 및 유지보수 쉬워짐
       
       * == 다수의 멤버로 개발하기 용이
   
   * **Django에서의 디자인 패턴**
     
     * MVC 패턴을 기반으로 한 MTV 패턴을 사용
       
       * 두 패턴 크게 다른 점 X, 일부 역할에 대해 부르는 이름이 다름
       
       | MVC        | MTV      |
       | ---------- | -------- |
       | Model      | Model    |
       | View       | Template |
       | Controller | View     |
   
   * **MTV 디자인 패턴**
     
     * **Model**
       
       * MVC 패턴에서 Model의 역할에 해당
       
       * **데이터와 관련된 로직** 관리
       
       * 응용프로그램의 **데이터 구조를 정의**하고 **데이터베이스의 기록 관리**
     
     * **Template**
       
       * **레이아웃과 화면**을 처리
       
       * 화면상의 **사용자 인터페이스 구조와 레이아웃**을 정의
       
       * MVC 패턴에서 View의 역할에 해당
     
     * **View**
       
       * Model & Template과 관련한 **로직 처리해서 응답 반환**
       
       * 클라이언트의 **요청에 대해 처리를 분기**하는 역할
       
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

1. **기본 설정**
   
   * Django 설치
     
     ```git
     pip install django==3.2.13
     ```
   
   * 패키지 목록 생성
     
     ```git
     pip freeze > requirements.txt
     ```
   
   * Django Project
     
     * 프로젝트 생성
       
       ```git
       django-admin startproject pjt_name .
       ```
     
     * 서버 실행
       
       ```git
       python manage.py runserver
       ```
   
   * **프로젝트 구조**
     
     * **\_\_init\_\_.py** : 파이썬에게 이 디렉토리를 **하나의 파이썬 패키지로 다루도록** 지시
       
       * 별도로 추가 코드 작성X
     
     * **asgi.py**
       
       * Asynchronous Server Gateway Interface
       
       * Django 애플리케이션이 **비동기식 웹 서버와 연결 및 소통**하는 것을 도움
       
       * 추후 배포 시에 사용하며 지금은 수정 X
     
     * **settings.py** : Django **프로젝트 설정을 관리**
     
     * **urls.py** : 사이트의 **url과 적절한 views의 연결**을 지정
     
     * **wsgi.py**
       
       * Web Server Gateway Interface
       
       * Django 애플리케이션이 **웹서버와 연결 및 소통**하는 것 도움
       
       * 추후 배포 시에 사용하며 지금은 수정 X
     
     * **manage.py**
       
       * Django 프로젝트와 다양한 방법으로 상호작용하는 **커맨드라인 유틸리티**
   
   * Django Application
     
     * 애플리케이션(앱) 생성
       
       ```git
       python manage.py startapp app_names
       ```
   
   * **애플리케이션 구조**
     
     * **admin.py** : 관리자용 페이지를 설정하는 곳
     
     * **apps.py** : 앱의 정보가 작성된 곳
       
       * 별도로 추가 코드 작성 X
     
     * **models.py** : 애플리케이션에서 사용하는 **Model을 정의**하는 곳
       
       - MTV패턴의 M에 해당
     
     * **tests.py** : 프로젝트의 **테스트 코드**를 작성하는 곳
     
     * **views.py** : **view 함수들이 정의** 되는 곳
       
       - MTV패턴의 V에 해당
   
   * **애플리케이션 등록**
     
     * 프로젝트에서 앱 사용 -> 반드시 INSTALLED_APPS 리스트에 반드시 추가
     
     * **INSTALLED_APPS** : Django installation에 **활성화 된 모든 앱** 지정하는 문자열 목록
   
   * **Project & Application**
     
     * Project
       
       * 앱의 집합
       
       * 여러 앱이 포함될 수 있음
       
       * 앱은 여러 프로젝트에 있을 수 있음
     
     * Application
       
       * **실제 요청을 처리하고 페이지를 보여주는 등**의 역할 담당
       
       * 일반적으로 앱은 **하나의 역할 및 기능 단위로 작성**하는 것 권장
   
   * **애플리케이션 주의사항**
     
     * 반드시 생성 후 등록: INSTALLED_APPS에 먼저 작성(등록)하고 생성하려면 앱이 생성되지 X

2. **요청과 응답**
   
   * 요청과 응답
     
     * URL -> VIEW -> TEMPLATE 순의 작성 순서로 코드를 작성해보고 데이터의 흐름 이해하기
     
     * **URLs**
       
       * urls.py 파일
       
       * from 앱이름 import views
       
       * path('경로명/', views.함수명)
     
     * **View**
       
       * HTTP 요청을 수신하고 HTTP 응답을 반환하는 함수 작성
       
       * Template에게 HTTP 응답 서식을 맡김
       
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
       
       * 템플릿 폴더 이름은 반드시 templates라고 지정해야 함
     
     * 코드 작성 순서: URL -> View -> Template
     
     * [참고] 추가 설정
       
       * <u>LANGUAGE_CODE</u>
         
         * 모든 사용자에게 제공되는 번역을 결정
         
         * 이 설정 적용되려면 USE_I18N이 활성화(True)되어 있어야 함
       
       * <u>TIME_ZONE</u>
         
         * 데이터베이스 연결의 시간대를 나타내는 문자열
         
         * USE_TZ가 True인 상태여야함, False인 상태로 이 값을 설정하는 것은 error 발생
       
       * USE_I18N: 번역 시스템을 활성화해야 하는지 여부 지정
       
       * USE_L10N: 데이터의 지역화된 형식을 기본적으로 활성화할지 여부
         
         * True일 경우, 현재 locale의 형식을 사용하여 숫자와 날짜 표시
       
       * USE_TZ: datetimes가 기본적으로 시간대를 인식하는지 여부를 지정
         
         * True일 경우 내부적으로 시간대 인식 날짜/시간을 사용

## 4. Django Template

----

1. **Django Template**
   
   * **Django Template**
     
     * **데이터 표현**을 제어하는 도구이자 표현에 관련된 로직
     
     * HTML 정적 부분과 동적 컨텐츠 삽입
     
     * Template System의 기본 목표 숙지
   
   * **Django Template System**
     
     * 데이터 표현을 제어하는 도구이자 표현에 관련된 로직을 담당
   
   * **Django Template Language (DTL)**
     
     * Django template에서 사용하는 built-in template system
     * 조건, 반복, 변수 치환, 필터 등의 기능 제공
       * python처럼 일부 프로그래밍 구조(if, for 등)를 사용할 수 있지만, 이것을 **python 코드로 실행되는 것이 아님**
       * Django 템플릿 시스템은 단순히 python이 HTML에 포함된 것이 아님
     * 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것임
   
   * **DTL Syntax**
     
     * Variable
     
     * Filters
     
     * Tags
     
     * Comments
   
   * **Variable: {{ variable }}**
     
     * 변수명: 영어, 숫자, 밑줄(\_)의 조합
       
       * 밑줄로 시작X
       
       * 공백, 구두점 문자X
     
     * **dot(.)** -> **변수 속성에 접근** 가능
     
     * render()의 세번째 인자로 {'key': value}와 같이 딕셔너리 형태 넘겨줌 -> key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨
   
   * **Filter : {{ variable | filter}}**
     
     * 표시할 변수를 수정할 때 사용
     
     * 60개의 built-in template filters를 제공
     
     * **chained가 가능**하며 일부 필터는 인자를 받기도 함
   
   * **Tags: {% tag %}**
     
     * 출력 텍스트, 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 **변수보다 복잡한 일들을 수행**
     
     * **일부 태그 -> 시작과 종료 태그 필요**
     
     * 약 24개의 built-in template tags 제공
   
   * **Comments**
     
     * **{# #}** : 한 줄 주석
     
     * **{% comment %} {% endcomment%}** : 여러 줄 주석
   
   * [실습] DTL Syntax

2. **Template inheritance**
   
   * **템플릿 상속**
     
     * 코드의 재사용성
     
     * 사이트의 모든 공통 요소를 포함하고, 하위 템플릿이 재정의(override)할 수 있는 블록을 정의하는 기본 'skeleton' 템플릿을 만들 수 있음
   
   * 템플릿 상속에 관련된 태그
     
     * **{% extends '' %}**
       
       * 자식(하위)템플릿이 **부모 템플릿을 확장한다는 것**을 알림
       
       * **반드시 템플릿 최상단에** 작성! (즉, **2개 이상 사용X**)
     
     * **{% block 'content' %}{% endblock 'content' %}**
       
       * 하위 템플릿에서 **재지정(overridden)** 할 수 있는 블록을 정의
       
       * 즉, 하위 템플릿이 채울 수 있는 공간
       
       * 가독성을 높이기 위해 선택적으로 endblock 태그에 이름 지정 가능
   
   * **추가 템플릿 경로 추가하기**
     
     * 앱 안의 템플릿 디렉토리가 아닌 프로젝트 최상단의 템플릿 디렉토리 안에 위치시키기
     
     * 기본 템플릿 경로 아닌 다른 경로 추가
       
       * 프로젝트의 **settings.py의 TEMPLATES** 안에 수정하기
         
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

1. **Sending and Retrieving form data**
   
   * 데이터를 보내고 가져오기
   
   * **Client & Server architecture**
     
     * 클라이언트 측에서 HTML form은 HTTP요청을 서버에 보내는 가장 편리한 방법
     
     * 이를 통해 사용자는 HTTP요청에서 전달할 정보를 제공할 수 있음

2. **Sending form data (Client)**
   
   * **HTML <form> element**
     
     * 데이터가 전송되는 방법 정의
     
     * 웹에서 사용자 정보를 입력하는 여러 방식(text, button, submit등)을 제공, **사용자로부터 할당된 데이터를 서버로 전송**하는 역할 담당
     
     * 데이터를 **어디(action)** 로 **어떤 방식(method)** 으로 보낼지
     
     * **핵심 속성**
       
       * action
       
       * method
   
   * **HTML form's attributes**
     
     * **action**: 입력 데이터가 전송될 URL을 지정
       
       * 데이터를 어디로 보낼 것인지 지정하는 것, 반드시 유효한 URL이어야 함
       
       * 이 속성 지정X -> 현재 form이 있는 페이지의 URL로 보내짐
     
     * **method**: 데이터를 어떻게 보낼 것인지 정의
       
       * 입력 데이터의 HTTP request methods를 지정
       
       * 2가지 방식: GET 방식(파라미터 노출), POST방식(비노출)
   
   * **HTML <input> element**
     
     * 사용자로부터 데이터를 입력 받기 위해 사용
     
     * type 속성에 따라 동작 방식 달라짐
       
       * 지정x -> 기본값: text
     
     * 핵심 속성 : name
     
     * **name**
       
       * form을 통해 데이터를 제출했을 때, name속성에 설정된 값을 서버로 전송하고, 서버는 **name 속성에 설정된 값을 통해** 사용자가 입력한 데이터 값에 **접근 가능**
       
       * 주요 용도 : GET/POST 방식으로 서버에 전달하는 파라미터(name은 key, value는 value)로 매핑하는 것
         
         * **GET방식**에서는 URL에서 **'?key=value&key=value/'** 형식으로 데이터 전달
   
   * **HTTP request methods**
     
     * **HTTP** : HTML 문서와 같은 **리소스(데이터, 자원)들을 가져올 수 있도록** 해주는 **프로토콜(규칙, 규약)**
     
     * 웹에서 이루어지는 모든 **데이터 교환의 기초**
     
     * 자원에 대한 행위(수행하고자 하는 동작)을 정의
     
     * 주어진 리소스(자원)에 수행하길 원하는 행동을 나타냄
     
     * HTTP Method 예시 : **GET, POST, PUT, DELETE**
   
   * **GET**
     
     * 서버로부터 **정보를 조회**하는 데 사용
       
       * 즉, 서버에서 리소스를 요청하기 위해 사용
     
     * **데이터를 가져올 때만** 사용해야 함
     
     * 데이터를 서버로 전송할 때 **Query String Parameters**를 통해 전송
       
       * 데이터는 **URL에 포함되어** 서버로 보내짐
     
     * GET 메서드 작성: 명시적 표현을 위해 대문자 사용 권장
   
   * **Query String Parameters**
     
     * 사용자가 입력 데이터를 전달하는 방법 중 하나, **url주소에 데이터를 파라미터를 통해 넘기는 것**
     
     * 이러한 문자열은 **앰퍼샌드(&)로 연결된 key=value 쌍**으로 구성, **기본URL과 ?로 구분**
     
     * **Query String**이라고도 함
     
     * 정해진 주소 이후에 물음표를 쓰는 것으로 Query String이 시작함을 알림
     
     * 'key=value'로 필요한 파라미터의 값을 적음
       
       * '='로 key와 value가 구분됨
     
     * 파라미터 여러개 -> &를 붙여 여러 개의 파라미터를 넘길 수 있음

3. **Retrieving the data (Server)**
   
   * 데이터 가져오기(검색하기)
   
   * 서버는 클라이언트로 받은 **key-value쌍의 목록과 같은 데이터를 받게 됨**
   
   * 이러한 목록에 접근하는 방법 -> 사용하는 특정 프레임워크에 따라 다름
   
   * catch 작성
   
   * action 작성
   
   * 데이터 가져오기
     
     * form이 보낸 데이터는 어디에 들어 있는 걸까?
     
     * URL에 포함되어 서버로 보내짐
     
     * 모든 요청 데이터는 **view 함수의 첫번째 인자 request에 들어있다.**
     
     * request 객체 살펴보기
     
     ![](C:\Users\3covl\AppData\Roaming\marktext\images\2022-09-10-20-56-35-image.png)
     
     *   에러를 강제로 발생시켜 살펴보기
       
       * raise
   
   * **Request and Response objects**
     
     * **요청과 응답 객체 흐름**
       
       * **페이지 요청**되면 -> Django는 요청에 대한 메타데이터를 포함하는 **HttpRequest object 생성**
       
       * 해당하는 적절한 **view 함수 로드**, **HttpRequest를 첫번째 인자로 전달**
       
       * view 함수는 **HttpResponse object를 반환**

## 6. Django URLs

-----

1. Django URLs

2. **Trailing URL Slashes**
   
   * URL 끝에 **/가 (Trailing slash) 없다면 자동으로 붙여주는 것이 기본 설정**
     
     * 모든 주소가 '/'로 끝나도록 구성되어있음
     
     * 그러나 모든 프레임워크가 이렇게 동작하는 것은 아님
   
   * foo.com/bar와 foo.com/bar/는 서로 다른 URL
     
     * 검색 엔진 로봇이나 웹 트래픽 분석 도구 -> 그 둘을 서로 다른 페이지로 봄
     
     * Django는 URL을 정규화하여 검색 엔진 로봇이 혼동하지 않게 해야 함
   
   * [참고] URL 정규화
     
     * 정규 URL(=오리지널로 평가되어야 할 URL)을 명시하는 것
     
     * 복수의 페이지에서 같은 콘텐츠가 존재하는 것을 방지하기 위함
     
     * Django에서는 trailing slash가 없는 요청에 대해 자동을 slash를 추가하여 통합된 하나의 콘텐츠로 볼 수 있도록 함

3. **Variable routing**
   
   * Variable routing의 필요성
     
     * 템플릿의 대부분 중복, 일부분만 변경되는 상황
   
   * **Variable routing**
     
     * **URL 주소를 변수로 사용하는 것**을 의미
     
     * **URL의 일부를 변수로 지정**하여 **view 함수의 인자로** 넘길 수 있음
     
     * 즉, **변수 값에 따라 하나의 path()에 여러 페이지를 연결** 시킬 수 있음
   
   * **Variable routing 작성**
     
     * **변수는 <>에 정의**하며, **view 함수의 인자로 할당**됨
     
     * 기본 타입은 string, 5가지 타입 명시 가능
       
       * str
         
         * '/'를 제외하고 비어있지 않은 모든 문자열
         
         * 작성하지 않을 경우 기본 값
       
       * int
         
         * 0 또는 양의 정수와 매치
       
       * slug
       
       * uuid
       
       * path
   
   * **View 함수 작성**
     
     * variable routing으로 할당된 변수를 인자로 받고 템플릿 변수로 사용할 수 있음
     
     * 주소 적을때 마지막에 /value
   
   * **[참고] Routing(라우팅)**
     
     * 어떤 네트워크 안에서 통신 데이터를 보낼 때 최적의 경로를 선택하는 과정

4. **App URL mapping**
   
   * 앱이 많아졌을 때 urls.py를 각 app에 매핑하는 방법 이해하기
   
   * **각 앱의 view 함수를 as를 통해 다른 이름으로 import** 가능
   
   * 각각의 앱 안에 urls.py를 만들고, 프로젝트 urls.py에서 각 앱의 urls.py 파일로 URL 매핑을 위탁
   
   * **각각의 app 폴더 안에 urls.py를 작성**
   
   * Including other URLconfs
     
     * urlpattern은 언제든지 다른 URLconf 모듈을 포함(include)할 수 있음
     
     * include되는 앱의 urls.py에 **urlpatterns가 작성되어 있지 않다면 에러 발생**
   
   * **include()**
     
     * 다른 URLconf(app1/urls.py)들을 참조할 수 있도록 돕는 함수
     
     * 함수 include()를 만나게 되면 URL의 그 시점까지 **일치하는 부분을 잘라내고**, 남은 문자열 부분을 **후속 처리**를 위해 **include된 URLconf로 전달**

5. **Naming URL patterns**
   
   * 필요성
     
     * "index/"의 문자열 주소를 "new-index/"로 바꿔야 할 때, 모든 곳을 찾아서 변경해야 하는 번거로움 발생
   
   * 링크에 URL 직접 작성 -> **path() 함수의 name 인자** 정의해서 사용
   
   * **DTL의 Tag 중 하나인 URL 태그**를 사용해서 path() 함수에 작성한 **name을 사용** 가능
   
   * 이를 통해 URL 설정에 정의된 특정한 경로들의 **의존성을 제거** 가능
   
   * URL에 이름을 지정하는 방법을 제공함으로써 view함수와 템플릿에서 특정 주소를 쉽게 참조할 수 있도록 도움
   
   * Built-in tag - "url": {% url '' %}
     
     * 주어진 **URL 패턴 이름 및 선택적 매개 변수**와 **일치하는 절대 경로 주소 반환**
     
     * 템플릿에 URL을 하드 코딩하지 않고도 **DRY 원칙을 위반하지 않**으면서 링크 출력하는 방법
   
   * **[참고] DRY 원칙**
     
     * Don't Repeat Yourself의 약어
     
     * 소스 코드에서 동일한 코드를 반복하지 말자
     
     * 동일한 코드 반복 -> 잠재적인 버그 위협 증가, 반복되는 코드 변경 시 모든 코드를 찾아서 수정해야 함
     
     * 이는 프로젝트 규모가 커질수록 애플리케이션의 유지 보수 비용이 커짐

## 7. 마무리

----

1. Django의 설계 철학 (Templates System)
   
   * 표현과 로직(view)을 분리
     
     * 템플릿 시스템은 표현을 제어하는 도구이자 표현에 관련된 로직일 뿐
     
     * 즉, 템플릿 시스템은 이러한 기본 목표를 넘어서는 기능을 지원하지 말아야 함
   
   * 중복을 배제
     
     * 대다수의 동적 웹사이트는 공통 header, footer, navbar 같은 사이트 공통 디자인을 갖음
     
     * Django 템플릿 시스템은 이러한 요소를 한 곳에 저장하기 쉽게하여 중복 코드를 없애야 함
     
     * 템플릿 상속의 기초가 되는 철학

2. Framework의 성격
   
   * 독선적(Opinionated)
     
     * 독선적인 프레임워크들은 어떤 특정 작업을 다루는 '올바른 방법'에 대한 분명한 의견(규약)을 가지고 있음
     
     * 대체로 특정 문제내에서 빠른 개발방법을 제시
     
     * 어떤 작업에 대한 올바른 방법 = 보통 잘 알려져 있고 문서화가 잘 되어있기 때문
     
     * 하지만, 주요 상황을 벗어난 문제 -> 그리 유연하지 못한 해결책을 제시할 수 있음
   
   * 관용적(Unopinionated)
     
     * 관용적인 프레임워크들 -> 구성요소를 한데 붙여서 해결 or 심지어 어떤 도구를 써야 한다는 '올바른 방법'에 대한 제약이 거의 X
     
     * 이는 개발자들이 특정 작업 완수를 위해 가장 적절한 도구들을 이용할 수 있는 자유도가 높음
     
     * but, 개발자 스스로가 그 도구들을 찾아야 한다는 수고 필요
   
   * 다소 독선적
     
     * 양쪽 모두에게 최선의 결과를 준다고 강조
   
   * 현대 개발에 있어서는 가장 중요한 것들 중 하나는 **'생산성'**
   
   * 프레임워크 -> 우리가 온전히 만들고자 하는 것에만 집중할 수 있게 도와주는 것
