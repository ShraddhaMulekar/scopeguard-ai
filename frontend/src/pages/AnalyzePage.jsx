import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { analyzeProject } from "../api";

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

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e)=>{
    e.preventDefault()

    setLoading(true)
    setError("")

    try {
      const result = await analyzeProject({
        ...form,
        time_weeks: Number(form.time_weeks),
        team: Number(form.team),
      })

      // navigate("/result", { state: result })
    } catch (error) {
      setError("Something went wrong. Please try again.", error);
      console.log(error)
    }
    finally{
      setLoading(false)
    }
  }

  console.log("form:", form);

  return (
    <div className="container">
      <h2>Project Risk Analyzer</h2>

      <form onSubmit={handleSubmit} className="form">
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

      {loading}
      {error && <p className="error">{error}</p>}
    </div>
  );
};

export default AnalyzePage;
