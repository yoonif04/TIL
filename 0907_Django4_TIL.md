## 0. Django

----

1. The Django authentication system

2. HTTP Cookies

3. Authentication in Web requests

4. Authentication with User

5. Limiting access to logged-in users

## 1. The Django authentication system

---

1. 개요
   
   * **인증(Authentication)** 과 **권한(Authorization)** 부여를 함께 제공(처리)하며, 이러한 기능이 어느 정도 결합되어 일반적으로 인증 시스템이라고 함
   
   * 필수 구성은 settings.py에 이미 포함되어 있으며 INSTALLED_APPS에서 확인 가능
     
     * **django.contrib.auth**
   
   * **Authentication(인증)**
     
     * 신원 확인
     
     * 사용자가 자신이 누구인지 확인하는 것
   
   * **Authorization(권한, 허가)**
     
     * 권한 부여
     
     * 인증된 사용자가 수행할 수 있는 작업을 결정
   
   * 사전 설정
     
     * 두번째 app accounts 생성 및 등록
       
       * auth와 관련한 경로나 키워드들을 Django 내부적으로 accounts라는 이름으로 사용하고 있기 때문에 되도록 accounts로 지정하는 것을 권장

2. Substituting a custom User model
   
   * 개요
     
     * 커스텀 User 모델로 대체하기
     
     * 기본 User model을 필수적으로 custom User model로 대체하는 이유 이해하기
     
     * Django는 기본적인 인증 시스템과 여러 가지 필드가 포함된 User Model을 제공, 대부분의 개발 환경에서 기본 User Model을 Custom User Model로 대체
     
     * 개발자들이 작성하는 일부 프로젝트에서는 django에서 제공하는 built-in User model의 기본 인증 요구사항이 적절하지 않을 수 있음
       
       * ex. 이메일을 식별 값으로 사용하는 것이 더 적합한 사이트인 경우 기존 User model을 수정해야하나 쉽지 않은 작업
     
     * Django는 현재 프로젝트에서 사용할 User Model을 결정하는 **AUTH_USER_MODEL** 설정 값으로 Default User Model을 재정의(override)할 수 있도록 함
   
   * AUTH_USER_MODEL
     
     * 프로젝트에서 User를 나타낼 때 사용하는 모델
     
     * 프로젝트가 진행되는 동안 (모델을 만들고 마이그레이션 한 후) 변경할 수 없음
     
     * 프로젝트 시작 시 설정하기 위한 것이며, 참조하는 모델은 첫 번째 마이그레이션에서 사용할 수 있어야 함
       
       * 즉, 첫번째 마이그레이션 전에 확정 지어야 하는 값
     
     * 기본 값
   
   * [참고] settings의 로드 구조
     
     * settings.py는 사실 global_settings.py를 상속받아 재정의하는 파일

