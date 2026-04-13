# Module 2: Match Dashboard (Coach-Facing View)

## Learning Goals
- Build a tactical match summary page
- Compare teams on xG, shots, field tilt, and final-third actions
- Present an actionable narrative, not just charts

## Build
Run:
```bash
streamlit run apps/02_match_dashboard.py
```

## Dashboard Blueprint
- Header: match metadata (teams, competition, date)
- KPI row: goals, xG, shots on target, possession
- Flow chart: xG by minute
- Event table: sortable timeline with key actions
- Coach notes section: textual interpretation

## Example Snippet: KPI Row
```python
col1, col2, col3, col4 = st.columns(4)
col1.metric("Home xG", f"{home_xg:.2f}")
col2.metric("Away xG", f"{away_xg:.2f}")
col3.metric("Shots On Target", int(total_sot))
col4.metric("Pass Completion", f"{pass_completion:.1f}%")
```

## Visualization Guidance
- Keep color assignment consistent per team across all visuals.
- Put outcome context next to process context (goals next to xG).
- Keep a tight visual hierarchy: headline insights first, tables later.

## Practice Tasks
1. Add halftime split metrics.
2. Add a possession phase filter (build-up, progression, final third).
3. Add rolling 5-minute xG momentum chart.
4. Add a short "three takeaways" auto-summary panel.

## Interpretation Prompt
"This dashboard lets staff quickly separate process from scoreline. If the result was poor but xG process was strong, tactical adjustments may be incremental rather than structural."

## Next Module
Proceed to [03-player-scouting-dashboard.md](./03-player-scouting-dashboard.md).
