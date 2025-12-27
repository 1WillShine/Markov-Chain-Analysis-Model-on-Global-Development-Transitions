def compute_dev_score(row):
    metrics = [
        "income_num", "gdp_growth_num", "inequality_num",
        "inflation_num", "life_exp_num", "poverty_num", "school_enroll_num"
    ]
    return row[metrics].sum()


def dev_stage(score):
    if score <= 7:
        return "Least Developed"
    elif score <= 12:
        return "Developing"
    elif score <= 17:
        return "Emerging"
    else:
        return "Advanced"
