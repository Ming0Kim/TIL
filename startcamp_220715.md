GIT = 분산 버전 관리 프로그램

1. 분산 버전 관리 → GIT
2. Git기반의 저장소 서비스 → GitHub
3. Github : 마이크로소프트 서버 어딘가에 내 코드가 저장됨
   1. 공개적 : 전세계 모든 사람들에게 나를 표현할 수 있음
4. GitLab : 저장하는 그 서버 자체를 내 맘대로 지정 가능
5. GitLab & GitHub 둘 다 사용!

<aside> 💡 Github

- [ ]  잔디밭 관리하기 - 1일1커밋 </aside>

------

### **CLI** vs GUI

1. GUI = Graphic User Interface

   1. 그래픽을 통해 사용자와 컴퓨터가 항호 작용하는 방식
   2. 사용하기 쉽지만 단계가 많고 컴퓨터의 성능을 더 많이 소모

2. CLI = Command Line Interface

   1. 명령어를 통해 사용자와 컴퓨터가 상호 작용하는 방식
   2. 수많은 서버 / 개발 시스템이 CLI를 통한 조작 환경을 제공
   3. 컴퓨터 리소스 절약
   4. 개발할 때 많이 씀

   ### 단축어

   - touch
     - 파일을 생성하는 명령어
   - Mkdir
     - 새 폴더를 생성하는 명령어
   - ls
     - 현재 작업 중인 디렉토리의 폴더/파일 목록을 보여주는 명령어
   - cd
     - 현재 작업 중인 디렉토리를 변경하는 명령어
   - start, open
     - 폴더/파일을 여는 명령어
   - rm
     - 파일을 삭제하는 명령어
     - -r 옵션을 주면 폴더 삭제 가능

   ![C:\Users\multicampus ⇒ 현재 작업중인 곳](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/75f7cfff-3573-400f-a64e-984dd2345a03/Untitled.png)

   C:\Users\multicampus ⇒ 현재 작업중인 곳

   ![desktop.ini ⇒ 숨김처리](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8255e055-528b-4109-bbb0-437887c33b90/Untitled.png)

   desktop.ini ⇒ 숨김처리

   ![cd(띄어쓰기).. ⇒ 상위 폴더](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9dd1f865-e189-4b41-a5ea-c8148a89b267/Untitled.png)

   cd(띄어쓰기).. ⇒ 상위 폴더

   ![. ⇒ 현재 위치](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2951806f-21cd-45ac-bc06-91904785ee07/Untitled.png)

   . ⇒ 현재 위치

   ------

### 절대경로 vs 상대경로

1. 절대 경로
   1. 루트 디렉토리부터 목적 지점까지 거치는 모든 경로를 전부 작성한 것
   2. 윈도우 바탕 화면의 절대 경로 - C:/Users/ssafy/Desktop
2. 상대 경로
   1. 현재 작업하고 있는 디렉토리를 기준으로 계산된 상대적 위치를 작성한 것
   2. 현재 작업하고 있는 디렉토리가  C:/Users일 때
   3. 윈도우 바탕 화면으로의 상대 경로는  ssafy/desktop
   4. ./: 현재 작업하고 있는 폴더
   5. ../: 현재 작업하고 있는 폴더의 부모 폴더

------

마크다운

1. 텍스트 기반의 가벼운 마크업 언어
2. 문서의 구조와 내용을 같이 쉽고 빠르게 적고자 탄생
3. [README.md](http://README.md) 파일을 통해 오픈 소스의 공식 문서 작성
4. 개인 프로젝트의 소개 문서 작성
5. 매일 학습한 내용 정리
6. 마크다운을 이용한 블로그 운영
7. 대부분의 웹 에디터에서 지원 (각종 블로그 사이트 등)
8. Jypyter Notebook, Notion, 다양한 메모장 프로그램 등

------

### Typora

- 실시간 마크다운 변환 제공
- 이미지 또는 표 삽입시 매우 편한  UI 제공
- _# 헤딩
- 1.2.2. *- 리스트
- SHIFT + TAP 내어쓰기
- 코드 블럭
- ‘’’CODE BLOCK’’’
- ‘inline code block’
- `inline code block`

```jsx
code block
dkfjdkfj

dkjfkdjf
```

- `[string](url)` 링크
- ![string](img_url) 이미지
- .assets???
- ‘**bold** ‘*italic* ‘strikeout 텍스트 강조
- *를 _로 대체 할 수 있다.
- ‘—-  : 수평선
- ‘—- -를 *나 _로 대체 할 수 있다.

[Markdown Cheat Sheet | Markdown Guide](https://www.markdownguide.org/cheat-sheet/)

치팅 가능 ㅎ

------

### Repository

- 특정 디렉토리를 버전 관리하는 

  저장소

  - **git init** 명령어로 로컬 저장소를 생성
  - **git** 디렉토리에 버전 관리에 필요한 모든 것이 들어있음

------

### Git 기본기

- README.md

   생성하기

  - 새 폴더를 만들고 [README.md](http://README.md) 파일을 생성해 주세요.
  - 이 파일을 버전 관리하며 Git을 사용해 봅시다.
  - → 특정 버전으로 남긴다 = “커밋(Commit)한다”

- `Working Directory` : 내가 작업하고 있는 실제 디렉토리

- `Staging Area` : 커밋으로 남기고 싶은, 특정 버전으로 관리하고 싶은 파일이 있는 곳 / 잠시 변경사항 등

- ```
  Repository
  ```

   : 저장소

  - 커밋은 이 3가지 영역을 바탕으로 동작