# =========================
# FAILSAFE - Data Preprocessing
# =========================

import pandas as pd


def load_and_preprocess(filepath):
    """
    Load and preprocess student dataset

    Parameters:
        filepath (str): Path to CSV file

    Returns:
        X (DataFrame): Features
        y (Series): Target
    """

    # Load dataset
    df = pd.read_csv(filepath, sep=";")

    # Create target variable
    # 1 = At Risk (G3 < 10)
    # 0 = Safe
    df["risk"] = df["G3"].apply(lambda x: 1 if x < 10 else 0)

    # Remove only G3
    # Keep G1 and G2 for better accuracy
    df = df.drop(["G2", "G3"], axis=1)

    # Convert categorical columns
    df = pd.get_dummies(df, drop_first=True)

    # Split features and target
    X = df.drop("risk", axis=1)
    y = df["risk"]

    return X, y


if __name__ == "__main__":

    X, y = load_and_preprocess("../dataset/student-mat.csv")

    print("Dataset Processed Successfully")
    print("Features Shape:", X.shape)
    print("Target Shape:", y.shape)

    print("\nFirst 5 Rows:")
    print(X.head())