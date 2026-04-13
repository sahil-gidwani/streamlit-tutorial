# Module 6: Deployment and Launch Playbook

## Learning Goals
- Deploy your Streamlit app for user access
- Prepare a stable launch workflow
- Mitigate common runtime and data issues during presentations

## Deployment Options
- Streamlit Community Cloud (fastest path to publish)
- Containerized deployment (for enterprise/internal infra)

Reference:
- https://docs.streamlit.io/deploy

## Launch Reliability Checklist
- Pin dependency versions in `requirements.txt`
- Warm caches before presentation starts
- Keep a local fallback run command ready
- Prepare screenshots for critical views as backup
- Validate data load in venue network conditions

## Recommended Product Walkthrough (10-12 mins)
1. Problem framing: football decision latency and fragmented reporting
2. Product walk-through from Home to Match Analysis
3. Scouting workflow and shortlist export
4. xG lab: one what-if simulation
5. Business impact and next roadmap

## Failure Handling Plan
- If cloud app is slow: switch to local instance
- If data source fails: use bundled sample CSV from `data/`
- If chart fails rendering: show cached summary tables first

## Practice Tasks
1. Create a one-command launcher script for your environment.
2. Add app-level status panel (`st.status` or `st.info`) for data freshness.
3. Add version and commit hash display in sidebar.
4. Add synthetic smoke tests using Streamlit testing API.

## Next Module
Finish with [07-capstone-and-extensions.md](./07-capstone-and-extensions.md).
