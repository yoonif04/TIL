## 0. 목차

----

1. Database

2. SQL

3. DDL (Data Definition Language)

4. DML (Data Manipulation Language)

## 1. Database

----

1. Intro
   
   * 지금은 데이터의 시대
     
     * 세상에는 수많은 데이터들이 존재
     
     * 웹 서비스나 애플리케이션을 통해 셀 수 없이 많은 데이터가 생성, 수정, 삭제됨
     
     * 데이터 규모는 점점 더 빠른 속도로 증가하고 있고, 이 데이터를 다루는 기술 또한 점점 중요해지고 있다.
   
   * 데이터베이스의 등장
     
     * 서비스 혹은 애플리케이션들은 어떻게, 어디에 데이터를 저장? -> 데이터베이스
     
     * 스프레드 시트와 달리 프로그래밍 언어를 사용해 작동시킬 수 있음
     
     * 많은 형태가 있지만, 실제 가장 많이 쓰이는 유형 => **RDB(Relational Database)** 라고 부르는 **관계형 데이터베이스**
     
     * RDB는 각각의 데이터를 테이블에 기입함
     
     * **파일**을 이용한 데이터 관리
       
       * **장점**
         
         * 운영체제 관계x 어디에서나 쉽게 사용가능
         
         * 이메일이나 메신저를 이용해 간편하게 전송 가능
       
       * **단점**
         
         * 성능, 보안적 측면에서 한계 명확
         
         * 대용량 데이터를 다루기에 적합하지 X
         
         * 데이터를 구조적으로 정리하기에 어려움
         
         * 확장이 불가능한 구조
     
     * **스프레드 시트**를 이용한 데이터 관리
       
       * 스프레드 시트(엑셀 시트) 사용
       
       * 컬럼(열)을 통해 데이터의 유형 지정, 레코드(행)을 통해 구체적인 데이터 값을 포함
       
       * 스프레드 시트 자체를 데이터베이스라고 부를 수는x, 데이터베이스로 가는 길목
   
   * 학습 목표
   
   * **Database 정의**
     
     * 체계화된 데이터의 모임
     
     * 여러 사람이 **공유**하고 **사용**할 목적으로 **통합 관리**되는 정보의 집합
     
     * 검색, 구조화 같은 작업을 보다 쉽게하기 위해 조직화된 데이터를 수집하는 저장시스템
       
       * 내용을 고도로 구조화함으로써 검색과 갱신의 효율화를 꾀한 것
       
       * 즉, 자료 파일을 조직적으로 통합하여 자료 항목의 중복을 없애고, 구조화하여 기억시켜 놓은 자료의 집합체
     
     * Database를 조작하는 프로그램 = **DBMS(Databse Management System)**
       
       * Oracle, MySQL, SQLite 등
       
       * **SQL**: DBMS에서 Database를 조작하기 위해 사용하는 언어
     
     * 웹 개발에서 대부분의 데이터베이스는 '<u>관계형 데이터베이스 관리 시스템(RDBMS)</u>'을 사용하여 SQL로 데이터와 프로그래밍을 구성

2. **RDB**
   
   * **RDB란**
     
     * **Relational Database (관계형 데이터베이스)**
     
     * 데이터를 테이블, 행, 열 등으로 나누어 구조화하는 방식
     
     * 자료를 여러 테이블로 나누어서 관리하고, 이 테이블간 관계를 설정해 여러 데이터를 쉽게 조작할 수 있다는 장점
     
     * SQL을 사용하여 데이터를 조회하고 조작
   
   * [참고] 테이블간 관계 설정 예시
   
   * **RDB 기본 구조**
     
     * 스키마
     
     * 테이블
       
       * 필드
       
       * 레코드
       
       * 기본키
   
   * **스키마(Schema)**
     
     * 테이블의 구조(Structure)
     
     * 데이터베이스에서 **자료의 구조, 표현 방법, 관계 등** 전반적인 명세를 기술한 것
   
   * **테이블(Table)**
     
     * 필드와 레코드를 사용해 조직된 데이터 요소들의 집합
     
     * 관계(Relation)라고도 부름
     
     * **필드(field)**: 속성, 컬럼(Column)
       
       * 각 필드에는 고유한 데이터 형식(타입)이 지정됨
     
     * **레코드(record)**: 튜플, 행(Row)
       
       * 테이블의 데이터는 레코드에 저장됨
   
   * **PK(Primary Key)**
     
     * 기본키
     
     * 각 레코드의 **고유한 값** - 각각의 데이터를 구분할 수 있는 고윳값
     
     * 기술적으로 다른 항목과 절대로 중복될 수 없는 **단일 값(unique)**
   
   * **관계형 데이터베이스의 이점**
     
     * 데이터를 **직관적**으로 표현 가능
     
     * 관련한 각 데이터에 **쉽게 접근** 가능
     
     * 대량의 데이터도 **효율적으로 관리** 가능
   
   * **RDBMS**
     
     * Relational Database Management System (관계형 데이터베이스 관리 시스템)
     
     * 관계형 데이터베이스를 만들고 업데이트하고 관리하는데 사용하는 프로그램
       
       * ex: SQLite, MySQL, PostgreSQL, Microsoft SQL Server, Oracle Database 등
   
   * **SQLite**
     
     * 응용 프로그램에 파일 형식으로 넣어 사용하는 비교적 가벼운 데이터베이스
     
     * 안드로이드, iOS, macOS에 기본적으로 탑재되어 있으며, 임베디드 소프트웨어에서도 많이 활용됨
     
     * 오픈소스 프로젝트이기 때문에 자유롭게 사용가능
   
   * **SQLite 단점**
     
     * 대규모 동시 처리 작업에는 적합하지 않음
     
     * 다른 RDBMS에서 지원하는 SQL 기능을 지원하지 않을 수 있음
   
   * SQLite 학습 이유
     
     * 어떤 환경에서나 실행 가능한 호환성
     
     * 데이터 타입이 비교적 적고 강하지 않기 때문에 유연한 학습 환경을 제공
     
     * Django Framework의 기본 데이터베이스

