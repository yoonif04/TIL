## 0. 목차

---

1. Managing static files

2. Image Upload

3. Image Resizing

4. QuerySet API Advanced

## 1. Managing static files

----

0. 개요
   
   * 개발자가 서버에 미리 준비한 혹은 사용자가 업로드한 정적파일을 클라이언트에게 제공하는 방법

1. **Static files**
   
   * **정적 파일**
     
     * 응답할 때 별도의 처리 없이 파일 내용을 <u>그대로 보여주면 되는</u> 파일
       
       * 요청한 것을 그대로 보여주는 파일
     
     * **파일 자체가 고정**되어 있고, 서비스 중에도 추가되거나 변경되지 않고 고정
       
       * ex) 웹 사이트는 일반적으로 이미지, 자바 스크립트 또는 CSS와 같은 미리 준비된 추가 파일(움직이지 않는)을 제공해야 함
     
     * Django는 이러한 파일은 "static file"이라 함
       
       * **staticfiles** 앱을 통해 정적 파일과 관련된 기능을 제공
   
   * **Media File**
     
     * 미디어 파일
     
     * 사용자가 웹에서 업로드하는 정적 파일 (user-uploaded)
     
     * <u>유저가 업로드</u>한 <u>모든 정적 파일</u>
   
   * **웹 서버와 정적 파일**
     
     * 웹 서버의 기본 동작
       
       * 특정 위치(URL)에 있는 자원을 요청(HTTP request) 받아서
       
       * 응답(HTTP response)을 처리하고 제공(serving)하는 것
     
     * 이는 "자원과 자원에 접근 가능한 주소가 있다"라는 의미
       
       * ex) 사진 파일은 자원이고 해당 사진 파일을 얻기 위한 경로인 웹 주소(URL)가 존재
     
     * 즉, 웹 서버는 요청 받은 URL로 서버에 존재하는 정적 자원(static resource)

2. **Static files 구성하기**
   
   * Django에서 정적파일 구성하고 사용하기 위한 **단계**
     
     * INSTALLED_APPS에 django.contrib.staticfiles 포함 여부 확인
     
     * settings.py에서 STATIC_URL 정의하기
     
     * 앱의 static 폴더에 정적 파일을 위치하기
       
       * ex) my_app/static/sample_img.jpg
     
     * 템플릿에서 static 템플릿 태그를 사용하여 지정된 경로에 있는 정적 파일의 URL 만들기
       
       * {% load static %}
       
       * <\img src="{% static 'sample_img.jpg' %}" alt="">
   
   * Django template tag
     
     * load tag: **{% load %}**
       
       * 특정 라이브러리, 패키지에 등록된 모든 템플릿 태그와 필터를 로드
     
     * static tag: **{% static '' %}**
       
       * STATIC_ROOT에 저장된 정적 파일에 연결
   
   * Static files 관련 **Core Settings**
     
     * **STATIC_ROOT**
       
       * Default: None
       
       * Django 포르젝트에서 사용하는 모든 정적 파일을 한곳에 모아 넣는 경로
       
       * **collectstatic**이 <u>배포를 위해</u> 정적 파일을 수집하는 디렉토리의 <u>절대 경로</u>
       
       * 개발 과정에서 settings.py의 **DEBUG 값이 True** -> 해당 값은 **작용되지 X**
       
       * 실 서비스 환경에서 Django의 모든 정적 파일을 **다른 웹 서버가 직접 제공**하기 위해 사용
       
       * 배포 환경에서는 Django를 직접 실행X -> 다른 서버에 의해 실행 -> 실행하는 다른 서버는 Django에 내장되어 있는 정적 파일들을 인식X (내장되어 있는 정적 파일들을 밖으로 꺼내는 이유)
     
     * **STATICFILES_DIRS**
       
       * Default: [] (Empty list)
       
       * app/static/ 디렉토리 경로를 사용하는 것(기본 경로) 외에 **추가적인 정적 파일 경로 목록**을 정의하는 리스트
       
       * 추가 파일 디렉토리에 대한 전체 경로를 포함하는 문자열 목록으로 작성되어야 함
     
     * **STATIC_URL**
       
       * Default: None
       
       * STATIC_ROOT에 있는 정적 파일을 참조할 때 사용할 URL
       
       * 개발 단계에서는 실제 정적 파일들이 저장되어 있는<u> app/static/ 경로(기본 경로) 및 STATICFILES_DIRS에 정의된 추가 경로들을 탐색</u>
       
       * 실제 파일이나 디렉토리가 아니며, URL로만 존재
       
       * **비어있지 않은 값**으로 설정한다면 -> **반드시 slash(/)로 끝나야 함**
   
   * **[참고] collectstatic**
     
     * STATIC_ROOT에 Django 프로젝트의 모든 정적 파일을 수집
     
     * settings.py에 STATIC_ROOT = BASE_DIR / 'staticfiles' 작성
     
     * \$ python manage.py collectstatic
   
   * **[참고] 소프트웨어 배포 (Deploy)**
     
     * 프로그램 및 애플리케이션을 <u>서버와 같은 기기에 설치</u>하여 <u>서비스를 제공</u>하는 것
     
     * 클라우드 컴퓨팅 서비스(AWS, Google Cloud, MS Azure 등)에 프로그램 및 애플리케이션을 설치해 제공하는 것

