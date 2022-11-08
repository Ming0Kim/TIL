# Django3

강의날짜: 2022/09/06
공부유형: 강의
복습: No
분야: django
작성일시: 2022년 9월 6일 오전 10:09
편집일시: 2022년 9월 7일 오후 10:37

# Django Form

---

### 개요

- 지금까지는 HTML form, input 태그를 통해서 데이터를 받았음
- 현재 우리 Django 서버는 들어오는 요청을 모두 수용하고 있는데, 이러한 요청 중에는 비정상적인 혹은 악의적인 요청이 있다는 것을 생각해야 함
- 이처럼 사용자가 입력한 데이터가 우리가 원하는 데이터 형식이 맞는지에 대한 **유효성 검증**이 반드시 필요
    - 유효성 검증은 많은 부가적인 것들을 고려해서 구현해야 하는데, 이는 개발 생산성을 늦추고 쉽지 않은 작업임
- **Django From**은 이 과정에서 과중한 작업과 반복 코드를 줄여줌으로써 훨씬 쉽게 유효성 검증을 진행할 수 있도록 만들어 줌

### **Form에 대항 Django의 역할**

- Form은 Django의 유효성 검사 도구 중 하나
- 외부의 악의적 공격 및 데이터 손상에 대한 중요한 방어 수단
- Django는 Form과 관련한 유효성 검사를 **단순화하고 자동화** 할 수 있는 기능을 제공
- 개발자가 직접 작성하는 코드보다 더 안전하고 빠르게 수행하는 코드를 작성할 수 있다
    - 개발자가 필요한 핵심 부분만 집중할 수 있도록 돕는 프레임워크의 특성

### **Django는 Form에 관련된 작업의 세 부분을 처리**

1. 렌더링을 위한 데이터 준비 및 재구성
2. 데이터에 대한 HTML forms 생성
3. 클라이언트로부터 받은 데이터 수신 및 처리

## The Django Form Class

---

### **개요**

- Form Class
    - Django form 관리 시스템의 핵심

### **Form Class 선언**

- Form Class 선언은 Model Class 선언과 비슷하고 비슷한 이름의 필드 타입을 많이 가지고 있음
    - 다만, 이름이 같을 뿐 같은 필드는 아님
- Model과 마찬가지로 상속을 통해 선언
    - forms 라이브러리의 Form 클래스를 상속받음
- 앱 폴더에 `forms.py`를 생성 후 AritcleForm Class 선언

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled.png)

- form에는 model field와 달리 TextField가 존재하지 않음
- 모델의 TextField처럼 사용하려면 어떻게 작성할 수 있을지는 곧 알아볼 예정
- Form Class를 `forms.py`에 작성하는 것은 규약이 아니다
    - 파일 이름이 달라도 되고 models.py나 다른 어디에도 작성 가능
    - 다만 더 나은 유지보수의 고나점 그리고 관행적으로 `[forms.py](http://forms.py)` 파일 안에 작성하는 것을 권장

✅ 모델 CharField 에서는 `max_length`가 필수, 하지만 Form에서는 아님

✅ 모델 에서는 Textfield 존재하지 않는다

### `new` view 함수 업데이트

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%201.png)

### `new` 템플릿 업데이트

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%202.png)

### 업데이트 후 **출력 확인**

- view 함수에서 정의한 ArticleForm의 인스턴스(form)하나로 input 과 label 태그가 모두 렌더링 됨
- 각 태그의 속성 값들 또한 자동으로 설정되어있음

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%203.png)

### **Form rendering options**

- **as_p()**
    - 각 필드가 단락(<p>태그)로 감싸져서 렌더링

### Django의 2가지 HTML input 요소 표현

1. `Form fields`
    - 입력에 대한 유효성 검사 로직을 처리
    - 템플릿에서 직접 사용됨
    
    ![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%204.png)
    
