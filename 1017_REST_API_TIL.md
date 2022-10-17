## 0. 목차

---

1. REST API

2. Response JSON

3. Django REST framework - Single Model

4. Django REST framework - N:1 Relation

## 1. REST API

----

0. 개요
   
   * HTTP 기본 개념 학습

1. HTTP
   
   * HyperText Transfer Protocol
   
   * HTML 문서와 같은 리소스(resource, 자원)들을 가져올 수 있도록 하는 프로토콜(규칙, 약속)
   
   * 웹 상에서 컨텐츠를 전송하기 위한 약속
   
   * 웹에서 이루어지는 모든 데이터 교환의 기초가 됨
   
   * 클라이언트-서버 프로토콜 이라고도 부름
   
   * 클라이언트와 서버는 다음과 같은 개별적은 메시지 교환에 의해 통신
     
     * 요청(request): 클라이언트에 의해 전송되는 메시지
     
     * 응답(response): 서버에서 응답으로 전송되는 메시지
   
   * **HTTP 특징**
     
     * **Stateless (무상태)**
       
       * 동일한 연결(connection)에서 연속적으로 수행되는 두 요청 사이에 링크가 없음
       
       * 즉, 응답을 마치고 연결을 끊는 순간 -> 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음
       
       * 특정 페이지와 일관되게 상호작용 하려는 사용자에게 문제가 될 수 있다. -> 쿠키와 세션을 사용해 서버 상태를 요청과 연결하도록 함
   
   * **HTTP Request Methods**
     
     * 리소스에 대한 행위(수행하고자 하는 동작)를 정의
     
     * 즉, 리소스에 대해 수행할 원하는 작업을 나타내는 메서드 모음을 정의
     
     * HTTP verbs 라고도 함
     
     * HTTP Method 예시: GET, POST, PUT, DELETE
   
   * **[참고] 리소스 (resource)**
     
     * HTTP 요청의 대상을 리소스라고 함
   
   * **대표 HTTP REquest Methods**
     
     * **GET**: 서버에 리소스의 표현을 요청
       
       * GET을 사용하는 요청 -> 데이터만 검색해야 함
     
     * **POST**: 데이터를 지정된 리소스에 **제출**
       
       * 서버의 상태를 변경
     
     * **PUT**: 요청한 주소의 리소스를 **수정**
     
     * **DELETE**: 지정된 리소스를 **삭제**
   
   * **HTTP response status codes**
     
     * 특정 HTTP 요청이 성공적으로 완료되었는지 여부
     
     * Informational responses (100-199)
     
     * Successful responses (200-299)
     
     * Redirection messages (300-399)
     
     * Client error responses (400-499)
     
     * Server error responses (500-599)

2. **Identifying resources on the Web**
   
   * **웹에서의 리소스 식별**
     
     * HTTP 요청의 대상 = 리소스(resource, 자원)
     
     * 리소스 -> 문서, 사진 또는 기타 어떤 것이든 될 수 있음
     
     * 각 리소스는 식별을 위해 **URI**로 식별됨

