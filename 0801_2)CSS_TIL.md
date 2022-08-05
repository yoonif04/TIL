## CSS

---

1. **CSS(Cascading Style Sheets)**
   
   * 스타일을 지정하기 위한 언어
   
   * CSS 구문
     
     ```css
     선택자(Selector) {
         속성: 값;   /*선언(Declaration)*/
     }
     
     h1 {
         color: blue;
         font-size: 15px;
     }
     ```
     
     * CSS 구문은 **선택자**를 통해 스타일을 지정할 HTML 요소를 선택
     
     * 중괄호 안에는 **속성과 값**, 하나의 쌍으로 이루어진 **선언**을 진행
     
     * 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미
       
       * **속성 (Property)** : 어떤 스타일 기능을 변경할지 결정
       
       * **값 (Value)** : 어떻게 스타일 기능을 변경할지 결정
   
   * CSS **정의 방법**
     
     * **인라인(inline)**
       
       * 인라인을 쓰게 되면 실수가 잦아짐(중복, 찾기 어려움)
       * 해당 태그에 직접 style 속성을 활용
       
       ```css
       <h1 style='color:blue; font-size:100px'>Hello</h1>
       ```
     
     * **내부 참조(embedding)** - <style>
       
       * head태그 내에 style선언
       
       * 내부 참조를 쓰게 되면 코드가 너무 길어짐
       
       ```css
       <head>
         <style>
           h1 {
           color: blue;
           font-size: 100px;
           }
         </style>   
       </head>
       ```
     
     * **외부 참조(link file)** - 분리된 CSS 파일
       
       * 외부 CSS파일을 <head>내 <link>를 통해 불러오기
       
       * 가장 많이 쓰는 방식
       
       ```css
       <head>
         <link rel='stylesheet' href='이름.css'>
       </head>
       ```
   
   * CSS with **개발자 도구**
     
     * **styles** : 해당 요소에 **선언된** 모든 CSS
     
     * **computed** : 해당 요소에 **최종 계산된** CSS

2. **CSS Selectors**
   
   * **선택자(Selector) 유형**
     
     * **기본 선택자**
       
       * 전체 선택자, 요소 선택자
       
       * 클래스 선택자, 아이디 선택자, 속성 선택자
     
     * **결합자(Combinators)**
       
       * 자손 결합자, 자식 결합자
       
       * 일반 형제 결합자, 인접 형제 결합자
     
     * **의사 클래스/요소(pseudo Class)**
       
       * 링크, 동적 의사 클래스
       
       * 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자
   
   * CSS **선택자 정리**
     
     * **요소 선택자**: HTML 태그를 직접 선택
     
     * **클래스(class) 선택자**: **마침표(.)문자로 시작**하며, 해당 클래스가 적용된 항목을 선택
     
     * **아이디(id)선택자**
       
       * **\#문자로 시작**하며, 해당 아이디가 적용된 항목을 선택
       
       * 일반적으로 하나의 문서에 1번만 사용
       
       * 여러 번 사용해도 동작하지만, 단일 id를 사용하는 것을 권장
   
   * CSS 적용 **우선순위 (cascading order)**
     
     * 1. **중요도(Importance)** - 사용시 주의
          
          * !important
          
          ```css
          h2 {
              color: darkviolet !important;
          }
          ```
       
       2. **우선 순위 (Specificity)**
          
          * **인라인 > id > class, 속성, pseudo-class > 요소, pseudo-element**
       
       3. **CSS 파일 로딩 순서**
   
   * **CSS 상속**
     
     * CSS 상속을 통해 부모 요소의 속성을 자식에게 상속한다.
       
       * 속성(프로퍼티) 중에는 상속이 되는 것과 되지 않는 것들이 있다.
       
       * **상속 되는 것**: **Text 관련 요소**(font, color, text-align), opacity, visibility 등
       
       * **상속 되지 않는 것**: **Box model 관련 요소**(width, height, margin, padding, border, box-sizing, display), **position 관련 요소**(position, top/right/bottom/left, z-index) 등

