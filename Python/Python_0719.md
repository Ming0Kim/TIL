### 프로그래밍

- 프로그래밍 용어 정리
    - **프로그래밍** : 컴퓨터에게 일을 시키기 위해서 프로그램을 만드는 행위
    - **프로그램** : 컴퓨터가 해야 할 일들의 모음
    - **프로그래머** : 프로그램을 만드는 사람(소프트웨어 개발자)
- 기계어 ⇒ `프로그래밍 언어`
    - 자신의 **생각을 나타내고 전달**하기 위해 사용하는 체계
    - 문법적으로 맞고, 언어 공동체 내에서 **이해될 수 있는** 말의 집합
    - 사람이 이해할 수 있는 문자
    - 기본적인 규칙과 문법이 존재
    - 소스 코드 : 프로그래밍 언어로 작성된 프로그램
    - 번역기 : 인터프리터

---

### **파이썬과 파이썬 개발환경**

- 인터프리터 언어
    - 파이썬은 소스코드를 기계어로 변환할 때 통역하듯이 1줄씩 변환
- **객체 지향 프로그래밍**
    - 현대 프로그래밍의 기본적인 설계 방법론

<aside>
💡 **주석을 다는 습관 매우 중요!!**

</aside>

- ‘’’으로 묶어서 표현!

**변수**

- 데이터를 저장하기 이해서 사용
- 추상화 : 변수를 사용하면 복잡한 값들을 쉽게 사용할 수 있음
- 동일 변수에 다른 데이터를 언제든 할당 가능
    - 같은 값을 동시에 할당 가능
    - 다른 값을 동시에 할당 가능

---

## 리스트

```python
# 변수 boxes에 문자열 'A', 'B', 리스트 ['apple', 'banana', 'cherry']를 할당합니다.
boxes = ['A','B',['apple','banana','cherry']]
# boxes의 길이를 len 함수를 이용하여 출력해 봅시다.
boxes
len(boxes)
3
# boxes의 3번째 요소를 인덱스로 접근하여 출력해 봅시다.
boxes[2]
['apple', 'banana', 'cherry']
# boxes의 3번째 요소들 중, 마지막 요소를 negative index로 접근하여 출력해 봅시다.
boxes[-1]
['apple', 'banana', 'cherry']
# boxes의 마지막 요소들 중, 두번째 요소의 첫번째 문자열을 출력해 봅시다.
boxes[2][-1][0]
'c'
```

## 튜플

```python
4.1.4  튜플 (Tuple)
생성과 접근

(value1, value2)
튜플은 리스트와 유사하지만, ()로 묶어서 표현합니다.

tuple은 수정 불가능(불변, immutable)합니다.

직접 사용하기 보다는 파이썬 내부에서 다양한 용도로 활용되고 있습니다.

# tuple을 만들어봅시다.
# 변수명이 my_tuple인 tuple을 만들어 봅시다. 단, 무작위 정수 2개를 포함하여 만듭니다.
# my_tuple의 타입을 출력해 봅시다.
my_tuple = (1, 2)
print(type(my_tuple))
<class 'tuple'>
# 아래와 같은 방식으로도 만들 수 있습니다.
another_tuple = 1, 2
print(another_tuple)
print(type(another_tuple))
(1, 2)
<class 'tuple'>
튜플 생성 주의 사항

단일 항목의 경우
# 하나의 항목으로 구성된 튜플은 생성 시 값 뒤에 쉼표를 붙여야 합니다.
# 아래 코드를 실행하여 변수 a의 타입을 확인해 봅시다.
a = 1,
print(a)
print(type(a))
(1,)
<class 'tuple'>
# 변수명이 single_tuple인 하나의 요소(값)로 구성된 tuple을 만들어 봅시다. (길이가 1)
# 하나의 요소(값)로 구성된 tuple은 값 뒤에 쉼표를 붙여서 만듭니다.
# single_tuple의 타입을 출력해 봅시다.
# single_tuple의 길이를 출력해 봅시다.
single_tuple = ('hello',)
print(type(single_tuple))
print(len(single_tuple))
<class 'tuple'>
1
# 길이가 1인 tuple을 만들 때 쉼표가 없는 경우 어떻게 되는지 확인 해봅시다.
tuple_or_not = ('hello')
print(type(tuple_or_not))
<class 'str'>
복수 항목의 경우
# 마지막 항목에 붙은 쉼표는 생략 할 수 있습니다.
# 아래 코드를 실행하여 변수 b와 c의 타입을 확인해 봅시다.
b = 1, 2, 3
print(b)
print(type(b))
(1, 2, 3)
<class 'tuple'>
c = 4, 5, 6,
print(c)
print(type(c))
(4, 5, 6)
<class 'tuple'>
튜플 대입

우변의 값을 좌변의 변수에 한번에 할당하는 과정을 의미합니다.
튜플은 일반적으로 파이썬 내부에서 활용됩니다.
추후 함수 파트에서 복수의 값을 반환하는 경우에도 확인할 수 있습니다.
# 파이썬 내부에서는 다음과 같이 활용됩니다. (변수 및 자료형 예제에서 사용된 코드입니다.)
x, y = 1, 2
print(x)
print(y)
1
2
# 실제로는 tuple로 처리됩니다.
x, y = (1, 2)
print(x)
print(y)
1
2
# 변수의 값을 swap하는 코드 역시 tuple을 활용하고 있습니다. 
x, y = y, x
print(x)
print(y)
2
1
# 변수명이 empty인 빈 tuple을 만들어 봅시다.
# 빈 tuple은 빈 괄호 쌍으로 만들어집니다.
# empty의 타입을 출력해 봅시다.
# empty의 길이를 출력해 봅시다.
empty = ()
print(type(empty))
print(len(empty))
<class 'tuple'>
0
```

