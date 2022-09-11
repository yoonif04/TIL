## 0. Django

----

1. Django Form

2. Django ModelForm

3. Handling HTTP requests

4. View decorators

## 1. Django Form

----

1. 개요
   
   * 지금까지 HTML form, input 태그를 통해서 사용자로부터 데이터를 받았음
   
   * 현재 우리 Django 서버 -> 들어오는 요청을 모두 수용하고 있음 -> 이러한 요청 중에는 비정상적인 혹은 악의적인 요청이 있다는 것을 생각해야함
   
   * 사용자가 입력한 데이터가 **우리가 원하는 데이터 형식**이 맞는지에 대한 **유효성 검증**이 반드시 필요
     
     * 유효성 검증은 많은 부가적인 것들을 고려해서 구현해야 함 -> 개발 생산성을 늦출뿐더러 쉽지 않은 작업
   
   * **Django Form**은 이 과정에서 과중한 작업과 반복 코드를 줄여줌으로써 훨씬 쉽게 유효성 검증을 진행할 수 있도록 만들어 줌

2. Form에 대한 Django의 역할
   
   * Form은 Django의 **유효성 검사 도구 중 하나**로 외부의 악의적 공격 및 데이터 손상에 대한 중요한 방어 수단
   
   * Form과 관련한 유효성 검사를 **단순화하고 자동화**할 수 있는 기능을 제공 -> 개발자가 직접 작성하는 코드보다 더 안전하고 빠르게 수행하는 코드 작성 가능
     
     * 개발자가 필요한 핵심 부분만 집중할 수 있도록 돕는 프레임워크의 특성

3. **Django는 Form에 관련된 작업의 세 부분을 처리**
   
   * **렌더링을 위한 데이터 준비 및 재구성**
   
   * 데이터에 대한 **HTML forms 생성**
   
   * 클라이언트로부터 받은 **데이터 수신 및 처리**

4. The Django Form Class
   
   * Form Class: Django form 관리 시스템의 핵심
   
   * **Form Class 선언**
     
     * Model Class를 선언하는 것과 비슷, 비슷한 이름의 필드 타입을 많이 가짐
     
     * Model과 마찬가지로 상속을 통해 선언 (**forms 라이브러리의 Form 클래스를 상속받음**)
     
     * 앱 폴더에 forms.py를 생성 후 Class 선언
     
     * form에는 model field와 달리 **TextField가 존재X**
     
     * 모델의 TextField처럼 사용하려면 -> 뒤에 나옴
     
     * Form Class를 forms.py에 작성하는 것 -> 규약x
       
       * 파일 이름이 달라도 되고 models.py나 다른 어디에도 작성 가능
       
       * 유지보수, 관행적으로 forms.py 파일 안에 작성 권장
     
     * view 함수, 템플릿 업데이트
       
       * view함수에서 정의한 클래스명From의 인스턴스(form) 하나로 input과 label 태그가 모두 렌더링 됨
   
   * **Form rendering options**
     
     * \<label\> & \<input\> 쌍에 대한 **3가지 출력 옵션**
     
     * **as_p()**: 각 필드가 단락(\<p\>태그)으로 감싸져서 렌더링
     
     * **as_ul()**: 각 필드가 **목록 항목(\<li\> 태그)** 으로 감싸져서 렌더링
       
       * **\<ul\> 태그는 직접 작성**해야 한다.
     
     * **as_table()**: 각 필드가 **테이블(\<tr\>태그)** 행으로 감싸져서 렌더링
   
   * Django의 **2가지 HTML input 요소 표현**
     
     * **Form fields**
       
       * 입력에 대한 **유효성 검사 로직**을 처리
       
       * 템플릿에서 직접 사용됨
     
     * **Widgets**
       
       * 웹 페이지의 HTML input 요소 렌더링을 담당
         
         * input 요소의 **단순한 출력 부분**을 담당
       
       * Widgets은 **반드시 form fields에 할당 됨**

5. Widgets
   
   * 개요
     
     * Django의 HTML input element의 표현 담당
     
     * 단순히 HTML 렌더링을 처리하는 것이며 **유효성 검증과 관계X**
   
   * 적용하기
   
   * 응용하기
     
     * forms.ChoiceField(choices=)

## 2. Django ModelForm

----

