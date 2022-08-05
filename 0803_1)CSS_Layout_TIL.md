## CSS Layout

-----

1. CSS layout techniques
   
   * Display
   
   * Position
   
   * Float(CSS1, 1996)
   
   * Flexbox (2012)
   
   * Grid (2017)
   
   * 기타
     
     * Responsive Web Design(2010), Media Queries(2012)

2. **float**
   
   * CSS 원칙1: Normal Flow
     
     * 모든 요소는 네모(박스모델)이고, 위->아래, 왼->오른쪽으로 쌓인다. (좌측상단)
     
     * 어떤 요소를 감싸는 형태로 배치는? 혹은 좌/우측에 배치는?
   
   * **Float**
     
     * 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함 인라인요소들이 주변을 wrapping하도록 함
     
     * 요소가 Normal flow를 벗어나도록 함
   
   * Float **속성**
     
     * **none** : 기본값
     
     * **left** : 요소를 왼쪽으로 띄움
     
     * **right** : 요소를 오른쪽으로 띄움
     
     ```html
     <head>
         <style>
             /* css 작성 */
             .box {
                 width: 150px;
                 height: 150px;
                 border: 1px solid black;
                 background-color: crimson;
                 margin: 20px;
             }
             .left {
                 float: left;
             }
             .right {
                 float: right;
             }
         </style>
     </head>
     <body>
         <!-- 클래스 선택자 . -->
         <!-- 자동완성 div.box*3 -->
         <div class="box left">float left</div>
         <!-- <div class="box left">float left</div> -->
         <!-- <div class="box right">float right</div> -->
         <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ea harum esse doloribus sint ullam, quae nostrum quod et, placeat fugiat consequuntur tempore eaque aut quaerat. Natus vero quae distinctio architecto!
             Lorem ipsum dolor sit amet consectetur adipisicing elit. Non repudiandae unde architecto adipisci, eos dolore tempore excepturi temporibus aliquid, fugiat cupiditate soluta laudantium natus sint consequatur delectus voluptates animi itaque.
             Lorem ipsum dolor sit amet consectetur adipisicing elit. Repudiandae vel tempora quibusdam itaque impedit inventore natus ab aut, sunt nesciunt, doloribus quaerat soluta minus voluptas cumque. Ducimus qui earum rerum!
             Lorem ipsum dolor sit amet consectetur adipisicing elit. Repudiandae vel tempora quibusdam itaque impedit inventore natus ab aut, sunt nesciunt, doloribus quaerat soluta minus voluptas cumque. Ducimus qui earum rerum!
             Lorem ipsum dolor sit amet consectetur adipisicing elit. Repudiandae vel tempora quibusdam itaque impedit inventore natus ab aut, sunt nesciunt, doloribus quaerat soluta minus voluptas cumque. Ducimus qui earum rerum!
             Lorem ipsum dolor sit amet consectetur adipisicing elit. Repudiandae vel tempora quibusdam itaque impedit inventore natus ab aut, sunt nesciunt, doloribus quaerat soluta minus voluptas cumque. Ducimus qui earum rerum!
         </p>
     </body>
     ```

