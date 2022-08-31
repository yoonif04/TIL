## 0. Django

----

1. Namespace

2. Django Model

3. Queryset API

4. CRUD with view functions

5. Admin site

## 1. Namespace

----

1. Namespace
   
   * 개요
     
     * 개체를 구분할 수 있는 범위를 나타내는 namespace(이름 공간)에 대한 이해
   
   * Namespace의 필요성
   
   * 2가지 문제 발생

2. URL Namespace
   
   * 개요
     
     * URL namespace를 사용하면 서로 다른 앱에서 동일한 URL 이름을 사용하는 경우에도 이름이 지정된 URL을 고유하게 사용할 수 있음
     
     * app_name 속성을 작성해 URL namespace를 설정
   
   * URL tag의 변화: {% url 'app_name:url_name' %}
   
   * URL 참조

3. Template namespace
   
   * 개요
     
     * Django는 기본적으로 app_name/templates/ 경로에 있는 templates 파일들만 찾을 수 있으며, setting.py의 INSTALLED_APPS에 작성한 app 순서로 template을 검색 후 렌더링 함
   
   * 디렉토리 생성을 통해 물리적인 이름공간 구분
     
     * Django templates의 기본 경로에 app과 같은 이름의 폴더를 생성해 폴더 구조를 app_name/templates/app_name/ 형태로 변경
     
     * 기본 경로 자체를 변경할 수는 없기 때문에 물리적으로 이름 공간을 만드는 것
   
   * 반드시 Template namespace를 고려해야 할까?
     
     * 단일 앱으로만 이루어진 프로젝트 -> 상관X
     
     * 여러 앱이 되었을 때에도 템플릿 파일 이름이 겹치지 않게 하면 됨. but, 앱이 많아지면 대부분은 같은 이름의 템플릿 파일이 존재

## 2. Django Model

----

1. Django Model
   
   * 개요
     
     * Model의 핵심 개념과 ORM을 통한 데이터베이스 조작 이해
     
     * Django는 웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 추상적인 계층(모델)을 제공

2. Database
   
   * Database
     
     * 체계화된 데이터의 모임
     
     * 검색 및 구조화 같은 작업을 보다 쉽게 하기 위해 조직화된 데이터를 수집하는 저장 시스템
   
   * Database 기본 구조
     
     * 스키마(Schema)
     
     * 테이블(Table)
   
   * 스키마(Schema)
     
     * 뼈대(Structure)
     
     * 데이터베이스에서 자료의 구조, 표현 방법, 관계 등을 정의한 구조
   
   * 테이블(Table)
     
     * 필드와 레코드를 사용해 조직된 데이터 요소들의 집합
     
     * 관계(Relation)라고도 부름
     
     * 필드(field): 속성, 컬럼(Column)
       
       * 각 필드에는 고유한 데이터 형식이 지정됨
       
       * INT, TEXT 등
     
     * 레코드(record): 튜플, 행(Row)
       
       * 테이블의 데이터는 레코드에 저장됨
   
   * PK (Primary Key)
     
     * 기본 키
     
     * 각 레코드의 고유한 값 (식별자로 사용)
     
     * 기술적으로 다른 항목과 절대로 중복될 수 없는 단일 값(unique)
     
     * 데이터베이스 관리 및 테이블 간 관계 설정 시 주요하게 활용 됨
   
   * 쿼리 (Query)
     
     * 데이터를 조회하기 위한 명령어
     
     * 조건에 맞는 데이터를 추출하거나 조작하는 명령어 (주로 테이블형 자료구조에서)
     
     * Query를 날린다 = 데이터베이스를 조작한다.

3. Model
   
   * 개요
     
     * Django는 Model을 통해 데이터에 접근하고 조작
     
     * 사용하는 데이터들의 필수적인 필드들과 동작들을 포함
     
     * 저장된 데이터베이스의 구조 (layout)
     
     * 일반적으로 각각의 모델은 하나의 데이터베이스 테이블에 매핑(mapping)
       
       * 모델 클래스 1개 == 데이터베이스 테이블 1개
   
   * [참고] 매핑
   
   * Model 작성하기
     
     * model.py 작성
       
       * 모델 클래스를 작성하는 것은 데이터베이스 테이블의 스키마를 정의하는 것
       
       * 모델 클래스 == 테이블 스키마
       
       * id 컬럼은 테이블 생성시 Django가 자동 생성
   
   * Model 이해하기
     
     * 각 모델은 django.models.Model 클래스의 서브 클래스
       
       * 즉, 각 모델은 django.db.models 모듈의 Model 클래스를 상속받아 구성됨
       
       * 클래스 상속 기반 형태의 Django 프레임워크 개발
     
     * models 모듈을 통해 어떠한 타입의 DB 필드(컬럼)을 정의할 것인지 정의
     
     * 클래스 변수(속성)명 = DB 필드의 이름
     
     * 클래스 변수 값 (models 모듈의 Field 클래스) = DB 필드의 데이터 타입
   
   * Django Model Field
     
     * Django는 모델 필드를 통해 테이블의 필드(컬럼)에 저장할 데이터 유형을 정의
     
     * 데이터 유형에 따라 다양한 모델 필드를 제공
   
   * 사용한 모델 필드 알아보기
     
     * CharField(max_length=None, \*\*options)
       
       * 길이의 제한이 있는 문자열을 넣을 때 사용
       
       * max_length
         
         * 필수 인자
         
         * 데이터베이스와 Django의 유효성 검사(값을 검증하는 것)에서 활용됨
     
     * TextField(\*\*options)
       
       * 글자의 수가 많을 때 사용
       
       * max_length 옵션 작성 시 사용자 입력 단계에서는 반영. but, 모델과 데이터베이스 단계에는 적용X
         
         * 실제로 저장될 때 길이에 대한 유효성 검증X

