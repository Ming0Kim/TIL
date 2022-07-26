### Try & Except

##### EOF : End of File
:check: 파일 입축력할 때 입력이 끝날 때까지 읽어들이기

##### 예외 처리를 하려면 다음과 같이 try에 실행할 코드를 넣고 except에 예외가 발생했을 때 처리하는 코드를 넣는다.

```
try:
  실행할 코드
except:
  예외가 발생했을 때 처리하는 코드

```

##### 예시
```
try:
  x = int(input('나눌 숫자를 입력하세요: '))
  y = 10 / x
  print(y)
except:  #예외가 발생했을 때 실행됨
  print('예외가 발생했습니다.')
```