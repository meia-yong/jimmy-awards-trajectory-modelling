# Modeling Broadway Trajectories: A Statistical Analysis of Early-Career Musical Theatre Signals

A quantitative study examining whether recognition from the National High School Musical Theatre Awards (The Jimmy Awards) is associated with differences in Broadway entry timing and long-term career outcomes.

---

# Executive Summary

This project evaluates whether an early-career artistic credential contains measurable information about subsequent professional outcomes.

Using a manually curated historical cohort dataset of Jimmy Awards finalists from 2010–2026 ($N=113$), the analysis applies survival analysis and count regression methods to investigate whether winner status is associated with differences in Broadway career trajectories.

The central research question is:

> Does Jimmy Award recognition contain measurable information about future Broadway career trajectories?

The project treats awards as an early-career signalling mechanism: an observable credential that may contain predictive information about future outcomes, analogous to signalling problems studied in labour economics and other fields where early indicators are used to evaluate future potential.

The analysis is observational and evaluates associations rather than causal effects. Winning a Jimmy Award is not interpreted as independently causing career advancement; instead, the project examines whether winner status is associated with measurable differences in observed outcomes.

## Key Findings

### Broadway Entry Timing

A multivariate **Cox Proportional Hazards Model** estimates that Jimmy Award winners enter Broadway at approximately twice the rate of finalists during the observation period.

* Hazard Ratio: **2.04**
* 95% Confidence Interval: **0.94–4.47**
* p-value: **0.0709**

The estimated effect is directionally large, but uncertainty remains due to the limited sample size.

### Cumulative Broadway Credits

Broadway credit accumulation is modelled using a **Negative Binomial Regression Model**, selected after testing for overdispersion in the count outcome.

The preferred model estimates:

* Expected credit multiplier for winners: **2.21x**
* 95% Confidence Interval: **0.98x–4.96x**
* p-value: **0.056**

The estimate suggests that Jimmy Award winners accumulate more Broadway credits on average within this dataset, although uncertainty remains.

These findings should be interpreted as associations rather than causal effects.

---

# Project Structure

```
├── src/
│   ├── main.py
│   ├── survival_analysis.py
│   └── longevity_analysis.py
├── data/
│   └── Jimmy Awards Dataset NEW.xlsx
├── plots/
│   └── broadway_survival_chart.png
└── docs/
    ├── methodology.md
    └── data_dictionary.md
```

---

# Research Questions

This project investigates three related questions:

1. Does Jimmy Award recognition predict faster transition into Broadway employment?

2. Is recognition associated with greater accumulation of Broadway credits?

3. How effectively can a single early-career credential function as a signal of future professional outcomes within a highly selective creative industry?

---

# Data Architecture & Bias Mitigation

The dataset tracks Jimmy Awards finalists from 2010 to 2026.

Data was manually curated and structured using reproducible empirical research practices, with explicit consideration of observation periods, sample construction, and measurement limitations.

## Broadway Entry Definition

Only official Broadway production contracts recorded by the Internet Broadway Database (IBDB) trigger a Broadway debut event.

National Tours, West End productions, and Off-Broadway performances are excluded to maintain a consistent institutional definition of Broadway entry.

## Look-Ahead Bias Prevention

Future casting announcements and productions that had not officially opened are excluded to prevent future information from entering historical observations.

## Cohort Construction

Performers are tracked from their Jimmy Award nomination year, creating a consistent baseline for measuring subsequent career outcomes.

Because Jimmy Award finalists already represent a highly selective group of young performers, the analysis compares differences within this elite cohort rather than estimating outcomes for all aspiring performers.

---

# Methodology & Key Findings

## 1. Speed to Broadway Entry (Survival Analysis)

To analyse the timing of Broadway debut, the project uses:

* Kaplan–Meier survival estimation
* Log-rank testing
* Multivariate Cox Proportional Hazards Regression

The outcome is:

```
Time from Jimmy Award nomination → Broadway debut
```