## 레인지

```python
4.1.5  레인지 (range())
range 는 정수의 시퀀스를 나타내기 위해 사용됩니다.

기본형 : range(n)

0부터 n-1까지 값을 가짐

범위 지정 : range(n, m)

n부터 m-1까지 값을 가짐

범위 및 스텝 지정 : range(n, m, s)

n부터 m-1까지 +s만큼 증가한다

# range를 만들어봅시다.
# 0부터 2까지 값을 가지는 range를 만들고 타입을 출력해 봅시다.
range(2)
range(0, 2)
# 0부터 9까지 값을 가지는 range를 만들고 list로 형 변환을 해 봅시다.
# 작성한 range를 list()로 감싸 형 변환 할 수 있습니다.
10
range(10)
list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 4부터 8까지의 숫자를 담은 range를 만들고 list로 형 변환을 해 봅시다.
range(4, 8)
list(range(4,8))
[4, 5, 6, 7]
# range(start, end, [step, ])을 활용합니다.
# 0부터 -9까지 담긴 range를 만들고 list로 형 변환을 해 봅시다.
# 출력 결과는 다음과 같습니다.
# [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
list
range(0,-10,-1)
list(range(0,-10,-1))
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
```

## 딕셔너리

```python
4.1.6  딕셔너리 (dictionary)
dictionary는 key와 value가 쌍으로 이뤄져있습니다.

생성과 접근

{Key1:Value1, Key2:Value2, Key3:Value3, ...}
{}를 통해 만들며, dict()로 만들 수 있습니다.
순서를 보장하지 않습니다.
key는 변경 불가능(immutable)한 데이터만 가능합니다. (immutable : string, integer, float, boolean, tuple, range)
value는 list, dictionary를 포함한 모든 것이 가능합니다.
# 비어있는 dictionary를 두가지 방법으로 만들어봅시다.
# {}와 dict()로 만들 수 있습니다.
# 두 변수의 타입을 출력해 봅시다.
type({})
type(dict())
dict
# dictionary에 중복된 key는 존재할 수 없습니다.
dict_a = {1: 1, 2: 2, 3: 3, 1: 4}
print(dict_a)
{1: 4, 2: 2, 3: 3}
# 지역번호가 담긴 전화번호부를 만들어봅시다.
# 변수 phone_book에 key를 지역명, value를 지역번호로 가지는 원소를 작성합니다.
# 예) 서울 - 02
phone_book = {'서울': '02', '강원도': '033', '경기도': '031'}
# 위에서 작성한 phone_book이 가지고 있는 key 목록을 확인 해 봅시다.
# dictionary의 .keys() 메소드를 활용하여 key를 확인 해볼 수 있습니다.
phone_book.keys()
dict_keys(['서울', '강원도', '경기도'])
# 위에서 작성한 phone_book이 가지고 있는 value 목록을 확인 해 봅시다.
# 딕셔너리의 .values() 메소드를 활용하여 value를 확인 해볼 수 있습니다.
phone_book
phone_book.values()
dict_values(['02', '033', '031'])
# 위에서 작성한 phone_book이 가지고 있는 key와 value 목록을 확인 해 봅시다.
# 딕셔너리의 .items() 메소드를 활용하여 key, value를 확인 해볼 수 있습니다.
phone_book.items()
dict_items([('서울', '02'), ('강원도', '033'), ('경기도', '031')])
```

