## 0. 목차

----

1. A many-to-one relationship

2. N:1 (Comment - Article)

3. N:1 (Article - User)

4. N:1 (Comment - User)

## 1. A many-to-one relationship

---

1. 개요
   
   * 관계형 DB에서의 외래키 속성을 사용해 모델간 N:1 관계 설정하기

2. Intro
   
   * RDB(관계형 데이터베이스) 복습
     
     * 데이터를 테이블, 행, 열 등으로 나누어 구조화하는 방식
     
     * RDB의 모든 테이블에는 행에서 고유하게 식별 가능한 기본키라는 속성이 있으며, 외래키를 사용하여 각 행에서 서로 다른 테이블 간의 관계를 만드는데 사용할 수 있음
   
   * **[참고] 관계 (Relationship)**
     
     * 테이블 간의 상호작용을 기반으로 설정되는 여러 테이블 간의 논리적인 연결
   
   * 테이블 간 관계 예시
     
     * 관계형 데이터베이스에서 한 테이블의 필드 중 다른 테이블의 행을 식별할 수 있는 키를 외래키(foreign key, FK)라 함
   
   * **RDB에서의 관계**
     
     * **1:1**
       
       * One-to-one relationships
       
       * 한 테이블의 레코드 하나가 다른 테이블의 레코드 단 한 개와 관련된 경우
     
     * **N:1**
       
       * Many-to-one-relationships
       
       * 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 경우
       
       * 기준 테이블에 따라(1:N, One-to-many relationships)이라고도 함
     
     * **M:N**
       
       * Many-to-many relationships
       
       * 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우
       
       * 양쪽 모두에서 N:1 관계를 가짐
   
   * Many-to-one relationships 예시

3. **Foreign Key**
   
   * 개념
     
     * **외래키(외부키)**
     
     * 관계형 DB에서 한 테이블의 필드 중 **다른 테이블의 행을 식별**할 수 있는 키
     
     * 참조되는 테이블의 기본키(Primary Key)를 가리킴
     
     * 참조하는 테이블의 행 1개의 값은, 참조되는 측 테이블의 행 값에 대응됨
       
       * 이 때문에 참조하는 테이블의 행에는, 참조되는 테이블에 나타나지 않는 값 포함X
     
     * 참조하는 테이블 행 여러개가, 참조되는 테이블의 동일한 행을 참조할 수 있음
   
   * **특징**
     
     * 키를 사용하여 부모 테이블의 **유일한 값을 참조**(by 참조 무결성)
     
     * 외래 키의 값이 반드시 부모 테이블의 **기본키일 필요는 없지만 유일한 값이어야 함**
   
   * **[참고] 참조 무결성**
     
     * DB 관계 모델에서 관련된 <u>2개의 테이블 간의 일관성</u>을 말함
     
     * 외래키가 선언된 테이블의 외래키 속성(열)의 값은 그 테이블의 부모가 되는 테이블의 기본키 값으로 존재해야 함

## 2. N:1 (Comment - Article)

----

1. 개요
   
   * Comment(N) - Article(1)
   
   * Comment 모델과 Article 모델 간 관계 설정
   
   * 0개 이상의 댓글은 1개의 게시글에 작성될 수 있음

2. 모델 관계 설정
   
   * 게시판의 게시글과 N:1 관계를 나타낼 수 있는 댓글 구현

3. **Django Relationship fields**
   
   * Django Relationship fields **종류**
     
     * **OneToOneField()**
     
     * **ForeignKey(to, on_delete, \*\*options)**
       
       * A many-to-one relationship을 담당하는 Django의 모델 필드 클래스
       
       * Django 모델에서 관계형 DB의 외래키 속성을 담당
       
       * **2개의 필수 위치 인자**가 필요
         
         * 참조하는 **model class**
         
         * **on_delete** 옵션
     
     * **ManyToManyField()**

4. **Comment Model**
   
   * Comment 모델 정의
     
     * 외래키 필드는 ForeignKey 클래스를 <u>작성하는 위치와 관계없이 필드의 마지막에 작성됨</u>
     
     * ForeignKey() 클래스의 인스턴스 이름은 **참조하는 모델 클래스 이름의 단수형(소문자)** 으로 작성하는 것을 권장
   
   * **ForeignKey arguments - on_delete**
     
     * 외래키가 참조하는 객체가 사라졌을 때, 외래 키를 가진 객체를 어떻게 처리할지를 정의
     
     * **데이터 무결성을 위해서 매우 중요**한 설정
     
     * **on_delete 옵션 값**
       
       * **CASCADE**: 부모 객체(참조된 객체)가 삭제되었을 때 이를 **참조하는 객체도 삭제**
       
       * **PROTECT, SET_NULL, SET_DEFAULT** 등 여러 옵션 값들이 존재
   
   * **[참고] 데이터 무결성 (Data Integrity)**
     
     * 데이터의 **정확성과 일관성을 유지하고 보증**하는 것
     
     * DB나 RDBMS의 중요한 기능
     
     * **무결성 제한의 유형**
       
       * 개체 무결성 (Entity integrity)
       
       * 참조 무결성 (Referential integrity)
       
       * 범위 무결성 (Domain integrity)
   
   * **Migration 과정 진행**
     
     * migrate 후 Comment 모델 클래스로 인해 생성된 테이블 확인
     
     * ForeignKey 모델 필드로 인해 작성된 컬럼의 이름 -> article_id
     
     * 만약 ForeignKey 인스턴스를 article이 아닌 abcd로 생성했다면 abcd_id로 만들어짐
       
       * 명시적인 모델 관계 파악을 위해 참조하는 클래스 이름의 소문자(단수형)로 작성하는 것 권장됨
   
   * 댓글 생성 연습하기
     
     * 외래키 데이터 입력

