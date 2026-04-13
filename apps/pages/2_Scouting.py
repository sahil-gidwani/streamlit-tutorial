import streamlit as st

from common import load_players


st.title("Scouting")

team = st.session_state.get("selected_team", "Demo FC")
players = load_players()

non_team = players[players["team"] != team].copy()
non_team["xg_p90"] = (non_team["xg"] / non_team["minutes"].clip(lower=1)) * 90
non_team["xa_p90"] = (non_team["xa"] / non_team["minutes"].clip(lower=1)) * 90

position = st.selectbox("Position", sorted(non_team["position"].unique()))
min_minutes = st.slider("Min minutes", 500, 2500, 1500, step=50)

shortlist = non_team[
    (non_team["position"] == position) & (non_team["minutes"] >= min_minutes)
]
shortlist = shortlist.sort_values(["xg_p90", "xa_p90"], ascending=False)

st.dataframe(
    shortlist[["player", "team", "position", "age", "minutes", "xg_p90", "xa_p90"]],
    use_container_width=True,
)

st.download_button(
    "Download shortlist",
    data=shortlist.to_csv(index=False),
    file_name="scouting_shortlist.csv",
    mime="text/csv",
)