1. 개요
   
   * Form Class를 작성하는 것 Model이랑 너무 중복
   
   * 이미 Article Model Class에 필드에 대한 정보를 작성했는데, 이를 Form에 맵핑하기 위해 Form Class에 필드를 재정의 해야만 했음
   
   * ModelForm을 사용하면 이러한 Form을 더 쉽게 작성 가능

2. **ModelForm Class**
   
   * Model을 통해 Form Class를 만들 수 있는 helper class
   
   * ModelForm은 Form과 똑같은 방식으로 View 함수에서 사용
   
   * **ModelForm 선언**
     
     * forms 라이브러리에서 파생된 **ModelForm 클래스 상속**받음
     
     * 정의한 ModelForm 클래스 안에 **Meta 클래스 선언**
     
     * **어떤 모델을 기반으로 form을 작성할 것인지**에 대한 정보를 **Meta 클래스에** 지정
   
   * **ModelForm에서의 Meta Class**
     
     * ModelForm의 정보를 작성하는 곳
     
     * ModelForm을 사용할 경우 **참조할 모델**이 있어야 하는데, **Meta class의 model 속성**이 이를 구성함
       
       * 참조하는 모델에 정의된 field 정보를 Form에 적용함
     
     * **fields 속성**에 **'\_\_all\_\_'** 를 사용하여 모델의 모든 필드를 포함할 수 있음
     
     * **exclude 속성**을 사용하여 모델에서 포함하지 않을 필드를 지정할 수 있음
     
     * fields와 exclude를 함께 작성해도 되나 권장x
   
   * **[참고] Meta data**
     
     * 데이터를 표현하기 위한 데이터
   
   * **[참고] 참조 값과 반환 값**
     
     * 호출하지 않고 이름만 작성하는 방식
     
     * 함수의 이름을 그대로 출력하는 것과 호출 후의 결과 비교
       
       * **함수의 이름**을 출력: **함수의 참조 값**을 출력
       
       * **함수 호출**: **함수의 반환 값** 출력
     
     * 언제 참조 값을 사용할까?
       
       * 함수를 호출하지 않고 함수 자체를 그대로 전달 -> 다른 함수에서 '**필요한 시점에**' 호출하는 경우
       * urlpatterns의 path에 views.index의 경우 -> view함수의 참조 값을 그대로 넘김으로써, path함수가 내부적으로 해당 view 함수를 "필요한 시점에" 사용하기 위해서
       * 클래스도 마찬가지로, 해당 클래스를 필요한 시점에 사용하기 위함 + 이 경우 인스턴스가 필요한 것이 아니라 실제 모델의 참조 값을 통해 **해당 클래스의 필드나 속성 등을 내부적으로 참조**하기 위한 이유도 존재
   
   * **주의 사항**
     
     * 클래스 안에 클래스 - 파이썬의 문법적 개념으로 접근X
     
     * ModelForm의 설계일 뿐

3. **ModelForm with view functions**
   
   * ModelForm으로 인한 view 함수의 구조 변화 알아보기
   
   * **CREATE**
     
     * 유효성 검사를 통과하면
       
       * 데이터 저장 후, 상세 페이지로 리다이렉트
     
     * 통과하지 못하면
       
       * 작성 페이지로 리다이렉트
     
     * **"is_valid()"** method
       
       * 유효성 검사를 실행하고, **데이터가 유효한지 여부를 boolean으로 반환**
       
       * 데이터 유효성 검사를 보장하기 위한 많은 테스트에 대해 Django는 is_valid()를 제공하여 개발자의 편의를 도움
     
     * **form 인스턴스의 errors 속성**
       
       * **is_valid()의 반환 값이 False**인 경우 **form 인스턴스의 errors 속성에 값이 작성됨** -> **유효성 검증을 실패한 원인이 딕셔너리 형태로 저장됨**
       
       * **input태그에 required 속성** -> 아무것도 입력 안하면 **팝업** -> HTML에서
     
     * **"save()"** method
       
       * form 인스턴스에 바인딩(들어간)된 데이터를 통해 **데이터베이스 객체를 만들고 저장**
       
       * ModelForm의 하위 클래스는 키워드 인자 **instance** 여부를 통해 생성할 지, 수정할 지를 결정함 
         
         * **제공X** -> save()는 지정된 모델의 **새 인스턴스를 만듦(CREATE)**
         
         * **제공O** -> save()는 **해당 인스턴스를 수정(UPDATE)**
   
   * **UPDATE**
     
     * ModelForm의 인자 instance는 수정 대상이 되는 객체(기존 객체)를 지정
     
     * **request.POST**: 사용자가 **form을 통해 전송한 데이터** (새로운 데이터)
     
     * **instance: 수정이 되는 대상**
   
   * **Form과 ModelForm**
     
     * ModelForm이 Form보다 더 좋은 것X -> 각자 역할이 다른 것
     
     * **Form**
       
       * 사용자로부터 받는 데이터가 **DB와 연관되어 있지 X** 경우 사용
       
       * DB에 영향X, **단순 데이터만 사용**되는 경우
       
       * 예시: 로그인, 사용자의 데이터를 받아 인증 과정에서만 사용 후 별도로 DB에 저장하지 않음
     
     * **ModelForm**
       
       * 사용자로부터 받는 데이터가 **DB와 연관 O**
       
       * 데이터의 **유효성 검사 끝나면** 데이터를 각각 **어떤 레코드에 맵핑해야 할지 이미 알고 있기 때문에 곧바로 save() 호출이 가능**

