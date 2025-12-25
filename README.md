# Global Development Dynamics via Markov Chains

## Overview
This project models long-run development dynamics of countries using a probabilistic framework.
Rather than relying on static development labels, I construct a composite development index and
analyze how countries transition between development states over time using Markov chains.

## Data
- Source: World Bank Open Data
- Coverage: 200+ countries, multiple decades
- Domains:
  - Income & growth
  - Health & education
  - Inequality & poverty
  - Inflation & macro stability

## Feature Engineering
Each country-year observation is categorized into five ordinal levels:
Very Low → Very High

Metrics used:
- GNI (income)
- GDP growth
- Income inequality
- Inflation (reverse coded)
- Life expectancy
- Poverty (reverse coded)
- School enrollment parity

Missing values are handled via income-conditioned median imputation.

## Composite Development Index
Each metric is encoded numerically (0–4) and summed to produce a development score:
- Min: 0
- Max: 28

States:
- Least Developed
- Developing
- Emerging
- Advanced

## Markov Chain Modeling
I estimate a transition probability matrix describing how countries move between
development states across time.

This allows analysis of:
- Development traps
- Upward mobility probabilities
- Persistence and regression
- Regional transition differences

## Visualization & App
An interactive Streamlit dashboard allows users to:
- Explore global development patterns
- Analyze individual countries
- Visualize transition probabilities
- Compare regions dynamically

## How to Run
```bash
pip install -r requirements.txt
streamlit run streamlit_app/app.py

