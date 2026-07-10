# Methodology

## Research Question

Does Jimmy Award recognition correlate with differences in subsequent Broadway career trajectories?

This project examines whether Jimmy Award winners and finalists differ in two measurable outcomes:

1. Time until first Broadway debut
2. Accumulated Broadway credits after nomination

The analysis is observational and evaluates associations rather than causal effects.

---

## Dataset Construction

The dataset contains every Jimmy Awards finalist from 2010 to 2026.

Each performer is classified according to:

- Jimmy Award outcome (Winner vs Finalist)
- Nomination year
- Broadway debut status
- Year of Broadway debut
- Total Broadway credits

Broadway career outcomes are measured using publicly available performer credits.

The analysis cohort includes 113 performers.

---

## Survival Analysis

### Research Question

Do Jimmy Award winners debut on Broadway faster than finalists?

### Outcome

Time from first Jimmy Award nomination to first Broadway debut.

Performers who had not debuted by 2026 are treated as right-censored observations.

### Models

Two survival methods are used:

**Kaplan–Meier Estimation**

Used to estimate the probability that a performer has not yet made a Broadway debut over time.

**Log-Rank Test**

Used to compare survival curves between winners and finalists.

**Cox Proportional Hazards Regression**

Used to estimate the relationship between Jimmy Award status and Broadway debut hazard while controlling for gender.

The proportional hazards assumption is required for interpretation of Cox regression coefficients.

---

## Count Regression

### Research Question

Do Jimmy Award winners accumulate more Broadway credits?

### Outcome

Total number of unique Broadway credits.

### Model

Poisson regression is used to model Broadway credit counts:

Total Broadway Credits ~ Winner Status + Gender

The winner coefficient is exponentiated to provide an interpretable multiplicative effect.

Potential overdispersion is recognised as a limitation of the Poisson specification.

---

## Limitations

This analysis has several limitations:

- Observational design prevents causal interpretation
- Small sample size limits statistical power
- Broadway credits represent only one dimension of career success
- Important factors such as training, representation, geography, and prior experience are not included
- Jimmy Award recognition may itself reflect existing industry advantages