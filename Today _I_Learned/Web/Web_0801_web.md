
## Web

### 웹 사이트의 구성 요소

- 웹사이트란 부라우저를 통해서 접속하는 웹 페이지(문서)들의 모음
- 웹 페이지란 글, 그림, 동영상 등 여러가지 정보를 담고 있으며, 마우스로 클릭하면 다른 웹 페이지로 이동하는 `링크`들이 있음. ‘링크’를 통해 여러 웹 페이지를 연결한 것을 웹 사이트라고 함.
- HTML ⇒ 구조 / CSS ⇒ 표현 / Javascript ⇒ 동작

### 웹 사이트와 브라우저

- 웹 사이트는 브라우저를 통해 동작함
- 브라우저마다 동작이 약간씩 달라서 문제가 생기는 경우가 많음(파편화)
- 해결책으로 웹 표준이 등장

### 웹 표준

- 웹에서 표준적으로 사용되는 기술이나 규칙
- 어떤 브라우저든 웹 페이지가 동일하게 보이도록 함(크로스 브라우징)

## HTML

### HTML

- **Hyper Text** Markup Language
- Markup Language : 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
    - HTML, Markdown
- 웹 페이지를 작성(구조화)하기 위한 언어

```html
<!-- HTML 스타일 가이드 -->

<body>
	<h1> 웹문서 </h1>
	<ul>
		<li>HTML</li>
		<li>CSS</li>
	</ul>
</body>
```

### HTML 기본 구조

- html : 문서의 최상위(root) 요소
- head : 문서 메타데이터 요소
    - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
    - 일반적으로 브라우저에는 나타나지 않는 내용
    - body : 문서 본문 요소
        - 실제 화면 구성과 관련된 내용

```html
<!-- HTML 기본 구조 -->

<!DOCTYPE html>
<html lang='en>
<head>
	<meta charset="UTF-8">
	<title>Document</title>
</head>
<body>

</body>
</html>
```

### head 예시

`<title>` : 브라우저 상단 타이틀

`<meta>` : 문서 레벨 메타데이터 요소

`<link>` : 외부 리소스 연결 요소(CSS 파일, favicon 등)

`<script>` : 스크립트 요소(JavaScript 파일)

`<style>` : CSS 직접 작성

```html
<!-- head 예시 -->

<head>
	<title>HTML 수업</title>
	<meta charset="UTF-8">
	<link href="style.css" rel="stylesheet">
	<script src="javascript.js"></script>
	<style>
		p {
			color: black;
		}
	</style>
</head>
```

### 요소

HTML의 요소는 태그와 내용(contents)로 구성되어 있다.

<aside>
💡 <h1>contents</h1>

</aside>

- HTML 요소는 시작 태그와 종료 태그 그리고 태그 사이에 위치한 내용으로 구성
    - 요소는 태그로 컨텐츠(내용)를 감싸는 것으로 그 저보와 성격과 의미를 정의
    - 내용이 없는 태그들도 존재(닫는 태그가 없음)
        - br, hr, img, input, link, meta
- 요소는 중첨(nested)될 수 있음
    - 요소의 중첩을 통해 하나의 문서를 구조화
    - 여는 태그와 닫는 태그의 쌍을 잘 확인해야함
        - 오류를 반환하는 것이 아닌 그냥 레이아웃이 깨진 상태로 출력되기 때문에, 디버깅이 힘들어질 수 있음

### 속성

<aside>
💡 <a href=”https://google.com”></a>

</aside>

- 속성을 통해 태그의 부가적인 정보를 설정할 수 있음
- 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가적인 정보를 제공
- 요소의 시작 태그에 작성하며 보통 이름과 값이 하나의 쌍으로 존재
- 태그와 상관없이 사용 가능한 속성(HTML Global Attribute)들도 있음

### HTML Global Attribute

- 모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성 (몇몇 요소에는 아무 효과가 없을 수 있음)
- `id` : 문서 전체에서 유일한 고유 식별자 지정
- `class` :공백으로 구분된 해당 요소의 클래스의 목록(CSS, JS에서 요소를 선택하거나 접근)
- `data-*` : 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용
- `style` : inline 스타일
- `title` : 요소에 대한 추가 정보 지정
- `tabindex` : 요소의 탭 순서

```html
 <!-- HTML 코드 예시 -->

<!DOCTYPE html>
<html lang="en">
<head<
	<meta charset="UTF-8">
	<title>Document</title>
</head>
<body>
	<!-- 이것은 주석입니다. -->
	<h1>나의 첫번째 HTML</h1>
	<p>이것은 본문입니다.</p>
	<span>이것은 인라인요소</span>
	<a href="http://www.naver.com">네이버로 이동!!</a>
</body>
</html>
```

### 시맨틱 태그

- HTML5에서 의미론적 요소를 담은 태그의 등장
    - 기존 영역을 의미하는 div 태그를 대체하여 사용
- 대표적인 태그 목록
    - `header` : 문서 전체나 섹션의 헤더(머리말 부분)
    - `nav` : 내비게이션
    - `aside` : 사이드에 위치한 공간, 메인 콘텐츠와 관련성이 적은 콘텐츠
    - `section` : 문서의 일반적인 구분, 컨텐츠의 그룹을 표현
    - `article` : 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
    - `footer` : 문서 전체나 섹션의 푸터(마지막 부분)
- Non semantic 요소는 div, span 등이 있으며 h1, table 태그들도 시맨틱 태그로 볼 수 있음
- 개발자 및 사용자 뿐만 아니라 검색엔진 등에 의미 있는 정보의 그룹을 태그로 표현
- 단순히 구역을 나누는 것 뿐만 아니라 ‘의미’를 가지는 태그들을 활용하기 위한 노력
- 요소의 의미가 명확해지기 때문에 코드의 가독성을 높이고 유지보수를 쉽게 함
    - 검색엔진최적화(SEO)를 위해서 메타태그, 시맨틱 태그 등을 통한 마크업을 효과적으로 활용 해야함
    
    ### 텍스트로 작성된 코드가 어떻게 웹사이트가 되는 걸까?
    
    렌더링 : 웹사이트 코드를 사용자가 보게되는 웹사이트로 바꾸는 과정
    
### form

- <form>은 정보(데이터)를 서버에 제출하기 위해 사용하는 태그
- <form> 기본 속성
    
    `action` : form을 처리할 서버의 URL(데이터를 보낼 곳)
    
    `method` : form을 제출할 때 사용할 HTTP 메서드(GET 혹은 POST)
    
    `enctype` : method가 post인 경우 데이터의 유형
    
    `application/x-www-form-urlencoded` : 기본값
    
    `multipart/form-data` : 파일 전송시(input type이 file인 경우)
    