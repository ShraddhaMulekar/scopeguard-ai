import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

const AnalyzePage = () => {
  const navigate = useNavigate();

  const [form, setForm] = useState({
    idea: "",
    experience: "",
    time_weeks: "",
    team: "",
    tech: "",
  });

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  return (
    <div>
      <h2>Project Risk Analyzer</h2>

      <form action="">
        <input
          type="text"
          name="idea"
          placeholder="Project Idea"
          required
          onChange={handleChange}
        />
        <input
          type="text"
          name="experience"
          placeholder="Experience Level Ex.(beginner, medium, advance)"
          required
          onChange={handleChange}
        />
        <input
          type="number"
          name="time_weeks"
          placeholder="Time (weeks)"
          required
          onChange={handleChange}
        />
        <input
          type="number"
          name="team"
          placeholder="Team size"
          required
          onChange={handleChange}
        />
        <input
          type="text"
          name="tech"
          placeholder="Tech Stack"
          required
          onChange={handleChange}
        />
        <button type="submit" disabled={loading}>
          {loading ? "Analyzing..." : "Analyze"}
        </button>
      </form>
      
      {loading && <Spinner />}
      {error && <p className="error">{error}</p>}
    </div>
  );
};

export default AnalyzePage;
