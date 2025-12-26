import streamlit as st
import pandas as pd
import plotly.express as px
from markov import build_transition_matrix
from data_loader import df_final
st.set_page_config(page_title="Global Development Dynamics", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("data/polished/final_polished_dataset.csv")

df = df_final

# Sidebar
st.sidebar.title("Controls")
country = st.sidebar.selectbox(
    "Select a Country",
    sorted(df["Country Name"].unique())
)

year_range = st.sidebar.slider(
    "Year Range",
    int(df["Year"].min()),
    int(df["Year"].max()),
    (2015, 2024)
)

df_filtered = df[
    (df["Year"].between(*year_range))
]

# Tabs
tab1, tab2, tab3 = st.tabs(["🌍 Global Overview", "📊 Country Analysis", "🔁 Markov Dynamics"])

# -------- Global Overview --------
with tab1:
    st.header("Global Development Overview")

    latest = df_filtered.sort_values("Year").groupby("Country Code").tail(1)

    fig = px.choropleth(
        latest,
        locations="Country Code",
        color="dev_score",
        hover_name="Country Name",
        color_continuous_scale="Viridis"
    )
    st.plotly_chart(fig, width='stretch')

# -------- Country Analysis --------
with tab2:
    st.header(f"{country} — Development Profile")

    country_df = df_filtered[df_filtered["Country Name"] == country]

    metrics = [
        "income", "gdp_growth", "inequality",
        "inflation", "life_exp", "poverty", "school_enroll"
    ]

    radar_df = country_df.sort_values("Year").iloc[-1][metrics].reset_index()
    radar_df.columns = ["metric", "value"]

    fig = px.line_polar(
        radar_df,
        r="value",
        theta="metric",
        line_close=True
    )

    st.plotly_chart(fig, width='stretch')

# -------- Markov Analysis --------
with tab3:
    st.header("Development Transition Dynamics")

    P = build_transition_matrix(df_filtered)

    fig = px.imshow(
        P,
        text_auto=".2f",
        color_continuous_scale="Blues"
    )

    st.plotly_chart(fig, width='stretch')
