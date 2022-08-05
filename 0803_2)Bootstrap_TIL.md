## Bootstrap

---

1. Bootstrap
   
   * quickly, responsive,...
   * CDN: Content Delivery(Distribution) Network
     * 컨텐츠를 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스탬
     * [Get started with Bootstrap · Bootstrap v5.2](https://getbootstrap.com/docs/5.2/getting-started/introduction/)

2. Bootstrap 기본 원리
   
   * **spacing (Margin and padding)**
     
     ```html
     {property}{sides}-{size}
      <!--ex. mt-3-->
     
     <div class="mt-3 ms-5">bootstrap-spacing</div>
     ```
     
     * **property**: margin인지 padding인지 (m, p)
     
     * **sides**: 위치지정. t, b, s, e, x, y, blank
       
       * sides 공백: 4방향
       
       | 약자  | 내용          |
       | --- | ----------- |
       | t   | top         |
       | b   | bottom      |
       | s   | left        |
       | e   | right       |
       | x   | left, right |
       | y   | top,bottom  |
     
     * **size**: 0, 1, 2, 3, 4, 5, auto
       
       * mx-auto: 수평 중앙 정렬, 가로 가운데 정렬
         
         | 약자  | rem     | px   |
         | --- | ------- | ---- |
         | 0   | 0rem    | 0px  |
         | 1   | 0.25rem | 4px  |
         | 2   | 0.5rem  | 8px  |
         | 3   | 1 rem   | 16px |
         | 4   | 1.5rem  | 24px |
         | 5   | 3 rem   | 48px |
   
   * **color**
     
     * primary, secondary, success, danger, warning, info, light, dark
     
     * bg-primary, text-success 등 사용
   
   * **Text**
     
     * text-start, text-center, text-end, text-decoration-none
     
     * fw-bold, fw-normal, fw-light, fst-italic
   
   * **Display**: d-inline, d-block
   
   * **Position**: fixed-top, fixed-bottom

3. Bootstrap 컴포넌트
   
   * Components
     
     - Bootstrap의 다양한 UI 요소를 활용할 수 있음
     
     - Components 탭 및 검색으로 원하는 UI 요소를 찾을 수 있음
     
     - 기본 제공된 Components를 변환해서 활용
   
   * Buttons: 클릭했을 때 어떤 동작이 일어나도록 하는 요소
   
   * Dropdowns: dropdown, dropdown-menu, dropdown-item 클래스를 활용해 옵션 메뉴 만들 수 있다.
   
   * Forms > Form controls: form-control클래스를 사용해 input및 form태그 스타일링 가능
   
   * Navbar: navbar클래스 활용 네비게이션 바 제작 가능
   
   * Carousel: 콘텐츠(사진)을 순환시키기 위한 슬라이드쇼
   
   * Modal
     
     * 사용자와 상호작용 하기 위해서 사용, 긴급 상황 알리는데 주로 사용
     
     * 현재 열려있는 페이지 위 또 다른 레이어
     
     * 페이지 이동시 사라짐(제거안해도 배경 클릭시 사라짐)
     
     * 중첩해서 들어가있으면XX
   
   * Flexbox in Bootstrap
     
     * 클래스에 d-flex justify-content-start와 같은 형식으로 
   
   * Card > Grid Card: 화면이 작아지면 1줄에 표시되는 카드의 개수가 줄어듦
   
   * Responsive Web
     
     * 다양한 화면 크기를 가진 디바이스들이 등장함에 따라 개념이 등장
     
     * 별도의 기술 이름X 웹 디자인에 대한 접근 방식, 사례들의 모음 등을 기술하는데 사용되는 용어

4. bootstrap grid system
   
   * **Grid system (web design)**
     
     * 요소들의 디자인과 배치에 도움을 주는 시스템
     
     * **기본 요소**
       
       * **Column** : **실제 컨텐츠**를 포함하는 부분
       
       * **Gutter** : 칼럼과 칼럼 **사이의 공간** (사이 간격)
       
       * **Container** : Column들을 담고 있는 공간
   
   * Bootstrap grid System
     
     * flex box로 제작됨
     
     * container, rows, column으로 컨텐츠를 배치하고 정렬
     
     * 반드시 기억해야 할 2가지!
       
       * **12개의 column**
       
       * **6개의 grid breakpoints**
   
   * Grid system breakpoints
     
     | Breakpoint        | Class infix | Dimensions |
     | ----------------- | ----------- | ---------- |
     | Extra small       | None        | <576px     |
     | Small             | sm          | >=576px    |
     | Medium            | md          | >=768px    |
     | Large             | lg          | >=992px    |
     | Extra large       | xl          | >=1200px   |
     | Extra extra large | xxl         | >=1400px   |

# 
