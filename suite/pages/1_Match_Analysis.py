import plotly.express as px
import streamlit as st

from common import load_events, load_matches


st.title("Match Analysis")

team = st.session_state.get("selected_team", "Demo FC")
matches = load_matches()
events = load_events()

team_matches = matches[
    (matches["home_team"] == team) | (matches["away_team"] == team)
].sort_values("date")

if team_matches.empty:
    st.warning("No matches available for selected team.")
    st.stop()

latest = team_matches.iloc[-1]
match_id = int(latest["match_id"])
match_events = events[events["match_id"] == match_id]

st.subheader(f"Latest Match: {latest['home_team']} vs {latest['away_team']}")

timeline = match_events.groupby(["minute", "team"], as_index=False)["xg"].sum()
fig = px.bar(timeline, x="minute", y="xg", color="team", barmode="group")
st.plotly_chart(fig, use_container_width=True)

st.dataframe(
    match_events[["minute", "team", "player", "outcome", "xg"]],
    use_container_width=True,
)
