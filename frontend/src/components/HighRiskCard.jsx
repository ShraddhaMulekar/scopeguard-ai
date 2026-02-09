function HighRiskCard({ data }) {

  return (
    <div className="card high">
      <h2>⚠ HIGH RISK</h2>
      <p><strong>Score:</strong> {data.risk_score}</p>
      <p>{data.summary}</p>

      <h3>Key Issues</h3>
      <ul>
        {data.key_issues.map((issue, i) => (
          <li key={i}>{issue}</li>
        ))} 
      </ul>

      <h3>Recommendations</h3>
      <ul>
        {data.recommendations.map((rec, i) => (
          <li key={i}>{rec}</li>
        ))}
      </ul>
    </div>
  );
}

export default HighRiskCard;