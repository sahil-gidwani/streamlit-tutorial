import numpy as np
import pandas as pd
import streamlit as st
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from common import load_events


st.set_page_config(page_title="xG Lab", layout="wide")
st.title("Expected Goals (xG) Lab")
st.caption("Module 5 demo app")

events = load_events().copy()
model_df = events[["distance", "angle", "body_part", "play_type", "is_goal"]].dropna()

X = model_df[["distance", "angle", "body_part", "play_type"]]
y = model_df["is_goal"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

pre = ColumnTransformer(
    [
        ("num", StandardScaler(), ["distance", "angle"]),
        ("cat", OneHotEncoder(handle_unknown="ignore"), ["body_part", "play_type"]),
    ]
)

clf = Pipeline([("pre", pre), ("lr", LogisticRegression(max_iter=1000))])
clf.fit(X_train, y_train)

y_prob = clf.predict_proba(X_test)[:, 1]
auc = roc_auc_score(y_test, y_prob)

m1, m2 = st.columns(2)
m1.metric("Model AUC", f"{auc:.3f}")
m2.metric("Samples", int(len(model_df)))

st.subheader("Shot Simulator")
distance = st.slider("Distance", min_value=5.0, max_value=30.0, value=12.0, step=0.5)
angle = st.slider("Angle", min_value=0.2, max_value=1.4, value=0.8, step=0.05)
body_part = st.selectbox("Body Part", sorted(model_df["body_part"].unique()))
play_type = st.selectbox("Play Type", sorted(model_df["play_type"].unique()))

sample = pd.DataFrame(
    [
        {
            "distance": distance,
            "angle": angle,
            "body_part": body_part,
            "play_type": play_type,
        }
    ]
)
shot_xg = clf.predict_proba(sample)[0, 1]
st.success(f"Predicted xG for this shot profile: {shot_xg:.3f}")

st.subheader("Model Caveats")
st.markdown(
    """
- This is a didactic toy model with limited features.
- Real xG models include richer context (pressure, keeper position, pass type, game state).
- Use this for communication and prototyping, not final performance analytics.
"""
)