3. **URI**
   
   * URI = Uniform Resource Identifier (통합 자원 식별자)
   
   * 인터넷에서 하나의 리소스를 가리키는 문자열
   
   * 가장 일반적인 URI -> 웹 주소로 알려진 URL
   
   * 특정 이름공간에서 이름으로 리소스를 식별하는 URI => **URN**
   
   * **URL**
     
     * **Uniform Resource Locator (통합 자원 위치)**
     
     * 웹에서 주어진 리소스의 주소
     
     * 네트워크 상에 리소스가 어디 있는지(주소)를 알려주기 위한 약속
       
       * 이러한 리소스는 HTML, CSS, 이미지 등이 될 수 있음
     
     * 여러 부분으로 구성되며 일부는 필수이고, 나머지는 선택사항
   
   * **URL 구조**
     
     * **Scheme (or protocol)**
       
       * 브라우저가 리소스를 요청하는데 사용해야하는 프로토콜
       
       * URL의 첫 부분은 브라우저가 어떤 규약을 사용하는지를 나타냄
       
       * 기본적으로 웹은 HTTP(S)를 요구, 메일을 열기위한 mailto:, 파일을 전송하기 위한 ftp: 등 다른 프로토콜도 존재
     
     * **Authority**
       
       * Scheme 다음은 문자 패턴 ://으로 구분된 Authority(권한)이 작성됨
       
       * domain과 port를 모두 포함하며 둘은 : (콜론)으로 구분됨
       
       * Domain Name
         
         * 요청중인 웹 서버를 나타냄
         
         * 직접 IP 주소를 사용하는 것도 가능 but, 외우기 어렵기 때문에 주로 Domain Name으로 사용
       
       * **Port**
         
         * 웹 서버의 리소스에 접근하는데 사용되는 기술적인 문(Gate)
         
         * HTTP 프로토콜의 표준 포트는 다음과 같고 **생략 가능** (나머지는 생략 불가능)
           
           * HTTP - 80
           
           * HTTPS - 443
         
         * Django의 경우 8000(80+00)이 기본 포트로 설정되어 있음
     
     * **Path**
       
       * 웹 서버의 리소스 경로
       
       * 초기 -> 실제 파일이 위치한 물리적 위치, 오늘날 -> 실제 위치가 아닌 **추상화된 형태의 구조 표현**
     
     * **Parameters**
       
       * 웹 서버에 제공하는 <u>추가적인 데이터</u>
       
       * 파라미터는 **'&'** 기호로 구분되는 **key-value 쌍 목록**
       
       * 서버는 리소스를 응답하기 전에 이러한 파라미터를 사용하여 추가 작업을 수행할 수 있음
     
     * **Anchor**
       
       * 리소스의 다른 부분에 대한 앵커
       
       * 리소스 내부 일종의 **"북마크"** 를 나타내며 브라우저에 해당 북마크 지점에 있는 콘텐츠를 표시
         
         * ex) HTML 문서에서 브라우저는 앵커가 정의한 지점으로 자동 스크롤
       
       * fragment identifier(부분 식별자)라고 부르는 **'#'** 이후 부분 -> **서버에 전송X**
         
         * 브라우저에게 해당 지점으로 이동할 수 있도록
   
   * **[참고] Anchor (앵커)**
     
     * 하이퍼링크와 비슷한 기능을 하는 인터넷상의 다른 문서와 연결된 문자 혹은 그림
   
   * **[참고] URN**
     
     * URL과 달리 자원의 위치에 영향X

4. **REST API**
   
   * **API**
     
     * **Application Programming Interface**
     
     * 애플리케이션과 프로그래밍으로 소통하는 방법
       
       * 개발자가 복잡한 기능을 보다 쉽게 만들 수 있도록 프로그래밍 언어로 제공되는 구성
     
     * API를 제공하는 애플리케이션과 다른 소프트웨어 및 하드웨어 등의 것들 사이의 간단한 계약(인터페이스)이라고 볼 수 있음
     
     * API는 복잡한 코드를 추상화하여 대신 사용할 수 있는 몇가지 더 쉬운 구문을 제공
   
   * **Web API**
     
     * 웹 서버 또는 웹 브라우저를 위한 API
     
     * 직접 개발하기보다 여러 Open API를 활용하는 추세
     
     * 대표적인 Third Party Open API 서비스 목록
     
     * API는 다양한 타입의 데이터를 응답
       
       * HTML, XML, JSON 등
   
   * **REST**
     
     * **Representational State Transfer**
     
     * API Server를 개발하기 위한 일종의 소프트웨어 설계 방법론
     
     * 소프트웨어 아키텍쳐 디자인 제약 모음
     
     * REST 원리를 따르는 시스템을 **RESTful** 하다고 부름
     
     * REST의 기본 아이디어는 리소스 즉 자원
       
       * 자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 방법을 서술
   
   * **REST에서 자원을 정의하고 주소를 지정하는 방법**
     
     * 자원의 식별 : URI
     
     * 자원의 행위 : HTTP Method
     
     * 자원의 표현
       
       * 자원과 행위를 통해 궁극적으로 표현되는 (추상화된) 결과물
       
       * JSON으로 표현된 데이터를 제공
   
   * **JSON**
     
     * JSON is a lightweight data-interchange format
     
     * JavaScript의 표기법을 따른 단순 문자열
     
     * 파이썬의 dictionary, 자바스크립트의 object처럼 C계열의 언어가 갖고 있는 자료구조로 쉽게 변환할 수 있는 key-value 형태의 구조를 갖고 있음
     
     * 사람이 읽고 쓰기 쉽고 기계가 파싱(해석 & 분석)하고 만들어내기 쉽기 때문에 현재 API에서 가장 많이 사용하는 데이터 타입

