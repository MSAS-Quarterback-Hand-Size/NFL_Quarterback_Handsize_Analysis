# NFL Quarterback Hand Size Analysis

This repository contains code and analysis for exploring the **hand sizes of NFL quarterbacks** and their relationships to other performance metrics and characteristics.

Hand size — measured at events such as the NFL Combine — has been a topic of interest among fans and analysts alike. While widely discussed as a physical attribute for quarterbacks, its actual impact on performance is debated. This analysis seeks to quantify and visualize hand size trends across quarterbacks using data science techniques.

## Table of Contents

- [Project Overview](#project-overview)  
- [Dataset](#dataset)  
- [Analysis](#analysis)  
- [How to Run](#how-to-run)  
- [Results](#results)  
- [Tools & Libraries](#tools--libraries)  
- [Contributing](#contributing)  
- [License](#license)

## Project Overview

This project:

- Collects quarterback hand size data along with relevant performance metrics.
- Cleans and preprocesses the data for analysis.
- Generates visualizations and statistical summaries to explore patterns.
- Tests hypotheses about relationships between hand size and performance in various contexts.

The NFL Combine measurement of hand size is frequently discussed among draft analysts and fans, even though statistical evidence for its impact remains mixed. :contentReference[oaicite:0]{index=0}

## Dataset

The repository includes (or links to) the data sources used for the analysis. Typical contents may include:

- `data/hand_sizes.csv` — Quarterback hand size measurements (combine or official sources).
- `data/stats.csv` — Career performance or combine performance stats.
- External references (if applicable) with links to the original measurement sources.

> Note: Some hand size statistics such as median hand size for drafted quarterbacks have been documented by media sources. :contentReference[oaicite:1]{index=1}

## Analysis

Analysis scripts demonstrate how data is:

1. Cleaned and normalized.
2. Correlated with other variables (e.g., draft pick, passer rating, win percentage).
3. Visualized (e.g., boxplots, scatter plots, trend lines).

Example files:

- `src/clean_data.py` — Data cleaning and preprocessing.
- `src/analysis.ipynb` — Jupyter notebook with exploratory analysis.
- `src/visualizations.py` — Scripts to generate charts.