3. **flexbox**
   
   * CSS Flexibla Box Layout
     
     * 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델
     
     * **축**
       
       * **main axis (메인 축)**
       
       * **cross axis (교차 축)**
     
     * **구성 요소**
       
       * **Flex Container (부모 요소)**
         
         * flex는 부모 요소에 적용
         * flebox item들이 놓여있는 영역
         * **display 속성을 flex 혹은 inline-flex**로 지정
         
         ```css
         .flex-container {
             display: flex;
         }
         ```
       
       * **Flex Item (자식 요소)**
         
         * 컨테이너에 속해 있는 컨텐츠
   
   * CSS Flexible Box Layout
     
     * 이전까지 Normal Flow를 벗어나는 수단은 Float 혹은 Position
     
     * (수동 값 부여 없이) 1. 수직 정렬 2. 아이템의 너비와 높이 혹은 간격을 동일하게 배치
   
   * Flex **속성**
     
     * **배치 설정**: flex-direction, flex-wrap
     
     * **공간 나누기**: justify-content (main axis), align-content (cross axis)
     
     * **정렬**: align-items (모든 아이템을 cross axis 기준으로), align-self (개별 아이템)
   
   * Flex 속성 : **flex-direction**
     
     * **Main axis 기준** 방향 설정
     
     * 역방향의 경우 HTML 태그 선언 순서와 시각적으로 다르니 유의 (웹 접근성에 영향)
     
     * 1)row, 2)row - reverse, 3)column, 4)column-reverse
   
   * Flex 속성 : **flex-wrap**
     
     * 아이템이 **컨테이너를 벗어나는 경우** **해당 영역 내에 배치되도록** 설정
     
     * 즉, 기본적으로 컨테이너 영역을 벗어나지 않도록 함
     
     * 1)wrap, 2)nowrap
   
   * Flex 속성 : **flex-direction & flex-wrap**
     
     * **flex-direction** : Main axis의 방향을 설정
     
     * **flex-wrap** : 요소들이 강제로 한 줄에 배치 되게 할 것인지 여부 설정
       
       * **nowrap (기본 값)** : **한 줄**에 배치
       
       * **wrap** : 넘치면 그 다음 줄로 배치
     
     * **flex-flow**
       
       * flex-direction과 flex-wrap의 **shorthand**
       
       * flex-direction과 flex-wrap에 대한 설정 값을 차례로 작성
       
       * 예시) flex-flow: row nowrap;
   
   * Flex 속성 : **justify-content**
     
     * **Main axis를 기준**으로 **공간 배분**
     
     * 1)flex-start, 2)flex-end, 3)center, 4)space-between, 5)space-around, 6)space-evenly
   
   * Flex 속성 : **align-content**
     
     * **Cross axis를 기준**으로 **공간 배분** (아이템이 한 줄로 배치되는 경우 확인할 수 없음)
     
     * 1)flex-start(기본값), 2)flex-end, 3)center, 4)space-between, 5)space-around, 6)space-evenly
   
   * Flex 속성 : **align-items**
     
     * **모든 아이템**을 **Cross axis를 기준**으로 정렬
     
     * 1)stretch, 2)flex-start, 3)flex-end, 4)center, 5)baseline
   
   * Flex 속성 : **align-self**
     
     * **개별 아이템**을 **Cross axis 기준**으로 정렬
       
       * 주의! 해당 속성은 컨테이너에 적용하는 것이 아니라 개별 아이템에 적용
     
     * 1)stretch, 2)flex-start, 3)flex-end, 4)center, 5)baseline
   
   * Flex 속성 : align-items & align-self
     
     * Cross axis를 중심으로
       
       * 1)stretch(기본 값), 2)flex-start, 3)flex-end, 4)center, 5)baseline: 텍스트 baseline에 기준선을 맞춤
   
   * Flex에 적용하는 속성
     
     * 기타 속성 (p.33)
       
       * **flex-grow** : 남은 영역을 아이템에 분배
       
       * **order** : 배치 순서
         
         * 숫자가 클수록 순서가 밀린다.
       
       ```html
       <div class="flex_item grow-1 order-3"></div>
       ```
   
   * 활용 레이아웃
     
     * 수직 수평 가운데 정렬
       
       ```css
       .container{
           display: flex;
           justify-content: center;
           align-items: center;
       }
       /*방법2*/
       .container{
           display: flex;
       }
       .item {
           margin: auto;
       }
       ```
     
     * 카드 배치
       
       ```css
       #layout_03{
           display: flex;
           flex-direction: column;
           flex-wrap: wrap;
           justify-content: space-aroud;
           align-content: space-around;
       }
       
       #layout_03{
           display: flex;
           flex-direction: row;
           flex-wrap: wrap;
           justify-content: space-aroud;
           align-content: space-around;
       }
       ```

4. 