2. `Widgets`
    - 웹 페이지의 HTML input 요소 렌더링을 담당
        - input 요소의 단순한 출력 부분을 담당
    - Widgets은 반드시 `form fields`에 할당됨
    
    ![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%205.png)
    

## Widgets

---

### 개요

- Django의 HTML input element의 표현을 담당
- **단순히 HTML 렌더링을 처리하는 것**이며 유효성 검증과 아무런 관계가 없음
    - **웹 페이지에서 input element의 단순 raw한 렌더링만을 처리하는 것일 뿐**

### Textarea 위젯 적용하기

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%206.png)

- 출력 결과 확인하기
- 다양한 built-in 위젯

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%207.png)

### Form fields와 widget 응용하기

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%208.png)

- 출력 결과를 확인하고 앞으로 어떻게 조합해서 사용할 수 있는지는 form field와 widgets 공식문서를 찾아보며 사용하도록 함

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%209.png)

## DJango ModelForm

---

### 개요

- Form Class를 작성하다보니 Model과 너무 중복되는 부분이 많음
- 이미 Article Model Class에 필드에 대한 정보를 작성했는데
- 이를 Form에 맵핑하기 위해 Form Class에 필드를 재정의 해야만 했음
- ModelForm을 사용하면 이러한 Form을 더 쉽게 작성할 수 있음

### ModelForm Class

- Model을 통해 Form Class를 만들 수 있는 `helper class`
- ModelForm은 Form과 똑같은 방식으로 View 함수에서 사용

### ModelForm 선언

- forms 라이브러리에서 파생된 ModelForm 클래스를 상속받음
- 정의한 ModelForm 클래스 안에 Meta 클래스를 선언
- 어떤 모델을 기반으로 form을 작성할 것인지에 대한 정보를 Meta 클래스에 지정

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%2010.png)

### ModelForm에서의 Meta Class

- ModelForm의 정보를 작성하는 곳
- ModelForm을 사용할 경우 참조할 모델이 있어야하는데,
- Meta class의 model 속성이 이를 구성함
    - 참조하는 모델에 정의된 field 정보를 Form에 적용함
    
    ![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%2011.png)
    
- fields 속성에 `'__all__'`를 사용하여 모델의 모든 필드를 포함할 수 있음
- 또는 exclude 속성을 사용하여 모델에서 포함되지 않을 필드를 지정할 수 있음

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%2012.png)

### ✅ Meta data

- **데이터를 표현하기 위한 데이터**
- 예시 - 사진 파일
    - 사진 데이터
    - 사진 데이터의 데이터(촬영 시각, 렌즈, 조리개 값 등)
    - 사진 데이터에 대한 데이터 (==사진의 Meta data)

### ✅ 참조값과 반환 값

- 호출하지 않고 이름만 작성하는 이 방식은 어떤 의미일까

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%2013.png)

- 함수를 예시로 들면 아래와 같은 함수가 있을 때 함수의 이름을 그대로 출력하는 것과 호출 후의 결과를 비교

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%2014.png)

- 첫번째 결과는 함수의 **참조값**을 출력
- 두번째 결과는 함수의 **반환값**을 출력
- 언제 참조값을 사용할까?
    - **함수를 호출하지 않고 함수 자체를 그대로 전달하여, 다른 함수에서 `필요한 시점에` 호출하는 경우**
    
    ![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%2015.png)
    
    - view함수의 참조값을 그대로 넘김으로써, path 함수가 내부적으로 해당 view 함수를 **필요한 시점에** 사용하기 위해서
- 결국 클래스도 마찬가지
- Article이라는 클래스를 **호출하지 않고 (== model을 인스턴스로 만들지 않고)** 작성하는 이유는 ArticleForm이 해당 클래스를 필요한 시점에 사용하기 위함
- 더불어 이 경우에는 인스턴스가 필요한 것이 아닌, 실제 Article 모델의 참조값을 통해 해당 클래스의 필드나 속성 등을 내부적으로 참조하기 위한 이유도 있음

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%2016.png)