3. CSS 기본 스타일
   
   * **크기 단위**
     
     * **px (픽셀)**
       
       * 모니터 해상도의 한 화소인 '픽셀' 기준
       
       * 픽셀의 크기는 변하지 않기 때문에 **고정적**인 단위
     
     * **%**
       
       * 백분율 단위
       
       * **가변적인 레이아웃**에서 자주 사용
     
     * **em**
       
       * (바로 위, 부모 요소에 대한) **상속의 영향**을 받음
       
       * 배수 단위, 요소에 지정된 사이즈에 **상대적인 사이즈**를 가짐
     
     * **rem**
       
       * (바로 위, 부모 요소에 대한) 상속의 영향을 받지 않음
       
       * **최상위 요소(html)의 사이즈**를 기준으로 **배수 단위**를 가짐
   
   * **크기 단위 (viewport)**
     
     * 웹 페이지를 방문한 유저에게 바로 보이게 되는 웹 컨텐츠의 영역 (**디바이스 화면**)
     
     * 디바이스의 viewport를 기준으로 **상대적인 사이즈**가 결정됨
     
     * vw, vh, vmin, vmax
     
     * px는 브라우저의 크기를 변경해도 그대로
     
     * **vw**는 브라우저의 크기에 따라 **크기가 변함**
   
   * **색상 단위**
     
     * **색상 키워드** (background-color: red;)
       
       * **대소문자를 구분하지 않음**
       
       * red, blue, black과 같은 특정 색을 직접 글자로 나타냄
     
     * **RGB** (background-color: rgb(0, 255, 0);)
       
       * 16진수 표기법 혹은 함수형 표기법을 사용해서 특정 색을 표현하는 방식
       * **'#' + 16진수** 표기법
       * **rgb() 함수형** 표기법
     
     * **HSL 색상**
       
       * **색상, 채도, 명도**를 통해 특정 색을 표현하는 방식
     
     * a는 alpha(투명도)
   
   * CSS 문서 표현 
     
     * 텍스트
       
       * 서체(**font-family**), 서체 스타일(**font-style**, **font-weight** 등)
       
       * 자간(**letter-spacing**), 단어 간격(**word-spacing**), 행간(**line-height**)등
     
     * 컬러(**color**), 배경(**background-image**, **background-color**)
     
     * 기타 HTML 태그별 스타일링
       
       * 목록(**li**), 표(**table**)

4. Selectors 심화
   
   * **결합자 (Combinators)**
     
     * **자손 결합자(공백)** : selectorA **하위의 모든** selectorB 요소
     
     * **자식 결합자(>)** : selectorA **바로 아래**의 selectorB 요소
     
     * **일반 형제 결합자(~)** : selectorA의 **형제 요소 중 뒤에 위치하는** selectorB요소를 모두 선택
     
     * **인접 형제 결합자(+)** : selectorA의 **형제 요소 중 바로 뒤에 위치하는** selectorB요소를 선택

5. **CSS Box model**
   
   * **CSS 원칙1**: 모든 요소는 **네모(박스모델)** 이고, 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다. (**좌측 상단에 배치**)
   
   * **Box model**
     
     * 모든 HTML 요소는 box 형태로 되어있음
     
     * 하나의 박스는 **네 부분(영역)** 으로 이루어짐: margin, border, padding, content
     
     * **margin**: 테두리 바깥의 외부 여백. 배경색 지정X
       
       * margin-top, margin-right, margin-bottom, margin-left
       
       * margin shorthand
     
     * **border**: 테두리 영역
       
       * border-width, border-style, border-color
       
       * border shorthand
     
     * **padding**: 테두리 안쪽의 내부 여백. 요소에 적용된 배경색, 이미지는 padding까지 적용
     
     * **content**: 글이나 이미지 등 요소의 실제 내용
     
     * **box-sizing**
       
       * 기본적으로 모든 요소의 box-sizing은 content-box
         
         * padding을 제외한 **순수 contents 영역만을 box로 지정**
       
       * 다만, 우리가 일반적으로 영역을 볼 때는 **border까지의 너비를 100px 보는 것을 원함**
         
         * 그 경우 **box-sizing을 border-box로** 설정