3. How to substituting a custom User model
   
   * 개요
     
     * 대체하는 과정 외우기 어려울 경우 공식문서 보며 순서대로 진행하는 것 권장
   
   * 대체하기
     
     * AbstractUser를 상속받는 커스텀 User 클래스 작성
     
     * 기존 User 클래스도 AbstractUser를 상속받기 때문에 커스텀 User 클래스도 완전히 같은 모습을 가지게 됨
     
     * Django 프로젝트에서 User를 나타내는데 사용하는 모델을 방금 생성한 커스텀 User 모델로 지정
     
     * admin.py에 커스텀 User 모델을 등록
       
       * 기본 User 모델이 아니기 때문에 등록하지 않으면 admin site에 출력되지 않음
   
   * [참고] AbstractUser
     
     * 관리자 권한과 함께 완전한 기능을 가지고 있는 User model을 구현하는 추상 기본클래스
     
     * Abstract base classes (추상 기본 클래스)
       
       * 몇 가지 공통 정보를 여러 다른 모델에 넣을 때 사용하는 클래스
       
       * 데이터베이스 테이블을 만드는데 사용되지 않으며, 대신 다른 모델의 기본 클래스로 사용되는 경우 해당 필드가 하위 클래스의 필드에 추가 됨
   
   * [주의] 프로젝트 중간에 AUTH_USER_MODEL 변경하기
     
     * 모델 관계에 영향을 미치기 때문에 훨씬 더 어려운 작업 필요
       
       * ex. 변경사항이 자동으로 수행될 수 없음 -> DB 스키마를 직접 수정하고, 이전 사용자 테이블에서 데이터를 이동, 일부 마이그레이션을 수동으로 다시 적용 등
     
     * 결론: 중간 변경 권장X (프로젝트 처음에 진행하기)
   
   * 데이터베이스 초기화
     
     * 데이터베이스 초기화 후 마이그레이션 (프로젝트 중간일 경우)
     
     * migrations 파일 삭제
       
       * migrations 폴더 및 \_\_init\_\_.py 삭제X
       
       * 번호가 붙은 파일만 삭제
     
     * db.sqlite3 삭제
     
     * migrations 진행
       
       * makemigrations
       
       * migrate
   
   * 반드시 User 모델을 대체해야 할까?
     
     * Django는 새 프로젝트를 시작하는 경우 비록 기본 User 모델이 충분하더라도 커스텀 User 모델을 설정하는 것을 **강력하게 권장**
     
     * 커스텀 User 모델은 기본 User 모델과 동일하게 작동하면서도 필요한 경우 나중에 맞춤 설정할 수 있기 때문
       
       * 단, User 모델 대체 작업은 프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 이 작업을 마쳐야 함

## 2. HTTP Cookies

----

1. 개요
   
   * 로그인과 로그아웃 이해하기위해

2. **HTTP**
   
   * Hyper Text Transfer Protocol
   
   * HTML 문서와 같은 **리소스들을 가져올 수 있도록** 해주는 프로토콜(규칙, 규약)
   
   * 웹(WWW)에서 이루어지는 모든 데이터 교환의 기초
   
   * 클라이언트 - 서버 프로토콜이라고도 부름
   
   * 요청과 응답
     
     * 요청 (requests): 클라이언트(브라우저)에 의해 전송되는 메시지
     
     * 응답 (response): 서버에서 응답으로 전송되는 메시지
   
   * **HTTP 특징**
     
     * **비 연결 지향(connectionless)**
       
       * 서버는 요청에 대한 **응답을 보낸 후 연결을 끊음**
     
     * **무상태(stateless)**
       
       * **연결을 끊는 순간** 클라이언트와 서버 간의 **통신이 끝**나며 **상태 정보가 유지되지 않음**
       
       * 클라이언트와 서버가 주고받는 메시지들은 서로 완전히 독립적
   
   * 어떻게 로그인 상태를 유지할까?
     
     * 서버와 클라이언트 간 지속적인 상태 유지를 위해 **"쿠키와 세션"** 이 존재

