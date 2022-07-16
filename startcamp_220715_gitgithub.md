### GIT = 분산 버전 관리 프로그램

1. 분산 버전 관리 → GIT
2. Git기반의 저장소 서비스 → GitHub
3. Github : 마이크로소프트 서버 어딘가에 내 코드가 저장됨
   1. 공개적 : 전세계 모든 사람들에게 나를 표현할 수 있음
4. GitLab : 저장하는 그 서버 자체를 내 맘대로 지정 가능
5. GitLab & GitHub 둘 다 사용!

### Repository

- 특정 디렉토리를 버전 관리하는 

  저장소

  - **git init** 명령어로 로컬 저장소를 생성
  - **git** 디렉토리에 버전 관리에 필요한 모든 것이 들어있음

### Git 기본기

- README.md 생성하기

  - 새 폴더를 만들고 [README.md](http://README.md) 파일을 생성해 주세요.
  - 이 파일을 버전 관리하며 Git을 사용해 봅시다.
  - → 특정 버전으로 남긴다 = “커밋(Commit)한다”

- `Working Directory` : 내가 작업하고 있는 실제 디렉토리

- `Staging Area` : 커밋으로 남기고 싶은, 특정 버전으로 관리하고 싶은 파일이 있는 곳 / 잠시 변경사항 등

- `repository` : 저장소

  - 커밋은 이 3가지 영역을 바탕으로 동작

- `Working Directory` 에서 `untracked` 파일이 `git add`를 통해 `staging area` 로 이동, `git commit`을 통해 `repository`로 `committed` 파일이 됨.

- `git status` : 현재 git으로 관리되고 있는 파일들의 상태를 알 수 있음
