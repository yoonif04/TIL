## 0. 목차

----

1. Git undoing

2. Git reset & revert

3. Git branch & merge

4. Git workflow

## 1. Git undoing

---

1. 개요
   
   * 작업 되돌리기
   
   * 작업 상태에 따라 크게 **세가지로 분류**
     
     * **Working Directory** 작업 단계
       
       * Working Directory에서 수정한 파일 내용을 이전 커밋 상태로 되돌리기
       
       * **git restore**
     
     * **Staging Area** 작업 단계
       
       * Staging Area에 반영된 파일을 Working Directory로 되돌리기
       
       * **git rm --cached**
       
       * **git restore --staged**
     
     * **Repository** 작업 단계
       
       * 커밋을 완료한 파일을 Staging Area로 되돌리기
       
       * **git commit --amend**

2. **Working Directory 작업 단계 되돌리기**
   
   * **직전 커밋으로** 되돌리기
   
   * **이미 버전 관리가 되고 있는 파일만** 되돌리기 가능
   
   * git restore를 통해 **되돌리면 -> 해당 내용을 복원할 수 X**
   
   * **git restore {파일 이름}**
   
   * [참고] git 2.23.0 버전 이전에는 git checkout -- {파일이름}
   
   * git restore
     
     * git 저장소 초기화: git init
     
     * test.md 파일 생성 후 커밋: touch test.md로 생성가능
     
     * Working Directory에서 test.md 파일 수정
     
     * git restore를 사용해서 test.md 파일을 수정 전으로 되돌리기

3. **Staging Area 작업 단계 되돌리기**
   
   * Working Directory로 되돌리기(==Unstage)
   
   * **root-commit 여부**에 따라 두가지 명령어로 나뉨
   
   * root-commit이 **없는 경우**: **git rm --cached {파일이름}**
     
     * git 저장소가 만들어지고 한번도 커밋을 안한 경우
     
     * git 저장소 초기화
     
     * test.md 파일 생성 후 add
     
     * git rm --cached 사용해서 working directory로
   
   * root-commit이 **있는 경우**: **git restore --staged {파일이름}**
     
     * git 저장소에 한개 이상의 커밋이 있는 경우
     
     * [참고] git 2.23.0 버전 이전에는 git reset HEAD {파일이름}

4. **Repository 작업 단계 되돌리기**
   
   * 커밋을 완료한 파일을 Staging Area로 되돌리기
   * 두가지 기능으로 나뉨
     * Staging Area로 **새로 올라온 내용X** -> 직전 커밋의 **메시지만 수정**
     * **새로 올라온 내용O** -> 직전 커밋을 **덮어쓰기**
       * 기존 commit -> 새로운 버전
       * amend 명령어 -> 기존 버전의 내용만 변경
   * 이전 커밋을 완전히 고쳐서 새 커밋으로 변경하므로, **이전 커밋은 일어나지 않은 일이 되며 히스토리에도 남지 않음!**
   * git commit --amend
   * [참고] Vim 간단 사용법
     * 입력 모드(i): 문서 편집 가능
     * 명령 모드(esc)
       * 저장 및 종료(:wq)
       * 강제 종료(:q!)
   * 확인: git reflog



## 2. Git reset & revert

----

1. 개요
   
   * 프로젝트를 특정 커밋(버전) 상태로 되돌림
   
   * 특정 커밋으로 되돌아 가면 -> 해당 커밋 이후로 쌓았던 커밋들은 전부 사라짐
   
   * **git reset [옵션] {커밋 ID}**
     
     * 옵션: **soft, mixed, hard** 중 하나 작성
     
     * 커밋 ID는 **되돌아가고 싶은 시점의 커밋 ID**를 작성
     
     * git reflog로 ID 확인 가능
   
   * 세가지 옵션
     
     * **--soft**: 되돌아간 커밋 **이후의 파일** -> **Staging Area**로 돌려놓음
     
     * **--mixed**: 되돌아간 커밋 **이후의 파일** -> **Working Area**로 돌려놓음
       
       * 기본값
     
     * **--hard**: 되돌아간 커밋 **이후의 파일** -> **삭제**
       
       * 기존의 Untracked 파일은 사라지지 않고 Untracked로 남아있음
   
   * **[참고] git reflog**
     
     * reset하기 전의 과거 커밋 내역을 모두 조회 가능
     
     * 이후 해당 커밋으로 reset하면 hard옵션으로 삭제된 파일도 복구 가능