3. **쿠키(Cookie)**
   
   * 개요: HTTP 쿠키는 **상태가 있는 세션**을 만들도록 해줌
   
   * 개념
     
     * 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각
     
     * 사용자가 웹사이트를 방문할 경우 해당 웹사이트의 서버를 통해 사용자의 컴퓨터에 설치되는 작은 기록 정보 파일
       
       * 브라우저(클라이언트)는 쿠키를 로컬에 <u>KEY-VALUE</u>의 데이터 형식으로 저장
       
       * 쿠키를 저장해 놓았다가, **동일한 서버에 재요청 시 저장된 쿠키를 함께 전송**
     
     * 쿠키는 두 요청이 <u>동일한 브라우저에서 들어왔는지 아닌지를 판단할 때</u> 주로 사용
       
       * 이를 이용해 사용자의 로그인 상태 유지
       
       * 상태가 없는 (stateless) HTTP 프로토콜에서 상태 정보를 기억시켜 주기 때문
     
     * 즉, 웹페이지에 접속 -> 웹페이지를 응답한 서버로부터 쿠키를 받아 브라우저에 저장 -> 클라이언트가 같은 서버에 재요청시 -> 요청과 함께 쿠키도 전송
   
   * 쿠키 사용 목적
     
     * 세션 관리 (Session management)
       
       * 로그인, 아이디 자동완성, 공지 하루 안 보기, 팝업 체크, 장바구니 등의 정보관리
     
     * 개인화 (Personalization)
       
       * 사용자 선호, 테마 등의 설정
     
     * 트래킹 (Tracking)
       
       * 사용자 행동을 기록 및 분석
   
   * 세션(Session)
     
     * 사이트와 특정 브라우저 사이의 "state(상태)"를 유지시키는 것
     
     * 클라이언트가 서버에 접속 -> 서버가 특정 session id를 발급 -> 클라이언트는 session id를 쿠키에 저장
       
       * 클라이언트가 다시 동일한 서버에 접속 -> 요청과 함께 쿠키(session id가 저장된)를 서버에 전달
       
       * 쿠키는 요청 때마다 서버에 함께 전송되므로 서버에서 session id를 확인해 알맞은 로직을 처리
     
     * session id는 세션을 구별하기 위해 필요하며, 쿠키에는 session id만 저장
   
   * 쿠키 Lifetime (수명)
     
     * Session cookie
       
       * 현재 세션(current session)이 종료되면 삭제됨
       
       * 브라우저 종료와 함께 세션이 삭제됨
     
     * Persistent cookies
       
       * Expires 속성에 지정된 날짜 혹은 Max-Age 속성에 지정된 기간이 지나면 삭제됨
   
   * Session in Django
     
     * Django는 **database-backed sessions 저장 방식** 을 기본 값으로 사용
       
       * session 정보는 Django DB의 **django_session 테이블**에 저장
       
       * 설정을 통해 다른 저장방식으로 변경 가능
     
     * Django는 특정 session id를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 session을 알아냄
     
     * Django는 우리가 session 매커니즘(복잡한 동작원리)에 대부분을 생각하지 않게끔 많은 도움을 줌

## 3. Authentication in Web requests

----

1. 개요
   
   * Django가 제공하는 인증 관련 built-in forms 익히기

2. Login
   
   * 개요: 로그인은 **Session을 Create**하는 과정
   
   * AuthenticationForm
     
     * 로그인을 위한 built-in form
       
       * 로그인 하고자 하는 사용자 정보를 입력 받음
       
       * 기본적으로 username과 password를 받아 데이터가 유효한지 검증
     
     * request를 첫번째 인자로 취함
   
   * login(request, user, backend=None)
     
     * 인증된 사용자를 로그인 시키는 로직으로 view함수에서 사용됨
     
     * 현재 세션에 연결하려는 인증 된 사용자가 있는 경우 사용
     
     * HttpRequest 객체와 User 객체가 필요
   
   * 로그인 로직 작성
   
   * **get_user()**
     
     * AuthenticationForm의 인스턴스 메서드
     
     * **유효성 검사를 통과했을 경우** 로그인 한 사용자 객체를 반환

3. 현재 로그인 되어있는 유저 정보 출력하기
   
   - 템플릿에서 인증 관련 데이터 출력
   
   - 어떻게 base 템플릿에서 context 데이터 없이 user 변수 사용?
     
     - settings.py의 **context processors** 설정 값 때문
   
   - **context processors**
     
     - 템플릿이 렌더링 될 때 <u>호출 가능한 컨텍스트 데이터 목록</u>
     
     - 작성된 컨텍스트 데이터는 기본적으로 **템플릿에서 사용 가능한 변수**로 포함됨
     
     - 즉, django에서 자주 사용하는 데이터 목록을 미리 템플릿에 로드해 둔 것
     
     - 현재 user 변수를 담당하는 프로세서는 'django.contrib.auth.context_processors.auth'
   
   - 'django.contrib.auth.context_processors.auth'
     
     - 현재 로그인한 사용자를 나타내는 User 클래스의 인스턴스가 템플릿 변수 {{ user }}에 저장됨
       
       - 로그인X -> AnonymousUser 클래스의 인스턴스로 생성

4. Logout
   
   - 개요: 로그아웃은 **Session을 Delete**하는 과정
   - logout(request)
     - HttpRequest 객체를 인자로 받고 반환 값X
     - 사용자가 로그인하지 않은 경우 -> 오류 발생X
     - 다음 2가지 일을 처리
       - 현재 요청에 대한 session data를 DB에서 삭제
       - 클라이언트의 쿠키에서도 session id를 삭제
       - 이는 다른 사람이 동일한 웹 브라우저를 사용하여 로그인하고, 이전 사용자의 세션 데이터에 엑세스하는 것 방지

