## 0. 목차

----

1. Vuex

2. Lifecycle Hooks

3. Todo with Vuex



## 1. Vuex

----

0. 개요
   
   * 상태 관리가 무엇인지
   
   * Vuex가 무엇인지

1. State Management
   
   * 상태(State): 현재에 대한 정보(data)
   
   * Web Application에서의 상태 -> 현재 App이 가지고 있는 Data
   
   * 여러 개의 component를 조합해서 하나의 App을 만듦
   
   * 각 component는 독립적 -> 각각의 상태(data)를 가짐
   
   * 여러 개의 component가 같은 상태(data)를 유지할 필요가 있음 -> 상태 관리 필요
   
   * Pass Props & Emit Event
   
   * Centralized Store
     
     * 중앙 저장소에 데이터를 모아서 상태 관리
     
     * 각 component는 중앙 저장소의 데이터 사용
     
     * 계층 상관없이 중앙 저장소에 접근해서 데이터를 얻거나 변경 가능
     
     * 중앙 저장소의 데이터가 변경 -> 각각의 component는 해당 데이터의 변화에 반응하여 새로 변경된 데이터를 반영
     
     * 규모가 크거나 컴포넌트 중첩이 깊은 프로젝트의 관리가 매우 편리
   
   * Vuex
     
     * "state management pattern + Library" for vue.js (상태 관리 패턴 + 라이브러리)
     
     * 데이터가 예측 가능한 방식으로만 변경 될 수 있도록하는 규칙을 설정하며, Vue의 반응성을 효율적으로 사용하는 상태 관리 기능을 제공

2. Vuex 시작하기
   
   * 프로젝트 with vuex
     
     * \$ vue create vuex-app
     
     * \$ cd vuex-app
     
     * \$ vue add vuex
   
   * src / store / index.js 가 생성됨
   
   * vuex의 핵심 컨셉 4가지
     
     * **state**
       
       * vue 인스턴스의 data에 해당
       
       * 중앙에서 관리하는 모든 상태 정보
       
       * 개별 component는 state에서 데이터를 가져와서 사용
       
       * state의 데이터가 변화 -> 해당 데이터를 사용(공유)하는 component도 자동으로 다시 렌더링
       
       * \$store.state로 state 데이터에 접근
     
     * **getters**
       
       * vue 인스턴스의 computed에 해당
       
       * state를 활용하여 계산된 값을 얻고자 할 때 사용
         
         * state의 원본 데이터를 건들지X, 계산된 값을 얻을 수 있음
       
       * getters의 결과 -> 캐시(cache), 종속된 값이 변경된 경우에만 재계산
       
       * getters에서 계산된 값 -> state에 영향 미치지 X
       
       * 첫번째 인자: state, 두번째 인자: getter
     
     * **mutations**
       
       * 실제로 **state를 변경**하는 **유일한 방법**
       
       * vue 인스턴스의 methods에 해당하지만 Mutations에서 호출되는 핸들러(handler) 함수는 반드시 **동기적**이어야 함
         
         * 비동기 로직으로 mutations를 사용해서 state를 변경 시 -> state의 변화의 시기를 특정X
       
       * 첫번째 인자로 **state**를 받으며, component 혹은 Actions에서 **commit()** 메서드로 호출됨
       
       * mutation, action에서 호출되는 함수 -> handler 함수
     
     * **actions**
       
       * mutations와 비슷하지만 **비동기 작업 포함 가능**
       
       * state를 직접 변경X, **commit()** 메서드로 **mutations를 호출**해서 state를 변경
       
       * **context** 객체를 인자로 받으며, 이 객체를 통해 store.js의 모든 요소와 메서드에 접근 가능(== 즉, state를 직접 변경 가능 but, 하지 않아야 함)
       
       * component에서 **dispatch()** 메서드에 의해 호출됨
     
     * Mutations & Actions
   
   * Vue와 Vuex 인스턴스 비교
   
   * 모든 데이터를 Vuex에서 관리?
     
     * 모든 데이터를 state에 넣어야 하는 것은X
     
     * Vuex에서도 pass props, emit event 사용해서 상태 관리 각능
     
     * 개발 환경에 따라 적절하게 사용
   
   * 정리

