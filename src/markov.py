import pandas as pd

STAGES = [
    "Least Developed",
    "Developing",
    "Emerging",
    "Advanced"
]

def build_transition_matrix(df):
    df = df.sort_values(["Country Code", "Year"])

    transitions = []

    for _, g in df.groupby("Country Code"):
        prev = g["dev_state"].shift(1)
        curr = g["dev_state"]

        mask = prev.notna()
        transitions.extend(zip(prev[mask], curr[mask]))

    T = pd.DataFrame(0, index=STAGES, columns=STAGES)

    for i, j in transitions:
        if i in STAGES and j in STAGES:
            T.loc[i, j] += 1

    return T.div(T.sum(axis=1), axis=0).fillna(0)

