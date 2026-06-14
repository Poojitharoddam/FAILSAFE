# =========================
# FAILSAFE - Student Risk Prediction Model
# =========================

import pandas as pd
import numpy as np
import joblib
import shap
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from xgboost import XGBClassifier
from preprocess import load_and_preprocess

X, y = load_and_preprocess("../dataset/student-mat.csv")

# =========================
# 6. Train-Test Split
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)


# =========================
# 7. Train Model (XGBoost)
# =========================

model = XGBClassifier()

model.fit(X_train, y_train)


# =========================
# 8. Predictions & Accuracy
# =========================

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\n=========================")
print("MODEL PERFORMANCE")
print("=========================")
print("Accuracy:", accuracy)
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))


# =========================
# 9. Feature Importance
# =========================

importances = model.feature_importances_

feat_imp = pd.DataFrame({
    "Feature": X.columns,
    "Importance": importances
}).sort_values(by="Importance", ascending=False)

print("\nTop Features:\n")
print(feat_imp.head(10))

plt.figure(figsize=(10,6))

feat_imp.head(10).plot(
    x="Feature",
    y="Importance",
    kind="barh"
)

plt.title("Top 10 Important Features")
plt.tight_layout()
plt.savefig("feature_importance.png", dpi=300)
plt.close()

# =========================
# 10. SHAP Explainability
# =========================

explainer = shap.Explainer(model)
shap_values = explainer(X_test)

# Summary plot (global explanation)
shap.summary_plot(shap_values, X_test, show=False)

plt.tight_layout()
plt.savefig("shap_summary.png", dpi=300, bbox_inches="tight")
plt.close()


# =========================
# 11. Save Model
# =========================

joblib.dump(model, "model.pkl")
joblib.dump(X.columns.tolist(), "features.pkl")

print("\nModel saved successfully!")