### ❗주의사항

- Meta 클래스는 왜 여기에 작성할까?
    - 파이썬의 문법적 개념으로 접근하지 말 것
- 단순히 모델 정보를 Meta라는 이름의 내부 클래스로 작성하도록 ModelForm의 설계가 이렇게 되어있을 뿐 우리는 ModelForm의 역할과 사용법을 숙지해아함
- 우리가 상속하고 있는 부모클래스인 ModelForm이 궁금하다면 공식문서

## ModelForm with view functions

---

### 개요

- ModelForm으로 인한 view 함수의 구조 변화 알아보기

### CREATE

- 유효성 검사를 통과하면
    - 데이터 저장 후
    - 상세 페이지로 리다이렉트
- 통과하지 못하면
    - 작성 페이지로 리다이렉트
    
    ![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%2017.png)
    

### `is_valid()` method

- 유효성 검사를 실행하고, 데이터가 유효한지 여부를 voolean으로 반환
- 데이터 유효성 검사를 보장하기 위한 많은 테스트에 대해 Django는 `is_valid()`를 제공하여 개발자의 편의를 도움

### The `save()` method

- form 인스턴스에 바인딩 된 데이터를 통해 데이터베이스 객체를 만들고 저장
- ModelForm의 하위 클래스는 키워드 인자 `instance` 여부를 통해 생성할지, 수정할지를 결정함
    - 제공되지 않은 경우 `save()`는 지정된 모델의 새 인스턴스를 만듦(CREATE)
    - 제공되면 `save()`는 해당 인스턴스를 수정(UPDATE)
    
    ![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%2018.png)
    

### form 인스턴스의 errors 속성

- `is_valid()`의 반환 값이 False인 경우 form 인스턴스의 errors 속성에 값이 작성되는데, 유효성 검증을 실패한 원인이 딕셔너리 형태로 저장됨

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%2019.png)

- title에 공백을 넣고 제출하기

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%2020.png)

- 이 같은 특징을 통해 다음과 같은 구조로 코드를 작성하면 유효성 검증을 실패했을 때 사용자에게 실제 결과 메세지를 출력할 수 있음

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%2021.png)

### UPDATE

- ModelForm의 인자 instance는 수정대상이 되는 객체(기존 객체)를 지정
1. `request.POST`
    - 사용자가 form을 통해 전송한 데이터(새로운 데이터)
2. `instance`
    - 수정이 되는 대상
- eidt - view 수정

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%2022.png)

- edit - template 수정

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%2023.png)

- update - view 수정

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%2024.png)

### ✅ ModelForm 키워드 인자 data와 instance 살펴보기

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%2025.png)

 `data=`는 생략가능한데 `instance=`는 생략하지 않는 이유

- `data=`는 첫번째 인자인데 `instance=`인자는 저 뒤에 있기 때문

### Form과 ModelForm

- ModelForm이 Form보다 더 좋은 것이 아니라 각자 역할이 다른 것
- Form
    - 사용자의 입력을 필요로 하며 직접 입력 데이터가 DB 저장에 사용되지 않거나 일부 데이터만 사용될 때
        - (예시 - 로그인, 사용자의 데이터를 받아 인증 과정에서만 사용 후 별도로 DB에 저장하지 않음)
- ModelForm
    - 사용자의 입력을 필요로 하며 입력을 받은 것을 그대로 DB 필드에 맞춰 저장할 때
    - 데이터의 유효성 검사가 끝나면 데이터를 각각 어떤 레코드에 맵핑해야 할지 이미 알고 있기 때문에 곧바로 `save()` 호출이 가능

## Widgets 활용하기

### 위젯을 작성하는 2가지 방법

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%2026.png)

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%2027.png)

## Handling HTTP requests

---

### 개요