3. Vuex 실습
   
   * state
     
     * {{\$store.state}}
     
     * \$store.state로 바로 접근하기 보다는 computed에 정의 후 접근 권장
   
   * actions
   
   * mutations
     
     * component 또는 actions에서 commit()에 의해 호출됨
     
     * commit(A, B)
       
       * A: 호출하고자 하는 mutations 함수
       
       * B: payload
     
     * mutations 함수 작성하기
       
       * 첫번째 인자: state
       
       * 두번째 인자: payload
     
     * getters

## 2. Lifecycle Hooks

----

1. Lifecycle Hooks
   
   * 각 Vue 인스턴스는 생성과 소멸의 과정 중 단계별 초기화 과정을 거침
     
     * Vue 인스턴스가 생성된 경우, 인스턴스를 DOM에 마운트하는 경우, 데이터가 변경되어 DOM을 업데이트하는 경우 등
   
   * 각 단계가 트리거가 되어 특정 로직을 실행할 수 있음
   
   * 이를 Lifecycle Hooks이라고 함
   
   * created
     
     * Vue instance가 생성된 후 호출됨
     
     * data, computed 등의 설정이 완료된 상태
     
     * 서버에서 받은 데이터를 vue instance의 data에 할당하는 로직 구현하기 적합
     
     * 단, mount되지 않아 요소에 접근X
   
   * mounted
     
     * Vue instance가 요소에 mount된 후 호출됨
     
     * mount된 요소를 조작할 수 있음
   
   * updated
     
     * 데이터가 변경되어 DOM에 변화를 줄 때 호출됨
   
   * Lifecycle Hooks 특징
     
     * instance마다 각각의 Lifecycle을 가지고 있음
     
     * Lifecycle Hooks는 컴포넌트별로 정의 가능
     
     * 부모 컴포넌트의 mounted hook이 실행 되었다고해서 자식이 mount된 것 X, 부모 컴포넌트가 updated hook이 실행 되었다고해서 자식이 updated된 것 X
       
       * 부착 여부가 부모-자식 관계에 따라 순서를 가지고 있지 않은 것



## 3. Todo with Vuex

-----

1. 개요
   
   * 구현 기능
     
     * Todo CRUD
     
     * Todo 개수 계산
       
       * 전체 Todo / 완료된 Todo / 미완료된 Todo

2. 사전 준비

3. Read Todo
   
   * state 데이터 가져오기

4. Create Todo

5. Delete Todo

6. Update Todo

7. 상태별 todo 개수 계산

8. Local Storage
   
   * 브라우저의 Local Storage에 todo 데이터를 저장하여 브라우저를 종료하고 다시 실행해도 데이터가 보존될 수 있도록 하기
   
   * Window.localStorage
     
     * 브라우저에서 제공하는 저장공간 중 하나인 Local Storage에 관련된 속성
     
     * 만료되지 않고 브라우저를 종료하고 다시 실행해도 데이터가 보존됨
     
     * 데이터가 문자열 형태로 저장됨
     
     * 관련 메서드
       
       * sestItem(key, value): key, value 형태로 데이터 저장
       
       * getItem(key): key에 해당하는 데이터 조회
   
   * Local Storage 실습
     
     * todos 배열을 Local Storage에 저장하기
     
     * 데이터가 문자열 형태로 저장되어야 하기 때문에 JSON.stringify를 사용해 문자열로 변환해주는 과정 필요
     
     * state를 변경하는 작업이 아니기 때문에 mutations가 아닌 actions에 작성
   
   * vuex-persistedstate
     
     * Vuex state를 자동으로 브라우저의 Local Storage에 저장해주는 라이브러리 중 하나
     
     * 페이지가 새로고침 되어도 Vuex state를 유지시킴
     
     * Local Storage에 저장된 data를 자동으로 state로 불러옴
     
     * 설치
     
     * 적용
