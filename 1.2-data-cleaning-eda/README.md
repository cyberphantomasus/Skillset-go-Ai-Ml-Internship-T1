# Week 1 - Task 1.2: Data Cleaning & EDA

Skill Set Go EduTech — AI/ML Internship (Offer ID: SSG/AIML/B1/0291)

## Objective
Clean a real-world dataset and explore it with NumPy, Pandas and Matplotlib to
uncover patterns and anomalies (Week 1 Task 1.2).

## Dataset
Titanic passenger data — 891 rows, 12 columns. Source:
[datasciencedojo/datasets](https://github.com/datasciencedojo/datasets) (`data/titanic.csv`).
Chosen for realistic messiness: missing Age (~20%), missing Cabin (~77%),
missing Embarked (2 rows), skewed Fare distribution.

## Tools
Python, Pandas, NumPy, Matplotlib, Jupyter.

## Setup
```bash
pip install pandas numpy matplotlib jupyter
jupyter notebook 1.2_data_cleaning_eda.ipynb
```

## Method
1. Inspected structure, dtypes, and summary statistics.
2. Audited missing values per column.
3. Cleaned: imputed Age by median-per-class, imputed Embarked by mode,
   converted sparse Cabin into a binary `HasCabin` flag, dropped
   non-analytical columns (Name, Ticket, PassengerId).
4. Checked for anomalies (zero fares, fare outliers).
5. Visualized: age/fare distributions, survival rate by class and sex,
   correlation matrix.

## Results — key insights
- Passenger class was the strongest structural driver of survival (1st
  class ~3x the survival rate of 3rd class).
- Sex was the single strongest predictor — women survived at a much higher
  rate than men.
- `HasCabin` correlates with survival but is a proxy for class/wealth, not
  a causal effect.
- Missingness was not random: Cabin and Age were disproportionately missing
  for lower classes, which is why imputation was done per-class rather than
  globally.

## Files
- `1.2_data_cleaning_eda.ipynb` — full notebook (cleaning + EDA + charts)
- `data/titanic.csv` — raw dataset
- `titanic_cleaned.csv` — cleaned output dataset
- `age_fare_distribution.png`, `survival_by_class_sex.png`, `correlation_matrix.png` — saved charts

## Next improvements
- Feature-engineer `Title` from `Name` before dropping it (would strengthen a future model).
- Add a statistical test (e.g. chi-square) to confirm the class/sex survival differences are significant.
