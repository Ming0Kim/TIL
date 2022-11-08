## CSS = Cascading Style Sheets

- **스타일을 지정하기 위한 언어** 선택하고, 스타일을 지정한다
- css 구문은 선택자를 통해 스타일을 지정할 HTML요소를 선택
- 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언을 진행
- 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미
    - 속성(property) : 어떤 스타일 기능을 변경할지 결정
    - 값(value) : 어떻게 스타일 기능을 변경할지 결정

### CSS 정의 방법

- 인라인(inline)
    - 인라인을 쓰게 되면 실수가 잦아짐(중복도 있을 것이고, 찾기가 어려워서)
- 내부 참조(embedding) - `<style>`
    - 내부 참조를 쓰게 되면 코드가 너무 길어짐
- **외부 참조(link file) - 분리된 CSS파일**
    - 가장 많이 쓰는 방식

### CSS with 개발자 도구

- styles : 해당 요소에 선언된 모든 CSS
- computed : 해당 요소에 최종 계산된 CSS

## CSS Selectors

### 선택자(Selector)유형

- **기본 선택자**
    - 전체 선택자, 요소 선택자
    - 클래스 선택자, 아이디 선택자, 속성 선택자
- 결합자(Combinators)
    - 자손 결합자, 자식 결합자
    - 일반 형제 결합자, 인접 형제 결합자
- 의사 클래스/요소(Pseudo Class)
    - 링크, 동적 의사 클래스
    - 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자

### CSS 적용 우선순위 (cascading order)

- css 우선순위를 아래와 같이 그룹을 지어볼 수 있다.
    1. 중요도(Importance) - 사용시 주의
        1. !importance
    2. 우선 순위(Specificity)
        1. 인라인 > id > class, 속성, pseudo-class > 요소, pseudo-element
    3. CSS 파일 로딩 순서

### CSS 상속

CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속한다.

- 속성(프로퍼티) 중에는 상속이 되는 것과 되지 않는 것들이 있다.
- 상속 되는 것 예시
    - Text 관련요소(font, color, text-align), opacity, visibility 등
- 상속 되지 않는 것 예시
    - Box model 관련 요소(wdth, height, margin, padding, border, box-sizing, display), position 관련 요소 (position, top/right/bottom/left, z-index) 등

## CSS 기본 스타일

### 크기 단위

- px (픽셀)
    - 모니터 해상도의 한 화소인 **픽셀** 기준
    - 픽셀의 크기는 변화지 않기 때문에 고정적인 단위
- %
    - 백분율 단위
    - 가변적인 레이아웃에서 자주 사용
- em
    - (바로 위, 부모 요소에 대한) 상속의 영향을 받음
    - 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐
- **rem**
    - (바로 위, 부모 요소에 대한) 상속의 영향을 받지 않음
    - 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐

### 크기 단위(viewport)

- 웹 페이지를 방문한 유저에게 바로 보이게 되는 웹 컨텐츠의 영역(디바이스 화면)
- 디바이스의 viewport를 기준으로 상대적인 사이즈가 결정됨
- vw, vh, vmin, vmax
- px는 브라우저의 크기를 변경해도 그대로
- vx는 브라우저의 크기에 따라 크기가 변함

### 색상 단위

- 색상 키워드(`backgrond- color : red`;)
    - 대소문자를 구분하지 않음
    - red, blue, black과 같은 특정 색을 직접 글자로 나타냄
- RGB 색상(`background-color: rgb(0, 255, 0)`;)
    - 16진수 표기법 혹은 함수형 표기법을 사용해서 특정 색을 표현하는 방식
- HSL 색상(`background-color: hsl(0, 100%, 50%)`;)
    - 색상, 채도, 명도를 통해 특정 색을 표현하는 방식

## Selectors 심화

### 결합자(Combinators)

- 자손 결합자(공백)
    - selectorA 하위의 모든 selectorB 요소
