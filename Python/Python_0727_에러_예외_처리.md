# 에러/예외 처리

## ✅디버깅

### 버그란?

- 최초의 버그는 1945년 프로그래밍 언어의 일종인 코볼 발명자 그레이스 호퍼가 발견
- 역사상 최초의 컴퓨터 버그는 Mark ll라는 컴퓨터 회로에 벌레인 나방이 들어가 합선을 일으켜 비정상적으로 동작
- 이때부터 소프트웨어에서 발생하는 문제를 버그라고 부름

### 디버깅의 정의

- 잘못된 프로그램을 수정하는 것을 디버깅이라함 de(없앤다) + bugging(버그)
- 에러 메시지가 발생하는 경우
    - 해당하는 위치를 찾아 메시지를 해결
- 로직 에러가 발생하는 경우
    - 명시적인 에러 메시지 없이 예상과 다른 결과가 나온 경우
        - 정상적으로 동작하였던 코드 이후 작성된 코드를 생각해봄
        - 전체 코드를 살펴봄
        - 휴식을 가져봄
        - 누군가에게 설명해봄

<aside>
💡 **제어가 되는 시점
조건/반복, 함수**

</aside>

### 디버깅

- print 함수 활용
    - 특정 함수 결과, 반복/조건 결과 등 나눠서 생각, 코드를 bisection으로 나눠서 생각
- 개발 환경(text editor, IDE) 등에서 제공하는 기능 활용
    - breakpoint, 변수 조회 등
- Python tutor 활용(단순 파이썬 코드인 경우)
- 뇌컴파일, 눈디버깅

## ✅에러와 예외

### 문법 에러(Syntax Error)

- SyntaxError가 발생하면, 파이썬 프로그램은 실행이 되지 않음
- 파일이름, 줄번호, ^문자를 통해 파이썬이 코드를 읽어나갈때(parser) 문제가 발생한 위치를 표현
- 줄에서 에러가 감지된 가장 앞의 위치를 가리키는 캐럿(caret)기호(^)를 표시
- Invalid syntax : 문법 오류

```python
while # SyntaxError : invalid syntax
```

- assign to literal : 잘못된 할당

```python
5 = 3 # SyntaxError: cannot assign to literal
```

- EOL(end of line)

```python
print('hello
# SyntaxError: EOL while scanning string literal
```

- EOF(end of file)

```python
print(
#SyntaxError : unexpected EOF while parsing
```

### 예외(Exception)

- 실행 도중 예상치 못한 상황을 맞이하면, 프로그램 실행을 멈춤
    - 문장이나 표현식이 문법적으로 올바르더라도 발생하는 에러
- 실행 중에 감지되는 에러들을 예외(Exception)라고 부름
- 예외는 여러 타입(type)으로 나타나고, 타입이 메시지의 일부로 출력됨
    - NameError, TypeError 등은 발생한 예외 타입의 종류(이름)
- 모든 내장 예외는 Exception Class를 상속받아 이뤄짐
- 사용자 정의 예외를 만들어 관리할 수 있음
- ZeroDivisionError : 0으로 나누고자 할 때 발생

```python
10/0 # ZeroDivisionError : division by zero
```

- NameError : namespace 상에 이름이 없는 경우

```python
print(name_error)
#NameError: name 'name_error' is not defined
```

- TypeError : 타입 불일치

```python
1 + '1'
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
round('3.5
# TypeError: type str doesn't define __rond__ method
```

- TypeError - argument 누락

```python
divmod()
# TypeError: divmod expected 2 arguments, got 0
import random
random.sample()
# TypeError: sample() missing 2 required positional arguments: 'population' and 'k'
```

- TypeError : argument 개수 초과

```python
divmod(1, 2, 3) 
# TypeError: divmod expected 2 arguments, got 3
import random
random.sample(range(3), 1, 2)
# TypeError: sample() takes 3 positional arguments but 4 were given
```

- TypeError : argument type 불일치

```python
import random
random.sample(1, 2)
# TypeError: Population must be a sequence. For dicts or sets, use sorted(d).
```

- ValueError : 타입은 올바르나 값이 적절하지 않거나 없는 경우

```python
int('3.5')
# ValueError: invalid literal for int() with base 10: '3.5'
range(3).index(6)
# ValueError: 6 is not in range
```

- IndexError : 인덱스가 존재하지 않거나 범위를 벗어나느 경우

```python
empty_list = []
empty_list[2]
# IndexError: list index out of range
```

- KeyError : 해당 키가 존재하지 않는 경우

```python
song = {'IU' : '좋은날'}
song['BTS'] # KeyError: 'BTS'
```

- ImportError : Module은 있으나 존재하지 않는 클래스/함수를 가져오는 경우

- KeyboardInterrupt : 임의로 프로그램을 종료하였을 때


- IndentationError : Indentation이 적절하지 않는 경우


### 파이썬 내장 예외(built-in-exceptions)


## ✅예외 처리

- try 문(statement) / except 절(clause)을 이용하여 예외 처리를 할 수 있음
- try문
    - 오류가 발생할 가능성이 있는 코드를 실행
    - 예외가 발생되지 않으면, except 없이 실행 종료
- except문
    - 예외가 발생하면, except 절이 실행
    - 예외 상황을 처리하는 코드를 받아서 적절한 조치를 취함

