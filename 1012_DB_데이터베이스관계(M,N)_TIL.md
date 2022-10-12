## 0. 목차

----

1. Many to many relationship

2. M:N (Article-User)
   
   * Like

3. M:N (User-User)
   
   * Follow

## 1. Many to many relationship

----

0. RDB에서의 관계 복습

1. Intro
   
   * 개요
     
     * 병원에 내원하는 환자와 의사의 예약 시스템을 구축
   
   * [참고] 데이터 모델링
     
     * 주어진 개념으로부터 논리적인 데이터 모델을 구성하는 작업
     
     * 물리적인 DB 모델로 만들어 고객의 요구에 따라 특정 정보 시스템의 DB에 반영하는 작업
   
   * 시작하기 전 용어 정리
     
     * target model : 관계 필드를 가지지 않은 모델
     
     * source model : 관계 필드를 가진 모델
   
   * **N:1의 한계**
     
     * 동일한 환자, 다른 의사에게 예약 -> 객체를 하나 더 만들어서 
     
     * 외래키 컬럼에 '1, 2'형태로 참조하는 것 -> Integer타입이 아니기 때문에 불가능
     
     * 예약 테이블을 만들자
   
   * **중개 모델**
     
     * 예약 모델 -> 의사와 환자에 각각 N:1 관계
   
   * **Django ManyToManyField**
     
     * .add()
     
     * .remove()
     
     * Django는 ManyToManyField를 통해 중개 테이블을 자동로 생성함
   
   * **'related_name' argument**
     
     * target model이 source model을 참조할 때 사용할 manager name
     
     * ForeignKey()의 related_name과 동일
   
   * **'through' argument**
     
     * 중개 모델을 직접 작성하는 경우는 없을까?
       
       * 중개 테이블을 수동으로 지정하려는 경우 through 옵션을 사용하여 사용하려는 중개 테이블을 나타내는 Django 모델을 지정할 수 있음
     
     * 가장 일반적인 용도는 중개테이블에 추가 데이터를 사용해 다대다 관계와 연결하려는 경우
     
     * through_defaults = {}
   
   * **정리**
     
     * M:N 관계로 맺어진 두 테이블에는 변화가 없음
     
     * Django의 ManyToManyField는 중개 테이블을 자동으로 생성함
     
     * Django의 ManyToManyField는 M:N 관계를 맺는 두 모델 어디에 위치해도 상관 없음
       
       * 대신 필드 작성 위치에 따라 참조와 역참조 방향을 주의할 것
     
     * N:1은 완전한 종속 관계, M:N은 의사에게 진찰받는 환자, 환자를 진찰하는 의사 두가지 형태로 모두 표현 가능

