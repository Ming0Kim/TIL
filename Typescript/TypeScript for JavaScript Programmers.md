JavaScript는 이미 `string`, `number`, `object`, `undefined` 같은 원시 타입을 가지고 있음
하지만 전체 코드베이스에 일관되게 할당되었는지는 확인불가

##### TypeScript는 이 레이어로서 동작

### 타입 추론 (types by Inference)

- 변수를 생성하면서 동시에 특정 값에 할당하는 경우, 그 갑승 ㄹ해당 변수의 타입으로 사용

```TypeScript
let helloWorld = "Hello World";
```

- JavaScript가 동작하는 방식을 이해함

- 타입을 명시하기 위해 추가로 문자로 사용할 필요가 없는 타입 시스템 제공

### 타입 정의하기 (Defining Types)

- TypeScript는 타입이 무엇이 되어야 하는지 명시 가능한 JavaScript 언어의 확장을 지원

- `name: string` 과 `id: number`를 포함하는 추론 타입을 가진 객체를 생성

```TypeScript
const user = {
  name: "Hayes",
  id: 0,
};
```

- `interface`로 선언 : 이 객체의 형태를 명시적으로 나타내기 위해서

```TypeScript
interface User {
  name: string;
  id: number;
}
```

- 변수 선언 뒤에 `: TypeName`의 그문을 사용해 JavaScript 객체가 새로운 `interface`의 형태를 따르고 있음을 선언

```TypeScript
interface User {
  name: string;
  id: number;
}

const user: User = {
  name: "Hayes",
  id: 0,
}
```

- 해당 인터페이스에 맞지 않는 객체를 생성 : TypeScript는 경고를 줌

```TypeScript
// @errors: 2322
interface User {
  name: string;
  id: number;
}

const user: User = {
  username: "Hayes",
  id: 0,
}
```

- JavaScript는 클래스와 객체 지향 프로그래밍을 지원하기 때문에, TypeScript 또한 동일

- 인터페이스는 클래스로도 선언할 수 있음

```TypeScript
interface User {
  name: string;
  id: number;
}

class UserAccount {
  name: string;
  id: number;

  constructor(name: string, id: number) {
    this.name = name;
    this.id = id;
  }
}

const user: User = new UserAccount("Murphy", 1);
```

- 인터페이스는 함수에서 매개변수와 리턴 값을 명시하는데도 사용

```TypeScript
// @noErrors
interface User {
  name: string;
  id: number;
}

function getAdminUser(): User {
  // ...
}

function deleteUser(user: User) {
  // ...
}
```

- JavaScript에서 사용할 수 있는 적은 종류의 원시 타입이 이미 있음

- 인터페이스에서 사용 가능 : `boolean`, `bigint`, `null`, `number`, `string`, `symbol`, `object` `undefined`

- TypeScript는 몇 가지 추가해 목록을 확장할 수 있음

- `any` : 무엇이든 허용, `unknown` : 이 타입을 사용하는 사람이 타입이 무엇인지 선언했는가를 확인, `never` : 이 타입은 발생될 수 없음, `void` : `undefined`를 리턴하거나 리턴 값이 없는 함수

### 타입 구성 (Composing Types)

- 객체들을 조합하여 더 크고 복잡한 객체를 만드는 방법과 유사하게 타입으로 이를 수행하는 도구가 있음

#### 유니언 (Unions)

- 유니언은 타입이 여러 타입 중 하나일 수 있음을 선언하는 방법

- `boolean` 타입을 `true` 또는 `false`로 설명할 수 있음

```TypeScript
type MyBool = true | false;
```

- ex) 값이 다음과 같이 허용되는 `string` 또는 `number`의 리터럴 집합을 설명하는 것

```TypeScript
type WindowStates = "open" | "closed" | "minimized";
type LockStates = "locked" | "unlocked";
type OddNumbersUnderTen = 1 | 3 | 5 | 7 | 9;
```

- ex) 다양한 타입을 처리하는 방법 제공 : `array` 또는 `string`을 받는 함수가 있을 수 있음

```TypeScript
function getLength(obj: string | string[]) {
  return obj.length
}
```

- TypeScript는 코드가 시간에 따라 변수가 변경되는 방식을 이해, 이러한 검사를 사용해 타입을 골라낼 수 있음
  |Type|Predicate|
  |---|---|
  |string|typeof === "string"|
  |number|typeof n === "number"|
  |boolean|typeof b === "boolean"|
  |undefined|typeof undefined === "undefined"|
  |function|typeof f === "function"|
  |array|Array.isArray(a)|

- ex) `typeof obj === "string"`을 이용하여 `string`고 `array`를 구분할 수 있으며, TypeScript는 객체가 다른 코드 경로에 있음을 알게됨

```TypeScript
function wrapInArray(obj: string | stringp[]) {
  if (typeof obj === "string") {
    return [obj];
    // ^?
  } else {
    return obj
  }
}
```

#### 제네릭 (Generics)

- 제네릭은 타입에 변수를 제공하는 방법

- 배열이 일반적인 예시, 제네릭이 없는 배열은 어떤 것이든 포함할 수 있음

- 제네릭이 있는 배열은 배열 안의 값을 설명할 수 있음

```TypeScript
type StringArray = Array<string>;
type NumberArray = Array<number>;
type ObjectWithNameArray = Array<{ name: string }>;
```

##### 출처 : Typescript 공식문서
