## Namespace

---

- 개체를 구분할 수 있는 범위를 나타내는 namespace(이름공간)에 대한 이해

### URL namespace

- URL namespace를 사용하면 서로 다른 앱에서 동일한 URL 이름을 사용하는 경우에도 이름이 지정된 URL을 고유하게 사용할 수 있음
- `app_name` : attribute를 작성해 URL namespace를 설정
- `app_name`을 지정한 이후에는 url 태그에서 반드시 `app_name:url_name` 형태로만 사용해야 함
- 그렇지 않으면 `NoreverceMatch` 에러 발생
    - url 태그만 확인하면 된다
- `articles:index`

### Template namespace

- Django는 기본적으로 `app_name/templates/` 경로에 있는 templates 파일들만 찾을 수 있으며, `setting.py`의 `INSTALLED_APPS`에 작성된 app 순서로 template을 검색 후 렌터링함

**디렉토리 생성을 통해 물리적인 이름공간 구분**

- Django templates의 기본 경로에 app과 같은 이름의 폴더를 생성해 폴더 구조를 `app_name/templates/app_name/`형태로 변경
- Django templates의 기본 경로 자체를 변경할 수는 없기 때문에 물리적으로 이름 공간을 만드는 것

**템플릿 경로 변경**

- 폴더 구조 변경 후 변경된 경로로 해당하는 모든 부분을 수정하기
- `return render(request, 'articles/index.html')`
- `return render(request, 'pages/index.html')`

## Django Model

---

- Mode(이하 모델)의 핵심 개념과 ORM을 통한 데이터베이스 조작 이해
- Django는 웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 추상적인 계층(모델)을 제공

### Database

- 체계화된 데이터의 모임
- 검색 및 구조화 같은 작업을 보다 쉽게 하기 위해 조직화된 데이터를 수집하는 저장시스템
- 스키마(Schema) / 테이블(Table)

**스키마(Schema)**

- 뼈대
- 데이터베이스에서 자료의 구조, 표현방법, 관계 등을 정의한 구조

**테이블(Table)**

- 필드와 레코드를 사용해 조직된 데이터 요소들의 집합
- 관계(Relation)라고도 부름
1. 필드(field) : 속성, 컬럼(col)
2. 레코드(record) : 튜플, 행(row)

**필드(field)**

- 속성 혹은 컬럼(col)
- 각 필드에는 고유한 데이터 형식이 지정됨 : INT, TEXT

**레코드(record)**

- 튜플 혹은 행(row)
- 테이블의 데이터는 레코드에 저장됨

**PK (Primary Key)**

- 기본 키
- 각 레코드의 고유한 값 (식별자로 사용)
- 기술적으로 **다른 항목과 절대로 중복되어 나타날 수 없는 단일 값(unique)**을 가짐
- 데이터베이스 관리 및 테이블 간 관계 설정 시 주요하게 활용됨

**쿼리(Query)**

- 데이터를 조회하기 위한 명령어를 일컬음
- 조건에 맞는 데이터를 추출하거나 조작하는 명령어

### Model

**개요**

- Django는 Model을 통해 데이터에 접속하고 관리
- 단일한 데이터에 대한 정보를 가짐
- 사용자가 저장하는 데이터들의 필수적인 필드들과 동작들을 포함
- 저장된 데이터베이스의 구조(layout)
- 일반적으로 각각의 모델은 하나의 데이터베이스 테이블에 매핑(mapping)
    - 모델 클래스 1개 == 데이터베이스 테이블 1개

**Model 작성하기**

- 모델 클래스를 작성하는 것 → 데이터베이스 **테이블의 스키마를 정의**하는 것
- `모델 클래스 == 테이블 스키마`
- **id 컬럼은 테이블 생성시 django가 자동으로 생성**

**Model 이해하기**

