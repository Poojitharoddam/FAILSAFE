function RecommendationCard({ recommendations }) {
  return (
    <div className="card">
      <h3>Recommendations</h3>

      <ul>
        {recommendations.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>
    </div>
  );
}

export default RecommendationCard;