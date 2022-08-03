## Bootstrap

---

1. Bootstrap
   
   * quickly, responsive,...
   * CDN: Content Delivery(Distribution) Network
     * 컨텐츠를 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스탬
     * [Get started with Bootstrap · Bootstrap v5.2](https://getbootstrap.com/docs/5.2/getting-started/introduction/)

2. Bootstrap 기본 원리
   
   * spacing (Margin and padding)
     
     ```html
     {property}{sides}-{size}
     mt-3
     
     <div class="mt-3 ms-5">bootstrap-spacing</div>
     ```
     
     * property: margin인지 padding인지 (m, p)
     
     * sides: 위치
       
       * t, b, s, e, x, y, blank
       
       | 약자  | 내용          |
       | --- | ----------- |
       | t   | top         |
       | b   | bottom      |
       | s   | left        |
       | e   | right       |
       | x   | left, right |
       | y   | top,bottom  |
     
     * size
       
       * 0, 1, 2, 3, 4, 5, auto
       
       | 약자  | rem     | px   |
       | --- | ------- | ---- |
       | 0   | 0rem    | 0px  |
       | 1   | 0.25rem | 4px  |
       | 2   | 0.5rem  | 8px  |
       | 3   | 1 rem   | 16px |
       | 4   | 1.5rem  | 24px |
       | 5   | 3 rem   | 48px |
   
   * color
     
     * bg-primary, bg-secondary, bg-danger 등
     
     * text-success, text-danger 등
   
   . Text
     
     * text-start, text-center, text-end, text-decoration-none
     
     * fw-bold, fw-normal, fw-light, fst-italic
   
   . Display
     
     . d-inline, d-block, box
   
   . Position
     
     - fixed-top, fixed-bottom

3. Bootstrap 컴포넌트
   
   . Components
     
     * Bootstrap의 다양한 UI 요소를 활용할 수 있음
     - Components 탭 및 검색으로 원하는 UI 요소를 찾을 수 있음
     
     - 기본 제공된 Components를 변환해서 활용
   
   . Buttons
   
   . Dropdowns
   
   . Forms > Form controls
   
   . Navbar
   
   . Carousel: 콘텐츠(사진)을 순환시키기 위한 슬라이드쇼
   
   . Modal
     
     . 중첩해서 들어가있으면 안됨!!!
   
   . Flexbox in Bootstrap
   
   . Card > Grid Card
   
   . Responsive Web
     
     * 다양한 화면 크기를 가진 디바이스들이 등장함에 따라 개념이 등장
     
     

4. bootstrap grid system
   
   * Grid system (web design)
     
     * 요소들의 디자인과 배치에 도움을 주는 시스템
     
     * 기본 요소
       
       * Column : 실제 컨텐츠를
       
       * Gutter
   
   * Bootstrap grid System
     
     * flex box로 제작됨
     
     * container, rows, column으로 컨텐츠를 배치하고 정렬
     
     * 반드시 기억해야 할 2가지!
       
       * 12개의 column
       
       * 6개의 grid breakpoints
   
   * Grid system breakpoints

## Responsive web

---
