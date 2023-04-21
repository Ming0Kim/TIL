### 원시 타입 : `string`, `number`, 그리고 `boolean`

- `string`은 `"Hello, world"`와 같은 문자열 값

- `number`은 `42`같은 숫자, `int` 또는 `float`과 같은 것은 존재하지 않음

- `boolean`은 `true`와 `false`라는 두 가지 값

### 배열

- `[1, 2, 3]`과 같은 배열 타입을 지정할 때, `number[]` 구문 사용

- `stringp[]`은 문자열의 배열 === `Array<number>`

- `[number]`은 전혀 다른 의미(튜플)

### `any`

- 특정 값으로 인하여 타입 검사 오류가 발생하는 것을 원하지 않을 때 사용할 수 있음

- 어떤 값의 타입이 `any`이면, 해당 값에 대하여 임의의 속성에 접근할 수 있고(이때 변환되는 값의 타입도 `any`)

- 함수인 것처럼 호출할 수 있고, 다른 임의 타입의 값에 할당하거나, 받고, 그 밖에도 구문적으로 유효한 것이라면 무엇이든 할 수 있음

```TypeScript
let obj: any = { x: 0 };
// 아래 이어지는 코드들은 모두 오류 없이 정상적으로 실행됩니다.
// `any`를 사용하면 추가적인 타입 검사가 비활성화되며,
// 당신이 TypeScript보다 상황을 더 잘 이해하고 있다고 가정합니다.
obj.foo();
obj();
obj.bar = 100;
obj = "hello";
const n: number = obj;
```

- `any`는 TypeScript를 안심시킬 수 있어서, 긴 타입을 새로 정의하고 싶지 않을 때 유용하게 사용가능

- `nolmplicitAny` : 타입이 지정되지 않으면 TypeScript은 문맥으로부터 그 타입을 추론해내서 컴파일러 `any` 타입을 부여, `nolmplicitAny`를 사용하면 암묵적으로 `any`로 간주하는 모든 경우에 오류를 발생

### 변수에 대한 타입 표기

- `const`, `var`, `let` 등을 사용하여 변수를 선언할 때, 변수의 타입을 명시적으로 지정하기 위하여 타입 표기를 추가할 수 있음

```TypeScript
let myName: string = "Alice";
```

- TypeScript는 자동으로 코드 내의 있는 타입들을 추론하고자 시도

```TypeScript
// 타입 표기가 필요하지 않습니다. 'myName'은 'string' 타입으로 추론됩니다.
let myName = "Alice";
```

### 함수

#### 매개변수 타입 표기

- 함수를 선언할 때, 함수가 허용할 매개변수 타입을 선언하기 위하여 각 매개변수 뒤에 타입을 표기

```TypeScript
// 매개변수 타입 표기
function greet(name: string) {
  console.log("Hello, " + name.toUpperCase() + "!!");
}
```

```TypeScript
// 만약 실행되면 런타임 오류가 발생하게 됩니다!
greet(42);
Argument of type 'number' is not assignable to parameter of type 'string'.
```

#### 변환 타입 표기

- 반환 타입은 매개변수 목록 뒤에 표기

```TypeScript
function getFavoriteNumber() :number {
  return 26;
}
```

- 변수 타입 표기와 마찬가지로, 반환 타입은 표기하지 않아도 되는 것이 일반적

- TypeScript가 해당 함수에 들어있는 `return`문으로 반환 타입을 추론할 것이기 때문

#### 익명 함수

- 함수가 코드상에서 위치한 곳을 보고 해당 함수가 어떻게 호출될지 알아낼 수 있다면, TypeScript는 해당 함수의 매개 변수에 자동으로 타입을 부여

```TypeScript
// 아래 코드에는 타입 표기가 전혀 없지만, TypeScript는 버그를 감지할 수 있습니다.
const names = ["Alice", "Bob", "Eve"];

// 함수에 대한 문맥적 타입 부여
names.forEach(function (s) {
  console.log(s.toUppercase());
Property 'toUppercase' does not exist on type 'string'. Did you mean 'toUpperCase'?
});

// 화살표 함수에도 문맥적 타입 부여는 적용됩니다
names.forEach((s) => {
  console.log(s.toUppercase());
Property 'toUppercase' does not exist on type 'string'. Did you mean 'toUpperCase'?
});
```

- **문맥적 타입 부여** : 매개 변수 `s`에는 타입이 표기되지 않았음에도 불구하고, TypeScript는 `s`의 타입을 알아내기 위하여 추론된 타입과 더불어 `forEach` 함수의 타입을 활용함

### 객체 타입

- 원시 타입을 제외하고 가장 많이 마주치는 타입

- 객체 : 프로퍼티를 가지는 JavaScript 값

- 객체 타입을 정의하려면, 해당 객체의 프로퍼티들과 각 프로퍼티의 타입들을 나열해야함

```TypeScript
// 매개 변수의 타입은 객체로 표기되고 있음
function printCoord(pt: { x: number; y: number}) {
  console.log("The coordinate's x value is " + pt.x);
  console.log("The coordinate's y value is " + pt.y);
}
printCoord({ x: 3, y: 7});
```

- 위에서 매개변수는 `x`와 `y`라는 두 개의 프로퍼티로 이루어진 타입으로 표기, 두 값은 모두 `number`

- 각 프로퍼티를 구분할 때, `,` 또는 `;`를 사용할 수 있고, 가장 마지막 구분자의 표기는 선택 사항