3. **Static files 사용하기**
   
   * static file 가져오기 2가지 방법
     
     * 기본 경로에 있는 static file 가져오기
       
       * articles/static/articles 경로에 이미지 파일 배치하기
       
       * static tag를 사용해 이미지 파일 출력하기
     
     * 추가 경로에 있는 static file 가져오기
       
       * 추가 경로 작성
         
         * STATICFILES_DIRS = []
   
   * STATIC_URL 확인하기
     
     * Django가 해당 이미지를 클라이언트에게 응답하기 위해 만든 image url 확인하기
     
     * "STATIC_URL + static file 경로"로 설정됨
     
     * 개발자도구 - Network에서 Request URL 확인해보기

## 2. Image Upload

---

0. 개념
   
   * Django ImageField를 사용해 사용자가 업로드한 정적 파일(미디어 파일) 관리하기

1. **ImageField()**
   
   * ImageField()
     
     * 이미지 업로드에 사용하는 모델 필드
     
     * FileField를 상속받는 서브 클래스 -> FileField의 모든 속성 및 메서드를 사용 가능
     
     * 사용자에 의해 업로드된 객체가 유효한 이미지인지 검사
     
     * ImageField 인스턴스는 최대 길이가 100자인 문자열로 DB에 생성되며, max_length 인자를 사용해 최대 길이 변경 가능
   
   * **FileField(upload_to='', storage=None, max_length=100, \*\*options)**
     
     * 파일 업로드에 사용하는 모델 필드
     
     * 2개의 선택인자
   
   * FileField / ImageField를 사용하기 위한 **단계**
     
     * **settings.py**에 **MEDIA_ROOT**, **MEDIA_URL** 설정
     
     * **upload_to 속성**을 정의하여 업로드 된 파일에 사용할 **MEDIA_ROOT의 하위 경로 지정**(선택사항)
   
   * **MEDIA_ROOT**
     
     * Default: ''
     
     * 사용자가 업로드한 파일(미디어 파일)들을 보관할 디렉토리의 **절대 경로**
     
     * Django는 성능을 위해 업로드 파일은 DB에 저장X
       
       * **DB에 저장**되는 것 -> "**파일 경로**"
     
     * MEDIA_ROOT는 <u>STATIC_ROOT와 반드시 다른 경로</u>로 지정해야 함
   
   * **MEDIA_URL**
     
     * Default: ''
     
     * MEDIA_ROOT에서 제공되는 미디어 파일을 처리하는 URL
     
     * 업로드된 파일의 주소(URL)를 만들어 주는 역할
       
       * 웹 서버 사용자가 사용하는 public URL
     
     * **비어 있지 않은 값**으로 설정한다면 **반드시 slash(/)로 끝나야함**
     
     * MEDIA_URL은 <u>STATIC_URL과 반드시 다른 경로</u>로 지정해야 함
   
   * 개발단계에서 사용자가 **업로드한 미디어 파일 제공하기**
     
     * 사용자로부터 업로드된 파일이 프로젝트에 업로드 되고나서, 실제로 사용자에게 제공하기 위해서는 업로드된 파일의 URL이 필요함
       
       * 업로드된 파일의 URL == **settings.MEDIA_URL**
       
       * 위 URL을 통해 참조하는 파일의 실제 위치 == **settings.MEDIA_ROOT**

