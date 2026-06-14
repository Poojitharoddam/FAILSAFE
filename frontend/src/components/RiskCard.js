function RiskCard({ risk, probability }) {
  return (
    <div className="card">
      <h3>Prediction Result</h3>

      <p>
        <strong>Risk:</strong> {risk}
      </p>

      <p>
        <strong>Probability:</strong> {probability}%
      </p>
    </div>
  );
}

export default RiskCard;