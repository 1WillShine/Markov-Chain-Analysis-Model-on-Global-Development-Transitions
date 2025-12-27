import streamlit as st
import pandas as pd
import plotly.express as px

from models.scoring import dev_stage
from models.markov import build_transition_matrix
from app.visuals import choropleth, radar_chart

st.set_page_config("Global Development Dynamics", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("data/polished/final_polished_dataset.csv")
    df["dev_stage"] = df["dev_score"].apply(dev_stage)
    return df

df = load_data()

tab1, tab2, tab3 = st.tabs([
    "🌍 Global Landscape",
    "📊 Country Deep Dive",
    "🔁 Probabilistic Transitions"
])

# -------- TAB 1 --------
with tab1:
    st.header("Global Development Landscape")
    latest = df.sort_values("Year").groupby("Country Code").tail(1)
    st.plotly_chart(choropleth(latest), use_container_width=True)

# -------- TAB 2 --------
with tab2:
    country = st.selectbox("Select Country", sorted(df["Country Name"].unique()))
    country_df = df[df["Country Name"] == country]
    latest_row = country_df.sort_values("Year").iloc[-1]

    st.subheader(f"{country} — Development Profile")
    st.metric("Development Stage", latest_row["dev_stage"])
    st.plotly_chart(radar_chart(latest_row), use_container_width=True)

    metrics = [
        "income_num", "gdp_growth_num", "inequality_num",
        "inflation_num", "life_exp_num", "poverty_num", "school_enroll_num"
    ]

    insight = pd.DataFrame({
        "Metric": metrics,
        "Score": latest_row[metrics]
    }).sort_values("Score")

    st.markdown("### 🚨 Bottlenecks")
    st.dataframe(insight.head(2))

    st.markdown("### 💪 Strengths")
    st.dataframe(insight.tail(2))

# -------- TAB 3 --------
with tab3:
    st.header("Development Transition Dynamics")

    P = build_transition_matrix(df)

    fig = px.imshow(
        P,
        text_auto=".2f",
        color_continuous_scale="Blues"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Country-Specific Transition")

    current = latest_row["dev_stage"]
    row = P.loc[current]

    prob_df = pd.DataFrame({
        "Next Stage": row.index,
        "Probability": row.values
    })

    fig2 = px.bar(
        prob_df,
        x="Next Stage",
        y="Probability",
        text_auto=".2f"
    )
    st.plotly_chart(fig2, use_container_width=True)
