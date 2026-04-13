from pathlib import Path

import pandas as pd
import streamlit as st


DATA_DIR = Path(__file__).resolve().parents[1] / "data"


@st.cache_data(show_spinner=False)
def load_matches() -> pd.DataFrame:
    df = pd.read_csv(DATA_DIR / "matches.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df


@st.cache_data(show_spinner=False)
def load_events() -> pd.DataFrame:
    df = pd.read_csv(DATA_DIR / "events.csv")
    df["is_goal"] = pd.to_numeric(df["is_goal"], errors="coerce").fillna(0).astype(int)
    df["xg"] = pd.to_numeric(df["xg"], errors="coerce").fillna(0.0)
    df["distance"] = pd.to_numeric(df["distance"], errors="coerce").fillna(
        df["distance"].median()
    )
    df["angle"] = pd.to_numeric(df["angle"], errors="coerce").fillna(
        df["angle"].median()
    )
    return df


@st.cache_data(show_spinner=False)
def load_players() -> pd.DataFrame:
    df = pd.read_csv(DATA_DIR / "players.csv")
    numeric_cols = [
        "age",
        "minutes",
        "shots",
        "key_passes",
        "progressive_passes",
        "tackles_won",
        "xg",
        "xa",
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    return df