2. **Git revert**
   
   * 이전 커밋을 **취소한다는 새로운 커밋**을 생성
   
   * **git revert {커밋 ID}**
   
   * **git reset과의 차이점**
     
     * reset: 커밋 내역 삭제
     
     * revert: 새로운 커밋 생성
       
       * 협업할 때, 충돌 방지 가능

## 3. Git branch & merge

---

1. 개요
   
   * 작업 공간을 나누어 독립적으로 작업할 수 있도록 도와주는 도구
   
   * **장점**
     
     * 독립 공간 -> 원본에 대해 안전
     
     * 하나의 작업 -> 하나의 브랜치 -> 체계적인 개발 가능
     
     * git은 브랜치를 만드는 속도가 굉장히 빠르고, 적은 용량 소모

2. **git branch**
   
   * **조회**
     
     * **git branch**: 로컬 저장소의 브랜치 목록 확인
     
     * **git branch -r**: 원격 저장소의 브랜치 목록 확인
   
   * **생성**
     
     * **git branch {브랜치 이름}**: 새로운 브랜치 생성
     
     * **git branch {브랜치 이름} {커밋 ID}**: 특정 커밋 기준으로 브랜치 생성
   
   * **삭제**
     
     * **git branch -d {브랜치 이름}**: 병합된 브랜치만 삭제 가능
     
     * **git branch -D {브랜치 이름}**: 강제 삭제

3. **git switch**
   
   * 현재 브랜치에서 다른 브랜치로 이동하는 명령어
   
   * **git switch {브랜치 이름}**: 다른 브랜치로 이동
   
   * **git switch -c {브랜치 이름}**: 브랜치를 새로 생성 및 이동
   
   * **git switch -c {브랜치 이름}{커밋 ID}**: 특정 커밋 기준으로 브랜치 생성 및 이동
   
   * switch하기 전, 해당 브랜치의 변경 사항을 **반드시 커밋**해야함!!!
     
     * 다른 브랜치에서 파일 만들고 커밋X 상태에서 switch -> 브랜치를 이동했음에도 불구하고 해당 파일이 그대로 남아있게 됨
   
   * **[참고] HEAD**
     
     * 현재 브랜치를 가리키고, 각 브랜치는 자신의 최신 커밋을 가리킴 --> 현재 브랜치의 최신 커밋을 가리킴
     
     * git log 혹은 cat .git/HEAD를 통해서 어떤 브랜치를 가리키는지 알수있음
     
     * git switch는 현재 브랜치에서 다른 브랜치로 HEAD를 이동시키는 명령어

4. **git merge**
   
   * 분기된 브랜치들을 하나로 합치는 명령어
   
   * master 브랜치가 상용이므로 주로 master브랜치에 병합
   
   * **git merge{합칠 브랜치 이름}**
     
     * **병합 전** 브랜치를 합치려고 하는, 즉 **메인 브랜치로 switch 해야함**
     
     * (master) $ git merge hotfix
     
     * 병합의 **세 종류**
       
       * **Fast-Forward**: 브랜치가 가리키는 커밋을 앞으로 이동
       
       * **3-way Merge**: 각 브랜치의 커밋 두 개와 **공통 조상 하나**를 사용하여 병합하는 방법
         
         * 각 브랜치에서 다른 파일을 수정해서 커밋 후 merge해야 충돌 안생김
       
       * **Merge Conflict**: 두 브랜치에서 같은 부분을 수정 -> git이 어느 브랜치의 내용으로 작성해야 하는지 판단X 충돌 발생 -> 해결하며 병합하는 방법
         
         * 보통 같은 파일의 같은 부분 수정시 자주 발생

