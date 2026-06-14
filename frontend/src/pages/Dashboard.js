import { useState } from "react";
import API from "../services/api";

import Navbar from "../components/Navbar";
import RiskCard from "../components/RiskCard";
import RecommendationCard from "../components/RecommendationCard";

function Dashboard() {

  const [risk, setRisk] = useState("");
  const [probability, setProbability] = useState(0);
  const [recommendations, setRecommendations] = useState([]);

  const [formData, setFormData] = useState({
    age: 18,
    Medu: 2,
    Fedu: 2,
    traveltime: 2,
    studytime: 2,
    failures: 0,
    internet: true,
    health: 3,
    absences: 5,
    activities: true
  });

  const handleSlider = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: Number(e.target.value)
    });
  };

  const predictRisk = async () => {

    try {

      const response = await API.post(
        "/predict",
        formData
      );

      setRisk(response.data.risk);
      setProbability(response.data.probability);
      setRecommendations(
        response.data.recommendations
      );

    } catch (error) {

      console.error(error);

      alert(
        "Prediction failed. Please check backend."
      );
    }
  };

  return (
    <>
      <Navbar />

      <div className="container">

        {/* Project Information */}

        <div className="card">

          <h1>FAILSAFE</h1>

          <h3>
            AI-Powered Student Failure Risk Prediction System
          </h3>

          <hr />

          <p>
            <strong>Dataset:</strong>
            {" "}UCI Student Performance Dataset
          </p>

          <p>
            <strong>Machine Learning Model:</strong>
            {" "}XGBoost Classifier
          </p>

          <p>
            <strong>Explainable AI:</strong>
            {" "}SHAP
          </p>

          <p>
            <strong>Model Accuracy:</strong>
            {" "}81%
          </p>

          <p>
            This system identifies students
            who may be at risk of academic
            failure and provides early
            intervention recommendations.
          </p>

        </div>

        {/* Input Form */}

        <div className="card">

          <h2>Student Assessment Form</h2>

          <hr />

          <label>
            <strong>Age</strong>
          </label>

          <input
            type="range"
            min="15"
            max="22"
            name="age"
            value={formData.age}
            onChange={handleSlider}
          />

          <p>{formData.age} years</p>

          <label>
            <strong>Mother's Education</strong>
          </label>

          <input
            type="range"
            min="0"
            max="4"
            name="Medu"
            value={formData.Medu}
            onChange={handleSlider}
          />

          <p>Level {formData.Medu}</p>

          <label>
            <strong>Father's Education</strong>
          </label>

          <input
            type="range"
            min="0"
            max="4"
            name="Fedu"
            value={formData.Fedu}
            onChange={handleSlider}
          />

          <p>Level {formData.Fedu}</p>

          <label>
            <strong>Travel Time</strong>
          </label>

          <input
            type="range"
            min="1"
            max="4"
            name="traveltime"
            value={formData.traveltime}
            onChange={handleSlider}
          />

          <p>Level {formData.traveltime}</p>

          <label>
            <strong>Study Time</strong>
          </label>

          <input
            type="range"
            min="1"
            max="4"
            name="studytime"
            value={formData.studytime}
            onChange={handleSlider}
          />

          <p>Level {formData.studytime}</p>

          <label>
            <strong>Previous Failures</strong>
          </label>

          <input
            type="range"
            min="0"
            max="4"
            name="failures"
            value={formData.failures}
            onChange={handleSlider}
          />

          <p>{formData.failures}</p>

          <label>
            <strong>Health Status</strong>
          </label>

          <input
            type="range"
            min="1"
            max="5"
            name="health"
            value={formData.health}
            onChange={handleSlider}
          />

          <p>{formData.health}/5</p>

          <label>
            <strong>Absences</strong>
          </label>

          <input
            type="range"
            min="0"
            max="40"
            name="absences"
            value={formData.absences}
            onChange={handleSlider}
          />

          <p>{formData.absences} days</p>

          <br />

          <label>
            <input
              type="checkbox"
              checked={formData.internet}
              onChange={(e) =>
                setFormData({
                  ...formData,
                  internet: e.target.checked
                })
              }
            />

            {" "}Internet Access Available
          </label>

          <br />
          <br />

          <label>
            <input
              type="checkbox"
              checked={formData.activities}
              onChange={(e) =>
                setFormData({
                  ...formData,
                  activities: e.target.checked
                })
              }
            />

            {" "}Participates in Extra Activities
          </label>

          <br />
          <br />

          <label>
            <input
              type="checkbox"
              checked={formData.gaurdian}
              onChange={(e) =>
                setFormData({
                  ...formData,
                  gaurdian: e.target.checked
                })
              }
            />

            {" "}Guardian Available
          </label>

          <br />
          <br />

          <button
            onClick={predictRisk}
          >
            Predict Student Risk
          </button>

        </div>

        {/* Results */}

        {risk && (

          <>
            <RiskCard
              risk={risk}
              probability={probability}
            />

            <RecommendationCard
              recommendations={recommendations}
            />
          </>

        )}

      </div>
    </>
  );
}

export default Dashboard;