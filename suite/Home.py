import streamlit as st

from common import load_events, load_matches, load_players


st.set_page_config(page_title="Football Analytics Suite", layout="wide")
st.title("Football Analytics Suite")
st.caption("Module 5 multipage app")

if "selected_team" not in st.session_state:
    st.session_state.selected_team = "Demo FC"

matches = load_matches()
events = load_events()
players = load_players()

teams = sorted(set(matches["home_team"]).union(set(matches["away_team"])))
team = st.sidebar.selectbox(
    "Team", teams, index=teams.index(st.session_state.selected_team)
)
st.session_state.selected_team = team

team_matches = matches[(matches["home_team"] == team) | (matches["away_team"] == team)]
team_events = events[events["team"] == team]
team_players = players[players["team"] == team]

c1, c2, c3 = st.columns(3)
c1.metric("Matches", int(len(team_matches)))
c2.metric("Shots", int(len(team_events)))
c3.metric("Squad Entries", int(len(team_players)))

st.markdown("### Navigation")
st.page_link("pages/1_Match_Analysis.py", label="Match Analysis")
st.page_link("pages/2_Scouting.py", label="Scouting")
st.page_link("pages/3_xG_Lab.py", label="xG Lab")

st.info(
    "Use the sidebar team filter, then jump across pages to keep context consistent."
)