Performers who had not debuted by 2026 are treated as right-censored observations.

![Broadway Survival Chart](plots/broadway_survival_chart.png)

The Cox model specification is:

```python
cph.fit(
    regression_df,
    duration_col='Timeline_Years',
    event_col='Broadway_Debut'
)
```

The model estimates that Jimmy Award winners have a higher rate of Broadway debut during the observation period compared with finalists.

However, the confidence interval includes no effect, meaning the estimate should be interpreted as suggestive rather than conclusive.

---

## 2. Cumulative Broadway Career Volume (Count Modelling)

To examine longer-term Broadway participation, the project models total Broadway credit counts.

Because Broadway credit accumulation is highly uneven, with many performers having few or no credits and a small number accumulating many credits, count regression methods are used.

A Poisson regression model was initially estimated. However, the data exhibited overdispersion:

```
Variance / Mean ratio = 1.68
```

Therefore, a Negative Binomial regression model was selected as the preferred specification.

The model:

```
Total Broadway Credits ~ Jimmy Award Winner Status + Gender
```

produced an estimated winner multiplier of:

```
2.21x expected Broadway credits
```

This suggests that Jimmy Award recognition is associated with greater Broadway credit accumulation within the observed cohort.

---

# Technical Stack

**Language:** Python 3.14

**Core Libraries:**

* `lifelines` — Cox Proportional Hazards and Kaplan–Meier estimation
* `statsmodels` — Poisson and Negative Binomial regression modelling
* `pandas` — data processing and dataset construction
* `matplotlib` — visualisation

---

# Reproducibility

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the analysis pipeline:

```bash
python3 src/main.py
```

The pipeline loads the manually curated dataset, performs feature engineering, estimates statistical models, and generates visual outputs.

---

# Model Limitations & Quantitative Edge Cases

While the models provide useful aggregate insights, artistic careers are complex and cannot be fully represented through Broadway-based metrics alone.

## 1. Small Sample Size

The Jimmy Awards represent a highly selective cohort with only 16 years of available history.

The limited sample size restricts statistical power and increases uncertainty around estimated relationships.

## 2. Multi-Hyphenate Career Paths

The model focuses primarily on Broadway outcomes and does not fully capture success outside the Broadway ecosystem.

For example, Renée Rapp (2018 Winner) transitioned from Broadway into major music and film opportunities. A Broadway-credit-only metric records her as having one Broadway credit and does not capture broader commercial success.

## 3. Credit Volume vs Career Stability

Cumulative Broadway credits provide a useful but incomplete measure of career participation.

A performer who remains with a successful production for many years may receive the same credit count as someone whose production closes quickly, despite different career outcomes.

For example, Tony Moreno (2017 Winner) has worked continuously on *The Book of Mormon* on Broadway from 2022 to present. The dataset records this as one Broadway credit and does not capture sustained employment duration.

## 4. Alternative Professional Markets

The analysis intentionally focuses on Broadway as an institutional benchmark.

This excludes important career pathways including Off-Broadway development, West End theatre, and national tours.

For example, Anna Zavelson (2022 Finalist) has one Broadway credit, but has also worked professionally in other major theatre markets, including playing Christine Daaé in *The Phantom of the Opera* in the West End, which is outside this dataset's measurement framework.

These exclusions create a trade-off: a narrower but more consistent measurement framework.

---

# Conclusion

This project demonstrates how quantitative econometric methods can be applied to complex, highly qualitative industries.

By analysing both **career entry timing** and **cumulative Broadway participation**, the results suggest:

1. Jimmy Award winners and finalists both face substantial barriers entering Broadway, with winner status alone not eliminating the competitive nature of the industry.

2. Winner status is associated with higher long-term Broadway credit accumulation, suggesting that early-career recognition may function as a persistent professional signal.

Ultimately, early-career accolades appear less like an immediate career guarantee and more like one observable indicator within a broader ecosystem of talent, timing, networks, and opportunity.
