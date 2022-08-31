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