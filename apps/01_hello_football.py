import streamlit as st

from common import load_events, load_matches


st.set_page_config(page_title="Hello Football", layout="wide")
st.title("Football Analytics: Hello Streamlit")
st.caption("Module 1 demo app")

matches = load_matches()
events = load_events()

teams = sorted(set(matches["home_team"]).union(set(matches["away_team"])))
selected_team = st.sidebar.selectbox(
    "Team", teams, index=teams.index("Demo FC") if "Demo FC" in teams else 0
)

team_matches = matches[
    (matches["home_team"] == selected_team) | (matches["away_team"] == selected_team)
].copy()
team_events = events[events["team"] == selected_team].copy()

if team_matches.empty:
    st.warning("No matches found for selected team.")
    st.stop()

avg_xg_for = team_matches.apply(
    lambda r: r["home_xg"] if r["home_team"] == selected_team else r["away_xg"], axis=1
).mean()

goals_for = team_matches.apply(
    lambda r: r["home_goals"] if r["home_team"] == selected_team else r["away_goals"],
    axis=1,
).sum()

shots = len(team_events)
conversion = (team_events["is_goal"].sum() / max(shots, 1)) * 100

c1, c2, c3, c4 = st.columns(4)
c1.metric("Matches", int(len(team_matches)))
c2.metric("Goals", int(goals_for))
c3.metric("Avg xG For", f"{avg_xg_for:.2f}")
c4.metric("Shot Conversion", f"{conversion:.1f}%")

trend = team_matches[["date"]].copy()
trend["xg_for"] = team_matches.apply(
    lambda r: r["home_xg"] if r["home_team"] == selected_team else r["away_xg"], axis=1
)
trend = trend.sort_values("date").set_index("date")

left, right = st.columns([2, 1])
left.subheader("xG Trend")
left.line_chart(trend["xg_for"])

right.subheader("Quick Notes")
right.markdown(
    """
- Use the sidebar to switch teams and compare trends.
- KPI cards summarize outcomes and chance creation.
- The table below provides match-level context.
"""
)

st.subheader("Recent Matches")
st.dataframe(
    team_matches.sort_values("date", ascending=False), use_container_width=True
)
