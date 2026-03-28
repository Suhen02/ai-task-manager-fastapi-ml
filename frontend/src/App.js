import { useState } from "react";
import Login from "./components/Login";
import Register from "./components/Register";
import Dashboard from "./components/Dashboard";
import "./App.css";

function App() {
  const [auth, setAuth] = useState(false);
  const [tab, setTab] = useState("login");

  if (auth) return <Dashboard />;

  return (
    <div className="container">
      <div className="card">
        <h2 style={{ textAlign: "center" }}>AI Task Manager</h2>

        {/* Tabs */}
        <div className="tabs">
          <div
            className={`tab ${tab === "login" ? "active" : ""}`}
            onClick={() => setTab("login")}
          >
            Login
          </div>
          <div
            className={`tab ${tab === "register" ? "active" : ""}`}
            onClick={() => setTab("register")}
          >
            Register
          </div>
        </div>

        {tab === "login" ? (
          <Login setAuth={setAuth} />
        ) : (
          <Register />
        )}
      </div>
    </div>
  );
}

export default App;