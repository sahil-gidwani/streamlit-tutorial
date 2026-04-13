import pandas as pd
import streamlit as st
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from common import load_events


st.title("xG Lab")

events = load_events().copy()
model_df = events[["distance", "angle", "body_part", "play_type", "is_goal"]].dropna()

X = model_df[["distance", "angle", "body_part", "play_type"]]
y = model_df["is_goal"]

pre = ColumnTransformer(
    [
        ("num", StandardScaler(), ["distance", "angle"]),
        ("cat", OneHotEncoder(handle_unknown="ignore"), ["body_part", "play_type"]),
    ]
)
clf = Pipeline([("pre", pre), ("lr", LogisticRegression(max_iter=1000))])
clf.fit(X, y)

st.markdown("Configure a synthetic shot and estimate conversion probability.")

distance = st.slider("Distance", 5.0, 30.0, 12.0, 0.5)
angle = st.slider("Angle", 0.2, 1.4, 0.8, 0.05)
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
prob = clf.predict_proba(sample)[0, 1]

st.metric("Predicted xG", f"{prob:.3f}")