## 2. SQL

---

1. **SQL**
   
   * SQL이란 
     
     * **Structured Query Language**
     
     * RDBMS의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어
     
     * RDBMS에서 데이터베이스 스키마를 생성 및 수정할 수 있으며, 테이블에서의 자료 검색 및 관리도 할 수 있음
     
     * 데이터베이스 객체에 대한 처리를 관리하거나 접근 권한을 설정하여 허가된 사용자만 RDBMS를 관리할 수 있도록 할 수 있음
     
     * 많은 데이터베이스 관련 프로그램들이 SQL을 표준으로 채택하고 있음
   
   * SQL 정리
     
     * SQL은 데이터베이스와 상호작용하는 방법
     
     * 따라서 SQL을 배우면서 데이터베이스의 동작원리 또한 익힐 수 있음

2. **SQL Commands**
   
   * SQL Commands **종류**
     
     * **DDL (Data Definition Language)**
     * **DML (Data Manipulation Language)**
     * **DCL (Data Control Language)**
       * SQLite는 파일로 관리되는 DB -> SQL을 이용하는 접근 제한x, 운영 체제의 파일 접근 권한으로만 제어가능 -> SQLite는 GRANT, REVOKE 지원x
     
     | 분류              | 개념                                                | SQL 키워드                         |
     | --------------- | ------------------------------------------------- | ------------------------------- |
     | DDL - 데이터 정의 언어 | 관계형 데이터베이스 구조(테이블, 스키마)를 정의(생성, 수정 및 삭제)하기 위한 명령어 | CREATE, DROP, ALTER             |
     | DML - 데이터 조작 언어 | 데이터를 조작(추가, 조회, 변경, 삭제)하기 위한 명령어                  | INSERT, SELECT, UPDATE, DELETE  |
     | DCL - 데이터 제어 언어 | 데이터의 보안, 수행제어, 사용자 권한 부여 등을 정의하기 위한 명령어           | GRANT, REVOKE, COMMIT, ROLLBACK |

3. **SQL Syntax**
   
   * 모든 SQL문(statement)는 SELECT, INSERT, UPDATE등과 같은 <u>키워드로 시작</u>, 하나의 statement는 <u>세미콜론(;)으로 끝</u>남
     
     * 세미콜론은 각 SQL문을 구분하는 표준 방법
   
   * SQL 키워드는 **대소문자를 구분하지 않음**
     
     * 하지만 <u>대문자로 작성하는 것 권장</u>
   
   * **[참고] Statement & Clause**
     
     * **Statement(문)**
       
       * 독립적으로 실행할 수 있는 완전한 코드 조각
       
       * statement는 clause로 구성됨
     
     * **Clause(절)**
       
       * statement의 하위 단위
     
     * SELECT column_name FROM table_name;
       
       * SELECT statement라 부름
       
       * 2개의 clause로 구성됨
         
         * SELECT column_name
         
         * FROM table_name

## 3. DDL

----

