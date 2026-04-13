# Module 7: Capstone and Extensions

## Capstone Goal
Deliver a coherent football analytics product demo that includes:
- Match diagnostics
- Scouting comparisons
- xG explainability
- A roadmap for production hardening

## Capstone Requirements
- At least 3 pages in your app
- 1 user-controlled scenario simulation
- 1 export feature (CSV)
- 1 transparent data-quality section
- 1 model caveat section

## Stretch Extensions
- Add mplsoccer shot map and pass network charts
- Add Understat API ingestion for broader league coverage
- Add authentication and role-aware pages
- Add alerting for KPI threshold breaches

Useful links:
- mplsoccer: https://mplsoccer.readthedocs.io/en/latest/
- Understat package: https://understat.readthedocs.io/en/latest/
- Streamlit authentication tutorial: https://docs.streamlit.io/develop/tutorials/authentication

## Evaluation Rubric (Demo Readiness)
- Clarity: Does a non-analyst understand the key message?
- Reliability: Does app run smoothly and predictably?
- Relevance: Are outputs tied to football decisions?
- Transparency: Are assumptions and caveats explicit?
- Reusability: Can this be extended for a real team workflow?

## Suggested Closing Slide
"From raw event data to decision-ready football insights in a reproducible, interactive Streamlit product."

## What To Do Next
- Convert sample data to real provider feeds.
- Add CI checks for data schema drift.
- Add model retraining cadence and monitoring.
- Add user feedback capture directly inside the app.
