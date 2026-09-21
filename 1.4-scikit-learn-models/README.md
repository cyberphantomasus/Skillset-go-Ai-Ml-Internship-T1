# Week 1 - Task 1.4: Two ML Models with Scikit-learn

Skill Set Go EduTech — AI/ML Internship (Offer ID: SSG/AIML/B1/0291)

## Objective
Build and evaluate one regression model and one classification model,
including preprocessing, train/test split, and metrics (Week 1 Task 1.4).

## Part A — Regression
- **Dataset:** scikit-learn's built-in Diabetes dataset (442 patients, 10 features).
- **Model:** Linear Regression.
- **Preprocessing:** train/test split (80/20) before scaling to avoid leakage; `StandardScaler` fit on train only.
- **Metrics:** MAE, MSE, RMSE, R².
- **Result:** R² ≈ 0.45–0.55 — baseline measurements only partially explain disease progression.

## Part B — Classification
- **Dataset:** cleaned Titanic dataset from Task 1.2 (891 passengers).
- **Model:** Logistic Regression.
- **Preprocessing:** `Sex` binary-mapped, `Embarked` one-hot encoded, stratified 80/20 split, `StandardScaler` fit on train only.
- **Metrics:** Accuracy, Precision, Recall, F1, ROC-AUC, confusion matrix, ROC curve.
- **Result:** Accuracy ≈ 0.81, ROC-AUC ≈ 0.84. `Sex` is the strongest predictor, consistent with the Task 1.2 EDA.

## Tools
Python, scikit-learn, Pandas, NumPy, Matplotlib.

## Setup
```bash
pip install scikit-learn pandas numpy matplotlib jupyter
jupyter notebook 1.4_ml_models.ipynb
```

## Files
- `1.4_ml_models.ipynb` — full notebook (both models + evaluation report)
- `data/titanic_cleaned.csv` — cleaned dataset (from Task 1.2)
- `regression_evaluation.png` — actual-vs-predicted + residual plot
- `classification_evaluation.png` — confusion matrix + ROC curve

## Evaluation report
See the "Evaluation Report — Summary" section at the end of the notebook for
the full metric comparison table and interpretation of both models.

## Next improvements
- Try a non-linear regressor (Random Forest / Gradient Boosting) on the diabetes data to address the residual heteroscedasticity.
- Add cross-validation instead of a single train/test split for more robust metrics.