1. 사전 준비
   
   * SQLite3 설치
   
   * Vscode SQLite 확장 프로그램 설치
   
   * 데이터베이스 파일 생성: 이름.sqlite3
   
   * DDL.sql 파일 생성
   
   * vscode 실행 후 DDL.sql 화면에서 마우스 우측 버튼 클릭 
     
     * Use Database 선택
     
     * 데이터베이스 목록에서 이름.sqlite3 선택

2. 개요
   
   * **Data Definition**
   
   * SQL 데이터 정의 언어를 사용하여 테이블 데이터베이스 개체를 만드는 방법 학습
   
   * DDL은 **테이블 구조를 관리**
     
     * **CREATE, ALTER, DROP**

3. **CREATE TABLE**
   
   * CREATE TABLE statement
     
     * 데이터베이스에 새 테이블을 만듦
     
     ```sql
     CREATE TABLE table_name (
         column_1 data_type constraints,
         column_2 data_type constraints,
         column_3 data_type constraints
     );
     ```
   
   * 실습
     
     * contacts 테이블 생성
     
     * Query 실행하기
     
     * 쿼리 실행 후 테이블 및 스키마 확인
     
     * id 컬럼은 직접 기본키 역할의 컬럼을 정의하지 않으면, 자동으로 **rowid**라는 컬럼으로 만들어짐

4. SQLite **Data Types**
   
   * **Data Types 종류**
     
     * **NULL**
       
       * NULL value
       
       * 정보가 <u>없거나 알 수 없음</u>을 의미 (missing information or unknown)
     
     * **INTEGER**
       
       * 정수
       
       * 크기에 따라 0,1,2,3,4,6 또는 8바이트와 같은 <u>가변 크기</u>를 가짐
     
     * **REAL**
       
       * 실수
       
       * 8바이트 부동 소수점을 사용하는 10진수 값이 있는 실수
     
     * **TEXT**
       
       * 문자 데이터
     
     * **BLOB (Binary Large Object)**
       
       * 입력된 그대로 저장된 데이터 덩어리 (대용 타입 없음)
       
       * 바이너리 등 멀티미디어 파일
       
       * ex) 이미지 데이터
   
   * **[참고] Boolean type**
     
     * SQLite에는 별도의 Boolean 타입이 없음
     
     * 대신 정수 **0(false)과 1(true)** 로 저장됨
   
   * **[참고] Date & Time Datatype**
     
     * SQLite에는 날짜 및 시간을 저장하기 위한 타입이 없음
     
     * SQLite의 built-in "Date And Time Functions"으로 TEXT, REAL 또는 INTEGER 값으로 저장할 수 있음
   
   * **[참고] Binary Data**
     
     * 데이터의 저장과 처리를 목적으로 0과 1의 이진 형식으로 인코딩 된 파일
     
     * 기본적으로 컴퓨터의 모든 데이터는 binary data
       
       * 다만, 이를 필요에 따라서 텍스트 타입으로 변형해서 사용하는 것
   
   * SQLite는 **다음 규칙을 기반으로 데이터 타입을 결정**
     
     * 값이 작은 따옴표나 큰따옴표로 둘러 쌓이면 - **TEXT**
     
     * 값에 둘러싸는 따옴표가 있고, 소수점 또는 지수가 없으면 - **INTEGER**
     
     * 값에 따옴표가 없고, 소수점, 지수가 있으면 - **REAL**
     
     * 값이 따옴표 없이 NULL이면 - **NULL**
   
   * SQLite Datatypes **특징**
     
     * 다른 모든 SQL 데이터베이스 엔진(MySQL, PostgreSQL 등)의 정적이고 엄격한 타입(static, rigid typing)이 아닌
     
     * **"동적 타입 시스템(dynamic type system"** 을 사용
       
       * 컬럼에 선언된 데이터 타입에 의해서가 아니라 **컬럼에 저장된 값에 따라 데이터 타입이 결정**됨
     
     * 또한 테이블을 생성할 때 컬럼에 대해 특정 **데이터 타입을 선언하지 않아도 됨**
       
       * 동일한 컬럼에 정수 1을 넣을 경우 INTEGER로 타입이 지정되고, 문자 '1'을 넣을 경우는 TEXT 타입으로 지정됨
       
       * 동적 타입 시스템을 사용하면 기존의 엄격하게 타입이 지정된 데이터베이스에서는 불가능한 작업을 유연하게 수행할 수 있음
       
       * 게다가 정적 타입 시스템이 지정된 데이터베이스에서 작동하는 SQL문이 SQLite에서 동일한 방식으로 작동한다
       
       * 다만, 이는 다른 데이터베이스와의 **호환성 문제**가 있기 때문에 테이블 생성 시 **데이터 타입을 지정하는 것을 권장**
     
     * 데이터 타입을 지정하게되면 SQLite는 입력된 데이터의 타입을 지정된 데이터 타입으로 변환
       
       * ex) TEXT 타입 컬럼에 정수 1을 저장 -> 문자 타입의 '1'로 저장됨
       
       * 허용 가능한 타입 변환
         
         | Column Datatype | Types Allowed In That Column |
         | --------------- | ---------------------------- |
         | INTEGER         | INTEGER, REAL, TEXT, BLOB    |
         | REAL            | REAL, TEXT, BLOB             |
         | TEXT            | TEXT, BLOB                   |
         | BLOB            | INTEGER, REAL, TEXT, BLOB    |
   
   * **[참고] "static, rigid typing" 데이터베이스**
     
     * statically, rigidly typed databases 라고도 부름
     
     * 저장되는 값의 데이터 타입 -> 컬럼에 선언된 데이터 타입에 의해 결정된다.
     
     * 동작 예시
       
       ```sql
       CREATE TABLE my_table(
           a INTEGER NOT NULL;
           b TEXT NOT NULL,
       );
       ```
       
       * a 컬럼에 '123', b 컬럼에 456 데이터 삽입 -> 삽입 수행 전 문자열 '123'을 정수 123으로 변환하고, 정수 456을 문자열 '456'으로 변환
   
   * **Type Affinity**
     
     * 타입 선호도
     
     * 특정 컬럼에 저장된 데이터에 권장되는 타입
     
     * SQLite의 5가지 데이터 타입이 아닌 **다른 데이터 타입 선언**한다면 => 내부적으로 각 타입의 지정된 선호도에 따라 **5가지 선호도로 인식**됨
       
       * INTEGER - TEXT - BLOB - REAL - NUMERIC
     
     * 타입 선호도 **존재 이유**
       
       * 다른 데이터베이스 엔진 간의 **호환성을 최대화**
       
       * 정적이고 엄격한 타입을 사용하는 데이터베이스의 SQL문을 SQLite에서도 작동하도록 하기 위함

