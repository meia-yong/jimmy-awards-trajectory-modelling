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

    # 5. Calculate the real-world multiplier effect
    winner_coef = model.params['Ever_Winner_Num']
    multiplier = np.exp(winner_coef)
    print("\n" + "="*55)
    print("   REAL-WORLD INTERPRETATION")
    print("="*55)
    print(f"Multiplier Effect: {multiplier:.2f}x")
    print(f"Jimmy Winners are expected to accumulate {((multiplier - 1)*100):.1f}% MORE unique Broadway credits")
    print("than Finalists, holding gender constant.")
    print("="*55)