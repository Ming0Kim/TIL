// [1] import useReducer
import React, { useState, useEffect, useReducer } from 'react';

import Card from '../UI/Card/Card';
import classes from './Login.module.css';
import Button from '../UI/Button/Button';

// [3] emailReducer 함수
// 컴포넌트 함수의 범위 밖에서 만들어질 수 있음
// 컴포넌트 함수 내부에서 정의된 그 어떤 것과도 상호 작용할 필요가 없기 때문
// [9]
// [11]
const emailReducer = (state, action) => {
  if (action.type === 'USER_INPUT') {
    return { value: action.val, isValid: action.val.includes('@') };
  }
  if (action.type === 'INPUT_BLUR') {
    return { value: state.value, isValid: state.value.includes('@') };
  }
  return { value: '', isValid: false };
};

const Login = props => {
  // const [enteredEmail, setEnteredEmail] = useState('');
  // const [emailIsValid, setEmailIsValid] = useState();
  const [enteredPassword, setEnteredPassword] = useState('');
  const [passwordIsValid, setPasswordIsValid] = useState();
  const [formIsValid, setFormIsValid] = useState(false);

  // [2] useReducer 호출
  const [emailState, dispatchEmail] = useReducer(emailReducer, {
    value: '',
    isValid: false,
  });

  useEffect(() => {
    console.log('EFFECT RUNNING');

    return () => {
      console.log('EFFECT CLEANUP');
    };
  }, [enteredPassword]);

  // useEffect(() => {
  //   const identifier = setTimeout(() => {
  //     console.log('Checking form validity');
  //     setFormIsValid(
  //       enteredEmail.includes('@') && enteredPassword.trim().length > 6
  //     );
  //   }, 500);

  //   return () => {
  //     console.log('Clean up!');
  //     clearTimeout(identifier);
  //   };
  // }, [enteredEmail, enteredPassword]);

  const emailChangeHandler = event => {
    // [8] dispatchEmail 호출하여 업데이트
    dispatchEmail({ type: 'USER_INPUT', val: event.target.value });

    setFormIsValid(
      event.target.value.includes('@') && enteredPassword.trim().length > 6
    );
  };

  const passwordChangeHandler = event => {
    setEnteredPassword(event.target.value);

    // [4] emailState 코드에서 사용
    setFormIsValid(emailState.isValid && event.target.value.trim().length > 6);
  };

  // [10] dispatchEamil
  // input이 focus를 잃었다만 중요
  // 추가해야하는 데이터 없음
  const validateEmailHandler = () => {
    dispatchEmail({ type: 'INPUT_BLUR' });
  };

  const validatePasswordHandler = () => {
    setPasswordIsValid(enteredPassword.trim().length > 6);
  };

  const submitHandler = event => {
    event.preventDefault();
    // [5] submitHandler에 값 전달
    props.onLogin(emailState.value, enteredPassword);
  };

  return (
    <Card className={classes.login}>
      <form onSubmit={submitHandler}>
        <div
          className={`${classes.control} ${
            // [6] emailState.isValid
            emailState.isValid === false ? classes.invalid : ''
          }`}
        >
          <label htmlFor="email">E-Mail</label>
          <input
            type="email"
            id="email"
            // [7]
            value={emailState.value}
            onChange={emailChangeHandler}
            onBlur={validateEmailHandler}
          />
        </div>
        <div
          className={`${classes.control} ${
            passwordIsValid === false ? classes.invalid : ''
          }`}
        >
          <label htmlFor="password">Password</label>
          <input
            type="password"
            id="password"
            value={enteredPassword}
            onChange={passwordChangeHandler}
            onBlur={validatePasswordHandler}
          />
        </div>
        <div className={classes.actions}>
          <Button type="submit" className={classes.btn} disabled={!formIsValid}>
            Login
          </Button>
        </div>
      </form>
    </Card>
  );
};

export default Login;