5. **Constraints**
   
   * 개요
     
     * 제약조건
     
     * 입력하는 자료에 대해 제약을 정함
     
     * 제약에 맞지 않다면 입력이 거부됨
     
     * 사용자가 원하는 조건의 데이터만 유지하기 위한 즉, **데이터의 무결성**을 유지하기 위한 보편적인 방법으로 테이블의 특정 컬럼에 설정하는 제약
   
   * **데이터 무결성**
     
     * 데이터베이스 내의 데이터에 대한 **정확성, 일관성**을 보장하기 위해 **데이터 변경 혹은 수정 시 여러 제한**을 두어 **데이터의 정확성을 보증**하는 것
       
       * 무결성: **데이터의 정확성, 일관성**을 나타냄
     
     * 데이터베이스의 저장된 데이터의 무결성을 보장하고 데이터베이스의 상태를 일관되게 유지하는 것이 목적
   
   * Constraints **종류**
     
     * **NOT NULL**
       
       * 컬럼이 NULL 값을 허용하지 않도록 지정
       
       * 기본적으로 테이블의 모든 컬럼은 NOT NULL 제약 조건을 명시적으로 사용하는 경우를 제외하고는 NULL 값을 허용
     
     * **UNIQUE**
       
       * 컬럼의 모든 값이 서로 구별되거나 고유한 값이 되도록 함
     
     * **PRIMARY KEY**
       
       * 테이블에서 행의 고유성을 식별하는데 사용되는 컬럼
       
       * 각 **테이블에는 하나의 기본키**만 있음
       
       * 암시적으로 **NOT NULL 제약 조건이 포함**되어 있음
       
       * 주의) **INTEGER 타입에만 사용가능** (INT, BIGINT 등 불가능)
     
     * **AUTOINCREMENT**
       
       * 사용되지 않은 값이나 이전에 삭제된 행의 값을 **재사용하는 것을 방지**
       
       * INTEGER PRIMARY KEY 다음에 작성하면, 해당 rowid를 다시 재사용하지 못하도록 함
       
       * Django에서 테이블 생성 시 **id 컬럼에 기본적으로 사용**하는 제약조건
     
     * **그외 기타 Constraints**
   
   * **rowid의 특징**
     
     * 테이블을 생성할 때마다 rowid라는 **암시적 자동 증가 컬럼**이 자동으로 생성됨
     
     * 테이블의 행을 고유하게 식별하는 64비트 부호 있는 정수 값
     
     * 테이블에 새 행을 삽입할 때마다 정수 값을 자동으로 할당
       
       * 값은 1에서 시작
       
       * 데이터 삽입 시에 rowid 또는 INTEGER PRIMARY KEY 컬럼에 **명시적으로 값이 지정되지 않은 경우**, SQLite는 테이블에서 **가장 큰 rowid보다 하나 큰 다음 순차 정수를 자동으로 할당** (**AUTOINCREMENT와 관계없이**)
     
     * 만약 <u>INTEGER PRIMARY KEY 키워드를 가진 컬럼</u>을 직접 만들면 이 컬럼은 **rowid 컬럼의 별칭(alias)** 이 됨
       
       * 즉, **새 컬럼 이름**으로 rowid에 엑세스 할 수 있으며, **rowid이름**으로도 여전히 **액세스 가능**
     
     * 데이터가 **최대 값에 도달**하고 새 행을 삽입하려고하면 **SQLite는 사용되지 않는 정수를 찾아 사용**
     
     * 만약 SQLite가 사용되지 않은 정수를 **찾을 수 없으면 SQLITE_FULL 에러**가 발생
       
       * 또한 <u>일부 행을 삭제하고 새 행을 삽입</u>하면 SQLite는 삭제된 행에서 **rowid 값을 재사용하려고 시도**

