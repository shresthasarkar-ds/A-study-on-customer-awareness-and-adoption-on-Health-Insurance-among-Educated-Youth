"""Re-computes the main statistical results of the study from the files in this folder.

Requires: numpy, pandas, scipy
Run:      python reproduce_results.py
"""
import numpy as np, pandas as pd
from scipy.stats import chi2_contingency, chi2, norm

# 1. Chi-square tests of independence (observed counts, no continuity correction)
t = pd.read_csv("03_chi_square_tests/contingency_tables_observed_expected.csv")
for name, g in t.groupby("test", sort=False):
    obs = g[["insured_observed", "uninsured_observed"]].to_numpy()
    c, p, dof, _ = chi2_contingency(obs, correction=False)
    print(f"{name}: chi2({dof}) = {c:.4f}, p = {p:.5f}")

# 2. Logistic regression (Newton-Raphson maximum likelihood)
d = pd.read_csv("05_logistic_regression/model_data.csv")
y = d["insured"].to_numpy(float)
X = np.column_stack([np.ones(len(d)), d[["awareness", "income_category", "importance", "student"]]])
beta = np.zeros(X.shape[1])
for _ in range(100):
    p = 1 / (1 + np.exp(-X @ beta))
    step = np.linalg.solve(X.T @ (X * (p * (1 - p))[:, None]), X.T @ (y - p))
    beta += step
    if abs(step).max() < 1e-12:
        break
p = 1 / (1 + np.exp(-X @ beta))
se = np.sqrt(np.diag(np.linalg.inv(X.T @ (X * (p * (1 - p))[:, None]))))
ll = np.sum(y * np.log(p) + (1 - y) * np.log(1 - p))
ll0 = len(y) * (y.mean() * np.log(y.mean()) + (1 - y.mean()) * np.log(1 - y.mean()))
out = pd.DataFrame({"coef": beta, "se": se, "z": beta / se,
                    "p": 2 * (1 - norm.cdf(abs(beta / se))), "odds_ratio": np.exp(beta)},
                   index=["Intercept", "Awareness", "Income", "Importance", "Student"])
print(out.round(4))
print(f"Log-likelihood = {ll:.4f}, McFadden R2 = {1 - ll / ll0:.4f}, "
      f"LR = {2 * (ll - ll0):.3f} (p = {1 - chi2.cdf(2 * (ll - ll0), 4):.4f})")
