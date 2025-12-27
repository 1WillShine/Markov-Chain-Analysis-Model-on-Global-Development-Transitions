# Global Development Dynamics via Markov Chains
🌍 Global Development Dynamics
------------------------------

**A Probabilistic Analysis of Country Development Trajectories**

### 📌 Project Overview

This project models global economic development as a **stochastic process**, combining socioeconomic indicators with **Markov chain dynamics** to analyze how countries transition between development stages over time.

Unlike static rankings, this system estimates **future development probabilities**, enabling conditional, country-specific insights.

### 🔍 Key Features

*   Composite development index from World Bank data
    
*   Categorical quantile-based normalization
    
*   Country-level radar diagnostics
    
*   Global transition matrix (Markov chain)
    
*   Conditional future-state probabilities
    
*   Interactive Streamlit dashboard
    

### 📊 Indicators Used

*   Income (GNI, Atlas)
    
*   GDP growth
    
*   Inequality (bottom 20% share)
    
*   Inflation (GDP deflator)
    
*   Life expectancy
    
*   Poverty rate ($3/day PPP)
    
*   School enrollment (GPI)
    

### 🧠 Methodology

1.  Continuous indicators → quintile categories (0–4)
    
2.  Composite development score (sum)
    
3.  Mapping scores → development stages
    
4.  Year-over-year transitions → Markov chain
    
5.  Conditional probability inference
    

### 🔁 Markov Model Interpretation

Each country is treated as occupying a discrete development state.Transition probabilities estimate how likely countries are to:

*   Advance
    
*   Stagnate
    
*   Regress
    

This enables **probabilistic forecasting**, not deterministic ranking.

### ⚠️ Model Assumptions

*   Equal weighting of indicators
    
*   Markov property (memoryless transitions)
    
*   Stationary transition probabilities
    
*   Quantile-based normalization
    
*   Missing data imputed conditionally
    

### ❗ Limitations

*   No causal inference
    
*   Policy shocks not modeled
    
*   Data availability varies by country
    
*   Development is multi-dimensional and nonlinear
    

### 🚀 Tech Stack

*   Python, Pandas, NumPy
    
*   Plotly
    
*   Streamlit
    
*   World Bank Open Data
    

### 📈 Possible Extensions

*   Metric-weighted scoring
    
*   Regional transition matrices
    
*   Bayesian updating
    
*   Policy simulation engine
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

