import pandas as pd
df_final = pd.read_csv("data/polished/final_polished_dataset.csv")
def assign_dev_state(score):
    if score <= 9:
        return "Least Developed"
    elif score <= 13:
        return "Developing"
    elif score <= 16:
        return "Emerging"
    else:
        return "Advanced"

df_final["dev_score"] = df_final.get("income_num") + df_final.get("gdp_growth_num") + df_final.get("inequality_num")+ df_final.get("inflation_num") + df_final.get("life_exp_num") + df_final.get("poverty_num") + df_final.get("school_enroll_num")
df_final["dev_state"] = df_final["dev_score"].apply(assign_dev_state)

#df_final.groupby("dev_state").count()["Country Name"]

