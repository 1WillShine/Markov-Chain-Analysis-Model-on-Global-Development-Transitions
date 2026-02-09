import pandas as pd
import numpy as np
from models.scoring import dev_stage

STAGES = ["Least Developed(D)", "Developing(C)", "Emerging(B)", "Advanced(A)"]

def build_transition_matrix(df):
    df = df.sort_values(["Country Code", "Year"])
    df["stage"] = df["dev_score"].apply(dev_stage)

    transitions = []

    for country, g in df.groupby("Country Code"):
        prev = g["stage"].shift(1)
        curr = g["stage"]
        mask = prev.notna()
        transitions += list(zip(prev[mask], curr[mask]))

    T = pd.DataFrame(0, index=STAGES, columns=STAGES)

    for i, j in transitions:
        T.loc[i, j] += 1

    return T.div(T.sum(axis=1), axis=0).fillna(0)