6. **ALTER TABLE**
   
   * 개요
     
     * 기존 테이블의 구조를 수정(변경)
     
     * SQLite의 ALTER TABLE문을 사용하면 기존 테이블을 다음과 같이 변경 가능
       
       * **Rename** a table
       
       * **Rename** a column
       
       * **Add** a new column to a table
       
       * **Delete** a column
   
   * **ALTER TABLE RENAME**
     
     ```sql
     ALTER TABLE table_name RENAME TO new_name;
     ```
   
   * **ALTER TABLE RENAME COLUMN**
     
     ```sql
     ALTER TABLE table_name RENAME COLUMN name TO new_name;
     ```
   
   * **ALTER TABLE ADD COLUMN**
     
     ```sql
     ALTER TABLE table_name ADD COLUMN name data_type constraints;
     ```
     
     * 만약 테이블에 **기존 데이터**가 있을 경우 다음과 같은 **에러**가 발생
     
     * 이전에 이미 저장된 데이터들은 새롭게 추가되는 컬럼에 값이 없기 때문에 **NULL이 작성됨**
     
     * 그런데 새로 추가되는 컬럼에  **NOT NULL 제약조건**이 있기 때문에 기본 값 없이는 추가될 수 없다는 에러가 발생
     
     * **DEFAULT 제약 조건**을 사용하여 해결할 수 있음
     
     ```sql
     ALTER TABLE table_name ADD COLUMN name data_type constraints DEFAULT "";
     ```
   
   * **[참고] DEFAULT 제약조건**
     
     * column 제약조건 중 하나
     
     * 데이터를 추가할 때 값을 생략할 시에 기본 값을 설정함
   
   * **ALTER TABLE DROP COLUMN**
     
     * 컬럼 삭제
       
       ```sql
       ALTER TABLE table_name DROP COLUMN column_name;
       ```
     
     * 단, **삭제하지 못하는 경우**가 있음
       
       * 컬럼이 **다른 부분에서 참조**되는 경우
         
         * **FOREIGN KEY(외래 키)** 제약조건에서 사****용되는 경우
       
       * **PRIMARY KEY**인 경우
       
       * **UNIQUE 제약 조건**이 있는 경우

7. **DROP TABLE**
   
   * 개요
     
     * 데이터베이스에서 **테이블을 제거**
       
       ```sql
       DROP TABLE table_name;
       ```
     
     * 존재하지 않는 테이블을 제거하면 오류
   
   * DROP TABLE **특징**
     
     * **한 번에 하나**의 테이블만 삭제 가능
     
     * 여러 테이블 제거 -> 여러 DROP TABLE문 실행
     
     * DROP TABLE문은 **실행 취소하거나 복구할 수 없음**

8. **DDL 정리**
   
   * 데이터 정의 언어
   
   * CREATE TABLE
     
     * 데이터 타입과 제약조건
   
   * ALTER TABLE
     
     * RENAME
     
     * RENAME COLUMN
     
     * ADD COLUMN
     
     * DROP COLUMN
   
   * DROP TABLE

## 4. DML

----

1. 개요
   
   * DML을 통해 데이터를 조작하기 (CRUD)
   
   * **INSERT, SELECT, UPDATE, DELETE**
   
   * 사전 준비
     
     * command-line program - "sqlite3"
     
     * sqlite3 사용하기
       
       * \$ sqlite3
       
       * sqlite> .open 이름.sqlite3
       
       * 혹은 \$ sqlite3 이름.sqlite3
       
       * 종료: sqlite> .exit
     
     * CSV 파일을 SQLite 테이블로 가져오기
       
       * DML.sql 파일 생성
       
       * 테이블 생성
       
       * 데이터베이스 파일 열기: \$ sqlite3 이름.sqlite3
       
       * 모드를 csv로 설정: sqlite> .mode csv
       
       * csv데이터를 테이블로 가져오기: sqlite> .import 파일명.csv 테이블명

