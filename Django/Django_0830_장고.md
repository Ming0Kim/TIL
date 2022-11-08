## Django intro

---

### Django 시작하기

**Framework**

- 서비스 개발에 필요한 기능들을 미리 구현해서 모아 놓은 것
- 일정한 뼈대, 틀을 가지고 일하다
- `소프트웨어 프레임워크` : 복잡한 문제를 해결하거나 서술하는 데 사용하는 기본 개념 구조
- 소프트웨어의 생산성과 품질을 높임

**Django를 써야하는 이유**

- Python으로 작성된 프레임워크
- 수많은 여러 유용한 기능들
- 검증된 웹 프레임워크
    - 화해, Toss, 두나무, 당근마켓, 요기요

<aside>
💡 **Django는 서버를 구현하는 웹 프레임워크**

</aside>

### Web 이해하기

- World Wide Web : 전세계에 퍼져있는 거미줄 같은 연결망
- 해저케이블 설치 → 연결되어있는 세계
- 인터넷을 이용한다는 것 : 전세계의 컴퓨터가 연결되어 있는 하나의 인프라를 이용하는 것

### 클라이언트와 서버

**클라이언트**

- 웹 사용자의 인터넷에 연결된 장치 (wifi에 연결된 컴퓨터 또는 모바일 등)
- Chrome 또는 Firefox와 같은 웹브라우저
- 서비스를 요청하는 주체

**서버**

- 웹 페이지, 사이트 또는 앱을 저장하는 컴퓨터
- 클라이언트가 웹페이지에 접근하려고 할 때 서버에서 클라이언트 컴퓨터로 웹 페이지 데이터를 응답해 사용자의 웹 브라우저에 표시됨
- 요청에 대해 서비스를 응답하는 주체

**상호작용 예시**

- Google 홈페이지에 접속한다는 것
1. 결론적으로 인터넷에 연결된 전세계 어딘가에 잇는 구글 컴퓨터에게 `google 홈페이지.html`파일을 달라고 요청하는 것
2. 그러면 구글 컴퓨터는 우리의 요청을 받고 `Google 홈페이지.html`파일을 인터넷을 통해서 우리 컴퓨터에게 응답해줌
3. 그렇게 전달받은 `Google 홈페이지.html`파일을 웹 브라우저가 우리가 볼 수 있도록 해석해주는 것
- `Google 홈페이지.html` 을 달라고 요청한 컴퓨터, 웹 브라우저 : **클라이언트**
- `Google 홈페이지.html` 제공한 컴퓨터, 프로그램 : **서버**
- **클라이언트** : 어떠한 자원을 달라고 요청하는 쪽
- **서버** : 자원을 제공해주는 쪽

<aside>
💡 앞으로 배우는 것 : **이 클라이언트-서버 구조를 만드는 방법**

</aside>

### Web browser와 Web page

**웹 브라우저**

- 웹에서 페이지를 찾아 보여주고, 사용자가 하이퍼링크를 통해 다른 페이지로 이동할 수 있도록 하는 프로그램
- 웹 페이지 파일을 우리가 보는 화면으로 바꿔주는 렌더링 프로그램
- **정적 웹페이지**
    - 있는 그대로를 제공하는 것
    - 우리가 지금까지 작성한 웹페이지
    - 한번 작성된 HTML 파일의 내용이 변하지 않고 모든 사용자에게 동일한 모습으로 전달되는 것
- **동적 웹페이지**
    - Dynamic Web page
    - 사용자의 요청에 따라 웹페이지에 추가적인 수정이 되어 클라이언트에게 전달되는 웹페이지
    - **서버** : 웹 페이지의 내용을 바꿔주는 주체
    - **Django** : 사용자의 요청을 받아 적절한 응답을 만들어주는 프로그램을 쉽게 만들 수 있게 도와주는 프레임워크
    - 다양한 서버 사이드 프로그래밍 언어(파이썬, 자바) 사용 가능 파일을 처리하고 데이터베이스와의 상호작용이 이루어짐
    - 이 중에서 `python`을 이용해서 개발할 수 있는 프레임워크인 `Django`를 학습하는 것

## 💡Django 구조 이해하기 (MTV Design Pattern)

### Design pattern