2. CREATE
   
   * ImageField 작성 - models.py
   
   * **Model field option**
     
     * **blank**
       
       * Default: False
       
       * True인 경우 필드를 비워둘 수 있음
         
         * DB에는 ''(빈 문자열)이 저장됨
       
       * 유효성 검사에서 사용 됨(is_valid)
         
         * Validation-related
         
         * 필드에 blank=True가 있으면 form 유효성 검사에서 빈 값을 입력할 수 있음
     
     * **null**
       
       * Default: False
       
       * True인 경우 Django는 빈 값을 DB에 NULL로 저장
         
         * Database-related
   
   * **null 관련 주의사항**
     
     * CharField, TextField와 같은 문자열 기반 필드 -> null 옵션 사용 피해야함
       
       * 데이터 없음에 대한 표현 -> 빈 문자열, NULL 2가지 모두 가능하게 됨
       
       * 데이터 없음에 대한 표현에 두개의 가능한 값을 갖는 것은 좋지 않음
       
       * Django는 문자열 기반 필드에서 NULL이 아닌 빈 문자열을 사용하는 것이 규칙
   
   * **Migrations**
     
     * ImageField를 사용하려면 반드시 Pillow 라이브러리 필요
   
   * **[참고] Pillow**
     
     * 광범위한 파일 형식 지원, 효율적이고 강력한 이미지 처리 기능을 제공하는 라이브러리
     
     * 이미지 처리 도구를 위한 견고한 기반 제공
   
   * Image 필드 출력 확인
     
     * 하지만 이미지가 업로드 되지 않음
     
     * 파일 또는 이미지 업로드시에는 **form 태그에 enctype 속성**을 다음과 같이 변경해야 함
       
       * **enctype = "multipart/form-data"**
   
   * [참고] form 태그의 enctype(인코딩) 속성 값
     
     * aplication/x-www-form-urlencoded
       
       * 기본값
       
       * 모든 문자 인코딩
     
     * multipart/form-data
       
       * 파일/이미지 업로드 시에 반드시 사용해야 함
       
       * 전송되는 데이터의 형식을 지정
       
       * \<input type = "file">을 사용할 경우 사용
     
     * text/plain
   
   * **request.FILES**
     
     * 파일 및 이미지는 request의 POST 속성값으로 넘어가지 않고 FILES 속성 값에 담겨 넘어감
   
   * **[참고] request.FILES가 두번째 위치 인자인 이유**
     
     * BaseModelForm Class의 생성자 함수 살펴보기
   
   * 이미지 첨부하기
     
     * 이미지를 첨부한 경우는 MEDIA_ROOT 경로에 이미지가 업로드 됨
     
     * 만약 같은 이름의 파일 업로드 -> 파일 이름 끝에 임의의 난수 값을 붙여 저장

3. **READ**
   
   * 업로드 이미지 출력하기
     
     * 업로드된 파일의 상대 URL은 Django가 제공하는 url 속성을 통해 얻을 수 있음
     
     * article.image.url - 업로드 파일의 경로
     
     * article.image - 업로드 파일의 파일 이름
     
     * 이미지 데이터가 있는 경우만 이미지 출력할 수 있도록 처리

4. **UPDATE**
   
   * 개요
     
     * 이미지는 바이너리 데이터 -> 텍스트처럼 일부만 수정X
     
     * 새로운 사진으로 대체하는 방식을 사용
   
   * 업로드 이미지 수정하기
     
     * update.html에서 enctype 속성값 추가
     
     * views.py에서 이미지 파일이 담겨있는 request.FILES 추가 작성

