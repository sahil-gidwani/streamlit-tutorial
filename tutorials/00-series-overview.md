# Streamlit Football Analytics Tutorial Series

## Who This Is For
- Data analysts and engineers who want to build interactive football analytics products
- Coaches, scouts, and content creators who need reusable demo dashboards
- Students and early-career analysts building a football analytics portfolio

## What You Will Build
By the end of this series, you will have:
- A set of standalone Streamlit mini apps (quick demos)
- A multipage football analytics app with a coherent navigation flow
- A lightweight expected goals model demo
- A deployment checklist and launch workflow

## Learning Path (Ordered)
1. [01-streamlit-fundamentals.md](./01-streamlit-fundamentals.md)
2. [02-match-dashboard.md](./02-match-dashboard.md)
3. [03-player-scouting-dashboard.md](./03-player-scouting-dashboard.md)
4. [04-expected-goals-lab.md](./04-expected-goals-lab.md)
5. [05-multipage-football-app.md](./05-multipage-football-app.md)
6. [06-deployment-and-demo-playbook.md](./06-deployment-and-demo-playbook.md)
7. [07-capstone-and-extensions.md](./07-capstone-and-extensions.md)

## Suggested Timeline
- Day 1: Modules 1-2
- Day 2: Modules 3-4
- Day 3: Modules 5-6
- Day 4: Module 7 + dry run demo

## Repo Map
- `apps/` runnable Streamlit examples
- `suite/` multipage Streamlit app (Home + pages)
- `data/` sample football datasets used across modules
- `tutorials/` detailed markdown lessons and exercises

## Quick Start
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run apps/01_hello_football.py
```

Then progress module by module while running each corresponding app in `apps/` and `suite/`.
