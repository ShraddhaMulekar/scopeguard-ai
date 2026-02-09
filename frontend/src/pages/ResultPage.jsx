import React from "react";
import { useLocation, useNavigate } from "react-router-dom";
import HighRiskCard from "../components/HighRiskCard";
import LowRiskCard from "../components/LowRiskCard";

const ResultPage = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const data = location.state;

  if (!data) {
    return <p>No result found.</p>;
  }

  return (
    <div className="container">
      <button onClick={() => navigate("/")}>← Back</button>

      {data.risk_level === "HIGH" ? (
        <HighRiskCard data={data} />
      ) : (
        <LowRiskCard data={data} />
      )}
    </div>
  );
};

export default ResultPage;