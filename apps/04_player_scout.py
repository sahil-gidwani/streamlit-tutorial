import numpy as np
import pandas as pd
import streamlit as st

from common import load_players


st.set_page_config(page_title="Player Scouting", layout="wide")
st.title("Player Scouting Dashboard")
st.caption("Module 4 demo app")

players = load_players()

st.sidebar.header("Filters")
positions = sorted(players["position"].dropna().unique().tolist())
leagues = sorted(players["league"].dropna().unique().tolist())

position = st.sidebar.selectbox(
    "Position", positions, index=positions.index("ST") if "ST" in positions else 0
)
league = st.sidebar.selectbox("League", leagues)
max_age = int(st.sidebar.slider("Max age", 18, 35, 28))
min_minutes = int(st.sidebar.slider("Min minutes", 300, 2500, 1500, step=50))

filtered = players[
    (players["position"] == position)
    & (players["league"] == league)
    & (players["age"] <= max_age)
    & (players["minutes"] >= min_minutes)
].copy()

metric_cols = ["shots", "key_passes", "progressive_passes", "tackles_won", "xg", "xa"]
for c in metric_cols:
    filtered[f"{c}_p90"] = (filtered[c] / filtered["minutes"].clip(lower=1)) * 90

if filtered.empty:
    st.warning("No players match current filters.")
    st.stop()

score_cols = [
    f"{c}_p90" for c in ["shots", "key_passes", "progressive_passes", "xg", "xa"]
]
for c in score_cols:
    mu = filtered[c].mean()
    sigma = filtered[c].std(ddof=0) if filtered[c].std(ddof=0) > 0 else 1.0
    filtered[f"z_{c}"] = (filtered[c] - mu) / sigma

filtered["profile_score"] = filtered[[f"z_{c}" for c in score_cols]].mean(axis=1)
shortlist = filtered.sort_values("profile_score", ascending=False)

st.subheader("Shortlist")
st.dataframe(
    shortlist[["player", "team", "age", "minutes", "profile_score"] + score_cols],
    use_container_width=True,
)

st.download_button(
    "Download shortlist",
    data=shortlist.to_csv(index=False),
    file_name="player_shortlist.csv",
    mime="text/csv",
)

st.subheader("Interpretation")
st.markdown(
    """
- Per-90 values normalize for minutes played.
- `profile_score` is a simple demo score from z-normalized attacking metrics.
- In production, replace with role-specific weighted scoring.
"""
)
