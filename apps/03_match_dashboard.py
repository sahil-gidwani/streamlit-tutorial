import pandas as pd
import plotly.express as px
import streamlit as st

from common import load_events, load_matches


st.set_page_config(page_title="Match Dashboard", layout="wide")
st.title("Match Dashboard")
st.caption("Module 3 demo app")

matches = load_matches().sort_values("date")
events = load_events()

match_options = [
    f"{r.match_id} | {r.home_team} vs {r.away_team} | {r.date.date()}"
    for r in matches.itertuples(index=False)
]
selected = st.sidebar.selectbox(
    "Select Match", match_options, index=len(match_options) - 1
)
match_id = int(selected.split("|")[0].strip())

m = matches[matches["match_id"] == match_id].iloc[0]
me = events[events["match_id"] == match_id].copy()

home_team = m["home_team"]
away_team = m["away_team"]
home_xg = float(m["home_xg"])
away_xg = float(m["away_xg"])

home_goals = int(m["home_goals"])
away_goals = int(m["away_goals"])

st.subheader(f"{home_team} {home_goals} - {away_goals} {away_team}")

k1, k2, k3, k4 = st.columns(4)
k1.metric("Home xG", f"{home_xg:.2f}")
k2.metric("Away xG", f"{away_xg:.2f}")
k3.metric("Total Shots", int(len(me)))
k4.metric("Goals", int(me["is_goal"].sum()))

xg_timeline = me.groupby(["minute", "team"], as_index=False)["xg"].sum()
fig = px.line(
    xg_timeline, x="minute", y="xg", color="team", markers=True, title="xG by Minute"
)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Event Timeline")
st.dataframe(
    me[["minute", "team", "player", "event_type", "outcome", "xg"]].sort_values(
        "minute"
    ),
    use_container_width=True,
)

st.subheader("Coach Notes")
if home_xg > away_xg and home_goals <= away_goals:
    st.info(
        "Process positive, result underwhelming: finishing variance likely played a role."
    )
elif away_xg > home_xg and away_goals <= home_goals:
    st.info("Away side generated better chances but did not convert efficiently.")
else:
    st.info("Chance quality and scoreline were directionally aligned in this match.")
