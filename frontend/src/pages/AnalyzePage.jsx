import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import Spinner from "../components/Spinner";
import "../styles.css";
import base_url from "../api/base_url";

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

  const handleSubmit = async (e) => {
    e.preventDefault();

    setLoading(true);
    setError("");

    try {
      const res = await fetch(`${base_url}/analyze`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          ...form,
          time_weeks: Number(form.time_weeks),
          team: Number(form.team),
        }),
      });

      if (!res.ok) {
        throw new Error("Server error");
      }

      const data = await res.json();

      navigate("/result", { state: data });
    } catch (err) {
      console.error(err);
      setError("Something went wrong. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">

      <div className="cont">
        <img
          className="logo"
          src="https://cdn.prod.website-files.com/646e363f9c29e4860c52c82e/646e363f9c29e4860c52c88c_CCE%20(1).png"
          alt="logo"
        />
        <h1>Scope Guard AI (Project Risk Analyzer)</h1>
      </div>

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

      {loading && <Spinner />}
      {error && <p className="error">{error}</p>}
    </div>
  );
};

export default AnalyzePage;