## 2. Response JSON

---

0. 개요
   
   * JSON 형태로의 서버 응답 변화
   
   * 다양한 방법의 JSON 응답
   
   * 서버가 응답하는 것
     
     * 지금까지 Django로 작성한 서버는 사용자에게 페이지(html)만 응답하고 있었음
     
     * 하지만 사실 서버가 응답할 수 있는 것은 페이지 뿐만 아니라 다양한 데이터 타입을 응답할 수 있음
     
     * JSON 데이터를 응답하는 서버로의 변환
     
     * 그렇다면 사용자에게 보여질 화면은 누가 구성?
     
     * JSON 데이터를 받아 화면을 구성하여 사용자에게 보여주는 것 -> Front-end Framework가 담당할 예정
     
     * Front-end Framework는 Vue.js를 사용
     
     * Django는 더이상 Template 부분에 대한 역할을 담당하지 X -> Front-end와 Back-end가 분리되어 구성되게 됨

1. **Response**
   
   * 다양한 방법으로 JSON 데이터 응답해보기
     
     * **HTML 응답**
     
     * **JsonResponser()** 를 사용한 JSON 응답
     
     * **Django Serializer**를 사용한 JSON 응답
     
     * **Django REST framework**를 사용한 JSON 응답
   
   * **HTML 응답**
   
   * [참고] 'Content-Type' entity header
   
   * **JsonResponser()를 사용한 JSON 응답**
     
     * Django가 기본적으로 제공하는 JsonResponse 객체를 활용하여 Python 데이터 타입을 손쉽게 JSON으로 변환하여 응답 가능
     
     * **JsonResponser()**
       
       * JSON-encoded response를 만드는 클래스
       
       * safe
   
   * **Django Serializer를 사용한 JSON 응답**
     
     * **HttpResponse()** 를 활용
     
     * JSON의 필드를 작성하지 않아도 됨
   
   * **Serialization**
     
     * 데이터 구조나 객체 상태를 동일 혹은 다른 컴퓨터 환경에 저장, <u>나중에 재구성할 수 있는 포맷으로 변환하는 과정</u>
       
       * 나중에 다시 쉽게 사용할 수 있는 포맷으로 변환하는 과정
     
     * 변환 포맷: json, xml, yaml이 있으며 json이 가장 보편적
     
     * Django의 **serialize()** 는 Queryset 및 Model Instance와 같은 복잡한 데이터를 JSON, XML 등의 유형으로 쉽게 변환할 수 있는 <u>Python 데이터 타입</u>으로 만들어 줌
   
   * **Django REST framework**를 사용한 JSON 응답
     
     * **Django REST framework (DRF)**
       
       * Django에서 Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리
       
       * Web API 구축을 위한 강력한 toolkit을 제공
       
       * REST framework를 작성하기 위한 여러 기능을 제공
       
       * DFR의 serializer는 Django의 Form 및 ModelForm 클래스와 매우 유사하게 작동

## 3. Django REST framework - Single Model

---

1. **ModelSerializer**
   
   * articles/serializers.py 생성
   
   * ModelSerializer 작성
   
   * ModelSerializer
     
     * ModelSerializer 클래스는 모델 필드에 해당하는 필드가 있는 Serializer 클래스를 자동으로 만들 수 있는 shortcut을 제공
       
       * Model 정보에 맞춰 자동으로 필드를 생성
       
       * serializer에 대한 유효성 검사기를 자동으로 생성
       
       * .create() 및 .update()의 간단한 기본 구현이 포함됨
   
   * Serializer 연습하기
     
     * shell_plus 실행 및 ArticleListSerializer import
   
   * ModelSerializer의 'many' option
     
     * QuerySet 또는 객체 목록을 serialize 하려면 many=True를 작성해야함

