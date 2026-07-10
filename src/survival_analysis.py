import sys
import subprocess
try:
    import lifelines
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "lifelines"])

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter, CoxPHFitter
from lifelines.statistics import logrank_test


def run_survival_analysis():

    # 1. Load the pristine dataset
    df = pd.read_excel('data/Jimmy Awards Dataset NEW.xlsx')

    # 2. Data Cleaning & Encoding
    # Map 'Y'/'N' to 1/0 so Python can run mathematical equations on them
    df['Ever_Winner'] = df['Ever_Winner'].map({'Y': 1, 'N': 0})

    # 3. Feature Engineering: Compute Time-to-Event (Timeline)
    # If they debuted, timeline = Debut Year - Nominated Year
    # If they haven't debuted, timeline = 2026 (current year) - Nominated Year
    df['Timeline_Years'] = np.where(
        df['Broadway_Debut'] == 1,
        df['Year_Of_Broadway_Debut'] - df['First_Year_Nominated'],
        2026 - df['First_Year_Nominated']
    )

    # 4. Initialize Kaplan-Meier Fitters
    kmf_winners = KaplanMeierFitter()
    kmf_finalists = KaplanMeierFitter()

    # Split our data into two cohorts
    winners = df[df['Ever_Winner'] == 1]
    finalists = df[df['Ever_Winner'] == 0]

    # 5. Fit the survival models
    # kmf.fit(durations, event_observed)
    kmf_winners.fit(durations=winners['Timeline_Years'], event_observed=winners['Broadway_Debut'], label='Jimmy Winners')
    kmf_finalists.fit(durations=finalists['Timeline_Years'], event_observed=finalists['Broadway_Debut'], label='Jimmy Finalists')

    from lifelines.statistics import logrank_test

    # 6. Run the statistical test comparing the two groups
    results = logrank_test(
        winners['Timeline_Years'], finalists['Timeline_Years'],
        event_observed_A=winners['Broadway_Debut'], event_observed_B=finalists['Broadway_Debut']
    )

    print("\n--- STATISTICAL LOG-RANK TEST RESULTS ---")
    print(f"P-value: {results.p_value:.4f}")
    print(f"Is it statistically significant (p < 0.05)? {results.p_value < 0.05}")

    # 7. Plotting the results
    plt.figure(figsize=(10, 6))

    # Plot curves with confidence intervals
    kmf_winners.plot_survival_function(ci_show=True)
    kmf_finalists.plot_survival_function(ci_show=True)

    # Graph annotations for standard quant presentation style
    plt.title('Time to Broadway Debut: Jimmy Winners vs. Finalists', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Years Elapsed Since Jimmy Award Nomination', fontsize=12)
    plt.ylabel('Probability of NOT Having Debuted Yet', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xlim(0, 16) # 16 years max timeline (2010 to 2026)
    plt.ylim(0, 1.05)

    # Show the plot window!
    plt.tight_layout()
    plt.savefig('plots/broadway_survival_chart.png', dpi=300)
    print("\n[SUCCESS] Survival chart saved as 'broadway_survival_chart.png' in your project folder!")

    from lifelines import CoxPHFitter

    print("\n" + "="*40)
    print("   RUNNING MULTIVARIATE COX REGRESSION")
    print("="*40)

    # We need to select the columns for the regression model
    # To keep the model stable with a small sample, we will look at Winner, Gender, and Timeline
    regression_df = df[['Timeline_Years', 'Broadway_Debut', 'Ever_Winner', 'Gender']].copy()

    # One-hot encode the 'Gender' column (convert Actor/Actress to 1s and 0s)
    regression_df = pd.get_dummies(regression_df, columns=['Gender'], drop_first=True)

    # Convert boolean columns to integers so the model can process them
    for col in regression_df.columns:
        if regression_df[col].dtype == 'bool':
            regression_df[col] = regression_df[col].astype(int)

    # Fit the Cox Model
    cph = CoxPHFitter()
    cph.fit(regression_df, duration_col='Timeline_Years', event_col='Broadway_Debut')

    # Print the professional summary table
    cph.print_summary()