- **HTTP request 처리에 따른 view 함수 구조 변화**
- new-create, edit-update의 view함수 역할을 잘 살펴보면 하나의 공통점과 하나의 차이점이 있음
- **공통점**
    - new-create는 모두 CREATE 로직을 구현하기 위한 공통목적
    - edit-update는 모두 UPDATE 로직을 구현하기 위한 공통목적
- **차이점**
    - new와 edit는 GET 요청에 대한 처리만을,
    - create와 update 는 POST 요청에 대한 처리만을 진행
- 이 공통점과 차이점을 기반으로, 하나의 view 함수에서 method에 따라 로직이 분리되도록 변경

### Create

- new와 create view 함수를 합침
- 각각의 역할은 `request.method` 값을 기준으로 나뉨

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%2028.png)

- 이제는 불필요해진 new의 view 함수와 url path를 삭제

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%2029.png)

- `new.html` → `create.html` 이름변경 및 action 속성 값 수정

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%2030.png)

- `new.html` → `create.html`이름변경으로 인한 템플릿 경로 수정

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%2031.png)

- index 페이지에 있던 new 관련 링크 수정

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%2032.png)

### context의 들여쓰기 위치

- 이렇게 작성하면 `if form.is_valid():`에서 flase로 평가 받았을 때 이어질 코드가 없음

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%2033.png)

- 반면 다음과 같이 작성하면 `if form.is_valid():`에서 false로 평가받았을때 에러 정보가 담긴 form 인스턴스가 context로 넘어갈 수 있음

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%2034.png)

### Update

- edit과 update view 함수를 합침

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%2035.png)

- new와 마찬가지로 불필요해진 edit의 view 함수와 url path를 삭제

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%2036.png)

- `edit.html` → `update.html` 이름변경으로 인한 관련 정보 수정

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%2037.png)

- `edit.html` → `update.html` 이름변경으로 인한 관련 정보 수정

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%2038.png)

- POST 요청에 대해서만 삭제가 가능하도록 수정

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%2039.png)

✅ **조회만 Get 이용 나머지는 다 POST**

# View decorators

---

### 개요

- View decorators 를 사용해 view 함수를 단단하게 만들기

### 데코레이터(Decorator)

- 기존에 작성된 함수에 기능을 추가하고 싶을 때, 해당 함수를 수정하지 않고 기능을 추가해주는 함수
- Django는 다양한 HTTP기능을 지원하기 위해 view 함수에 적용할 수 있는 여러 데코레이터를 제공
- 데코레이터 동작 예시

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%2040.png)

## Allowed HTTP methods

---

### 개요

- `django.views.decorators.http`의 데코레이터를 사용하여 요청 메서드를 기반으로 접근을 제한할 수 있음
- 일치하지 않는 메서드 요청이라면 405 Method Not allowed를 반환
- 메서드 목록
    1. `require_http_methods()`
    2. `require_POST()`
    3. `require_safe()`

✅ 405 Method Not Allowed

- 요청 방법이 서버에게 전달 되었으나 사용 불가능한 상태

### `require_http_methods()`

- view 함수가 특정한 요청 method만 허용하도록 하는 데코레이터

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%2041.png)

### `require_POST()`

- View 함수가 POST 요청 method만 허용하도록 하는 데코레이터

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%2042.png)

- url로 delete 시도 후 서버 로그에서 405 http status code 확인해보기

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%2043.png)

### `require_safe()`

- `require_GET`이 있지만 Django에서는 `reauire_safe`를 사용하는 것을 권장

![Untitled](Django3%20ef6f718be9014bff9fc2e61bfe6d8f84/Untitled%2044.png)

## 마무리

---

- DJango Form Class
    - Django 프로젝트의 주요 유효성 검사 도구
    - 공격 및 데이터 손상에 대한 중요한 방어 수단
    - 유효성 검사에 대해 개발자에게 강력한 편의를 제공
- View 함수 구조 변화
    - HTTP requests 처리에 따른 구조 변화