6. **Display**
   
   * **CSS 원칙2**: **display에 따라 크기와 배치가 달라진다.**
   
   * 대표적으로 활용되는 display
     
     * display : **block**
       
       * 줄 바꿈이 일어나는 요소
       
       * 화면 크기 전체의 가로 폭을 차지
       
       * 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음.
     
     * display : **inline**
       
       * 줄 바꿈이 일어나지 않는 행의 일부 요소
       
       * content 너비만큼 가로 폭을 차지
       
       * width, height, margin-top, margin-bottom **지정 불가**
       
       * **상하 여백은 line-height**로 지정한다.
   
   * **블록 레벨 요소와 인라인 레벨 요소**
     
     * **블록 레벨 요소**: div / ul, ol, li / p / hr / form 등
     
     * **인라인 레벨 요소**: span / a / img / input, label / b, em, i, strong 등
   
   * 속성에 따른 수평 정렬
     
     * margin
     
     * text-align: 부모 요소에 사용해야
   
   * display
     
     * display: **inline-block**
       
       * block과 inline레벨 요소의 특징을 모두 가짐
       
       * inline처럼 한 줄에 표시할 수 있고, block처럼 width, height, margin 속성 모두 지정 가능
     
     * display: **none**
       
       * 해당 요소를 화면에 표시하지 않고, **공간조차 부여X**
       
       * **visibility: hidden**은 해당 요소가 **공간은 차지**하나 **화면에 표시X**

7. **CSS Position**
   
   * 문서 상에서 요소의 위치를 지정
   
   * **static** : 모든 태그의 **기본 값**(기준 위치)
     
     * 일반적인 요소의 배치 순서에 따름 (**좌측 상단**)
     
     * 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치 됨
   
   * 아래는 좌표 프로퍼티(top, bottom, left, right)를 사용하여 이동 가능 
     
     * **relative** : 상대 위치
       
       * **자기 자신의 static 위치를 기준**으로 이동 (**normal flow 유지**)
       
       * 레이아웃에서 요소가 **차지하는 공간은 static일 때와 같음** (normal position 대비 offset)
     
     * **absolute** : 절대 위치
       
       * 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음 (**normal flow에서 벗어남**)
       
       * **static이 아닌** 가장 가까이 있는 **부모/조상 요소를 기준**으로 이동 (없는 경우 브라우저 화면 기준 이동)
     
     * **fixed** : 고정 위치
       
       * 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 **공간을 차지하지 않음** (**normal flow에서 벗어남**)
       
       * 부모 요소와 관계없이 viewport를 기준으로 이동
         
         * **스크롤 시에도 항상 같은 곳**에 위치함
     
     * **sticky**: 스크롤에 따라 **static -> fixed**로 변경
       
       * 속성을 적용한 박스는 평소에 문서 안에서 **position: static** 상태와 같이 일반적인 흐름에 따르지만 **스크롤 위치가 임계점**에 이르면 **position: fixed**와 같이 박스를 화면에 고정할 수 있는 속성
     
     * absolute vs relative
       
       * **absolute**는 normal flow에서 벗어남 -> **다음 블록 요소**가 **좌측 상단**으로 붙음
       
       * **relative**는 normal flow 유지 -> 실제 위치는 그대로, 사람 눈에만 이동
   
   * CSS 원칙
     
     * CSS 원칙 1,2: Normal flow
       
       * 모든 요소는 네모(박스모델), 좌측상단에 배치
       
       * display에 따라 크기와 배치가 달라짐
     
     * CSS 원칙 3
       
       * position으로 **위치의 기준을 변경**
         
         * relative : 본인의 원래 위치
         
         * absolute : 특정 부모의 위치
         
         * fixed : 화면의 위치
         
         * sticky : 기본적으로 static이나 스크롤 이동에 따라 fixed로 변경

## 개발자 도구

----

1. 크롬 개발자 도구
   
   * 주요 기능
     
     * Elements - DOM 탐색 및 CSS 확인 및 변경
       
       * Styles: 요소에 적용된 CSS 확인
       
       * Computed: 스타일이 계산된 최종 결과
       
       * Event Listeners: 해당 요소에 적용된 이벤트 (JS)
     
     * Sources, Network, Performance, Application, Security, Audits 등
