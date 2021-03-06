#### 모듈

##### 모듈과 패키지

- **모듈** : 다양한 기능을 하나의 파일로
- **패키지** : 다양한 파일을 하나의 폴더로
- **라이브러리** : 다양한 패키지를 하나의 묶음으로
- 라이브러리 vs 프레임워크 구분이 쉽지 않다
    - 라이브러리 → 도구 (삽) : 내가 주도적으로 할 수 있음
    - 프레임워크 → 도구 (포크레인) : 사실상 내가 막 다룰 수 없음
- **pip** : 이것을 관리하는 관리자
- **가상환경** : 패키지의 활용 공간

##### 모듈과 패키지

- 외부 개발자가 만든 코드를 가져다 쓸 수 있다
- 모듈
    - 특정 기능을 하는 코드를 파이썬 파일(,py) 단위로 작성한 거
- 패키지
    - 특정 기능과 관련된 여러 모듈의 집합
    - 패키지 안에는 또 다른 서브 패키지를 포함

##### 가상환경

- 파이썬 표준 라이브러리가 아닌 외부 패키지와 모듈을 사용하는 경우
- 모두 pip를 통해 설치를 해야함
- 복수의 프로젝트를 하는 경우 버전이 상이할 수 있음
    - 과거 외주 프로젝트 - django 버전 2.x
    - 신규 회사 프로젝트 - django 버전 3.x
- 이러한 경우 가상환경을 만들어 프로젝트 별로 독립적인 패키지를 관리 할 수 있음
- 가상 환경을 만들고 관리하는데 사용되는 모듈(Python 버전 3.5부터)
- 특정 디렉토리에 가상 환경을 만들고, 고유한 파이썬 패키지 집합을 가질 수 있음
    - 특정 폴더에 가상 환경이(패키지 집합 폴더 등) 있고
    - 실행환경(예-bash{)에서 가상환경을 활성화 시켜
    - 해당 폴더에 있는 패키지를 관리/사용함