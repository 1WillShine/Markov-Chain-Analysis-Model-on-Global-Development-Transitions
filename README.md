🌍 Global Development Dynamics via Markov Chains
================================================

_A Probabilistic Analysis of Country Development Trajectories_

Motivation
----------

Global development is often communicated through static rankings or categorical labels that obscure uncertainty and long-run dynamics. I was interested in whether probabilistic models—specifically Markov chains—could offer a more honest and informative way to understand how countries evolve across development stages over time. This project applies stochastic modeling to global socioeconomic data in order to study development mobility, persistence, and inequality without relying on deterministic predictions.

Project Overview
----------------

This project models global economic development as a discrete-state stochastic process. Rather than assigning countries fixed development labels, I construct a composite development index from World Bank indicators and estimate transition probabilities between development stages using a Markov chain framework. The result is a system that describes how countries tend to advance, stagnate, or regress probabilistically over time, and what the implied long-run global distribution of development looks like under current dynamics.

Data
----

The analysis uses World Bank Open Data covering over 200 countries across multiple decades. Indicators span income and growth, health and education, inequality and poverty, and macroeconomic stability. Missing values are handled using income-conditioned median imputation to preserve cross-country comparability while minimizing bias.

Methodology
-----------

Each socioeconomic indicator is normalized into quintile-based ordinal categories to ensure comparability across countries and time. These encoded metrics are summed into a composite development score, which is then mapped into four ordered development states ranging from least developed to advanced. Year-over-year changes in state assignments are used to estimate a transition probability matrix under the Markov assumption that future states depend only on the current state. From this matrix, I compute conditional transition probabilities and the stationary distribution to analyze long-run system behavior.

Model Interpretation
--------------------

The Markov chain does not predict individual country outcomes. Instead, it characterizes the structure of global development dynamics by quantifying persistence, upward mobility, and regression risk across states. The stationary distribution provides insight into long-run inequality and development traps implied by current transition patterns, while conditional probabilities allow country-level analysis without overclaiming predictive certainty.

Results & Insights
------------------

The model reveals strong persistence in development states and asymmetric mobility, with upward transitions occurring less frequently than stagnation. Certain states behave as near-absorbing, contributing to long-run inequality in the stationary distribution. Regional differences remain visible even in equilibrium, suggesting structural rather than transitory disparities. Overall, the project demonstrates how probabilistic models can describe macro social systems more responsibly than static rankings.

Technical Stack
---------------

The project is implemented in Python using pandas and NumPy for data processing, Plotly for visualization, and Streamlit for interactive deployment. Transition matrices and stationary distributions are computed using standard linear algebra techniques.

Limitations
-----------

The model does not establish causality, incorporate policy shocks, or allow for time-varying transition dynamics. Equal weighting of indicators and the Markov assumption are simplifications made for interpretability rather than realism.

How to Run
----------

Install dependencies using pip install -r requirements.txt, then launch the dashboard with streamlit run streamlit\_app/app.py.