5. **'upload_to' argument**
   
   * 사용자 지정 업로드 경로와 파일 이름 설정하기
     
     * ImageField는 업로드 디렉토리와 파일 이름을 설정하는 2가지 방법 제공
       
       * 문자열 값이나 경로 지정 방법
         
         * upload_to 인자에 새로운 이미지 저장 경로를 추가 후 migration 과정 진행
         
         * 단순 문자열 뿐만 아니라 파이썬 time 모듈의 strftime() 형식도 포함될 수 있으며, 이는 파일 업로드 날짜/시간으로 대체됨
       
       * 함수 호출 방법
         
         * upload_to는 독특하게 함수처럼 호출이 가능하며 해당 함수가 호출되면서 반드시 2개의 인자를 받음
         
         * instance
           
           * FileField가 정의된 모델의 인스턴스
           
           * 대부분 이 객체는 아직 DB에 저장되기 전이므로 아직 PK값이 없을 수 있으니 주의
         
         * filename
           
           * 기존 파일 이름

## 3. Image Resizing

---

0. 개요
   
   * 실제 원본 이미지를 서버에 그대로 로드하는 것은 여러 이유로 부담이 큼
   
   * HTML \<img> 태그에서 직접 사이즈를 조정할 수도 있지만, 업로드될 때 이미지 자체를 resizing하는 것을 사용해 볼 것

1. **사전 준비**
   
   * django-imagekit 모듈 설치 및 등록
   
   * [참고] django-imagekit
     
     * 이미지 처리를 위한 Django 앱
       
       * 썸네일, 해상도, 사이즈, 색깔 등을 조정 가능
   
   * **썸네일 만들기**
     
     * 2가지 방식으로 
     
     * 원본 이미지 저장X
     
     * 원본 이미지 저장O
       
       * 기본적으로 원본 이미지가 업로드되고 출력됨
       
       * detail.html에서 article.image_thumbnail.url 추가
       
       * 썸네일이 사용되었을때만 resizing한 이미지 생성
       
       * 이미지가 출력되는 다른 detail 페이지에 이동할 때마다 썸네일 생성됨
   
   * [참고] pilkit

## 4. QuerySet API Advanced

----

1. 사전 준비

2. **CRUD 기본**
   
   * 모든 user 레코드 조회: User.objects.all()
   
   * user 레코드 생성
   
   * 101번 user 레코드 조회
   
   * 101번 user 레코드의 last_name을 김으로 수정
   
   * 101번 user 레코드 삭제
   
   * 전체 인원 수 조회
     
     * **.count()**
       
       * QuerySet과 일치하는 데이터베이스의 개체 수를 나타내는 정수를 반환
       
       * .all()을 사용하지 않아도 됨
     
     * 파이썬의 len함수 활용
       
       * len(User.objects.all())

3. **Sorting data**
   
   * 나이가 어린 순으로 이름과 나이 조회하기
     
     * **.order_by(\*fields)**
       
       * QuerySet의 정렬을 재정의
       
       * 기본적으로 오름차순으로 정렬하며, 필드명에 **'-'(하이픈)을 작성하면 내림차순**으로 정렬
       
       * 인자로 **'?'를 입력하면 랜덤**으로 정렬
     
     * **.values(\*fields, \*\*expressions)**
       
       * 모델 인스턴스가 아닌 딕셔너리 요소들을 가진 QuerySet을 반환
       
       * \*fields는 선택인자, 조회하고자하는 필드명을 가변인자로 입력 받음
         
         * **필드를 지정** -> 각 딕셔너리에는 **지정한 필드에 대한 key와 value**만을 출력
         
         * **입력하지 않을 경우** -> 각 딕셔너리에는 레코드의 **모든 필드에 대한 key와 value**를 출력
   
   * 이름과 나이를 나이가 많은 순서대로 조회하기
   
   * 이름, 나이, 계좌 잔고를 나이가 어린순으로, 만약 같은 나이라면 계좌 잔고가 많은 순으로 정렬해서 조회하기
   
   * **[참고] order_by 주의사항**
     
     * order_by를 여러번 호출 -> 마지막 호출만 적용됨