- 타입을 지정하지 않는다면, 해당 프로퍼티는 `any`타입으로 간주

#### 옵셔널 프로퍼티

- 객체 타입은 일부 또는 모든 프로퍼티의 타입을 선택적(옵셔널) 타입으로 지정할 수 있음

- 프로퍼티 이름 뒤에 `?`를 붙이면 됨

```TypeScript
function printName(obj: { first: string; last?: string}) {
  // ...
}
// 둘 다 OK
printName({ first: "Bob" });
printName({ first: "Alice", last: "Alisson" });
```

- JavaScript에서는 존재하지 않는 프로퍼티에 접근하였을 때, 런타임 오류가 발생하지 않고 `undefined` 값을 얻게 됨

- 옵셔널 프로퍼티를 읽었을 때, 해당 값을 사용하기에 앞서 `undefined`인지 여부를 확인해야함

```TypeScript
function printName(obj: { first: string; last?: string }) {
  // 오류 - `obj.last`의 값이 제공되지 않으면 프로그램이 멈춤
  console.log(obj.last.toUpperCase())

  if (obj.last !== undefined) {
    // OK
    console.log(obj.last.toUpperCase());
  }

  console.log(obj.last?.toUpperCase());
}
```

### 유니언 타입

- TypeScript의 타입 시스템에서는 기존의 타입을 기반으로 다양한 연산자를 사용하여 새로운 타입을 만들 수 있음

#### 유니언 타입 정의하기

- **유니언** : 서로 다른 두 개 이상의 타입들을 사용하여 만드는 것

- 타입 조합에 사용된 타입 중 **무엇이든 하나**를 타입으로 가질 수 있음

- **멤버** : 조합에 사용된 각 타입

```TypeScript
function printId(id: number | string) {
  console.log("Your ID is: " + id);
}
// OK
printId(101);
// OK
printId("202");
// 오류
printID({ myID: 22342 });
```

#### 유니언 타입 사용하기

- TypeScript에서 유니언을 다룰 때는 해당 유니언 타입의 **모든** 멤버에 대하여 유효한 작업일 때에만 허용됨

- ex) `string | number`라는 유니언 타입의 경우 `string` 타입에만 유효한 메서드는 사용할 수 없음

```TypeScript
// 오류
function printId(id: number | string) {
  console.log(id.toUpperCase());
}
```

- 이를 해결하기 위해서는 유니언을 **좁혀야**함

```TypeScript
function printId(id: number | string) {
  if (typeof id === "string") {
    // 이 분기에서 id는 'string' 타입을 가짐
    console.log(id.toUppperCase());
  } else {
    // 이 분기에서 id는 'number' 타입을 가짐
    console.log(id);
  }
}
```

- 또 다른 방법 : `Array.isArray`와 같은 함수를 사용

```TypeScript
function welcomePeople(x: string[] | string) {
  if (Array.isArray(x)) {
    // 여기에서 'x'는 'string[]' 타입
    console.log("Hello, " + x.join(" and "));
  } else {
    // 이 분기에서 'x'는 'string'
    console.log("Welcome lone traveler " + x);
  }
}
```

- 유니언의 모든 멤버가 무언가 공통점을 가질 수도 있음 : 배열과 문자열은 둘 다 `slice` 메서드를 내장

```TypeScript
// 반환 타입은 'number[] | string'으로 추론
function getFirstThree(x: number[] | string) {
  return x.slice(0, 3);
}
```

### 타입 별칭

- 지금까지는 직접 해당 타입 표기했지만, 똑같은 타입을 한 번 이상 재사용하거나 또 다른 이름으로 부르고 싶을 때

- **타입**을 위한 이름을 제공

```TypeScript
type Point = {
  x: number;
  y: number;
};

function printCoord(pt: Point) {
  console.log("The coordinate's x value is " + pt.x);
  console.log("The coordinate's y value is " + pt.y);
}

printcoord({ x: 100, y: 100 });
```

- 유니언 타입에 대하여 타입 별칭 부여할 수 있음

```TypeScript
type ID = number | string;
```

- 타입 별칭은 **단지** 별칭에 지나지 않고, 동일 타입에 대하여 각기 구별되는 **여러 버전**을 만드는 것은 아님

```TypeScript
type UserInputSanitizedString = string;

function sanitizeInput(str: string): UserInputSanitizedString {
  return sanitize(str);
}

// 보안 처리를 마친 입력을 생성
let userInput = sanitizeInput(getInput());

// 물론 새로운 문자열을 다시 대입할 수도 있음
userInput = "new input";
```

### 인터페이스

- **인터페이스 선언**은 객체 타입을 만드는 또 다른 방법

```TypeScript
interface Point {
  x: number;
  y: number;
}

function printCoord(pt: Point) {
  console.log("The coordinate's x value is " + pt.x);
  console.log("The coordinate's y value is " + pt.y);
}

printCoord({ x: 100, y: 100 })
```

- 위 코드는 마치 타입이 없는 임의의 익명 객체를 사용하는 것처럼 동작

- **구조적 타입 시스템** : TypeScript는 오직 `printCoord`에 전달된 값의 **구조**에만 관심을 가짐

#### 타입 별칭과 인터페이스의 차이점

- `type`과 `interface`는 매우 유사, `interface`가 가지는 대부분의 기능은 `type`에도 동일하게 사용 가능

- 가장 핵심적인 차이 : `type`은 새 프로퍼티를 추가하도록 개방될 수 없는 반면, `interface`는 항상 확장될 수 있음