2. **Simple query**
   
   * **SELECT statement**
     
     * 특정 테이블에서 **데이터를 조회**하기 위해 사용
     
     * 문법 규칙
       
       * **SELECT 절**에서 컬럼 또는 쉼표로 구분된 **컬럼 목록**을 지정
       
       * **FROM 절**(clause)에서 데이터를 가져올 **테이블**을 지정
     
     * 다양한 절과 함께 사용할 수 있음
       
       * ORDER BY
       
       * DISTINCT
       
       * WHERE
       
       * LIMIT
       
       * LIKE
       
       * GROUP BY
     
     * **전체 데이터 조회**: 모든 컬럼에 대한 shorthand(약칭)인 \***(asterisk)** 사용
     
     * <u>rowid 컬럼 조회</u>: rowid **명시**

3. **Sorting rows**
   
   * **ORDER BY clause**
     
     * SELECT 문에 추가하여 결과를 정렬
     
     * **FROM절 뒤**에 위치
     
     * 하나 이상의 컬럼을 기준으로 결과를 오름차순, 내림차순으로 정렬 가능
       
       * **ASC**: 오름차순 (기본 값)
       
       * **DESC**: 내림차순
     
     * 하나 이상의 컬럼을 정렬할 경우 첫번째 열을 사용하여 행을 정렬, 그런 다음 두번째 컬럼을 사용하여 정렬 되어있는 행을 정렬하는 방식
   
   * **[참고] Sorting NULLs**
     
     * NULL의 정렬 방식
     
     * SQLite는 NULL을 다른 값보다 **작은 것으로 간주**
     
     * 즉, ASC를 사용하는 경우 시작 부분에 NULL 표시
     
     * DESC를 사용 -> 결과의 끝에 NULL이 표시

