# Module 5: Multipage Football Analytics App

## Learning Goals
- Organize features into pages for real product feel
- Share state and filters across pages
- Build navigation aligned to user workflows

## Build
Run:
```bash
streamlit run suite/Home.py
```

## Page Architecture in This Repo
- `suite/Home.py`: overview + navigation
- `suite/pages/1_Match_Analysis.py`
- `suite/pages/2_Scouting.py`
- `suite/pages/3_xG_Lab.py`

## Recommended Navigation Flow
1. Club overview and KPIs
2. Match analysis (recent matches)
3. Player scouting shortlist
4. xG lab for what-if simulation

## Shared State Pattern
```python
if "selected_team" not in st.session_state:
    st.session_state.selected_team = "Demo FC"

team = st.sidebar.selectbox("Team", ["Demo FC", "Rival United"],
                            index=0 if st.session_state.selected_team == "Demo FC" else 1)
st.session_state.selected_team = team
```

## Practice Tasks
1. Add a season selector that persists across pages.
2. Add URL query param support for deep links.
3. Add a global reset filters button.
4. Add role-based page visibility (coach/scout/analyst demo mode).

## Suggested User Flow
"Start with club KPIs, move into match process, continue to scouting, and finish with a transparent xG simulation view."

## Next Module
Move to [06-deployment-and-demo-playbook.md](./06-deployment-and-demo-playbook.md).