## 4. Authentication with User

----

1. 개요
   
   * User Object와 User CRUD에 대한 이해
     
     * 회원 가입, 탈퇴, 회원정보 수정, 비밀번호 변경

2. **회원 가입**
   
   * 회원 가입은 User를 Create하는 것, **UserCreationForm** built-in form을 사용
   
   * UserCreationForm
     
     * 주어진 username과 password로 <u>권한이 없는</u> 새 user를 생성하는 ModelForm
     
     * 3개의 필드를 가짐
       
       * username (from the user model)
       
       * password 1
       
       * Password 2
   
   * 회원가입 진행 후 에러 페이지
     
     * 회원가입에 사용하는 UserCreationForm이 우리가 대체한 커스텀 유저 모델이 아닌 기존 유저 모델로 인해 작성된 클래스이기 때문
     
     * forms.py 작성

3. Custom user & Built-in auth forms
   
   * 개요
     
     * Custom user와 기존 Built-in auth forms 간의 관계
     
     * Custom user로 인한 Built-in auth forms 변경
   
   * AbstractBaseUser의 모든 subclass와 호환되는 forms
     
     * 아래 Form 클래스는 User 모델을 대체하더라도 커스텀 하지 않아도 사용가능
     
     * AuthenticationForm
     
     * SetPasswordForm
     
     * PasswordChangeForm
     
     * AdminPasswordChangeForm
     
     * 기존 User 모델을 참조하는 Form이 아니기 때문
   
   * 커스텀 유저 모델을 사용하려면 다시 작성하거나 확장해야 하는 forms
     
     * UserCreationForm
     
     * UserChangeForm
     
     * 두 form 모두 class Meta: model = User 가 등록된 form이기 때문에 반드시 커스텀(확장)해야 함
   
   * UserCreationForm() UserChangeForm() 커스텀하기
   
   * get_user_model()
     
     * 현재 프로젝트에서 활성화된 사용자 모델(**active user model**)을 반환
     
     * 직접 참조하지 않는 이유
       
       * 커스텀 한 상황에서는 커스텀 User 모델을 자동으로 반환해주기 때문
     
     * Django는 User 클래스를 직접 참조하는 대신 get_user_model()을 사용해 참조해야 한다고 강조

4. 회원 탈퇴
   
   * 개요: DB에서 유저를 Delete하는 것과 같음
   
   * [참고] 탈퇴하면서 해당 유저의 세션 정보도 함께 지우고 싶을 경우
     
     * 탈퇴 후 로그아웃
       
       * 먼저 로그아웃해버리면 -> 해당 요청 객체 정보가 없어지기 때문에 탈퇴에 필요한 정보 또한 없어지기 때문

5. 회원정보 수정
   
   * 개요: UserChangeForm built-in form 사용
   
   * UserChangeForm
     
     * 사용자의 정보 및 권한을 변경하기 위해 **admin 인터페이스**에서 사용되는 **ModelForm**
     
     * ModelForm이기 때문에 instance 인자로 기존 user 데이터 정보를 받는 구조 또한 동일함
     
     * 이미 CustomUserChangeForm으로 확장했음
   
   * UserChangeForm 사용 시 문제점
     
     * 일반 사용자가 접근해서는 안 될 정보들(fields)까지 모두 수정이 가능해짐
       
       * admin 인터페이스에서 사용되는 ModelForm이기 때문
     
     * 따라서 UserChangeForm을 상속받아 작성해 두었던 서브 클래스 CustomUserChangeForm에서 접근 가능한 필드를 조정해야함
   
   * CustomUserChangeForm fields 재정의

