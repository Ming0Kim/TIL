import React, { useState } from 'react';

// 컴포넌트 외적화를 위해서 React.memo를 사용
const TodoItem = React.memo(function TodoItem({ todo, onToggle }) {
	return (
		<li
			style={{ textDecoration: todo.done ? 'line-through' : 'none' }}
			onClick={() => onToggle(todo.id)}
		>
			{todo.text}
		</li>
	);
});

// 컴포넌트 외적화를 위해서 React.memo를 사용
const TodoList = React.memo(function TodoList({ todos, onToggle }) {
	return (
		<ul>
			{todos.map((todo) => (
				<TodoItem key={todo.id} todo={todo} onToggle={onToggle} />
			))}
		</ul>
	);
});

function Todos({ todos, onCreate, onToggle }) {
	// 리덕스를 사용한다고 해서 모든 상태를 리덕스에서 관리해야하는 것은 아님
	const [text, setText] = useState('');
	const onChange = (e) => setText(e.target.value);
	const onSubmit = (e) => {
		e.preventDefault(); // Submit 이벤트 발생 새로고침 방지
		onCreate(text);
		setText(''); // 인풋 초기화
	};

	return (
		<div>
			<form onSubmit={onSubmit}>
				<input
					value={text}
					placeholder='할 일을 입력하세요..'
					onChange={onChange}
				/>
			</form>
		</div>
	);
}
