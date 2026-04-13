# Module 4: Player Scouting Dashboard

## Learning Goals
- Build role-aware player comparison views
- Normalize metrics per 90 minutes
- Create shortlist logic for recruitment workflows

## Build
Run:
```bash
streamlit run apps/04_player_scout.py
```

## Product Framing
A scouting app should answer:
- Who matches our role profile?
- Which attributes are elite, average, or risky?
- What does the confidence level of the sample look like?

## Core Features
- Position filter (CB, FB, CM, Winger, Striker)
- League and age filters
- Minimum minutes slider
- Radar-like comparison table (simple version with z-scores)
- Export shortlist as CSV

## Example Snippet: Per-90 Normalization
```python
metric_cols = ["shots", "key_passes", "progressive_passes", "tackles_won"]
for c in metric_cols:
    df[f"{c}_p90"] = (df[c] / df["minutes"].clip(lower=1)) * 90
```

## Analytical Notes
- Always pair per-90 with total minutes to avoid small-sample traps.
- Separate possession-heavy and transition-heavy team contexts when scouting.
- Use percentile ranks for cross-league communication.

## Practice Tasks
1. Add a percentile rank column for selected metrics.
2. Build a binary fit score (profile match yes/no).
3. Add a confidence label based on minutes played thresholds.
4. Add a downloadable shortlist report.

## Next Module
Continue to [05-expected-goals-lab.md](./05-expected-goals-lab.md).