4. Migrations
   
   * 개요: Django가 모델에 생긴 변화(필드 추가, 수정 등)을 실제 DB에 반영하는 방법
   
   * Migrations 관련 주요 명령어
     
     * makemigrations
     
     * migrate
   
   * makemigrations
     
     * 모델의 변경사항에 대한 새로운 migration을 만들 때 사용
     
     * 테이블을 만들기 위한 설계도를 생성하는 것
     
     * 명령어 실행 후 migrations/0001_initial.py 가 생성됨
     
     * 파이썬으로 작성된 설계도
   
   * migrate
     
     * makemigrations로 만든 설계도를 실제 데이터베이스에 반영하는 과정(db.sqlite3 파일에 반영)
     
     * 모델의 변경사항과 데이터베이스를 동기화
   
   * [참고] Migrations 기타 명령어
     
     * showmigrations
       
       * migrations 파일들이 migrate 됐는지 여부 확인 용도
       * X 표시 -> migrate 완료 의미
     
     * sqlmigrate
       
       * migrations 파일이 SQL 문으로 어떻게 해석 될 지 미리 확인 가능

5. 추가 필드 정의
   
   * Model 변경사항 반영하기
     
     * 추가 모델 필드 작성 후 다시 makemigrations 진행
     
     * 이미 존재하는 테이블에 새로운 컬럼이 추가되는 요구 사항 -> 이 컬럼들은 기본적으로 빈 값으로 추가될 수 없음
       
       * 추가되는 컬럼에 대한 기본 값 설정 어떻게 할지?
       
       * 1 입력 후 Enter -> 새 컬럼의 기본 값 직접 입력 -> 아무것도 입력 안하고 Enter 입력 시 기본 디폴트 값으로 입력
       
       * 2 입력 후 Enter -> 모델 필드에 default 속성을 직접 작성
     
     * 새로운 설계도 파일 완성 후 migrate 명령어로 DB와 동기화 진행
   
   * DateTimeField()
     
     * python의 datetime.datetime 인스턴스로 표시되는 날짜 및 시간을 값으로 사용하는 필드
     
     * DateField를 상속받는 클래스
     
     * 선택 인자
       
       * auto_now_add
         
         * 최초 생성 일자
         
         * 데이터가 실제로 만들어질 때 현재 날짜와 시간으로 자동으로 초기화 되도록 함
       
       * auto_now
         
         * 최종 수정 일자
         
         * 데이터가 수정될 때마다 현재 날짜와 시간으로 자동으로 갱신되도록 함
   
   * 반드시 기억해야 할 migration 3단계
     
     * models.py에서 변경사항 발생
     
     * migration 생성 : makemigrations
     
     * DB 반영 (모델과 DB의 동기화) : migrate
   
   * 설계도는 어떻게, 누가 해석할까
     
     - makemigrations로 만들어진 설계도 -> 파이썬으로 작성
     
     - SQL만 알아들을 수 있는 DB가 어떻게 설계도를 이해하고 동기화?
     
     - 이 과정에서 중간에 해석을 담당하는 것이 ORM

6. ORM
   
   * 개요
     
     * Object-Relational-Mapping
     
     * 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에(Django <-> SQL)데이터를 변환하는 프로그래밍 기술
     
     * 객체 지향 프로그래밍에서 데이터베이스를 연동할 때, 데이터베이스와 객체 지향 프로그래밍 언어 간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법
     
     * 내장 Django ORM을 사용
   
   * ORM 장단점
     
     * 장점
       
       * SQL을 잘 알지 못해도 객체지향 언어로 DB 조작이 가능
       
       * 객체 지향적 접근으로 인한 높은 생산성
     
     * 단점
       
       * ORM만으로 완전한 서비스 구현하기 어려운 경우가 있음
   
   * ORM을 사용하는 이유
     
     * 생산성