- 여러번 짓다보니 **자주 사용되는 구조가 있다는 것**을 알게 되었고 **이를 일반화해서 하나의 공법**으로 만들어 둔 것
- `패턴` : 각기 다른 기능을 가진 다양한 응용 소프트웨어를 개발할 때 공통적인 설계 문제가 존재하며, 이를 처리하는 해결책 사이에도 공통점이 있다는 것을 발견

**소프트웨어 디자인 패턴의 목적**

- 클라이언트-서버 구조도 소프트웨어 디자인 패턴 중 하나
- 자주 사용되는 소프트웨어의 구조를 소수의 뜅어난 엔지니어가 일반적인 구조화를 해둔 것
- 특정 문맥에서 공통적으로 발생하는 문제에 대해 재사용 가능한 해결책을 제시
- 프로그래머가 어플리케이션이나 시스템을 디자인할 때 발생하는 공통된 문제들을 해결하는데 형식화된 가장 좋은 관행

**소프트웨어 디자인 패턴의 장점**

- 다수의 엔지니어들이 일반화된 패턴으로 소프트웨어 개발을 할 수 있도록 한 규칙, 커뮤니케이션의 효율성을 높이는 기법

### Django’s Design Pattern ⇒ MTV 패턴

- MTV 패턴은 **MVC 디자인 패턴**을 기반으로 조금 변형된 패턴

**MVC 소프트웨어 디자인 패턴**

- MVC : Model - View - Controller
    - 데이터 및 논리 제어를 구현하는데 널리 사용되는 소프트웨어 디자인 패턴
- 세가지 역할
    - `Model` : 데이터와 관련된 로직을 관리
    - `View` : 레이아웃과 화면을 처리
    - `Controller` : 명령을 `model`과 `view`부분으로 연결

**MVC 소프트웨어 디자인 패턴의 목적**

- **관심사 분리**
- 각 부분을 독립적으로 개발할 수 있어, 하나를 수정하고 싶을 때 모두 건들지 않아도 됨
    - 개발 효율성 및 유지보수가 쉬워짐
    - 다수의 멤버로 개발하기 용이함

**django에서의 디자인 패턴**

- Django는 MVC패턴을 기반으로 한 MTV패턴을 사용
- 두 패턴은 서로 크게 다른 점 없으나 일부 역할에 대해 부르는 이름이 다름

| MVC | MTV |
| --- | --- |
| Model | Model |
| View | Template |
| Controller | View |

### MTV 디자인 패턴

**Model**

- MVC  패턴에서 model의 역할에 해당
- 데이터와 관련된 로직을 관리
- 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리

**Template**

- 레이아웃과 화면을 처리
- 화면상의 사용자 인터페이스 구조와 레이아웃을 정의
- MVC 패턴에서 View의 역할에 해당

**View**

- Model & Template과 관련한 로직을 처리해서 응답을 반환
- 클라이언트의 요청에 대해 처리를 분기하는 역할
- 동작 예시
    - 데이터가 필요하다면 `mode`에 접근해서 데이터를 가져옴
    - 가져온 데이터를 `template`로 보내 화면을 구성함
    - 구성된 화면을 응답으로 만들어 클라이언트에게 반환
- MVC 패턴에서 `Controller`의 역할에 해당

✅ **정리**

- Django는 MTV 디자인 패턴을 가지고있음
    - Model : 데이터 관련
    - Template : 화면 관련
    - View : Model & Template 중간 처리 및 응답 반환

## Django Quick Start

---

### 기본 설정

**가상환경 설정 및 활성화**

- `python -m venv venv` : 가상환경 설정
- `source ./venv/Scripts/activate` : 가상환경 활성화
- `pip install django==3.2.13` : 가상환경에 장고 설치 3.2.13(LTS)이 우리가 쓰는 버전
- `pip freeze > requirements.txt` : 패키지 목록 생성
- `pip install -r requirements.txt` : 파일을 이용해 패키지 한번에 설치

**Django 설치**

- **설치 전 가상환경 설정 및 활성화를 마치고 진행**
    - 버전 명시해서 설치 : `pip install django==3.2.13`
    - 패키지 목록 생성 : `pip freeze > requirements.txt`

**Django Project**

- 프로젝트 생성 : `django-admin startproject firstpjt .`
    - project 이름에는 python이나 django에서 사용 중인 키워드 및 ‘-’(하이픈) 사용 불가
    - ‘.’을 붙이지 않을 경우 현재 디렉토리에 프로젝트 디렉토리를 새로 생성하게 디ㅗㅁ
