# Module 1: Streamlit Fundamentals for Football Analytics

## Learning Goals
- Understand Streamlit's rerun model and widget-driven interaction
- Build your first football-themed app with KPIs and charts
- Learn baseline layout patterns: sidebar filters, columns, tabs, metrics

## Why This Matters in Football Analytics
Football analytics products are consumed by non-technical stakeholders. Streamlit helps you convert analysis notebooks into interactive tools quickly.

## Prerequisites
- Python basics
- `pip install -r requirements.txt`

## Build: Hello Football App
Run:
```bash
streamlit run apps/01_hello_football.py
```

### Core Concepts Used
- `st.set_page_config`
- `st.sidebar.*` filters
- `st.metric` KPI tiles
- `st.line_chart` for trend visualization
- `st.dataframe` for table inspection

### Minimal Starter Snippet
```python
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Football Analytics 101", layout="wide")
st.title("Football Analytics Demo")

df = pd.DataFrame({
    "matchday": [1, 2, 3, 4, 5],
    "xg_for": [1.1, 1.4, 0.9, 2.2, 1.8],
})

st.metric("Avg xG", round(df["xg_for"].mean(), 2))
st.line_chart(df.set_index("matchday")["xg_for"])
```

## Practice Tasks
1. Add a team selector in the sidebar.
2. Add two extra KPIs: goals scored and pass completion.
3. Add a tab for "Raw Match Data" and another for "Trend View".
4. Add a `st.download_button` for CSV export.

## Discussion Prompts for Demo Audience
- Why xG is better than just goals for short-term performance tracking
- How interactive filters reduce back-and-forth with coaching staff

## Checklist
- App runs without errors
- Sidebar filters update all charts
- KPI cards remain readable on laptop projector resolution

## Next Module
Continue with [02-data-ingestion-and-cleaning.md](./02-data-ingestion-and-cleaning.md) to load and normalize football event data.