4. **Filtering data**
   
   * 개요
     
     * 데이터를 필터링하여 중복 제거, 조건 설정 등 쿼리를 제어하기
     
     * **Clause**
       
       * **SELECT DISTINCT**
       
       * **WHERE**
       
       * **LIMIT**
     
     * **Operator**
       
       * **LIKE**
       
       * **IN**
       
       * **BETWEEN**
   
   * **SELECT DISTINCT clause**
     
     * 조회 결과에서 **중복된 행을 제거**
     
     * SELECT에서 선택적으로 사용 가능
     
     * 문법 규칙
       
       * SELECT 키워드 바로 뒤에 나타나야 함
       
       * DISTINCT 키워드 뒤에 컬럼 또는 컬럼 목록 작성
     
     * 각 컬럼의 중복을 따로 계산하는 것x -> **두 컬럼을 하나의 집합으로 보고 중복을 제거**
   
   * **[참고] NULL with DISTINCT**
     
     * NULL값을 **중복으로 간주**
     
     * NULL값이 있는 컬럼에 DISTINCT절 사용 -> SQLite는 NULL 값의 한 행을 유지
   
   * **WHERE clause**
     
     * 조회 시 **특정 검색 조건**을 지정
     
     * SELECT 문에서 선택적으로 사용 가능
       
       * **UPDATE, DELETE 문에서도** WHERE 절 **사용 가능**
     
     * **FROM 절 뒤**에 작성
     
     * WHERE의 검색 조건 작성 형식
   
   * **SQLite comparision operators 비교 연산자**
     
     * 두 표현식이 동일한지 테스트
     
     * **=, <> (or !=), <, >, <=, >=**
   
   * **SQLite logical operators 논리 연산자**
     
     * 일부 표현식의 truth를 테스트할 수 있음
     
     * **1, 0 또는 NULL 값을 반환**
     
     * SQLite는 Boolean 데이터 타입을 제공x -> **1은 TRUE** 의미, **0은 FALSE** 의미
     
     * **ALL, AND, ANY, BETWEEN, IN, LIKE, NOT, OR 등**
   
   * **LIKE operator**
     
     * **패턴 일치**를 기반으로 데이터를 조회
     
     * SELECT, DELETE, UPDATE 문의 **WHERE절에서 사용**
     
     * 기본적으로 **대소문자 구분X**
     
     * 패턴 구성을 위한 두개의 **와일드카드** 제공
       
       * **%(percent)**: **0개 이상**의 문자가 올 수 있음
       
       * **\_(underscore)**: **단일(1개)** 문자가 있음을 의미
     
     * wildcard 예시
   
   * **[참고] "wildcards" character**
     
     * 파일을 지정할 때, 구체적인 이름 대신에 여러 파일을 <u>동시에 지정</u>할 목적으로 사용하는 특수 기호
       
       * \*, ? 등
     
     * 주로 <u>특정한 패턴</u>이 있는 문자열 혹은 파일을 찾거나, <u>긴 이름을 생략</u>할 때 쓰임
     
     * 텍스트 값에서 알 수 없는 문자를 사용할 수 있는 특수 문자로, <u>유사하지만 동일한 데이터가 아닌 여러 항목</u>을 찾기에 매우 편리한 문자
     
     * <u>지정된 패턴 일치</u>를 기반으로 데이터를 수집하는데도 도움이 될 수 있음
   
   * **IN operator**
     
     * 값이 값 목록 결과에 있는 값과 일치하는지 확인
     * 표현식이 값 목록의 값과 일치하는지 여부에 따라 <u>true 또는 false를 반환</u>
     * IN 연산자의 결과를 부정 -> **NOT IN** 연산자 사용
     * IN 연산자 대신 **OR 연산자**를 사용하여 동일한 결과 반환 가능
   
   * **BETWEEN operator**
     
     * 값이 값 범위에 있는지 테스트
     * 값이 지정된 범위에 있으면 true를 반환
     * SELECT, DELETE, UPDATE 문의 <u>WHERE절에서 사용 가능</u>
     * **AND 연산자**를 사용하여 동일한 결과 반환 가능
     * 연산자의 결과를 부정 -> **NOT BETWEEN** 연산자 사용
     * **OR 연산자**를 사용하여 동일한 결과 반환 가능
   
   * **LIMIT clause**
     
     * 쿼리에서 **반환되는 행 수를 제한**
     
     * SELECT 문에서 선택적으로 사용 가능
     
     * 반환되는 행 수를 양의 정수로 입력
     
     * **ORDER BY 절과 함께 사용**하여 **지정된 순서로 여러 행**을 가져올 수도 있음
       
       * LIMIT절에 지정된 행 수를 가져오기 전에 결과를 정렬하기 때문
     
     ```sql
     SELECT column_list FROM table_name LIMIT row_count;
     ```
   
   * **OFFSET keyword**
     
     * LIMIT 절 사용 -> 첫번째 데이터부터 지정한 수만큼
     * LIMIT 절을 OFFSET과 함께 사용하면 **특정 지정된 위치에서부터** 데이터 조회 가능

5. **Grouping data**
   
   * **GROUP BY clause**
     
     * 특정 그룹으로 묶인 결과를 생성
     
     * 선택된 컬럼 값을 기준으로 데이터(행)들의 공통 값을 묶어서 결과로 나타냄
     
     * SELECT문에서 선택적으로 사용가능
     
     * **FROM절 뒤**에 작성
       
       * WHERE절이 포함된 경우 **WHERE절 뒤**에 작성해야 함
     
     * 각 그룹에 대해 MIN, MAX, SUM, COUNT 또는 AVG와 같은 **집계함수를 적용**하여 각 그룹에 대한 추가적인 정보를 제공할 수 있음
   
   * **Aggregate function**
     
     * 집계 함수
     
     * 값 집합의 최대값, 최소값, 평균, 합계 및 개수를 계산
     
     * 값 집합에 대한 **계산을 수행하고 단일 값을 반환**
       
       * 여러 행으로부터 하나의 결과 값을 반환하는 함수
     
     * SELECT문의 GROUP BY절과 함께 종종 사용됨
     
     * 제공하는 함수 목록
       
       * **AVG(), COUNT(), MAX(), MIN(), SUM()**
     
     * AVG(), MAX(), MIN(), SUM()는 숫자를 기준으로 계산이 되어져야 함 -> 반드시 컬럼의 데이터 타입이 숫자(INTEGER)일 때만 사용 가능
   
   * **[참고] COUNT 참고사항**
     
     * COUNT(), COUNT(age), COUNT(last_name) 등 어떤 컬럼을 넣어도 결과는 같음
     
     * 현재 쿼리에서는 그룹화된 country를 기준으로 카운트하는 것이기 때문에, 어떤 컬럼을 카운트해도 전체 개수는 동일하기 때문
   
   * **AS 키워드**
     
     * 컬럼명을 임시로 변경하여 조회 가능