- 서버 실행 : `python [manage.py](http://manage.py) runserver`

**프로젝트 구조**

- `__init__.py`
    - python에게 이 디렉토리를 하나의 python 패키지로 다루도록 지시
    - 별도로 추가 코드 작성 X
- `asgi.py`
    - Asynchronous Server Gateway Interface
    - django 애플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 도움
    - 추후 배포 시에 사용하며 지금은 수정하지 않음
- ✅ `settings.py`
    - Django 프로젝트 설정을 관리
- ✅ `urls.py`
    - 사이트의 url과 적절한 views의 연결을 지정
- `wsgi.py`
    - Web Server Gateway Interface
    - Django 애플리케이션이 웹서버와 연결 및 소통하는 것을 도움
    - 추후 배포 시에 사용하며 지금은 수정하지 않음
- `manage.py`
    - Django 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티

**Django Application**

- 애플리케이션(앱) 생성 : `python [manage.py](http://manage.py) startapp articles`
    - 일반적으로 애플리케이션 이름은 ‘복수형’으로 작성하는 것을 권장

**애플리케이션 구조**

- `admin.py`
    - 관리자용 페이지를 설정하는 곳
- `apps.py`
    - 앱의 정보가 작성된 곳
    - 별도로 추가 코드를 작성하지 않음
- `models.py`
    - 애플리케이션에서 사용하는 Model을 정의하는 곳
    - MTV패턴의 M에 해당
- `tests.py`
    - 프로젝트의 테스트 코드를 작성하는 곳
- `views.py`
    - view 함수들이 정의되는 곳
    - MTV 패턴의 V에 해당

**애플리케이션 등록**

- 프로젝트에서 앱을 사용하기 위해서는 반드시 `INSTALLED_APPS`리스트에 추가해야함
- Django installation에 활성화 된 모든 앱을 지정하는 문자열 목록

**Project & Application**

- Project
    - `collection of apps`
    - 프로젝트는 앱의 집합
    - 프로젝트에는 여러 앱이 포함될 수 있음
    - 앱은 여러 프로젝트에 있을 수 있음
- Application
    - 앱은 실제 요청을 처리하고 페이지를 보여주는 등의 역할을 담당
    - 일반적으로 앱은 하나의 역하 및 기능 단위로 작성하는 것을 권장함

**애플리케이션 주의사항**

- **반드시 생성 후 등록**
    - `INSTALLED_APPS`에 먼저 작성(등록)하고 생성하려면 앱이 생성되지 않음
- 해당 순서를 지키지 않아도 수업 과정에서는 문제가 없지만, 추후 advanced한 내용을 대비하기 위해 지키는 것을 권장

### 요청과 응답

- `URLs` : `URL` → `VIEW` → `TEMPLATE` 순의 작성 순서로 코드를 작성해보고 데이터의 흐름을 이해하기
    
    ```python
    #urls.py
    
    from django.contrib import admin
    from django.urls import path
    from articles import views
    
    urlpatters = [
    		path('admin/', admin.site.urls),
    		path(index/', views.index),
    ]
    ```
    
- `View`
    - HTTP 요청을 수신하고 HTTP 응답을 반환하는 함수 작성
    - `Template`에게 HTTP 응답 서식을 맡김
    
    ```python
    # articles/views.py
    
    def index(request):
    return render(request, 'index.html')
    ```
    
- `render()`
    - `render(request, template_name, context)`
    - 주어진 템플릿을 주어진 컨텍스트 데이터와 결합하고 렌더링된 텍스트와 함께HttpResponse(응답) 객체를 반환하는 함수
    - `request` : 응답을 생성하는 데 사용되는 요청 객체
    - `template_name` : 템플릿의 전체 이름 또는 템플릿 이름의 경로
    - `context` : 템플릿에서 사용할 데이터 (딕셔너리 타입으로 작성)
- `Templates`
    - 실제 내용을 보여주는데 사용되는 파일
    - 파일의 구조나 레이아웃을 정의
    - Template 파일의 기본 경로
        - app 폴더 안의 templates 폴더
        - `app_name/templates/`
        - **템플릿 폴더 이름은 반드시 templates라고 지정해야 함
    
    ```html
    <!-- articles/templates/index.html -->
    
    <!DOCTYPE html>
    <html lang="en">
    <head>
    	<!-- 생략 -->
    </head>
    <body>
    	<h1>만나서 반가워요!</h1>
    </body>
    </html>
    ```
    
