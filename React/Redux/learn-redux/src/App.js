import React from 'react';
import CounterContainer from './containers/CounterContainer';
import TodosContainer from './containers/TodosContainer';
import './App.css';

function App() {
	return (
		<div>
			<CounterContainer />
			<hr />
			<TodosContainer />
		</div>
	);
}

export default App;