4. Filtering data
   
   * 중복없이 모든 지역 조회하기
     
     * **.distinct()**
   
   * 지역 순으로 오름차순 정렬하여 중복없이 모든 지역 조회하기
   
   * 이름과 지역이 중복없이 모든 이름과 지역 조회하기
   
   * 이름과 지역 중복없이 지역 순으로 오름차순 정렬하여 모든 이름과 지역 조회하기
   
   * 나이가 30인 사람들의 이름 조회
   
   * 나이가 30살 이상인 사람들의 이름과 나이 조회하기
   
   * **Field lookups**
     
     * SQL WHERE절의 상세한 조건을 지정하는 방법
     
     * QuerySet 메서드 filter(), exclude() 및 get()에 대한 키워드 인자로 사용됨
     
     * 문법 규칙
       
       * 필드명 뒤에 "double-underscore" 이후 작성함
   
   * 나이가 30살 이상이고 계좌 잔고가 50만원 초과인 사람들의 이름, 나이, 계좌 잔고 조회하기
   
   * 이름에 '호'가 포함되는 사람들의 이름과 성 조회하기
     
     * **contains**
   
   * 핸드폰 번호가 011로 시작하는 사람들의 이름과 핸드폰 번호 조회
     
     * SQL에서의 '%'와일드 카드와 같음
     
     * '\_'(under score)는 별도로 정규 표현식을 사용해야 함
     
     * **startswith**
   
   * 이름이 '준'으로 끝나는 사람들의 이름 조회하기
     
     * **endswith**
   
   * 경기도 혹은 강원도에 사는 사람들의 이름과 지역 조회하기
     
     * **in**
   
   * 경기도 혹은 강원도에 살지 않는 사람들의 이름과 지역 조회하기
     
     * **.exclude(\*\*kwargs)**
       
       * 주어진 매개변수와 일치하지 않는 객체를 포함하는 QuerySet 반환
   
   * 나이가 가장 어린 10명의 이름과 나이 조회하기
     
     * 슬라이싱 활용
   
   * 나이가 30이거나 성이 김씨인 사람들 조회
     
     * 'Q' objects
       
       * 기본적으로 filter()와 같은 메서드의 키워드 인자는 AND statement를 따름
       
       * 만약 더 복잡한 쿼리를 실행해야 하는 경우가 있다면 Q 객체가 필요함
         
         * ex) OR statement 같은 경우
         
         * from django.db.models import Q
       
       * '&' 및 '|'를 사용하여 Q 객체를 결합할 수 있음
       
       * 조회를 하면서 여러 Q 객체를 제공할 수도 있음

5. **Aggregation(Grouping data)**
   
   * **aggregate()**
     
     * 전체 queryset에 대한 값을 계산
     
     * 특정 필드 전체의 합, 평균, 개수 등을 계산할 때 사용
     
     * 딕셔너리를 반환
     
     * aggregation functions: **Avg, Count, Max, Min, Sum 등**
   
   * 나이가 30살 이상인 사람들의 평균 나이 조회하기
     
     * from django.db.models import Avg
     
     * .aggregate(Avg('이름'))
       
       * 딕셔너리 key 이름을 수정할 수도 있다.
         
         * .aggregate(avg_value=Avg('이름'))
   
   * 가장 높은 계좌 잔액 조회하기
   
   * 모든 계좌 잔액 총액 조회하기
   
   * **annotate()**
     
     * 쿼리의 각 항목에 대한 **요약 값**을 계산
     
     * SQL의 **GROUP BY**에 해당
     
     * '주석을 달다'라는 사전적 의미를 가지고 있음
   
   * 각 지역별로 몇 명씩 살고 있는지 조회하기
   
   * 각 지역별로 몇 명씩 살고 있는지 + 지역별 계좌 잔액 평균 조회하기
   
   * 각 성씨가 몇 명씩 있는지 조회하기
   
   * N:1 예시
     
     * 'comment' -> 모델 이름
