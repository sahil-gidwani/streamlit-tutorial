# Streamlit Tutorial Series for Football Analytics

This repository contains a complete, demo-ready Streamlit learning path focused on football analytics use cases.

## What You Get
- An ordered 8-module tutorial series in markdown
- Runnable Streamlit apps mapped to each module
- Sample football datasets for reliable demo execution
- Curated docs, articles, and video links
- A local `skills/` directory with Streamlit agent skills assets

## Repository Structure
- `tutorials/` detailed learning modules and resources
- `apps/` standalone and multipage Streamlit demo apps
- `data/` sample match, event, and player data
- `skills/` local copy of agent skills for experimentation/reference
- `requirements.txt` pinned dependencies for reproducibility

## Start Here
1. Open the full curriculum: `tutorials/00-series-overview.md`
2. Install dependencies and run the first app:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run apps/01_hello_football.py
```

## Run Apps by Module
- Module 1: `streamlit run apps/01_hello_football.py`
- Module 2: `streamlit run apps/02_data_explorer.py`
- Module 3: `streamlit run apps/03_match_dashboard.py`
- Module 4: `streamlit run apps/04_player_scout.py`
- Module 5: `streamlit run apps/05_xg_lab.py`
- Module 6+: `streamlit run apps/Home.py`

## Core Learning Resources
- Streamlit tutorials: https://docs.streamlit.io/develop/tutorials
- Streamlit API reference: https://docs.streamlit.io/develop/api-reference
- Streamlit deployment docs: https://docs.streamlit.io/deploy
- StatsBomb open data: https://github.com/statsbomb/open-data
- mplsoccer docs: https://mplsoccer.readthedocs.io/en/latest/

See the full curated list in `tutorials/resources.md`.