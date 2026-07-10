# Methodology

## Research Question

Does Jimmy Award recognition contain measurable information about subsequent Broadway career trajectories?

This project examines whether Jimmy Award winners and finalists differ in two measurable career outcomes:

1. Time until first Broadway debut
2. Accumulated Broadway credits after nomination

The analysis is observational and evaluates associations rather than causal effects. Winning a Jimmy Award is not interpreted as directly causing career success; instead, the project investigates whether early-career recognition functions as a measurable signal associated with later Broadway outcomes.

---

## Dataset Construction

The dataset contains every Jimmy Awards finalist from 2010 to 2026.

Each performer is classified according to:

* Jimmy Award outcome (Winner vs Finalist)
* Nomination year
* Broadway debut status
* Year of Broadway debut
* Total Broadway credits

Broadway career outcomes are measured using publicly available performer credits.

The final analysis cohort includes 113 performers.

Because Jimmy Awards finalists represent a selected group of high-achieving young performers, the analysis compares differences within this cohort rather than attempting to estimate outcomes for the broader population of performers.

---

# Survival Analysis

## Research Question

Do Jimmy Award winners debut on Broadway faster than finalists?

## Outcome

The survival outcome is time from first Jimmy Award nomination to first Broadway debut.

Performers who had not made a Broadway debut by 2026 are treated as right-censored observations. This allows performers with different observation periods to be included without assuming that non-debuting performers will never enter Broadway.

## Models

Three survival methods are used:

### Kaplan–Meier Estimation

Kaplan–Meier estimation is used to estimate the probability that a performer has not yet made a Broadway debut over time.

### Log-Rank Test

The log-rank test compares estimated survival curves between Jimmy Award winners and finalists to assess whether the timing of Broadway entry differs between groups.

### Cox Proportional Hazards Regression

A Cox proportional hazards model estimates the relationship between Jimmy Award status and the rate of Broadway debut while controlling for gender.

The model specification is:

```
Broadway Debut Hazard ~ Jimmy Award Winner Status + Gender
```

The proportional hazards assumption is assessed using statistical diagnostics. The assumption was not violated for Jimmy Award winner status, although gender showed evidence of possible non-proportionality. Therefore, interpretation focuses primarily on the winner coefficient.

---

# Count Regression

## Research Question

Do Jimmy Award winners accumulate more Broadway credits after nomination?

## Outcome

The outcome variable is the total number of unique Broadway credits accumulated by each performer.

Because Broadway credit accumulation is a count outcome with many performers having few or no credits, count regression models are used.

## Model Selection

A Poisson regression model was initially estimated:

```
Total Broadway Credits ~ Jimmy Award Winner Status + Gender
```

The winner coefficient was exponentiated to provide an interpretable multiplicative effect.

However, Poisson regression assumes that the variance of the outcome is approximately equal to its mean. The dataset exhibited overdispersion:

```
Variance / Mean ratio = 1.68
```

indicating that Broadway credit counts were more dispersed than the Poisson model assumes.

Therefore, a Negative Binomial regression was estimated as the preferred specification. Negative Binomial regression allows additional variation in count outcomes and is more appropriate for highly uneven career distributions.

Model specification:

```
Total Broadway Credits ~ Jimmy Award Winner Status + Gender
```

The exponentiated winner coefficient is interpreted as the estimated multiplier in expected Broadway credit counts, holding gender constant.

---

# Model Interpretation

All regression results are interpreted as associations rather than causal effects.

For example, a higher estimated Broadway credit count among Jimmy Award winners does not imply that winning directly produces additional Broadway opportunities. Instead, it suggests that Jimmy Award recognition is associated with measurable differences in observed career trajectories.

---

# Limitations

This analysis has several limitations:

* The observational design prevents causal interpretation.
* The sample size is limited, reducing statistical power and increasing uncertainty around estimates.
* Jimmy Award finalists represent a selected group of high-achieving performers, limiting generalisation beyond this population.
* Broadway credits represent only one dimension of career success and do not capture other outcomes such as regional theatre, touring, recording, television, film, or creative roles.
* Important factors such as training background, representation, geography, industry connections, and prior professional experience are not included.
* Jimmy Award recognition may itself reflect pre-existing advantages or opportunities rather than an independent driver of later outcomes.
