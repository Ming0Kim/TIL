- JavaScript는 오직 **동적** 타입만을 제공, 코드를 실행해야만 어떤 일이 벌어지는지 비로소 확인할 수 있다

- 따라서 **정적** 타입 시스템을 사용하여 코드가 실행되기 **전에** 코드에 대하여 예측하기

### 정적 타입 검사

- TypeScript는 우리가 작성한 프로그램에서 사용된 값들의 형태와 동작을 설명

- 코드가 실행되기 전에 오류 메시지 확인

### 예외가 아닌 실행 실패

```TypeScript
const user = {
  name: "Daniel",
  age: 26,
};

user.location
// Javascript : undefined를 반환
// TypeScript : Property 'location' does not exist on type '{ name: string; age: number; }'.
```

- TypeScript는 겉으로 드러나지 않는 버그를 꽤 많이 잡아냄 : 오타, 호출되지 않은 함수, 기본적인 논리 오류

### 프로그래밍 도구로서의 타입

- TypeScript는 코드 상 실수를 저질렀을 때 버그를 잡아줄 뿐만 아니라 더 나아가 우리가 실수를 저지르는 바로 그 순간 이를 막아줌

- 프로퍼티를 제안해줌

### `tsc`, TypeScript 컴파일러

- 타임 검사기

```bash
tsc hello.ts
```

- `hello.ts`로 `hello.js` 뱉어내기

```TypeScript
function greet(person, date) {
  console.log(`Hello ${person}, today is ${date}!`);
}

greet("Brendan");
```

```Bash
$ tsc hello.ts
hello.ts:7:1 - error TS2554: Expected 2 arguments, but got 1.

7 greet("Brendan");


hello.ts:3:24
  3 function greet(person, date) {
                           ~~~~
  An argument for 'date' was not provided.


Found 1 error in hello.ts:7

```