## 4. Git workflow

----

1. 개요
   
   * 원격 저장소와 브랜치를 이용해 협업하는 두가지 방법
     
     * 원격 저장소 **소유권O** -> **Shared repository model**
     
     * 원격 저장소 **소유권X** -> **Fork & Pull model**

2. **Shared repository model**
   
   * 원격 저장소가 자신의 소유이거나 Collaborator로 등록되어 있는 경우
   
   * master 브랜치에 직접 개발X, 기능별로 브랜치를 따로 만들어 개발
   
   * **Pull Request**를 사용하여 팀원 간 변경 내용에 대한 소통 진행
   
   * 방법
     
     * 소유권이 있는 원격 저장소를 로컬 저장소로 **clone 받기**
     
     * 사용자는 자신이 작업할 기능에 대한 **브랜치를 생성**하고, 그 안에서 기능을 구현
     
     * 기능 구현 완료 -> 원격 저장소에 해당 브랜치 **push**
       
       * add, commit 후 브랜치명에 push
     
     * 각 기능의 브랜치가 원격 저장소에 반영됨
     
     * **Pull Request**를 통해 브랜치를 master에 반영해달라는 요청을 보냄
     
     * 병합 완료된 브랜치는 불필요 -> **원격 저장소에서 삭제**
     
     * 원격 저장소에서 **병합이 완료** -> 사용자는 로컬에서 **master 브랜치로 switch**
     
     * 병합 후 변경된 원격 저장소의 **master 내용을 로컬에 Pull**
       
       * gut pull origin master(main)
     
     * 기존 로컬 브랜치 삭제
       
       * git branch -d 브랜치명

3. **Fork & Pull model**
   
   * 오픈소스 프로젝트와 같이, **자신의 소유가 아닌 원격 저장소**인 경우
   
   * 원본 원격 저장소를 그대로 **내 원격 저장소에 복제**(이러한 행위를 **Fork**라고 함)
   
   * **기능 완성 후** 복제한 내 원격 저장소에 **Push**
   
   * 이후 **Pull Request**를 통해 원본 원격 저장소에 반영될 수 있도록 요청함
     
     * 방법
       
       * 소유권이 없는 원격 저장소 fork를 통해 내 원격 저장소로 복제
       
       * fork 이후 clone
       
       * 로컬 저장소와 원본 원격 저장소를 동기화 하기 위해 연결
       
       * 사용자는 브랜치 생성, 그 안에서 기능 구현
       
       * 기능 구현 완료 -> 복제 원격 저장소에 해당 브랜치 push
       
       * 복제 원격 저장소(origin)에 브랜치 반영됨
       
       * Pull Request를 통해 origin의 브랜치를 upstream에 반영해달라는 요청을 보냄
       
       * upstream에 브랜치가 병합되면 origin의 브랜치 삭제
       
       * 이후 사용자는 로컬에서 master 브랜치로 switch
       
       * 병합으로 인해 변경된 upstream의 master 내용을 로컬에 pull
       
       * upstream의 master 내용을 받았으므로, 기존 로컬 브랜치 삭제

4. **Git 브랜치 전략**
   
   * 브랜치 생성 규칙 혹은 방법론
   
   * **git-flow**
     
     * 5개의 브랜치로 나누어 소스코드 관리
       
       * master: 제품 출시
       
       * develop: 다음 출시 버전 개발 전용
       
       * feature: 기능 개발
       
       * release: 이번 출시 버전 준비
       
       * hotfix: 출시 버전에서 발생한 버그 수정
     
     * 대규모 프로젝트에 적합한 브랜치 전략
   
   * **github-flow**
     
     * Pull Request 기능 사용 권장, 병합 후 배포가 자동화로 이루어짐
   
   * **gitlab-flow**
     
     * master브랜치와 production 브랜치 사이에 pre-production 브랜치를 두어 개발 내용을 바로 반영하지 않고, 배포 시기를 조절함




