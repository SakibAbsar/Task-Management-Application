
import React, { useEffect, useState } from 'react';
import { fetchTasks } from '../api';

function TaskList() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    fetchTasks().then(data => setTasks(data));
  }, []);

  return (
    <ul>
      {tasks.map(task => (
        <li key={task.id}>
          {task.title} - {task.completed ? "Done" : "Pending"}
        </li>
      ))}
    </ul>
  );
}

export default TaskList;
