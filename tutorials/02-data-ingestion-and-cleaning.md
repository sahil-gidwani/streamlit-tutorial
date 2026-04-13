# Module 2: Data Ingestion and Cleaning for Football Data

## Learning Goals
- Load football datasets from CSV and JSON
- Normalize inconsistent columns and data types
- Cache expensive data-loading functions
- Build reusable data prep logic for downstream dashboards

## Football Analytics Context
Event data can be noisy and inconsistent. If your ingestion layer is weak, every dashboard and model downstream becomes unreliable.

## Build: Data Explorer App
Run:
```bash
streamlit run apps/02_data_explorer.py
```

## Data Sources Covered
- Local sample files in `data/`
- Optional extension: StatsBomb open-data JSON files

Reference:
- https://github.com/statsbomb/open-data

## Key Streamlit Patterns
- `st.file_uploader` for ad hoc data
- `@st.cache_data` for deterministic transforms
- `st.warning` and `st.error` for data-quality flags

### Example: Cached Loader
```python
import streamlit as st
import pandas as pd

@st.cache_data(show_spinner=False)
def load_events(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["xg"] = pd.to_numeric(df["xg"], errors="coerce").fillna(0.0)
    df["is_goal"] = df["outcome"].eq("Goal")
    return df
```

## Data Quality Rules to Implement
- Validate required columns: `team`, `player`, `x`, `y`, `event_type`
- Enforce range checks: coordinates should be in known pitch bounds
- Handle missing values explicitly (drop, fill, or flag)
- Standardize category names (`"man utd" -> "Manchester United"`)

## Practice Tasks
1. Add a quality report section with counts of nulls by column.
2. Add a toggle for dropping rows with missing locations.
3. Add a "cleaned preview" and "raw preview" comparison table.
4. Cache both the raw load and cleaned transform steps.

## Interview-Style Demo Talking Points
- Why caching matters for live demos and stakeholder confidence
- Tradeoff between strict cleaning (data loss) and permissive cleaning (noise)
- How to design transparent validation messages

## Next Module
Move to [03-match-dashboard.md](./03-match-dashboard.md) to build your first coach-facing match analysis dashboard.
