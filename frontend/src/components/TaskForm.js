import { useState } from "react";
import API from "../services/api";

function TaskForm({ refresh }) {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");

  const createTask = async () => {
    await API.post("/tasks/", { title, description });
    setTitle("");
    setDescription("");
    refresh();
  };

  return (
    <div>
      <h3>Create Task</h3>
      <input placeholder="title" value={title} onChange={(e) => setTitle(e.target.value)} />
      <input placeholder="description" value={description} onChange={(e) => setDescription(e.target.value)} />
      <button onClick={createTask}>Add Task</button>
    </div>
  );
}

export default TaskForm;