- 각 모델은 django.models.Model 클래스의 서브 클래스
    - 즉, 각 모델은 django.db.models 모듈의 Model 클래스를 상속받아 구성됨
    - **클래스 상속 기반 형태의 Django프레임워크 개발**
        - 프레임워크에서는 잘 만들어진 도구를 가져다가 잘 쓰는 것
- models 모듈을 통해 어떠한 타입의 DB필드(컬럼)을 정의할 것인지 저으이
    - Article에는 어떤 데이터 구조가 필요한지 정의 : `스키마`
    - 클래스 변수 title과 content은 DB필드를 나타냄
1. 클래스 변수(속성)명
    1. DB 필드의 이름
2. 클래스 변수 값(models 모듈의 Field 클래스)
    1. DB 필드의 데이터 타입

**Django Model Field**

- django는 모델 필드를 통해 테이블의 필드(컬럼)에 저장할 데이터 유형 (INT, TEXT 등)을 정의
- 데이터 유형에 따라 다양한 모델 필드를 제공
    - DataField(), CharField(), IntegerField() 등
    - 공식 문서 : [https://docs.djangoproject.com/en/3.2/ref/models/fields/](https://docs.djangoproject.com/en/3.2/ref/models/fields/)
- `CharField(max_length=None, **options)`
    - 길이의 제한이 있는 문자열을 넣을 때 사용
    - `max_length`
        - 필드의 최대 길이(문자)
        - CharField의 필수 인자
        - 데이터베이스와 Django의 유효성 검사(값을 검증하는 것)에서 활용됨
- `TextField(**options)**`
    - 글자의 수가 많을 때 사용
    - `max_length` 옵션 작성 시 사용자 입력 단계에서는 반영되지만, 모델과 데이터베이스 단계에는 적용되지 않음(CharField를 사용해야 함)
        - 실제로 저장될 때 길이에 대한 유효성을 검증하지 않음
- 데이터베이스 스키마
    - 지금까지 작성한 `models.py`는 다음과 같은 데이터베이스 스키마를 설계한 것
    - 이제 데이터베이스에 테이블을 생성하기 위한 **설계도** 작성이 필요함

### Migrations

- 모델에 대한 청사진(blueprint)을 만들고 이를 통해 테이블을 생성하는 일련의 과정
- Django가 모델에 생긴 변화(필드 추가, 모델 삭제 등)를 반영하는 방법

**makemigrations**

- 모델을 작성 혹은 변경한 것에 기반한 새로운 migration(설계도, 청사진 이하 마이그레이션)을 만들 때 사용
- **테이블을 만들기 위한 설계도를 생선하는 것**
- `python [manage.py](http://manage.py) makemigrations`

**migrate**

- makemigrations로 만든 설계도를 실제 `db.sqlite3` DB 파일에 반영하는 과정
- 결과적으로 모델에서의 변경사항들과 DB의 스키마가 동기화를 이룸
    - **모델과 DB의 동기화**
- `python [manage.py](http://manage.py) migrate`

### 추가 필드 정의

**Model 변경사항 반영하기**

```python
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)
```

- Django 입장에서는 이미 존재하는 테이블에 새로운 컬럼이 추가되는 요구사항을 받았는데, 이 컬럼들은 기본적으로 빈 값으로 추가될 수 없음
- 기본 값 설정해야 하니 어떻게 어떤 값을 설정할 것인지를 물어보는 과정을 진행
- `DateTimeField()`
    - python의 `datetime.datetime` 인스턴스로 표시되는 날짜 및 시간을 값으로 사용하는 필드
    - DateField를 상속받는 클래스
    - 선택인자
        1. `auto_now_add`
            1. 최초 생성 일자(Useful for creation of timestamps)
            2. Django ORM이 최초 insert(테이블에 데이터 입력)시에만 현재 날짜와 시간으로 갱신(테이블에 어떤 값을 최초로 넣을 때)
        2. `auto_now`
            1. 최종 수정일자(Useful for **last-modified** timestamps)
            2. Django ORM이 save를 할 때마다 현재 날짜와 시간으로 갱신
- 반드시 기억해야 할 migration 3단계
1. `models.py`에서 변경사항이 발생하면
2. `migrations`파일 생성 (설계도 생성)
    1. `makemigrations`
3. DB 반영 ( 모델과 DB의 동기화)
    1. `migrate`

**그런데 설계도는 어떻게 , 누가 해석할까**

- makemigrations로 인해 만들어진 설계도는 파이썬으로 작성되어있음
- 그런데 SQL만 알아들을 수 있다는 DB가 어떻게 이 설계도를 이해하고 동기화를 이룰 수 있을까?
- `ORM` : 바로 이 과정에서 중간에 번역을 담당

### ORM

- `Object-Relational-Mapping`
- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에(Django ↔ DB) 데이터를 변환하는 프로그래밍 기술
- 객체 지향 프로그래밍에서 데이터베이스를 연동할 때, 데이터베이스와 객체 지향 프로그래밍 언어 간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법
- Django는 내장 Django ORM을 사용
- **SQL을 사용하지 않고 데이터베이스를 조작할 수 있게 만들어주는 매개체**

**ORM 장단점**

- 장점
    - SQL을 잘 알지 못해도 객체지향 언어로 DB조작이 가능
    - 객체 지향적 접근으로 인한 높은 **생산성**
    - DB를 객체(object)로 조작하기 위해 ORM을 사용
- 단점
    - ORM 만으로 완전한 서비스를 구현하기 어려운 경우가 있음

## QuerySet API

---

### 사전 준비

**외부 라이브러리 설치 및 설정**

- `pip install ipython django-extensions`
- `settings.py`에 추가
- 패키지 목록 업데이트
    - `pip freeze > requirements.txt`

**Django shell**

- ORM관련 구문 연습을 위해 파이썬 Django쉘을 사용
- `python [manage.py](http://manage.py) shell_plus`

### QuerySet API

**Database API**

- Django가 기본적으로 ORM을 제공함에 따른 것으로 DB를 편하게 조작할 수 있도록 도움
- Model을 만들면 Django는 객체들을 만들고 읽고 수정하고 지울 수 있는 DB API를 자동으로 만듦

<aside>
💡 Article.objects.all()
`Model class`. `Manager` . `Queryset API`

</aside>

**objects manager**

- Django 모델이 데이터베이스 쿼리 작업을 가능하게 하는 인터페이스
- Django는 기본적으로 모든 Django 모델 클래스에 대해 Objects라는 Manager 객체를 자동으로 추가함
- 이 Manager(objects)를 통해 특정 데이터를 조작(메서드)할 수 있음
- **DB를 Python class로 조작할 수 있도록 여러 메서드를 제공하는 manager**

**Query**

- 데이터베이스에 특정한 데이터를 보여 달라는 요청
    - 쿼리문을 작성한다 ⇒ 원하는 데이터를 얻기 위해 데이터베이스에 요청을 보낼 코드를 작성한다
- 이 때, 파이썬으로 작성한 코드가 ORM에 의해 SQL로 변환되어 데이터베이스에 전달되며, 데이터베이스의 응답 데이터를 ORM이 **QuerySet**라는 자료 형태로 변환하여 우리에게 전달

**QuerySet**

- 데이터베이스에게서 전달받은 객체목록(데이터 모음)
    - 순회가 가능한 데이터로써 1개 이상의 데이터를 불러와 사용할 수 있음
- Django ORM을 통해 만들어진 자료형이며, 필터를 걸거나 정렬 등을 수행할 수 있음
- “objects” manager를 사용하여 복수의 데이터를 가져오는 queryset method를 사용할 때 반환되는 객체
- 단, 데이터베이스가 단일한 객체를 반환할 때는 QuerySet이 아닌 모델(Class)의 인스턴스로 반환됨

<aside>
💡 QuerySet API : QuerySet과 상호작용하기 위해 사용하는 도구(메서드, 연산자 등)

</aside>

## QuerySet API 익히기

---

### CRUD

- Create / Read / Update / Delete
    - 생성 / 조회 / 수정 / 삭제
- 대부분의 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리 기능 4가지를 묶어서 일컫는 말

### CREATE

- 데이터 객체를 만드는(생성하는) 3가지 방법
1. 첫번째 방법 
    1. `article = Article()` : 클래스를 통한 인스턴스 생성
    2. `article.title` : 클래스 변수명과 같은 이름의 인스턴스 변수를 생성 후 값 할당
    3. `article.save()` : 인스턴스로 save 메서드 호출
    - DB 테이블의 컬럼 이름이 id임에도 pk를 사용할 수 있는 이유는 Django가 제공하는 shortcut이기 때문
2. 두번째 방법
    - 인스턴스 생성 시 초기 값을 함께 작성하여 생성
    1. `article = Article(title='second', content='django!')`
    2. `article.save`
3. 세번째 방법
    - QuerySet API 중 create() 메서드 활용
    1. `Article.objects.create(title='third', content='django!')`
- `.save()`
    - **saving object**
    - 객체를 데이터베이스에 저장함
    - 데이터 생성 시 save를 호출하기 전에는 객체의 id 값은 None
        - id 값은 Django가 아니라 데이터베이스에서 계산되기 때문
    - 단순히 모델 클래스를 통해 인스턴스를 생성하는 것은 DB에 영향을 미치지 않기 때문에 반드시 save를 호출해야 테이블에 레코드가 생성됨

### READ

- QuerySet API method를 사용해 데이터를 다양하게 조회하기
- QuerySet API method는 크게 2가지로 분류됨
    1. Methods that **return new querysets**
    2. Methods that **do not return querysets**

**all()**

- QuerySet return
- 전체 데이터 조회
- `Article.objects.all()`

**get()**

- 단일 데이터 조회
- 객체를 찾을 수 없으면 DoesNotExist 예외를 발생시키고, 둘 이상의 객체를 찾으면 MultipleObjectsReturned 예외를 발생시킴
- 위와 같은 특징을 가지고 있기 때문에 `primary key`와 같이 **고유성을 보장하는 조회에서 사용해야 함**
- `Article.objects.get(id=1)`
- `Article.objectsget(pk=1)`
- `Aricle.objects.get(pk=100)` → 없는 값 : DoesNotExist

**filter()**

- 지정된 조회 매개 변수와 일치하는 객체를 포함하는 새 QuerySet을 반환
- `Article.objects.filter(content='django!')`
- `Article.object.filter(title='ssafy')`→ 조회된 객체 없음 : 빈 QuerySet 반환 : `<QuerySet []>`
- `Article.object.filter(title='first')` → 조회된 객체 1개여도 QuerySet 반환
- pk로 조회시 `Article.object.filter(pk=1)`→ `<QuerySet [<Article object (1)>]>`과 같이 한 겹 씌여있는 QuerySet 반환
    - 없을 때는 빈 QuerySet 반환

**Field lookups**

- 특정 레코드에 대한 조건을 설정하는 방법
- QuerySet 메서드 filter(), exclude() 및 get()에 대한 키워드 인자로 지정됨
- `Article.objects.filter(content__contains='ja')`

### UPDATE

**update 과정**

1. `article = Article.objects.get(pk=1)` : 수정하고자 하는 article 인스턴스 객체를 조회 후 반환 값을 저장
2. `article.title = 'byebye'` : article 인스턴스 객체의 인스턴스 변수 값을 새로운 값으로 할당
3. `article.save()` : save() 인스턴스 메서드 호출

### DELETE

**Delete 과정**

1. `article = Article.objects.get(pk=1)` : 삭제하고자 하는 article 인스턴스 객체를 조회 후 반환 값을 저장
2. `article.delete()` : delete() 인스턴스 메서드 호출

**[참고] str()**

- 표준 파이썬 클래스의 메서드인 **str()**을 정의하여 각각의 object가 사람이 읽을 수 있는 문자열을 반환(return)하도록 할 수 있음