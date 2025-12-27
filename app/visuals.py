import plotly.express as px
import pandas as pd

STAGE_COLORS = {
    "Least Developed": "#d73027",
    "Developing": "#fc8d59",
    "Emerging": "#91bfdb",
    "Advanced": "#1a9850"
}

def choropleth(latest):
    fig = px.choropleth(
        latest,
        locations="Country Code",
        color="dev_stage",
        hover_name="Country Name",
        color_discrete_map=STAGE_COLORS,
        projection="natural earth"
    )
    fig.update_layout(height=650)
    return fig


def radar_chart(latest_row):
    metrics = [
        "income_num", "gdp_growth_num", "inequality_num",
        "inflation_num", "life_exp_num", "poverty_num", "school_enroll_num"
    ]

    df = pd.DataFrame({
        "metric": metrics,
        "value": latest_row[metrics]
    })

    fig = px.line_polar(
        df,
        r="value",
        theta="metric",
        line_close=True,
        range_r=[0, 4]
    )
    return fig