## 암시적 형변환 : 자동

```python
1.1  암시적 형변환(Implicit Typecasting)
사용자가 의도하지 않았지만, 파이썬 내부적으로 자동으로 형변환 하는 경우입니다. 아래의 상황에서만 가능합니다.

bool
Numeric Type (int, float, complex)
# boolean과 integer는 더할 수 있을까요?
# True와 임의의 정수를 더해봅시다.
rue + 1
True + 1
2
# int, float, complex를 각각 변수에 대입해봅시다.
# 변수 int_number 에 정수를 할당해봅시다.
# 변수 float_numbe 에 실수를 할당해봅시다.
*
x = 3
y = 3.5
z = (-3)**0.5
int_number = 1
float_number = 2.5
# int와 float를 더해봅시다. 그리고 값을 출력해봅시다.
# 그 결과의 type은 무엇일까요?
y
x+y
type(x+y)
float
# int와 complex를 더해봅시다. 그리고 값을 출력해봅시다.
# 그 결과의 type은 무엇일까요?
z
x + z
type(x+z)
complex
```

## 명시적 형변환

```python
1.2  명시적 형변환(Explicit Typecasting)
위의 상황을 제외하고는 모두 명시적으로 형변환을 해주어야합니다.

string -> intger : 형식에 맞는 숫자만 가능
integer -> string : 모두 가능
암시적 형변환이 되는 모든 경우도 명시적으로 형변환이 가능합니다.

int() : string, float를 int로 변환
float() : string, int를 float로 변환
str() : int, float, list, tuple, dictionary를 문자열로 변환
# integer와 string 사이의 관계는 명시적으로 형변환을 해줘야만 합니다.
# 정수와 문자열을 더해보고 오류를 확인해봅시다.
1 + 'abc'
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Input In [16], in <cell line: 1>()
----> 1 1 + 'abc'

TypeError: unsupported operand type(s) for +: 'int' and 'str'

# 정수를 문자열로 형변환하고 문자열과 더해봅시다.
abd
str(1) + 'abd'
'1abd'
# 변수 a에 string 3을 할당하고 integer로 변환해봅시다.
)
a = str(3)
type(int(a))
int
# 변수 a에 string 3.5를 할당하고 float로 변환해봅시다.
a = str(3.5)
float(a)
3.5
# string은 글자가 숫자일때만 형변환이 가능합니다.
# 변수 a에 문자열 'hi'를 할당하고 integer로 변환해봅시다.
a
a = 'hi'
int(a)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Input In [25], in <cell line: 2>()
      1 a = 'hi'
----> 2 int(a)

ValueError: invalid literal for int() with base 10: 'hi'

# string 3.5를 int로 변환할 수는 없습니다.
# 변수 a에 string 3.5를 저장하고 integer로 변환하고 오류를 확인해봅시다.
a
a = str(3.5)
int(a)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Input In [27], in <cell line: 2>()
      1 a = str(3.5)
----> 2 int(a)

ValueError: invalid literal for int() with base 10: '3.5'

# float 3.5는 int로 변환이 가능합니다.
# 변수 a에 실수 3.5를 저장하고 integer로 변환해봅시다.
a = float(3.5)
int(a)
3
```

## 컨테이너형 형변환

파이썬에서 컨테이너는 서로 변환할 수 있습니다.

![https://user-images.githubusercontent.com/18046097/61180466-a6a67780-a651-11e9-8c0a-adb9e1ee04de.png](https://user-images.githubusercontent.com/18046097/61180466-a6a67780-a651-11e9-8c0a-adb9e1ee04de.png)