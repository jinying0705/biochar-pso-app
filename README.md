# biochar-pso-app
A Streamlit app for optimizing biochar experiment using PSO
# biochar-pso-app

A Streamlit web application for optimizing biochar experimental conditions using Particle Swarm Optimization (PSO).

## 🔍 Introduction

This project provides a simple interface to help researchers or engineers **reverse-optimize** biochar experimental parameters based on desired output properties.

Users input:
- A set of input ranges for experimental factors (e.g., temperature, residence time, etc.)
- Desired outputs (e.g., biochar yield, surface area)
- Custom weights for each output

The app uses PSO (Particle Swarm Optimization) to suggest an optimal combination of input parameters.

🚀 Features

- Interactive Streamlit web UI
- Custom weight settings for each output
- Dynamic input range configuration
- PSO-based optimization algorithm
- Optimized output presented with clear metrics

🧠 Algorithms Used

- [Particle Swarm Optimization (PSO)](https://en.wikipedia.org/wiki/Particle_swarm_optimization)
- Regression or surrogate model (XGBoost-based prediction)

🛠️ Installation (Local)

```bash
git clone https://github.com/jinying0705/biochar-pso-app.git
cd biochar-pso-app
pip install -r requirements.txt
streamlit run app.py