2. **Build RESTful API - Article**
   
   * URL과 HTTP requests methods 설계
   
   * **GET - List**
     
     * 게시글 데이터 목록 조회하기
     
     * DRF에서 api_view 데코레이터 작성은 필수
   
   * 'api_view' decorator
     
     * DRF view 함수가 응답해야하는
   
   * **GET - Detail**
     
     * 단일 게시글 데이터 조회하기
     
     * 각 데이터의 상세 정보를 제공하는 ArticleSerializer 정의
   
   * **POST**
     
     * 게시글 데이터 생성하기
     
     * 요청에 대한 데이터 생성이 성공 -> 201 Created 상태 코드 응답
     
     * 실패 -> 400 Bad request를 응답
   
   * Raising an exception on invalid data
     
     * 유효하지 않은 데이터에 대해 예외 발생시키기
     
     * is_valid()는 유효성 검사 오류가 있는 경우 ValidationError 예외를 발생시키는 선택적 raise_exception 인자를 사용할 수 있음
     
     * DRF에서 제공하는 기본 예외 처리기에 의해 자동으로 처리되며 기본적으로 HTTP 400 응답을 반환
   
   * **DELETE**
     
     * 게시글 데이터 삭제하기
     
     * 요청에 대한 데이터 삭제가 성공 -> 204 No Content 상태 코드 응답
   
   * **PUT**
     
     * 게시글 데이터 수정하기
     
     * 요청에 대한 데이터 수정 성공 -> 200 OK 상태 코드 응답

## 4. Django REST framework - N:1 Relation

----

0. 개요
   
   * N:1 관계에서

1. 사전 준비

2. GET - List

3. GET - Detail

4. POST
   
   * Passing Additional attributes to .save()
     
     * save() 메서드는 특정 Serializer 인스턴스를 저장하는 과정에서 추가적인 데이터를 받을 수 있음
     
     * CommentSerializer를 통해 Serialize되는 과정에서 Parameter로 넘어온 article_pk에 해당하는 article 객체를 추가적인 데이터를 넘겨 저장
   
   * **읽기 전용 필드 설정**
     
     * **read_only_fields**를 사용해 외래키 필드를 '읽기 전용 필드'로 설정
     
     * 읽기 전용 필드는 데이터를 전송하는 시점에 **해당 필드를 유효성 검사에서 제외**시키고 **데이터 조회시에는 출력**하도록 함

5. DELETE & PUT

6. **N:1 - 역참조 데이터 조회**
   
   * 특정 게시글에 작성된 댓글 목록 출력하기 -> 기존 필드 override
     
     * Nested relationships
       
       * 모델 관계 상으로 참조된 대상은 참조하는 대상의 표현에 포함되거나 중첩(nested)될 수 있음
       
       * 이러한 중첩된 관계는 serializers를 필드로 사용하여 표현 가능
       
       * 두 클래스의 상/하 위치를 변경해야 함
   
   * 특정 게시글에 작성된 댓글의 개수 출력하기 -> 새로운 필드 추가
     
     * source
       
       * serializers field's argument
       
       * 필드를 채우는데 사용할 속성의 이름
       
       * 점 표기법(dotted notation)을 사용하여 속성 탐색 가능
   
   * [주의] 읽기 전용 필드 지정 이슈
     
     * 특정 필드를 override 혹은 추가한 경우 read_only_fields 가 동작X

7. Django shortcuts functions
   
   * django.shortcuts 패키지는 개발에 도움이 될 수 있는 여러 함수와 클래스를 제공
   
   * 제공되는 shortcuts 목록
     
     * render(), redirect(), get_object_or_404(), get_list_or_404()
   
   * get_object_or_404()
     
     * 모델 manager objects에서 get()을 호출, 해당 객체가 없을 땐 기존 DoesNotExist 예외 대신 Http404를 raise함
   
   * get_list_or_404()
     
     * 모델 manager objects에서 filter()의 결과를 반환하고, 해당 객체 목록이 없을 땐 Http404를 raise함
   
   * 왜 사용해야 할까?
     
     * 클라이언트 입장에서 "서버에 오류가 발생하여 요청을 수행할 수 없다(500)" -> 원인이 정확하지 X
     
     * 서버가 적절한 예외 처리를 하고 클라이언트에게 올바른 에러를 전달하는 것 또한 중요한 요소