- 코드 작성 순서
    - 앞으로 Django에서의 코드 작성은 `URL -> View -> Template` 순으로 작성
    - **데이터의 흐름 순서**
        - `URL` : `path('index/', views.index)`
        - `View` : `def index(request): / return render(request, 'index.html')`
        - `Template` : `articles/templates/in`

## Djnago Templates

---

**데이터 표현을 제어하는 도구이자 표현에 관련된 로직**

- Django Template을 이용한 HTML 정적 부분과 동적 컨텐츠 삽입
- Template System의 기본 목표를 숙지

### **Django Template Language (DTL)**

**DTL Syntax**

1. Variable : `{{variable}}`
2. Filters : `{{variable|filter}}`
3. Tags : `{%tag%}`
4. Comments : `{# #}`

### Template inheritance

**템플릿 상속**

- 템플릿 상속은 기본적으로 코드의 재사용성에 초점을 맞춤
- `{% extends '' %}` : 자식(하위 텤플릿이 부모 템플릿을 확장한다
    - **반드시 템플릿 최상단에 작성되어야 함 (즉, 2개 이상 사용할 수 없음)**
- `{% block content %}{% endblock content %}`
    - 하위 템플릿에서 재지정할 수 있는 블록

**추가 템플릿 경로 추가하기**

- 추가 템플릿 경로
    - `app_name/templates/` 디렉토리 경로 외 추가 경로를 설정한 것

## Sending and Retrieving from data

---

### Sending form data (Client)

**HTML <form> elemnet**

- 데이터가 전송되는 방법을 정의
- 웹에서 사용자 정보를 입력하는 여러 방식(text, button, submit 등)을 제공하고, **사용자로부터 할당된 데이터를 서버로 전송**하는 역할을 담당
- **데이터를 어디(action)로 어떤 방식(method)으로 보낼지**
- 핵심 속성 : `action` `method`

**HTML form’s attributes**

1. `action`
    - 입력 데이터가 전송될 URL을 지정
    - 데이터를 어디로 보낼 것인지 지정하는 것이며 이 값은 반드시 유효한 URL이어야 함
    - 만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 URL로 보내짐
2. `method`
    - 데이터를 어떻게 보낼 것인지 정의
    - 입력 데이터의 HTTP request methods를 지정
    - HTML form 데이터는 오직 2가지 방법으로만 전송할 수 있는데 바로 GET 방식과 POST 방식

**HTML <input> element**

- 사용자로부터 데이터를 입력 받기 위해 사용
- **type**속성에 따라 동작 방식이 달라진다
    - input 요소의 동작 방식은 type 특성에 따라 현격히 달라지므로 각각의 type은 별도로 MDN 문서에서 참고하여 사용하도록 함
    - type을 지정하지 않은 경우, 기본값은 **text**
- 핵심 속성 : `name`

**HTML input’s attribute**

1. `name`
    - form을 통해 데이터를 제출(submit)했을 때 name 속성에 설정된 값을 서버로 전송하고, 서버는 name 속성에 설정된 값을 통해 사용자가 입력한 데이터 값에 접근할 수 있음
    - 주요 용도는 GET/POST 방식으로 서버에 전달하는 파라미터(name은 key, value는 value)로 매핑하는 것
        - GET 방식에서는 URL에서 `'?key=value&key=value/'`형식으로 데이터를 전달

**HTTP request method**

- HTTP
    - HTML 문서와 같은 리소스(데이터, 자원)들을 가져올 수 있도록 해주는 프로토콜(규칙, 규약)
- 웹에서 이루어지는 모든 데이터 교환의 기초
- HTTP는 주어진 리소스가 수행할 원하는 작업을 나타내는 request methods를 정의
- 자원에 대한 행위(수행하고자 하는 동작)을 정의
- 주어진 리소스(자원)에 수행하길 원하는 행동을 나타냄
- HTTP Method 예시
    - GET, POST, PUT, DELETE

**GET**

- 서버로부터 정보를 조회하는 데 사용
    - 즉, 서버에게 리소스를 요청하기 위해 사용
- 데이터를 가져올 때만 사용해야함
- 데이터를 서버로 전송할 때 Query String Parameters를 통해 전송
    - 데이터는 URL에 포함되어 서버로 보내짐

**Query String Parameters**

- 사용자가 입력 데이터를 전달하는 방법 중 하나로, url 주소에 데이터를 파라미터를 통해 넘기는 것
- 이러한 문자열은 앰퍼샌드로 연결된 `key=value`쌍으로 구성되며, 기본 URL과 물음표로 구분됨
    - `http://host:port/path?key=value&ket=value`
- Query String이라고도 함
- 정해진 주소 이후에 물음표를 쓰는 것으로 Query String이 시작함을 알림
- `key=value`로 필요한 파라미터의 값을 적음
    - =로 key와 value가 구분됨
- 파라미터가 여러 개일 경우 &을 붙여 여러 개의 파라미터를 넘길 수 있음

### Retrieving the data (Server)

- **데이터 가져오기(검색하기)**
- 서버는 클라이언트로 받은 `key=value`쌍의 목록과 같은 데이터를 받게 됨
- 이러한 목록에 접근하는 방법은 사용하는 특정 프레임워크에 따라 다름
- 우리는 Django 프레임워크에서 어떻게 데이터를 가져올 수 있을지 알아볼 것

**Request and Response objects**

- 요청과 응답 객체 흐름
1. 페이지가 요청되면 Django는 요청에 대한 메타데이터를 포함하는 `HttpRequest object`를 생성
2. 그리고 해당하는 적절한 view함수를 로드하고 HttpRequest를 첫번째 인자로 전달
3. 마지막으로 view함수는 HttpResponse object를 반환

## DJango URLs

---

- **Dispatcher로서의 URL 이해하기**
- 웹 어플리케이션은 URL을 통한 클라이언트의 요청에서부터 시작함

### Trailing URL Slashes

- Django는 URL 끝에 /가(Trailing slash) 없다면 자동으로 붙여주는 것이 기본 설정
    - 그래서 모든 주소가 /로 끝나도록 구성되어 있음
    - 그러나 모든 프레임워크가 이렇게 동작하는 것은 아님
- Django의 url 설계 철학을 통해 먼저 살펴보면 다음과 같이 설명함
- **기술적인 측면에서, `[foo.com/bar`와](http://foo.com/bar와) `[foo.com/bar/`는](http://foo.com/bar/는) 서로 다른 URL이다.**
    - 검색 엔진 로봇이나 웹 트래픽 분석 도구에서는 그 둘을 서로 다른 페이지로 봄
    - 그래서 Django는 URL을 정규화하여 검색 엔진 로봇이 혼동하지 않게 해야함

### Variable routing

**Variable routing의 필요성**

- 템플릿의 많은 부분이 중복되고, 일부분만 변경되는 상황에서 비슷한 URL과 템플릿을 계속해서 만들어야 할까?

**Variable routing**

- URL 주소를 변수로 사용하는 것을 의미
- URL의 일부를 변수로 지정하여 view함수의 인자로 넘길 수 있음
- 즉, 변수 값에 따라 하나의 `path()`에 여러 페이지를 연결 시킬 수 있음

**Variable routing 작성**

- 변수는 <>에 정의하며 view 함수의 인자로 할당됨
- 기본 타입은 string이며 5가지 타입으로 명시할 수 있음
1. str
    - /를 제외하고 비어있지 않은 모든 문자열
    - 작성하지 않을 경우 기본 값
2. int
    - 0 또는 양의 정수와 매치
3. slug
4. uuid
5. path

### App URL mapping

- 앱이 많아졌을 때 `urls.py`를 각 app에 매핑하는 방법을 이해하기
- 두번째 app인 **pages**를 생성 및 등록 하고 진행
- app의 view함수가 많아지면서 사용하는 `path()` 또한 많아지고, app 또한 더 많이 작성되기 떄문에 프로젝트의 `urls.py`에서 모두 관리하고 것은 프로젝트 유지보수에 좋지 않음
- 하나의 프로젝트의 여러 앱이 존재한다면, 각각의 앱 안에 `urls.py`을 만들고 프로젝트 `urls.py`에서 각 앱의 `urls.py`파일로 URL 매핑을 위탁할 수 있음
- **각각의 app 폴더 안에 `urls.py`를 작성**하고 수정

**Including other URLconfs**

- urlpattern은 언제든지 다른 URLconf 모듈을 포함(include)할 수 있음

<aside>
💡 include되는 앱의 url.py에 urlpatterns가 작성되어 있지 않다면 에러가 발생
예를 들어, pages 앱의 urlpatterns가 빈 리스트라도 작성되어 있어야함

</aside>

- 이제 메인 페이지의 주소는 이렇게 바뀌었음
    - `[http://127.0.0.1:8000/index/](http://127.0.0.1:8000/index/)` → `http://127.0.0.1:8000/articles/index/`
- `include()`
    - 다른 URLconf(app1/urls.py)들을 참조할 수 있도록 돕는 함수
    - 함수 include()를 만나게 되면 URL의 그 시점까지 일치하는 부분을 잘라내고, 남은 문자열 부분을 후속 처리를 위해 include된 URLconf로 전달

### Naming URL patterns

**Naming URL patterns의 필요성**

- 만약 `index/`의 문자열 주소를 `new-index/`로 바꿔야 한다고 가정
- 그렇다면 `index/`주소를 사용햇던 모든 곳을 찾아서 변경해야 하는 번거로움이 발생

**Naming URL patterns**

- 이제는 링크에 URL을 직접 작성하는 것이 아니라 `path()`함수의 name인자를 정의해서 사용
- DTL의 Tag중 하나인 **URL 태그**를 사용해서 `path()`함수에 작성한 name을 사용할 수 있음
- 이를 통해 URL 설정에 정의된 특정한 경로들의 의존성을 제거할 수 있음
- Django는 URL에 이름을 지정하는 방법을 제공함으로써 view함수와 템플릿에서 특정 주소를 쉽게 참조할 수 있도록 도움

**Built-in tag-”url”**

- `{% url '' %}`
- 주어진 URL 패턴 이름 및 선택적 매개 변수와 일치하는 절대 경로 주소를 반환
- 템플릿에 URL을 하드 코딩하지 않고도 DRY원칙을 위반하지 않으면서 링크를 출력하는 방법

### Django의 설계 철학 (Templates System)

1. **표현과 로직(view)를 분리**
    - 템플릿 시스템은 표현을 제어하는 도구이자 표현에 관련된 로직일 뿐
    - 즉, 템플릿 시스템은 이러한 기본 목표를 넘어서는 기능을 지원하지 말아야함
2. **중복을 배제**
    - 대다수의 동적 웹사이트는 공통 header, footer, navbar 같은 사이트 공통 디자인을 가짐
    - Django 템플릿 시스템은 이러한 요소를 한 곳에 저장하기 쉽게 하여 중복 코드를 없애야 함
    - 템플릿 상속의 기초가 되는 철학

### Framework의 성격

- **독선적(Opinionated)**
    - 독선적인 프레임워크들은 어떤 특정 작업을 다루는 ‘올바른 방법’에 대한 분명한 의견을 가지고 있음
    - 대체로 특정 문제 내에서 빠른 개발방법을 제시
    - 어떤 작업에 대한 올바른 방법이란 보통 잘 알려져 있고 문서화가 잘 되어있기 때문
    - 하지만 주요 상황을 벗어난 문제에 대해서는 그리 유연하지 못한 해결책을 제시할 수 있음
- **관용적(Unopinionated)**
    - 관용적인 프레임워크들은 구성요소를 한데 붙여서 해결해야 한다거나 심지어 어떤 도구를 써야 한다는 ‘올바른 방법’에 대한 제약이 거의 없음
    - 이는 개발자들이 특정 작업을 완수하는데 가장 적절한 도구들을 이용할 수 있는 자유도가 높음
    - 하지만 개발자 스스로가 그 도구들을 찾아야 한다는 수고가 필요

### Django Framework의 성격

- **다소 독선적**
    - 양쪽 모두에게 최선의 결과를 준다고 강조
- 결국 하고자 하는 말은 현대 개발에 있어서는 가장 중요한 것들 중 하나는 **생산성**
- 프레임워크는 우리가 하는 개발을 방해하기 위해 규칙, 제약을 만들어 놓은 것이 아님
- 우리가 온전히 만들고자 하는 것에만 집중할 수 있게 도와주는 것
- **수레바퀴를 다시 만들지 말라**