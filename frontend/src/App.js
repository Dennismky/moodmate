import React, { useState } from "react";
import { login, logMood, getMoodLogs, deleteMood } from "./api/moodmate";
import "./App.css";

function App() {
  const [username, setUsername] = useState("");
  const [user, setUser] = useState(null);
  const [mood, setMood] = useState("");
  const [suggestion, setSuggestion] = useState("");
  const [moodLogs, setMoodLogs] = useState([]);

  const handleLogin = async () => {
    const userData = await login(username);
    setUser(userData);
    const logs = await getMoodLogs(username);
    setMoodLogs(logs);
  };

  const handleLogMood = async () => {
    if (!user) return;
    if (!mood) {
      alert("Please select a mood");
      return;
    }
    const result = await logMood(user.id, mood);
    setSuggestion(result.suggestion);
    const updatedLogs = await getMoodLogs(user.name);
    setMoodLogs(updatedLogs);
    setMood("");
  };

  const handleDeleteMood = async (moodId) => {
    try {
      await deleteMood(moodId);
      const updatedLogs = await getMoodLogs(user.name);
      setMoodLogs(updatedLogs);
    } catch (error) {
      alert("Failed to delete mood. Please try again.");
    }
  };

  return (
    <div className="app-container">
      <h1>MoodMate</h1>

      {!user ? (
        <div className="login-section">
          <input
            type="text"
            placeholder="Enter your name"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
          <button onClick={handleLogin}>Login</button>
        </div>
      ) : (
        <div className="mood-section">
          <h2>Welcome, {user.name}!</h2>

          <div className="mood-form">
            <label htmlFor="mood-select">Choose your mood:</label>
            <select
              id="mood-select"
              value={mood}
              onChange={(e) => setMood(e.target.value)}
              className="mood-select"
            >
              <option value="">--Select Mood--</option>
              {[
                "Happy", "Sad", "Angry", "Jovial", "Axious", "Energetic", "Tired", "Frustrated", "Hopeful", "Content",
                "Nervous", "Relaxed", "Overwhelmed", "Inspired", "Lonely",
                "Grateful", "Bored", "Confident", "Restless", "Curious"
              ].map((m) => (
                <option key={m} value={m}>
                  {m.charAt(0).toUpperCase() + m.slice(1)}
                </option>
              ))}
            </select>
            <button onClick={handleLogMood} className="submit-btn">
              Submit Mood
            </button>
          </div>

          {suggestion && (
            <div className="suggestion">
              <h3>Suggestion:</h3>
              <p>{suggestion}</p>
            </div>
          )}

          <div className="history">
            <h3>Your Mood History:</h3>
            <ul>
              {moodLogs.map((log) => (
                <li key={log.id}>
                  <strong>{log.mood}</strong> - {log.suggestion} ({log.timestamp})
                  <button
                    onClick={() => handleDeleteMood(log.id)}
                    style={{
                      marginLeft: "10px",
                      color: "white",
                      backgroundColor: "red",
                      border: "none",
                      borderRadius: "4px",
                      padding: "2px 8px",
                      cursor: "pointer"
                    }}
                  >
                    Delete
                  </button>
                </li>
              ))}
            </ul>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;