- 자식 결합자(>)
    - selectorA 바로 아래의 selectorB 요소
- 일반 형제 결합자(~)
    - selectorA의 형제 요소 중 뒤에 위치하는 selectorB 요소를 모두 선택
- 인접 형제 결합자(+)
    - selectorA이 형제 요소 중 바로 뒤에 위치하는 selectorB 요소를 선택

## CSS box model

<aside>
💡 모든 요소는 **네모(박스모델)**이고, 위에서부터 아래로 왼쪽에서 오른쪽으로 쌓인다. **(좌측 상다에 배치)**

</aside>

### Box model

- 모든 HTML 요소는 box 형태로 되어있음
- 하나의 박스는 네 부분(영역)으로 이루어짐
    - margin
    - border
    - padding
    - content
- 상하좌우

### box sizing
- 기본적으로 모든 요소의 box-sizing은 content-box

## CSS Display

### CSS 원칙 2

- 모든 요소는 네모(박스모델)이고, 좌측상단에 배치.
- **Display에 따라 크기와 배치가 달라진다**

### 대표적으로 활용되는 display

- display: block
    - 줄 바꿈이 일어나는 요소
    - 화면 크기 전체의 가로 폭을 차지한다.
    - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음.
- display: inline
    - 줄 바꿈이 일어나지 않는 행의 일부 요소
    - content 너비만큼 가로 폭을 차지한다.
    - width, height, margin-top, margin-bootom을 지정할 수 없다.
    - 상하 여백은 line-height로 지정한다.

### 블록 레벨 요소와 인라인 레벨 요소

- 블록 레벨 요소와 인라인 레벨 요소 구분 (HTML 4.1 까지)
- 대표적인 블록 레벨 요소
    - div / ul,ol,li / p/ hr/ form 등
- 대표적인 인라인 레벨 요소
    - span/ a / img/ imput, label/ b, em, i, strong 등

### CSS position

- 문서 상에서 요소의 위치를 지정
- static : 모든 태그의 기본 값(기준위치)
    - 일반적인 요소의 배치 순성 따름(좌측 상단)
    - 부모 요소 내에서 배치 될 때는 부모 요소의 위치를 기준으로 배치 됨
- 아래는 좌표 프로퍼티(top, bottom, left, right)를 사용하여 이동 가능
    1. relative
    2. absolute
    3. fixed
    4. sticky
1. relative: 상대 위치
    - 자기 자신의 static 위치를 기준으로 이동(normal flow 유지)
    - 레이아웃에서 요소가 차지하는 공간은 static일 때와 같음 (normal position 대비 offset)
2. absolute : 절대 위치
    - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음(normal flow에서 벗어남)
    - static이 아닌 가장 가까이 있는 부모/ 조상 요소를 기준으로 이동(없는 경우 브라우저 화면 기준으로 이동)
3. fixed : 고정 위치
    - 요소를 이란적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음(normal flow에서 벗어남)
    - 부모 요소와 관계없이 viewport를 기준으로 이동
        - 스크롤 시에도 항상 같은 곳에 위치함
4. stikcy: 스크롤에 다라 static → fixed로 변경
    - 속성을 적용한 박스는 평소에 문서 안에서 position: static 상태와 같이 일반적인 흐름에 따르지만 스크롤 이치가 임계점에 이르면 position: fixed와 같이 박스를 화면에 고정할 수 있는 속성

### CSS 원칙

- CSS 원칙 1, 2 :Normal flow
    - 모든 요소는 네모(박스모델), 좌측상단에 배치
    - display에 따라 크기와 배치가 달라짐
- CSS 원칙 3
    - **position으로 위치의 기준을 변경**
        - relative : 본인의 원래 위치
        - absolute : 특정 부모의 위치
        - fixed : 화면의 위치
        - sticky : 기본적으로 static이나 스크롤 이동에 따라 fixed로 변경