4. **Widgets 활용하기**
   
   * 위젯을 작성하는 2가지 방법
     
     * Meta 클래스 내부에 작성
     
     * ModelForm 내부에 각 form별로 작성 -> 권장
   
   * 위젯에서 maxlength 속성 -> 유효성 검사와 무관, 입력 자체를 막음

## 3. Handling HTTP requests

----

1. 개요
   
   * HTTP requests 처리에 따른 view 함수 구조 변화
   
   * new-create, edit-update의 view 함수 역할을 잘 살펴보면 하나의 공통점과 하나의 차이점 존재
   
   * **공통점**
     
     * new-create는 모두 CREATE 로직을 구현하기 위한 공통 목적
     
     * edit-update는 모두 UPDATE 로직을 구현하기 위한 공통 목적
   
   * **차이점**
     
     * new와 edit는 GET 요청에 대한 처리만을
     
     * create와 update는 POST 요청에 대한 처리만을 진행
   
   * 이 공통점과 차이점을 기반으로, 하나의 view 함수에서 **method에 따라 로직 분리되도록 변경**

2. **Create**
   
   * new와 create view 함수를 합침
   * 각각의 역할은 request.method 값을 기준으로 나뉨
   * context의 들여쓰기 위치

3. **Update**
   
   * edit과 update view 함수를 합침

## 4. View decorators

----

1. 개요
   
   * View decorators를 사용해 view 함수를 단단하게 만들기

2. **데코레이터(Decorator)**
   
   * **기존에 작성된 함수에 기능을 추가**하고 싶을 때, 해당 함수를 수정하지 않고 기능을 추가해주는 함수
   
   * Django는 다양한 HTTP 기능을 지원하기 위해 view 함수에 적용할 수 있는 여러 데코레이터를 제공

3. **Allowed HTTP methods**
   
   * 개요
     
     * **django.views.decoration.http**의 데코레이터를 사용하여 요청 메서드를 기반으로 접근을 제한할 수 있음
     
     * **일치X 메서드 요청** -> **405 Method Not Allowed를 반환**
     
     * **메서드 목록**
       
       * require_http_methods()
       
       * require_POST()
       
       * require_safe()
   
   * **[참고] 405 Method Not Allowed** : 요청 방법이 서버에게 전달 but, 사용 불가능한 상태
   
   * **require_http_methods()**
     
     * View 함수가 **특정한 요청 method만 허용**하도록하는 데코레이터
   
   * **require_POST()**
     
     * View 함수가 **POST 요청 method만 허용**하도록 하는 데코레이터
   
   * **require_safe()**
     
     * require_GET이 있지만 Django에서는 require_safe를 사용 권장

## 5. Rendering fields manually

---

## 6. 마무리

----

1. 마무리
   
   * Django Form Class
     
     * Django 프로젝트의 주요 유효성 검사 도구
     
     * 공격 및 데이터 손상에 대한 중요한 방어 수단
     
     * 유효성 검사에 대해 개발자에게 강력한 평의 제공
   
   * View 함수 구조 변화
     
     * HTTP requests 처리에 따른 구조 변화
