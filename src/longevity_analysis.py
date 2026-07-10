import pandas as pd
import numpy as np
import statsmodels.formula.api as smf


def run_longevity_analysis():

    # 1. Load the dataset
    df = pd.read_excel('data/Jimmy Awards Dataset NEW.xlsx')

    # 2. Prepare variables
    # Map Y/N to 1/0
    df['Ever_Winner_Num'] = df['Ever_Winner'].map({'Y': 1, 'N': 0})
    df['Gender_Actress'] = (df['Gender'] == 'Actress').astype(int)

    print("="*55)
    print("   RUNNING LONGEVITY ANALYSIS (POISSON REGRESSION)")
    print("="*55)

    # 3. Fit a Poisson Regression Model
    # This models the count of Total Broadway Credits based on Winner Status and Gender
    model = smf.poisson('Total_Broadway_Credits ~ Ever_Winner_Num + Gender_Actress', data=df).fit()

    # 4. Print the professional statistical summary table
    print(model.summary())

    # 5. Poisson robustness check
    mean_credits = df['Total_Broadway_Credits'].mean()
    variance_credits = df['Total_Broadway_Credits'].var()

    print("\n" + "="*55)
    print("   POISSON DISPERSION CHECK")
    print("="*55)
    print(f"Mean credits: {mean_credits:.2f}")
    print(f"Variance credits: {variance_credits:.2f}")
    print(f"Variance / Mean ratio: {variance_credits / mean_credits:.2f}")

    print("\n" + "="*55)
    print("   RUNNING NEGATIVE BINOMIAL REGRESSION")
    print("="*55)

    nb_model = smf.negativebinomial(
        'Total_Broadway_Credits ~ Ever_Winner_Num + Gender_Actress',
        data=df
    ).fit()

    print(nb_model.summary())

    print("\nMODEL COMPARISON")
    print("-"*55)

    print(f"Poisson AIC: {model.aic:.2f}")
    print(f"Negative Binomial AIC: {nb_model.aic:.2f}")

    # 6. Calculate real-world multiplier effects

    print("\n" + "="*55)
    print("   EFFECT SIZE INTERPRETATION")
    print("="*55)

    # Poisson multiplier
    poisson_winner_coef = model.params['Ever_Winner_Num']
    poisson_multiplier = np.exp(poisson_winner_coef)

    print(f"Poisson Winner Multiplier: {poisson_multiplier:.2f}x")

    # Negative Binomial multiplier
    nb_winner_coef = nb_model.params["Ever_Winner_Num"]
    nb_multiplier = np.exp(nb_winner_coef)

    print(f"Negative Binomial Winner Multiplier: {nb_multiplier:.2f}x")

    # Negative Binomial confidence interval
    nb_conf = nb_model.conf_int().loc["Ever_Winner_Num"]

    nb_lower = np.exp(nb_conf[0])
    nb_upper = np.exp(nb_conf[1])

    print(
        f"Negative Binomial 95% CI: {nb_lower:.2f}x - {nb_upper:.2f}x"
    )

    print("="*55)