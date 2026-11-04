# Data Dictionary

**Dataset:** `health_insurance_survey_responses.csv`
**Study:** A Study on Customer Awareness and Adoption of Health Insurance Among Educated Youth
**Collection method:** Structured questionnaire (Google Forms style), convenience sampling
**Rows:** 65 respondents | **Columns:** 18 | **Missing values:** none in any column

Each row is one respondent. Columns 7, 10, 14 and 16 are multi-select questions: the selected options are stored in a single cell, separated by semicolons (`;`).

---

## Column Reference

| # | Original column header | Suggested clean name | Type | Allowed values (count) |
|---|---|---|---|---|
| 1 | Age Group | `age_group` | Ordinal | 18-22 (38), 23-27 (24), 28-32 (2), Above 32 (1, see data note 1) |
| 2 | Gender | `gender` | Categorical | Male (51), Female (14) |
| 3 | Educational Qualification | `education` | Categorical | Postgraduate (47), Undergraduate (18) |
| 4 | Employment Status | `employment_status` | Categorical | Student (33), Employed (Private Sector) (22), Self-Employed (8), Employed (Government Sector) (2) |
| 5 | Monthly Income (if applicable) | `monthly_income` | Ordinal | 0 (21), Below 20000/- (21), 20000/- to 50000/- (16), 50000/- to 100000/- (4), Above 100000/- (3) |
| 6 | Are you aware of health insurance and its benefits? | `awareness_level` | Ordinal | Not aware (5), Somewhat aware (29), Yes, fully aware (31) |
| 7 | How did you learn about health insurance? (Select all that apply) | `awareness_sources` | Multi-select | Social Media & Internet (33), Family & Friends (32), Employer/College/University (24), Insurance Agents (19), Advertisements (TV, Print, Online) (17) |
| 8 | Are you aware of government health insurance schemes (e.g., Ayushman Bharat, ESI, PMJAY)? | `aware_govt_schemes` | Binary | Yes (50), No (15) |
| 9 | Do you currently have health insurance? | `has_insurance` | Categorical | Yes, self-purchased (30), Yes, provided by employer/university (9), No (26) |
| 10 | If you don't have health insurance, what is the reason? (Select all that apply) | `reasons_not_insured` | Multi-select | Lack of awareness (21), Too expensive (16), Policies are too complex (14), Rely on family's coverage, I don't feel the need for it, and one further option (see data note 4) |
| 11 | What type of health insurance do you have? | `plan_type` | Categorical | Family Floater Plan (24), Individual Health Plan (23), Government Scheme (9), Employer-Provided Plan (9) |
| 12 | How much do you pay annually for health insurance? | `annual_premium` | Ordinal | Below 5,000 (32), 5,000 to 15,000 (17), 15,000 to 30,000 (13), Above 100000/- (3, see data note 2) |
| 13 | How important do you think health insurance is? | `importance` | Ordinal | Very important (47), Somewhat important (15), Not important (3) |
| 14 | What challenges do you face in getting health insurance? (Select all that apply) | `challenges` | Multi-select | High premium costs (27), Difficult claim settlement process (27), Limited awareness and understanding (22), Lack of transparency in policies (14), Not enough benefits for the cost (9) |
| 15 | Would you be interested in purchasing health insurance in the future? | `future_interest` | Categorical | Yes (44), No (13), Not Sure (8) |
| 16 | What would encourage you to buy health insurance? (Select all that apply) | `purchase_motivators` | Multi-select | Digitalized and simple policy selection (35), Easy claim settlement process (34), More awareness and education programs (32), Lower premium rates (30), Government incentives/subsidies (22) |
| 17 | Would you prefer to purchase health insurance through: | `preferred_channel` | Categorical | Online platforms (websites/apps) (26), Insurance agents (18), Government schemes (12), Employer/university benefits (9) |
| 18 | On a scale of 1 to 5, how satisfied are you with your current health insurance | `satisfaction` | Ordinal (1-5) | Very Dissatisfied = 1 (5), Dissatisfied = 2 (7), Neutral = 3 (27), Satisfied = 4 (22), Very Satisfied = 5 (4) |

Counts for multi-select columns are the number of respondents who selected that option, so they add up to more than 65.

---

## Variable Roles in the Analysis

| Role | Variables |
|---|---|
| Demographics | age_group, gender, education, employment_status, monthly_income |
| Awareness | awareness_level, awareness_sources, aware_govt_schemes |
| Adoption (main outcome) | has_insurance (can be recoded as binary: Yes = insured, No = uninsured) |
| Policy details | plan_type, annual_premium, satisfaction |
| Attitudes and barriers | importance, reasons_not_insured, challenges |
| Future intent | future_interest, purchase_motivators, preferred_channel |

**Suggested recoding for modelling**

- `has_insurance`: "Yes, self-purchased" and "Yes, provided by employer/university" become 1; "No" becomes 0 (39 insured, 26 uninsured).
- `awareness_level`: Not aware = 0, Somewhat aware = 1, Fully aware = 2.
- `satisfaction`: map to 1-5 as shown above.
- Multi-select columns: split on `;` and create one 0/1 column per option.

---

## Data Notes and Known Issues

1. **Age Group, "Above 100000/-":** one respondent has this value in the age column, which looks like a data-entry slip. The analysis workbook counts this respondent as "Above 32", so it is most likely that category.
2. **Annual premium, "Above 100000/-":** three respondents have this value, which does not fit an annual premium scale (the other options top out at 15,000 to 30,000). The label is probably a mislabelled top category. Please verify against the original form before relying on it.
3. **Character encoding:** the CSV is not UTF-8. The rupee symbol and apostrophes are corrupted in some headers and values (columns 10 and 12). Re-save the file as UTF-8 before uploading. Because the original characters were overwritten, some values cannot be recovered from the file itself.
4. **Reasons for not having insurance (column 10):** because of the encoding problem, some option texts are cut off after the apostrophe (for example "I don't ..." and "Rely on family's ..."). Restore the full option wording from the questionnaire. Options containing an apostrophe cannot be reliably counted until then.
5. **Questions answered by insured respondents too:** all 65 respondents have a value in columns 10, 11, 12 and 18, including the 26 who said they have no insurance. If you analyse these only for insured respondents, filter on `has_insurance` first.
6. **Income value "0":** 21 respondents entered 0, which corresponds mainly to students with no income. Treat it as "no income" rather than missing.
7. **Sample:** convenience sample of 65 educated young people (about 78% male, 72% postgraduate, 58% aged 18-22), so results should not be generalised to all Indian youth.
