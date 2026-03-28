import { useEffect, useState } from "react";
import API from "../services/api";
import TaskForm from "./TaskForm";
import "../App.css";

function Dashboard() {
  const [tasks, setTasks] = useState([]);

  const fetchTasks = async () => {
    const res = await API.get("/tasks");
    setTasks(res.data.data);
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  return (
    <div className="dashboard">
      <h2>Dashboard</h2>

      <TaskForm refresh={fetchTasks} />

      <div className="task-grid">
        {tasks.map((task) => (
          <div key={task.id} className="task-card">
            <h4>{task.title}</h4>
            <p>{task.description}</p>
            <p><b>Category:</b> {task.category}</p>
            <p><b>Priority:</b> {task.priority}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Dashboard;