2. ManyToManyField
   
   * ManyToManyField(to, **options)
     
     * 다대다 관계 설정 시 사용하는 모델 필드
     
     * 하나의 필수 위치인자(M:N 관계로 설정할 모델 클래스)가 필요
     
     * 모델 필드의 RelatedManager를 사용하여 관련 개체를 추가, 제거 또는 만들 수 있음
       
       * add(), remove(), create(), clear()
   
   * **DB에서의 표현**
     
     * Django는 다대다 관계를 나타내는 중개 테이블을 만듦
     
     * 테이블 이름은 ManyToManyField 이름과 이를 포함하는 모델의 테이블 이름을 조합하여 생성됨
     
     * 'db_table' arguments를 사용하여 중개 테이블의 이름을 변경 가능
   
   * **ManyToManyField's Arguments**
     
     * **related_name**
       
       * target model이 source model을 참조할 때 사용할 manager name
       
       * ForeignKey의 related_name과 동일
     
     * **through**
       
       * 중개 테이블을 직접 작성하는 경우, through 옵션을 사용하여 중개 테이블을 나타내는 Django 모델을 지정
       
       * 일반적으로 중개 테이블에 추가 데이터를 사용하는 다대다 관계와 연결하려는 경우(extra data with a many-to-many relationship)에 사용됨
     
     * **symmetrical**
       
       * 기본값: True
       
       * ManyToManyField가 동일한 모델(on self)을 가리키는 정의에서만 사용
       
       * True일 경우
         
         * \_set 매니저를 추가하지 X
         
         * source 모델의 인스턴스가 target 모델의 인스턴스를 참조하면 자동으로 target 모델 인스턴스도 source 모델 인스턴스를 자동으로 참조하도록 함(대칭)
       
       * 대칭을 원하지 않는 경우 False로 설정
   
   * **Related Manager**
     
     * N:1 혹은 M:N 관계에서 사용 가능한 문맥(context)
     
     * Django는 모델 간 N:1 혹은 M:N 관계가 설정되면 -> 역참조시에 사용할 수 있는 manager를 생성
     
     * 같은 이름의 메서드여도 각 관계(N:1, M:N)에 따라 다르게 사용 및 동작됨
       
       * N:1에서는 target 모델 객체만 사용 가능
       
       * M:N관계에서는 관련된 두 객체에서 모두 사용 가능
     
     * 메서드 종류: add(), remove(), create(), clear(), set() 등
   
   * **methods** - many-to-many relationships일 때의 동작만 작성되었음
     
     * **add()**
       
       * 지정된 객체를 관련 객체 집합에 추가
       
       * 이미 존재하는 관계에 사용 -> 관계 복제X
       
       * 모델 인스턴스, 필드값(PK)을 인자로 허용
     
     * **remove()**
       
       * 관련 객체 집합에서 지정된 모델 개체를 제거
       
       * 내부적으로 QuerySet.delete()를 사용하여 관계 삭제
       
       * 모델 인스턴스, 필드값(PK)을 인자로 허용
   
   * **중개 테이블 필드 생성 규칙**
     
     * 소스(source model) 및 대상(target model) 모델이 **다른 경우**
       
       * id
       
       * \<containing_model>\_id
       
       * \<other_model>\_id
     
     * ManyToManyField가 동일한 모델을 가리키는 경우
       
       * id
       
       * from\_\<model>\_id
       
       * to\_\<model>\_id

## 2. M:N (Article-User)

----

0. 개요
   
   * 좋아요 기능 구현

1. LIKE
   
   * 모델 관계 설정
     
     * ManyToManyField 작성
     
     * Migration 진행 후 에러 확인
     
     * like_users 필드 생성 -> 역참조 -> .article_set 매니저가 생성됨
     
     * 그러나 이전 N:1(Article-User) 관계에서 이미 해당 매니저를 사용중
       
       * user.article_set.all() -> 해당 유저가 작성한 모든 게시글 조회
       
       * user가 작성한 글들(user.article_set)과 user가 좋아요를 누른 글(user.article_set)을 구분X
     
     * user와 관계된 ForeignKey 혹은 ManyToManyField 중 하나에 related_name을 작성해야함
     
     * related_name 작성 후 Migration
     
     * 생성된 중개 테이블 확인
     
     * User-Article간 사용 가능한 related manager 정리
       
       * article.user -> 게시글을 작성한 유저 N:1
       
       * user.article_set -> 유저가 작성한 게시글(역참조) N:1
       
       * article.like_users -> 게시글을 좋아요한 유저 M:N
       
       * user.like_articles -> 유저가 좋아요한 게시글(역참조) M:N
   
   * **LIKE 구현**
     
     * url 및 view 함수 작성
     
     * .exists()
       
       * QuerySet에 결과가 포함되어 있으면 True 반환, 그렇지 않으면 False 반환
       
       * 큰 QuerySet에 있는 특정 개체의 존재와 관련된 검색에 유용
     
     * index 템플릿에서 각 게시글에 좋아요 버튼 출력하기
     
     * 데코레이터 및 is_authenticated 추가

## 3. M:N (User-User)

---

0. 개요
   
   * User 자기 자신과의 M:N 관계 설정을 통한 팔로우 기능 구현

1. Profile
   
   * 프로필 페이지 먼저 작성
   
   * Profile 구현
     
     * url 및 view 함수 작성
     
     * profile 템플릿 작성
     
     * profile 템플릿으로 이동할 수 있는 하이퍼 링크 작성

2. Follow
   
   * ManyToManyField 작성 및 Migration 진행
   
   * url 및 view 함수 작성
   
   * 프로필 유저의 팔로잉, 팔로워 수 & 팔로우, 언팔로우 버튼 작성
   
   * 데코레이터 및 is_authenticated 추가
