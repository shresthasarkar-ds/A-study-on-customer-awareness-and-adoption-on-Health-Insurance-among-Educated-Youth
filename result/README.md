# Statistical Results

Results for *A Study on Customer Awareness and Adoption of Health Insurance Among Educated Youth* (n = 65).
Every table is saved as CSV so it can be opened in Excel or loaded in Python/R. The numbers come from
`Health_Insurance_Study_Analysis_with_Charts.xlsx` and were re-computed independently in Python (all values match).

## Folder structure

```
results/
├── README.md
├── hypothesis_testing_summary.csv        all tests in one table
├── reproduce_results.py                  re-computes chi-square and logistic regression
├── 01_descriptive/
│   ├── frequency_tables.csv              counts and % for demographics, awareness, ownership, satisfaction, plan type
│   └── multi_select_option_counts.csv    sources, reasons, challenges, motivators (respondents per option)
├── 02_crosstabs/
│   ├── awareness_by_age_group.csv
│   ├── awareness_by_future_interest.csv
│   ├── employment_by_ownership.csv
│   ├── income_by_plan_type.csv
│   └── plan_type_by_satisfaction.csv
├── 03_chi_square_tests/
│   ├── chi_square_summary.csv            statistic, df, p-value, Cramer's V, Yates-corrected values
│   └── contingency_tables_observed_expected.csv
├── 04_correlation/
│   └── spearman_results.csv
└── 05_logistic_regression/
    ├── model_summary.csv                 log-likelihood, LR test, McFadden R2, accuracy, AUC
    ├── coefficients.csv                  coefficients, SE, z, p, odds ratios, 95% CIs
    └── model_data.csv                    the 65 rows used to fit the model
```

## Key results

| Hypothesis | Test | Statistic | p-value | Decision (5%) |
|---|---|---|---|---|
| Awareness vs current ownership | Chi-square | χ²(2) = 3.215 | 0.200 | Do not reject H0 |
| Income group vs current ownership | Chi-square | χ²(1) = 7.581 | 0.006 | Reject H0 |
| Employment group vs current ownership | Chi-square | χ²(1) = 8.628 | 0.003 | Reject H0 |
| Awareness vs future purchase intention | Spearman | rs = 0.302 | 0.015 | Reject H0 |
| Income category vs current ownership | Spearman | rs = 0.304 | 0.014 | Reject H0 |
| Overall logistic model | Likelihood ratio | LR = 13.729 (df 4) | 0.008 | Reject H0 |

**Logistic regression** (dependent variable: currently insured = 1; n = 65; McFadden pseudo R² = 0.157)

| Predictor | Coefficient | Odds ratio | 95% CI (OR) | p-value |
|---|---|---|---|---|
| Intercept | -1.452 | 0.234 | 0.016 – 3.393 | 0.287 |
| Awareness (0-2) | 0.559 | 1.749 | 0.693 – 4.413 | 0.236 |
| Income category (0-4) | 0.443 | 1.558 | 0.817 – 2.970 | 0.178 |
| Perceived importance (0-2) | 1.077 | 2.936 | 0.855 – 10.088 | 0.087 |
| Student (1 = student) | -1.192 | 0.304 | 0.083 – 1.104 | 0.070 |

The model as a whole is significant, but no single predictor is significant at 5%. Importance and student status
are the closest (p < 0.10). The odds-ratio confidence intervals are wide, which reflects the small sample.

## Notes on interpretation

- **Awareness and ownership:** two cells in the awareness table have expected counts below 5 (minimum 2.0), so the
  chi-square approximation is weak for that test. Treat it as indicative.
- **2×2 tests:** the values above are uncorrected. With Yates' continuity correction the income test gives
  χ² = 6.193 (p = 0.013) and the employment test χ² = 7.204 (p = 0.007), so both conclusions hold.
- **Effect sizes (Cramér's V):** 0.22 (awareness), 0.34 (income), 0.36 (employment), i.e. small to moderate.
- **Classification accuracy** (69.2%), sensitivity (76.9%), specificity (57.7%) and AUC (0.763) are supplementary
  figures calculated for this folder. They are not in the paper.
- **Multi-select questions:** respondents could choose several options, so percentages add up to more than 100%.

## Inconsistencies found between the paper and the workbook

1. **Section 4.7.1 (Spearman, awareness vs intention):** the paper states intention was coded No = 0, Not Sure = 1,
   Yes = 2, but the workbook used Yes = 0, No = 1, Not Sure = 2. That gives rs = -0.317 (p = 0.0100), and the
   paper reads it as "higher awareness, lower intention". With the coding the paper describes, rs = +0.302
   (p = 0.0146), which is also the value quoted in Section 5.1.5. The correct reading is that higher awareness goes
   with higher purchase intention. This folder reports the corrected value and keeps the workbook value for reference.
2. **Chart "Factors Encouraging Adoption":** shows Government incentives/subsidies = 25 (38.5%). The survey data
   gives 22 (33.8%). The other four bars are correct.
3. **Chart "Factors Influencing Non-Adoption":** shows Rely on family's insurance = 12. The Excel pivot gives 14
   (12 on its own plus 2 who also chose other options). The CSV text for this question is corrupted, so verify it
   against the original form.
4. **Conditional questions:** all 65 respondents answered the "reasons for not buying", plan type, premium and
   satisfaction questions, including the 26 uninsured. Counts for these questions are not restricted to the
   relevant subgroup.