## 3. QuerySet API

----

1. 사전 준비
   
   * 외부 라이브러리 설치 및 설정
   
   * [참고]
   
   * 첫 ORM 명령어 사용하기

2. QuerySet API
   
   * Database API
     
     * Django가 제공하는 ORM을 사용해 데이터베이스를 조작하는 방법
   
   * Database API 구문 : Model_class명.Manager.Queryset_API
   
   * objects manager
     
     * Django 모델이 데이터베이스 쿼리 작업을 가능하게 하는 인터페이스
     
     * 기본적으로 모든 모델 클래스에 대해 objects라는 Manager 객체를 자동으로 추가함
   
   * Query
     
     * 데이터베이스에 특정한 데이터를 보여 달라는 요청
   
   * QuerySet
     
     * 데이터베이스에게서 전달 받은 객체 목록(데이터 모음)
       
       * 순회 가능한 데이터, 1개 이상의 데이터를 불러와 사용 가능
     
     * Django ORM을 통해 만들어진 자료형, 필터를 걸거나 정렬 등 수행 가능
     
     * objects manager를 사용하여 복수의 데이터를 가져오는 queryset method를 사용할 때 반환되는 객체
     
     * 단, 데이터베이스가 단일한 객체를 반환할 때는 QuerySet이 아닌 모델(Class)의 인스턴스로 반환됨
   
   * QuerySet API: QuerySet과 상호작용하기 위해 사용하는 도구(메서드, 연산자 등)

3. QuerySet API 익히기
   
   * CRUD: Create / Read / Update / Delete
     
     * 생성 / 조회 / 수정 / 삭제
     
     * 대부분의 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리 기능 4가지를 묶어서 일컫는 말
   
   * CREATE
     
     * 데이터 객체를 만드는(생성하는) 3가지 방법
     
     * 첫번째 방법
       
       * 클래스를 통한 인스턴스 생성 : article = Article()
       
       * 인스턴스 변수 생성 후 값 할당 : article.title
       
       * 인스턴스로 save 메서드 호출 : article.save()
     
     * 두번째 방법
       
       * 인스턴스 생성 시 초기 값을 함께 작성하여 생성
     
     * 세번째 방법
       
       * QuerySet API 중 create() 메서드 활용
       
       * save() 필요 없이 바로 생성된 데이터 반환
     
     * .save()
       
       * 객체를 데이터베이스에 저장함
       
       * 데이터 생성 시 save를 호출하기 전에는 객체의 id 값은 None
         
         * id 값은 Django가 아니라 데이터베이스에서 계산되기 때문
       
       * 단순히 인스턴스 생성 -> DB에 영향 미치지 X -> 반드시 save 호출해야 테이블에 레코드가 생성됨
   
   * READ
     
     * QuerySet API method를 사용해 데이터를 다양하게 조회하기
     
     * QuerySet API method는 크게 2가지로 분류됨
       
       * Methods that 'return new querysets'
       
       * Methods that 'do not return querysets'
     
     * all()
       
       * QuerySet return
       
       * 전체 데이터 조회
     
     * get()
       
       * 단일 데이터 조회
       
       * 객체 찾을 수 X -> DoesNotExist 예외 발생
       
       * 둘 이상의 객체를 찾으면 -> MultipleObjectsReturned 예외 발생
       
       * primary key와 같이 고유성(uniqueness)을 보장하는 조회에서 사용해야 함
     
     * filter()
       
       * 지정된 조회 매개 변수와 일치하는 객체를 포함하는 새 QuerySet 반환
       
       * 조회된 객체가 없거나 1개여도 QuerySet을 반환
     
     * Field lookups
       
       * 특정 레코드에 대한 조건을 설정하는 방법
       
       * QuerySet 메서드 filter(), exclude() 및 get()에 대한 키워드 인자로 지정됨
   
   * UPDATE
     
     * 수정하고자 하는 인스턴스 객체를 조회 후 반환 값을 저장
     
     * 인스턴스 객체의 인스턴스 변수 값을 새로운 값으로 할당
     
     * save() 인스턴스 메서드 호출
   
   * DELETE
     
     * 삭제하고자 하는 인스턴스 객체를 조회 후 반환 값을 저장
     
     * delete() 인스턴스 메서드 호출
   
   * [참고] \_\_str\_\_()
     
     * DB에 영향을 주지 않음 -> migrations 필요 X

## 4. CRUD with view functions

----

1. 개요
   
   * QuerySet API를 통해 view 함수에서 직접 CRUD 구현하기

2. 사전 준비
