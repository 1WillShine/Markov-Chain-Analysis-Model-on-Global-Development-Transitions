import pandas as pd
import numpy as np

STATES = ["Least Developed", "Developing", "Emerging", "Advanced"]


def build_transition_matrix(df, country_col="Country Code", year_col="Year", state_col="dev_state"):
    """
    Builds a Markov transition matrix P(i -> j)
    """

    df_sorted = df.sort_values([country_col, year_col])

    transitions = []

    for _, group in df_sorted.groupby(country_col):
        states = group[state_col].values
        for i in range(len(states) - 1):
            if pd.notna(states[i]) and pd.notna(states[i + 1]):
                transitions.append((states[i], states[i + 1]))

    transition_df = pd.DataFrame(transitions, columns=["from", "to"])

    matrix = (
        transition_df
        .groupby(["from", "to"])
        .size()
        .unstack(fill_value=0)
        .reindex(index=STATES, columns=STATES, fill_value=0)
    )

    transition_matrix = matrix.div(matrix.sum(axis=1), axis=0)

    return transition_matrix
