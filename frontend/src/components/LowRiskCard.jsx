function LowRiskCard({ data }) {
  const explanation = data.explanation || {};

  return (
    <div className="card low">
      <h2>✅ LOW RISK</h2>
      <p><strong>Score:</strong> {data.risk_score}</p>
      <p>{data.summary}</p>

      <h3>Why Feasible</h3>
      <ul>
        {explanation.why_feasible?.map((item, i) => (
          <li key={i}>{item}</li>
        ))}
      </ul>

      <h3>Assumptions</h3>
      <ul>
        {explanation.assumptions?.map((item, i) => (
          <li key={i}>{item}</li>
        ))}
      </ul>

      <h3>Monitoring</h3>
      <ul>
        {explanation.monitoring?.map((item, i) => (
          <li key={i}>{item}</li>
        ))}
      </ul>
    </div>
  );
}

export default LowRiskCard;