5. **관계 모델 참조**
   
   * **Related manager**
     
     * Related manager는 **N:1 혹은 M:N 관계**에서 사용 가능한 문맥(context)
     
     * Django는 모델 간 N:1 혹은 M:N 관계가 설정되면 **역참조**할 때에 사용할 수 있는 manager를 생성
       
       * 이전에 모델 생성 시 objects라는 매니저를 통해 queryset api를 사용했던 것처럼 related manager를 통해 queryset api를 사용할 수 있게 됨
   
   * **역참조**
     
     * 나를 참조하는 테이블(나를 외래 키로 지정한)을 참조하는 것
     
     * 즉, <u>본인을 외래 키로 참조 중인 다른 테이블에 접근</u>하는 것
     
     * N:1 관계에서는 1이 N을 참조하는 상황
       
       * 외래키를 가지지 않은 1이 외래 키를 가진 N을 참조
   
   * article.comment_set.method()
     
     * Article 모델이 Comment 모델을 참조(역참조)할 때 사용하는 매니저
     
     * article.comment 형식으로는 댓글 객체를 참조X
       
       * 실제로 Article 클래스에는 Comment와의 어떠한 관계도 작성X
     
     * 대신 Django가 역참조 할 수 있는 **comment_set** manager를 자동으로 생성해 article.comment_set 형태로 댓글 객체를 참조할 수 있음
       
       * N:1 관계에서 생성되는 **Related manager의 이름**은 참조하는 **'모델명\_set'** 이름 규칙으로 만들어짐
     
     * 반면 참조 상황(Comment -> Article)에서는 실제 ForeignKey 클래스로 작성한 인스턴스가 Comment 클래스의 클래스 변수이기 때문에 comment.article 형태로 작성 가능
   
   * Related manager 연습하기
     
     * dir(): 클래스 객체가 사용할 수 있는 메서드 목록
   
   * ForeignKey arguments - **related_name**
     
     * **역참조** 시 사용하는 **매니저 이름**(model_set manager)을 **변경할 수 있음**
     
     * 작성 후, migration 과정 필요
     
     * 변경하면 기존 article.comment_set은 더 이상 사용X ->  대체
   
   * admin site 등록

6. **Comment 구현**
   
   * **CREATE**
     
     * CommentForm 작성
     
     * detail 페이지에서 CommentForm 출력(view 함수, 템플릿)
     
     * 실 서비스에서는 댓글을 어떤 게시글에 작성하는지 직접 게시글 번호를 선택하지 않음
     
     * Comment 클래스의 외래 키 필드 article 또한 데이터 입력이 필요하기 때문에 출력되고 있는 것
     
     * but, **외래키 필드** -> 사용자의 입력으로 받는 것이 아니라 **view 함수 내에서** 받아 **별도로 처리되어 저장**되어야 함
     
     * 외래키 필드를 출력에서 제외 -> forms.py에서 exclude에 추가
     
     * 출력에서 제외된 외래키 데이터는 어디서 받아와야 할까?
     
     * detail 페이지의 url을 살펴보면 url에 해당 게시글의 pk 값이 사용되고 있음
     
     * 댓글의 외래키 데이터에 필요한 정보가 바로 게시글의 pk 값
     
     * **variable routing**을 사용
     
     * save()메서드는 DB에 저장하기 전에 객체에 대한 추가적인 작업을 진행할 수 있도록 인스턴스만을 반환해주는 옵션 값을 제공
   
   * The save() method
     
     * **save(commit=False)**
       
       * 아직 **DB에 저장되지 않은 인스턴스를 반환**
       
       * 저장하기 전에 <u>객체에 대한 사용자 지정 처리</u>를 수행할 때 유용하게 사용
   
   * READ
     
     * 작성한 댓글 목록 출력 -> 역참조로 모든 댓글 가져온 후 context에 추가, 템플릿에서 댓글 목록 출력
   
   * DELETE
   
   * **댓글 수정**을 지금 구현하지 않는 이유
     
     * 일반적으로 댓글 수정은 수정 페이지로 이동 없이 **현재 페이지가 유지된 상태로** 댓글 작성 Form 부분만 변경되어 수정할 수 있도록 함
     
     * 이처럼 **페이지의 일부 내용만 업데이트** 하는 것 -> **JavaScript의 영역**