6. **Changing data**
   
   * 개요
     
     * 데이터를 삽입, 수정, 삭제하기
     
     * **INSERT, UPDATE, DELETE**
     
     * 사전 준비 - 실습 편의를 위해 새 테이블 생성
   
   * **INSERT**
     
     - **새 행을 테이블에 삽입**
     
     - 문법 규칙
       
       - 먼저 INSERT INTO 키워드 뒤에 데이터를 삽입할 테이블의 이름 지정
       
       - 테이블 이름 뒤에 쉼표로 구분된 컬럼 목록 추가
         
         - 컬럼 목록은 선택 사항이지만, 포함하는 것 권장됨
       
       - VALUES 키워드 뒤에 쉼표로 구분된 값 목록 추가
         
         - **만약 컬럼 목록을 생략**하는 경우 값 목록의 **모든 컬럼에 대한 값 지정해야 함**
         
         - 값 목록의 값 개수는 컬럼 목록의 컬럼 개수와 같아야 함
     
     - 단일 행 삽입
       
       ```sql
       INSERT INTO table_name (컬럼명1, 컬럼명2, ...)
       VALUES (값1, 값2, ...)
       INSERT INTO table_name
       VALUES (값1, 값2, ...)
       ```
     
     - 여러 행 삽입
       
       ```sql
       INSERT INTO table_name
       VALUES 
         (값1, 값2, ...),
         (값1, 값2, ...),
         (값1, 값2, ...),...
       ```
   
   * **UPDATE**
     
     - 테이블에 있는 **기존 행의 데이터를 업데이트**
     
     - 문법 규칙
       
       - UPDATE 절 이후에 업데이트할 테이블을 지정
       
       - **SET 절**에서 테이블의 각 컬럼에 대해 새 값을 설정
       
       - **WHERE 절**의 조건을 사용하여 업데이트할 행을 지정
         
         - WHERE 절은 선택 사항, 생략 -> 테이블의 모든 행에 있는 데이터를 업데이트
       
       - 선택적으로 <u>ORDER BY 및 LIMIT</u>절을 사용하여 <u>업데이트할 행 수를 지정 할 수도 있음</u>
     
     ```sql
     UPDATE table_name
     SET column_1 = new_value_1,
         column_2 = new_value_2
     WHERE
         search_condition;
     ```
   
   * **DELETE**
     
     * 테이블에서 **행을 제거**
     
     * 테이블의 한 행, 여러 행 및 모든 행을 삭제할 수 있음
     
     * 문법 규칙
       
       * DELETE FROM 키워드 뒤에 행을 제거하려는 테이블의 이름 지정
       
       * WHERE절에 검색 조건을 추가하여 제거할 행을 식별
         
         * WHERE 절은 선택 사항, 생략 -> 테이블의 모든 행 삭제
       
       * 선택적으로 <u>ORDER BY 및 LIMIT절</u>을 사용하여 <u>삭제할 행 수를 지정 할 수도 있음</u>
     
     ```sql
     DELETE FROM table_name
     WHERE search_condition;
     ```

## 5. 마무리

---

1. Database
   
   * RDB

2. SQL

3. DDL
   
   * CREATE TABLE
     
     * Data Type
     
     * Constraints
   
   * ALTER TABLE
   
   * DROP TABLE

4. DML
   
   * SELECT
     
     * SELECT DISTINCT
   
   * ORDER BY
   
   * WHERE
     
     * LIKE, IN, BETWEEN
   
   * LIMIT, OFFSET
   
   * GROUP BY
     
     * Aggregate Function
   
   * INSERT / UPDATE / DELETE

5. **데이터 구조화의 중요성**
   
   * 다루고자하는 데이터를 구조화해서 저장하면 **데이터의 가공 및 확장이 용이**
   
   * 모든 서비스는 데이터를 효율적으로 다루는 것이 필수적
     
     * 예를 들어 빅데이터, 인공지능과 같은 대규모 데이터로부터 의미 있는 분석결과를 뽑아낼 수 있음

6. **데이터베이스의 미래**
   
   * 오늘날 인터넷에서의 방대한 데이터 수집은 세상을 빠르게 변화 시키고 있음
   
   * 이전에는 데이터를 단순히 저장하고 조회하기 위한 용도였다면, 이제는 저장된 데이터를 분석하고 활용하는 시대
     
     * 기업들은 이러한 분석을 통해 더 나은 의사 결정을 하고 기업의 확장성과 민첩성을 높임
   
   * 따라서 데이터에 대한 엑세스 및 처리량을 최적화 하는 것이 점점 중요해지고 있으며 앞으로 데이터베이스는 점점 자동화되어 클라우드 기술, 머신러닝 등을 사용해 더욱 더 고도화된 데이터를 다루고 처리하게 될 것
