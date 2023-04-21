import React, { ChangeEvent, useState } from "react";
import { ITask } from "./Interfaces";

const App: React.FC = () => {
  const [task, setTask] = useState<string>("");
  const [deadLine, setDeadLine] = useState<number>(0);
  const [todo, setTodo] = useState<ITask[]>([]);

  // handleChange : 유저 인풋이 string이면, 우리가 원하는 타입으로 바꿔준다
  // deadLine -> number
  const handleChange = (event: ChangeEvent<HTMLInputElement>) => {
    if (event.target.name === "task") {
      setTask(event.target.value);
    } else {
      setDeadLine(Number(event.target.value));
    }
  };

  // add button 누를 때마다 add task
  const addTask = () => {
    const newTask = {
      taskName: task,
      deadLine: deadLine,
    };
    setTodo([...todo, newTask]);
    setTask("");
    setDeadLine(0);
  };

  return (
    <div className="App">
      <div className="header">
        <div className="inputContainer">
          <input
            type="text"
            name="task"
            placeholder="Add a task"
            value={task}
          />
          <input
            type="number"
            name="deadLine"
            placeholder="Set a deadline(in days)"
            value={deadLine}
          />
        </div>
        <button>Add</button>
      </div>
      <div className="todoList"></div>
    </div>
  );
};

export default App;