7. Comment 추가 사항
   
   * 댓글 개수 출력하기
     
     * DTL filter - length 사용
       
       * {{comments|length}}
       
       * {{article.comment_set.all|length}}
     
     * Queryset API - count() 사용
       
       * {{comments.count}}
       
       * {{article.comment_set.count}}
   
   * 댓글이 없는 경우 대체 컨텐츠 출력하기
     
     * DTL for empty 활용하기
       
       * {% empty %}

## 3. N:1 (Article - User)

---

1. 개요
   
   * Article(N) - User(1)
   
   * Article 모델과 User 모델 간 관계 설정
   
   * 0개 이상의 게시글은 1개의 회원에 의해 작성될 수 있음

2. **Referencing the User model**
   
   * Django에서 **User 모델을 참조**하는 방법
     
     * **settings.AUTH_USER_MODEL**
       
       * 반환 값: **'accounts.User'** (**문자열**)
       
       * User 모델에 대한 외래키 또는 M:N 관계를 정의할 때 사용
       
       * **models.py의 모델 필드**에서 **User 모델을 참조할 때** 사용
     
     * **get_user_model()**
       
       * 반환 값: **User Object** (**객체**)
       
       * 현재 활성화(active)된 User 모델을 반환
       
       * 커스터마이징한 User 모델이 있을 경우는 Custom User 모델, 그렇지 않으면 User 반환
       
       * **models.py가 아닌 다른 모든 곳**에서 유저 모델을 참조할 때 사용

3. 모델 관계 설정
   
   * models.py에 settings 활용하여 외래키 작성
   
   * Migration 진행
     
     * 기본적으로 모든 컬럼은 NOT NULL 제약조건이 있기 때문에 데이터가 없이는 새로 추가되는 외래키 필드 user_id가 생성되지 않음
     
     * 그래서 기본값을 어떻게 작성할 것인지 선택해야 함
   
   * **Django에서 User 모델을 참조하는 방법 정리**
     
     * 문자열과 객체를 반환하는 특징과 Django의 내부적인 실행 원리에 관련된 것
     
     * User 모델을 참조할 때
       
       * models.py에서는 settings.AUTH_USER_MODEL
       
       * 다른 모든 곳에서는 get_user_model()

4. CREATE
   
   * 개요
     
     * 인증된 회원의 게시글 작성 구현하기
     
     * 작성하기 전 로그인을 먼저 진행한 상태로 진행
   
   * forms.py 
   
   * views.py에서 save의 commit 옵션 활용 작성자 정보 함께 저장

5. DELETE
   
   * 게시글 삭제 시 작성자 확인
     
     * 현재 삭제를 요청하려는 사람과 게시글을 작성한 사람을 비교 -> 본인의 게시글만 삭제할 수 있도록

6. UPDATE
   
   * 게시글 수정 시 작성자 확인 -> 본인의 게시글만 수정할 수 있도록
   * 게시글 작성자가 아니라면 -> 수정/삭제 버튼 출력하지 않도록

7. READ
   
   * index 템플릿과 detail 템플릿에서 각 게시글의 작성자 출력

## 4. N:1 (Comment-User)

---

1. 개요
   
   * Comment(N) - User(1)
   
   * 0개 이상의 댓글은 1개의 회원에 의해 작성 될 수 있음

2. 모델 관계 설정
   
   * models.py 외래키 작성
   
   * migration 진행

3. CREATE
   
   * forms.py에서 출력 필드 수정
   
   * views.py에서 save의 commit 옵션 활용하여 작성자 정보 저장

4. READ
   
   * detail 템플릿에서 각 게시글의 작성자 출력

5. DELETE
   
   * views.py에서 본인의 댓글만 삭제할 수 있도록 함
   
   * 템플릿에서 해당 댓글의 작성자가 아니라면, 삭제 버튼 출력하지 않도록 함

6. **인증된 사용자에 대한 접근 제한**하기
   
   * is_authenticated와 View decorator를 활용하여 코드 정리하기
   
   * 인증된 사용자인 경우만 댓글 작성 및 삭제하기
   
   * 비인증 사용자는 CommentForm을 볼 수 없도록 하기

## 5. 마무리

---

1. A many-to-one relationship
   
   * Foreign Key
   
   * Django Relationship fields
   
   * Related manager

2. N:1 모델 관계 설정
   
   * Comment - Article
   
   * Article - User
     
     * Referencing the User model
   
   * Comment - User
