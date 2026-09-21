# Week 1 - Task 1.3: Math for ML Practice Set

Skill Set Go EduTech — AI/ML Internship (Offer ID: SSG/AIML/B1/0291)

## Objective
Solved applied problems in statistics, probability, linear algebra, and basic
calculus as used in ML algorithms (Week 1 Task 1.3).

## Structure
| Section | Covers | Tied to |
|---|---|---|
| 1. Statistics | Mean/median/mode, variance/std, z-scores, quartiles & IQR outlier detection | Feature scaling, outlier detection used in Task 1.2 |
| 2. Probability | Conditional probability, Bayes' theorem, normal distribution fit | Naive Bayes, Gaussian model assumptions |
| 3. Linear Algebra | Dot product/cosine similarity, matrix ops, the Normal Equation | Similarity/embeddings, closed-form linear regression |
| 4. Calculus | Symbolic derivatives, chain rule, partial derivatives, gradient descent from scratch | Backpropagation, how models actually learn |

Each section computes results **by formula first**, then verifies against
NumPy/SciPy/SymPy/scikit-learn — and section 4.3 confirms gradient descent
converges to the same line as the closed-form Normal Equation in section 3.3.

## Dataset
Reuses the cleaned Titanic dataset from Task 1.2 (`data/titanic_cleaned.csv`)
for the probability section, so the math is grounded in real data rather
than toy numbers.

## Tools
Python, NumPy, SciPy, SymPy, Pandas, Matplotlib, scikit-learn.

## Setup
```bash
pip install numpy scipy sympy pandas matplotlib scikit-learn jupyter
jupyter notebook 1.3_math_for_ml.ipynb
```

## Files
- `1.3_math_for_ml.ipynb` — full worked-solutions notebook
- `data/titanic_cleaned.csv` — cleaned dataset (from Task 1.2)
- `normal_distribution_fit.png`, `gradient_descent_convergence.png` — saved charts

## Next improvements
- Add eigenvalues/eigenvectors worked example tied to PCA.
- Extend gradient descent to multivariate regression (2+ features).
