import streamlit as st

from common import load_events, load_matches, load_players


st.set_page_config(page_title="Football Analytics Suite", layout="wide")
st.title("Football Analytics Suite")
st.caption("Module 5 multipage app")

st.html(
    """
        <style>
            .suite-hero {
                padding: 1rem 1.1rem;
                border-radius: 14px;
                background: linear-gradient(120deg, #eaf4ff 0%, #f8f4ff 100%);
                border: 1px solid #dbe6f3;
                margin-bottom: 0.9rem;
            }
            .suite-hero h3 {
                margin: 0 0 0.3rem 0;
                color: #12385b;
                font-size: 1.1rem;
            }
            .suite-hero p {
                margin: 0;
                color: #35526d;
                font-size: 0.95rem;
            }
            .suite-tags {
                margin-top: 0.6rem;
                display: flex;
                gap: 0.45rem;
                flex-wrap: wrap;
            }
            .suite-tag {
                font-size: 0.78rem;
                background: #ffffff;
                border: 1px solid #d7e3ef;
                color: #244967;
                border-radius: 999px;
                padding: 0.2rem 0.55rem;
            }
        </style>

        <section class="suite-hero">
            <h3>Welcome to the Football Analytics Suite</h3>
            <p>
                Explore team performance, match-level context, scouting filters, and xG simulation
                in one guided app flow.
            </p>
            <div class="suite-tags">
                <span class="suite-tag">Match Analysis</span>
                <span class="suite-tag">Scouting</span>
                <span class="suite-tag">xG Lab</span>
            </div>
        </section>
        """
)

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