6. 비밀번호 변경
   
   * PasswordChangeForm
     
     * 사용자가 비밀번호를 변경할 수 있도록 하는 Form
     
     * 이전 비밀번호를 입력하여 비밀번호를 변경할 수 있도록 함
     
     * 이전 비밀번호를 입력하지 않고 비밀번호를 설정할 수 있는 SetPasswordForm을 상속받는 서브 클래스
   
   * 비밀번호 변경 로직 작성
     
     * 작성 후 비밀번호 변경 확인
       
       * 변경 후 로그인 상태 지속X
   
   * 암호 변경 시 세션 무효화 방지하기
     
     * 비밀번호 변경 -> 기존 세션과의 회원 인증 정보 일치X -> 로그인 상태 유지X
     
     * 비밀번호는 잘 변경 but, 기존 세션과의 회원 인증 정보가 일치하지 않기 때문
   
   * update_session_auth_hash(request, user)
     
     * 현재 요청과 새 session data가 파생 될 업데이트 된 사용자 객체를 가져오고, session data를 적절하게 업데이터해줌
     
     * 암호 변경되어도 로그아웃 되지 않도록 새로운 password의 session data로 session을 업데이트



## 5. Limiting access to logged-in users

----

1. 개요
   
   * 로그인 사용자에 대한 접근 제한하기
   
   * 로그인 사용자에 대해 접근을 제한하는 2가지 방법
     
     * The raw way
       
       * **is_authenticated** attribute
     
     * The **login_required** decorator

2. **is-authenticated**
   
   * User model의 속성 중 하나
   
   * 사용자가 인증 되었는지 여부를 알 수 있는 방법
   
   * 모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성
     
     * AnonymousUser에 대해서는 항상 False
   
   * 일반적으로 request.user에서 이 속성을 사용 (request.user.is_authenticated)
   
   * 권한(permission)과는 관련X, 사용자가 활성화 상태(active)이거나 유효한 세션(valid session)을 가지고 있는지도 확인X
     
     * 로그인, 비로그인 사용자인지만 확인
   
   * 적용하기

3. **login_required**
   
   * 데코레이터
   
   * 사용자가 로그인 되어 있으면 정상적으로 view 함수를 실행
   
   * 로그인 하지 않은 사용자의 경우 settings.py의 LOGIN_URL 문자열 주소로 redirect
   
   * [참고] LOGIN_URL 기본값은 /accounts/login/
   
   * 두번째 app이름을 accounts로 했던 이유 중 하나
   
   * /articles/create/로 강제 접속 시도하면
     
     * 로그인 페이지로 리다이렉트 후 /accounts/login/?next=/articles/create/
     
     * 인증 성공 시 사용자가 redirect 되어야하는 경로는 "next"라는 쿼리 문자열 매개 변수에 저장됨

4. **"next" query string parameter**
   
   * 로그인이 정상적으로 진행되면 이전에 요청했던 주소로 redirect하기 위해 Django가 제공해주는 쿼리 스트링 파라미터
   
   * 해당 값을 처리할지 말지는 자유, 별도로 처리해주지 않으면 view에 설정한 redirect 경로로 이동하게 됨
   
   * **주의 사항**
     
     * 만약 login 템플릿에서 form action이 작성되어 있다면 동작하지 않음
     
     * 해당 action 주소 next 파라미터가 작성되어있는 현재 url이 아닌 /accounts/login/으로 요청을 보내기 때문

5. **두 데코레이터로 인해 발생하는 구조적 문제**
   
   * 먼저 비로그인 상태로 detail 페이지에서 게시글 삭제 시도
   
   * delete view 함수의 @login_required로 인해 로그인 페이지로 리다이렉트
   
   * redirect로 이동한 로그인 페이지에서 로그인 진행
   
   * delete view 함수의 @require_POST로 인해 405 상태 코드를 받게 됨
     
     * 405(Method Not Allowed) status code
   
   * 로그인 성공 이후 GET method로 next 파라미터 주소에 리다이렉트 되기 때문
   
   * 두가지 문제가 발생한 것
     
     * redirect 과정에서 POST 요청 데이터의 손실
     
     * redirect로 인한 요청은 GET 요청 메서드로만 요청됨
   
   * 해결방안
     
     * @login_required는 GET request method를 처리할 수 있는 View 함수에서만 사용해야 함
     
     * POST method만 허용하는 delete 같은 함수는 내부에서는 is_authenticated 속성 값을 사용해서 처리
