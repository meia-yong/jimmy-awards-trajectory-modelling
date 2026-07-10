# Results

This document reports the empirical results from the Jimmy Awards trajectory analysis. Full details on dataset construction, variable definitions, and model selection are provided in `methodology.md`.

---

# 1. Broadway Entry Timing

Broadway debut timing was analysed using Kaplan–Meier survival estimation, a log-rank test, and a Cox proportional hazards model.

## Log-Rank Test

| Test             | Result |
| ---------------- | -----: |
| Log-rank p-value | 0.0769 |

The Kaplan–Meier comparison suggests that Jimmy Award winners may debut on Broadway more quickly than finalists, although the difference is not statistically significant at the 5% level.

## Cox Proportional Hazards Model

| Variable           | Hazard Ratio | 95% Confidence Interval | p-value |
| ------------------ | -----------: | ----------------------: | ------: |
| Jimmy Award Winner |         2.04 |               0.94–4.47 |   0.070 |
| Gender (Actress)   |         0.69 |               0.32–1.50 |   0.350 |

The Cox model estimates that Jimmy Award winners had approximately twice the rate of Broadway debut compared with finalists during the observation period, controlling for gender. However, the confidence interval includes no effect, so the estimate should be interpreted cautiously.

---

# 2. Broadway Career Volume

Broadway career volume was analysed using count regression models with total Broadway credits as the outcome.

## Dispersion Check

| Statistic             | Value |
| --------------------- | ----: |
| Mean credits          |  0.34 |
| Variance              |  0.56 |
| Variance / Mean ratio |  1.68 |

The variance exceeded the mean, indicating overdispersion in Broadway credit counts.

## Model Comparison

| Model                        |    AIC |
| ---------------------------- | -----: |
| Poisson Regression           | 178.45 |
| Negative Binomial Regression | 172.43 |

Because the Negative Binomial model provided better fit, it is treated as the preferred count specification.

## Negative Binomial Regression Results

| Variable           | Expected Credit Multiplier | 95% Confidence Interval | p-value |
| ------------------ | -------------------------: | ----------------------: | ------: |
| Jimmy Award Winner |                      2.21x |             0.98x–4.96x |   0.056 |
| Gender (Actress)   |                      0.68x |             0.30x–1.53x |   0.350 |

The preferred model estimates that Jimmy Award winners accumulated approximately 2.21 times the expected number of Broadway credits compared with finalists, controlling for gender. As with the survival results, uncertainty remains due to the limited sample size.

---

# 3. Overall Interpretation

Across both outcome measures, Jimmy Award winners exhibit stronger estimated Broadway outcomes than finalists within the observed cohort.

* Winners appear to debut on Broadway at a faster rate.
* Winners appear to accumulate more Broadway credits over time.

These results do not imply that Jimmy Award recognition independently causes career success. A more cautious interpretation is that early-career recognition may function as a persistent professional signal associated with later Broadway participation, while operating alongside many other factors such as training, networks, representation, timing, and opportunity.
