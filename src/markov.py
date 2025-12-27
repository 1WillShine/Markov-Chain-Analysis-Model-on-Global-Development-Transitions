import pandas as pd
import numpy as np
from data_loader import df_final
df = df_final
STAGES = ["Least Developed", "Developing", "Emerging", "Advanced"]

def build_transition_matrix(df):
    df = df.sort_values(["Country Code", "Year"])
    #df["stage"] = df["dev_score"].apply(dev_stage)

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
